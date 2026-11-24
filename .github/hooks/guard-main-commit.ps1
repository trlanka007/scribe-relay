# PreToolUse guard: ask for confirmation before committing on, or pushing to, main/master.
$ErrorActionPreference = 'SilentlyContinue'

$raw = [Console]::In.ReadToEnd()
$cmd = ''
if ($raw) {
    try {
        $json = $raw | ConvertFrom-Json
        foreach ($candidate in @(
                $json.tool_input.command,
                $json.toolInput.command,
                $json.input.command,
                $json.command)) {
            if ($candidate) { $cmd = "$cmd $candidate" }
        }
    } catch { }
}
$origCmd = $cmd.Trim()
$cmd = $cmd.ToLower()

function Request-Confirmation([string]$reason) {
    @{
        hookSpecificOutput = @{
            hookEventName            = 'PreToolUse'
            permissionDecision       = 'ask'
            permissionDecisionReason = $reason
        }
    } | ConvertTo-Json -Compress | Write-Output
    exit 0
}

if ($cmd -notmatch 'git') { exit 0 }

# Matches "git" followed by any global options, then the given subcommand.
$tok = '(?:"[^"]*"|''[^'']*''|\S+)'
$globals = "(?:\s+(?:-[cC]\s+$tok|--(?:git-dir|work-tree|namespace|exec-path|super-prefix|config-env)(?:=$tok|\s+$tok)|-{1,2}[\w-]+(?:=$tok)?))*"
function Get-GitMatch([string]$sub) {
    [regex]::Match($origCmd, "(?i)\bgit$globals\s+$sub\b")
}

$commit = Get-GitMatch 'commit'
if ($commit.Success) {
    if ((Get-GitMatch 'switch').Success -or (Get-GitMatch 'checkout').Success) {
        Request-Confirmation 'Command switches branches and commits; it may commit directly on main/master. Run them as separate steps on a feature branch.'
    }
    $gitArgs = @()
    $dir = [regex]::Match($commit.Value, "(?:^|\s)-C\s+($tok)")
    if ($dir.Success) { $gitArgs = @('-C', $dir.Groups[1].Value.Trim('"', "'")) }
    $branch = (& git @gitArgs symbolic-ref --short -q HEAD 2>$null)
    if ($branch -in @('main', 'master')) {
        Request-Confirmation "Committing directly on $branch. Create a feature branch (feat/ fix/ docs/ chore/) and open a PR instead."
    }
}

$push = Get-GitMatch 'push'
if ($push.Success) {
    $gitArgs = @()
    $dir = [regex]::Match($push.Value, "(?:^|\s)-C\s+($tok)")
    if ($dir.Success) { $gitArgs = @('-C', $dir.Groups[1].Value.Trim('"', "'")) }
    $current = (& git @gitArgs symbolic-ref --short -q HEAD 2>$null)
    $rest = $origCmd.Substring($push.Index + $push.Length)
    $rest = ($rest -split '&&|\|\||[;&|]')[0]
    $words = @([regex]::Matches($rest, $tok) | ForEach-Object { $_.Value.Trim('"', "'") })
    $positional = @()
    foreach ($w in $words) {
        if ($w -match '^--(all|mirror)$') {
            Request-Confirmation 'git push --all/--mirror may update main/master. Push an explicit feature branch instead.'
        }
        if ($w -notmatch '^-') { $positional += $w }
    }
    $refspecs = @($positional | Select-Object -Skip 1)
    $dests = @()
    if ($refspecs.Count -eq 0) {
        # Implicit destination: the checked-out branch.
        if (-not $current) { Request-Confirmation 'Cannot determine the push destination (detached HEAD or unknown repo). Specify a feature branch explicitly.' }
        $dests = @($current)
    } else {
        foreach ($r in $refspecs) {
            $d = $r.TrimStart('+')
            if ($d.Contains(':')) { $d = $d.Substring($d.LastIndexOf(':') + 1) }
            if ($d -ceq 'HEAD' -or $d -eq '') {
                if (-not $current) { Request-Confirmation 'Cannot determine the push destination from detached HEAD. Specify a feature branch explicitly.' }
                $d = $current
            }
            $dests += ($d -replace '^refs/heads/', '')
        }
    }
    if (@($dests | Where-Object { $_ -in @('main', 'master') }).Count -gt 0) {
        Request-Confirmation 'Pushing to the default branch. Push a feature branch and open a PR instead.'
    }
}
exit 0