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

if ($cmd -match 'git\s+commit') {
    $branch = (& git rev-parse --abbrev-ref HEAD 2>$null)
    if ($branch -in @('main', 'master')) {
        Request-Confirmation "Committing directly on $branch. Create a feature branch (feat/ fix/ docs/ chore/) and open a PR instead."
    }
}

if ($cmd -match 'git\s+push' -and $cmd -match '(^|[\s:])(main|master)($|[\s:])') {
    Request-Confirmation 'Pushing to the default branch. Push a feature branch and open a PR instead.'
}

exit 0
