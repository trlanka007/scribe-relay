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
    $gitArgs = @()
    $dir = [regex]::Match($commit.Value, "(?:^|\s)-C\s+($tok)")
    if ($dir.Success) { $gitArgs = @('-C', $dir.Groups[1].Value.Trim('"', "'")) }
    $branch = (& git @gitArgs symbolic-ref --short -q HEAD 2>$null)
    if ($branch -in @('main', 'master')) {
        Request-Confirmation "Committing directly on $branch. Create a feature branch (feat/ fix/ docs/ chore/) and open a PR instead."
    }
}

if ((Get-GitMatch 'push').Success -and $cmd -match '(^|[\s:])(main|master)($|[\s:])') {
    Request-Confirmation 'Pushing to the default branch. Push a feature branch and open a PR instead.'
}

exit 0