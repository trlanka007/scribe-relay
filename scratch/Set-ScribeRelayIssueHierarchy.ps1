#requires -Version 5.1
<#
.SYNOPSIS
  Apply the verified ScribeRelay epic/feature/PBI/task map as native GitHub sub-issues.
.DESCRIPTION
  Read-only preview by default. -Apply adds missing relationships, never replaces
  an existing parent. -RemoveParentReferences optionally removes only exact,
  redundant parent headers after ALL relationships have been verified.
  Uses the locally authenticated GitHub CLI. No repository files or git refs are changed.
  Safe to rerun after interruption; stops on unexpected errors or conflicts.
#>
[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$RemoveParentReferences,
    [ValidateRange(1000,10000)][int]$WriteDelayMs = 1500
)
$ErrorActionPreference = 'Stop'
$repo = 'trlanka007/scribe-relay'
$base = "repos/$repo"
$apiVersion = '2026-03-10'
if ($RemoveParentReferences -and -not $Apply) { throw '-RemoveParentReferences requires -Apply.' }
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'Install GitHub CLI (gh), then authenticate with gh auth login.' }

# Snapshot verified against the live repository on 2026-11-25.
# Each entry maps a parent issue NUMBER to its direct child issue NUMBERS.
# The REST API receives the child's numeric database ID, resolved at runtime.
$groups = [ordered]@{
    # Epics -> features
    '11' = @(19)
    '12' = @(20,21,22)
    '13' = @(23,24,25)
    '14' = @(26,27,28,29,30,31)
    '15' = @(32,33,34)
    '16' = @(35,36,37,38)
    '17' = @(39,40,41)
    '10' = @(42,43,44,45,46)
    '18' = @(47,48,49)
    # Features -> PBIs
    '19' = @(50)
    '20' = @(51)
    '21' = @(52)
    '22' = @(53)
    '23' = @(54)
    '24' = @(55)
    '25' = @(56)
    '26' = @(57)
    '27' = @(58)
    '28' = @(59)
    '29' = @(60)
    '30' = @(61)
    '31' = @(62)
    '32' = @(63)
    '33' = @(64)
    '34' = @(65)
    '35' = @(66)
    '36' = @(67)
    '37' = @(68)
    '38' = @(69)
    '39' = @(70)
    '40' = @(71)
    '41' = @(72)
    '42' = @(73)
    '43' = @(74)
    '44' = @(75)
    '45' = @(76,131,132)
    '46' = @(77)
    '47' = @(78)
    '48' = @(79)
    '49' = @(80)
    # PBIs -> tasks (includes existing documentation debt #5-7)
    '50' = @(114)
    '51' = @(115)
    '52' = @(116)
    '53' = @(117)
    '54' = @(118,6)
    '55' = @(119,5,7)
    '56' = @(120)
    '57' = @(81)
    '58' = @(82,83,84,85,86,87)
    '59' = @(88,89,90)
    '60' = @(91,92)
    '61' = @(93)
    '62' = @(94,95)
    '63' = @(96)
    '64' = @(97)
    '65' = @(98)
    '66' = @(99)
    '67' = @(100)
    '68' = @(101)
    '69' = @(102)
    '70' = @(103)
    '71' = @(104)
    '72' = @(105)
    '73' = @(106,121)
    '74' = @(107,122,123)
    '75' = @(108,124,125)
    '76' = @(109,126,127)
    '77' = @(110,128,129,130)
    '78' = @(111)
    '79' = @(112)
    '80' = @(113)
    '131' = @(133)
    '132' = @(134)
}

function Invoke-GhApi {
    param([string[]]$Arguments, [switch]$AllowNotFound)
    # Capture native stderr without PowerShell treating it as a terminating error.
    $saved = $ErrorActionPreference
    try {
        $ErrorActionPreference = 'Continue'
        # PS 7.3+ may promote nonzero native exits to errors; disable locally.
        $PSNativeCommandUseErrorActionPreference = $false
        $raw = & gh api --hostname github.com -H 'Accept: application/vnd.github+json' -H "X-GitHub-Api-Version: $apiVersion" @Arguments 2>&1
        $code = $LASTEXITCODE
    } finally { $ErrorActionPreference = $saved }
    $output = ($raw | ForEach-Object { $_.ToString() }) -join "`n"
    if ($code -ne 0) {
        if ($AllowNotFound -and $output -match '\(HTTP 404\)') { return $null }
        throw "GitHub API failed (exit $code): $($Arguments -join ' ')`n$output"
    }
    if ([string]::IsNullOrWhiteSpace($output)) { return $null }
    return (ConvertFrom-Json -InputObject $output)
}

function Get-CurrentParent {
    param([int]$Child)
    # A 404 may also indicate inaccessible resources. We separately validate
    # repository/issue visibility; POST never replaces an existing parent.
    return (Invoke-GhApi -Arguments @('--method','GET',"$base/issues/$Child/parent") -AllowNotFound)
}

function Test-ExpectedParent {
    param($Actual, [int]$Expected)
    return ($null -ne $Actual -and [int]$Actual.number -eq $Expected -and
        $Actual.repository_url -eq "https://api.github.com/$base")
}

# Validate the fixed map before any requests that could write.
$edges = @(
    foreach ($parent in $groups.Keys) {
        foreach ($child in $groups[$parent]) {
            [pscustomobject]@{ Parent = [int]$parent; Child = [int]$child }
        }
    }
)
if ($edges.Count -ne 119) { throw "Expected 119 relationships, found $($edges.Count)." }
$parentOf = @{}
foreach ($edge in $edges) {
    if ($edge.Parent -eq $edge.Child -or $parentOf.ContainsKey($edge.Child)) { throw 'Duplicate child or self-parent in map.' }
    $parentOf[$edge.Child] = $edge.Parent
}
foreach ($edge in $edges) {
    $seen = @{}
    $n = $edge.Child
    while ($parentOf.ContainsKey($n)) {
        if ($seen.ContainsKey($n)) { throw 'Cycle in hierarchy map.' }
        $seen[$n] = $true
        $n = $parentOf[$n]
    }
}
$required = @($edges.Parent + $edges.Child | Sort-Object -Unique)
if ($required.Count -ne 128) { throw 'Unexpected issue inventory in map.' }

Write-Host "Repository: $repo" -ForegroundColor Cyan
Write-Host $(if ($Apply) { 'Mode: APPLY' } else { 'Mode: READ-ONLY PREVIEW' })
$repoInfo = Invoke-GhApi -Arguments @('--method','GET',$base)
if ($repoInfo.full_name -ne $repo) { throw 'Repository identity mismatch.' }
if ($Apply -and -not ($repoInfo.permissions.push -or $repoInfo.permissions.admin -or $repoInfo.permissions.triage -or $repoInfo.permissions.maintain)) {
    throw 'Current GitHub CLI account lacks an appropriate repository write/triage permission.'
}
$issues = @{}
for ($page = 1; ; $page++) {
    $batch = @(Invoke-GhApi -Arguments @('--method','GET',"$base/issues?state=all&per_page=100&page=$page") | Where-Object { $null -ne $_ })
    foreach ($issue in $batch) {
        if (-not $issue.pull_request) { $issues[[int]$issue.number] = $issue }
    }
    if ($batch.Count -lt 100) { break }
}
$levels = @('type:epic','type:feature','type:pbi','type:task')
foreach ($n in $required) {
    if (-not $issues.ContainsKey([int]$n)) { throw "Missing or inaccessible issue #$n. No changes made." }
    $type = @($issues[[int]$n].labels | Where-Object { $_.name -in $levels })
    if ($type.Count -ne 1) { throw "Issue #$n must have exactly one hierarchy type label." }
}
foreach ($edge in $edges) {
    $pt = @($issues[$edge.Parent].labels | Where-Object { $_.name -in $levels })[0].name
    $ct = @($issues[$edge.Child].labels | Where-Object { $_.name -in $levels })[0].name
    if ([array]::IndexOf($levels,$ct) -ne ([array]::IndexOf($levels,$pt) + 1)) {
        throw "Hierarchy type mismatch: #$($edge.Parent) ($pt) -> #$($edge.Child) ($ct)."
    }
}

# Preflight every relationship; never silently reparent an issue.
$pending = @()
$existing = 0
$conflicts = @()
foreach ($edge in $edges) {
    $actual = Get-CurrentParent -Child $edge.Child
    if (Test-ExpectedParent -Actual $actual -Expected $edge.Parent) { $existing++; continue }
    if ($null -ne $actual) {
        $conflicts += "#$($edge.Child) has parent $($actual.html_url); expected #$($edge.Parent)"
        continue
    }
    $pending += $edge
}
Write-Host "Expected: $($edges.Count) | Already linked: $existing | Missing: $($pending.Count) | Conflicts: $($conflicts.Count)"
if ($conflicts.Count -gt 0) { throw "Existing parent conflicts; no writes attempted.`n$($conflicts -join "`n")" }
if (-not $Apply) {
    foreach ($edge in $pending) { Write-Host "WOULD LINK #$($edge.Parent) -> #$($edge.Child)" }
    Write-Host 'Preview complete. Run with -Apply to create relationships.' -ForegroundColor Green
    return
}

# Sequential writes with a deliberate pause; avoid secondary rate limits.
$added = 0
foreach ($edge in $pending) {
    $childId = [long]$issues[$edge.Child].id
    if ($childId -le 0) { throw "Invalid database ID for #$($edge.Child)." }
    # replace_parent=false ensures concurrent changes cannot silently reparent.
    $null = Invoke-GhApi -Arguments @('--method','POST',"$base/issues/$($edge.Parent)/sub_issues",'-F',"sub_issue_id=$childId",'-F','replace_parent=false')
    $added++
    Write-Host "LINKED #$($edge.Parent) -> #$($edge.Child) ($added/$($pending.Count))"
    Start-Sleep -Milliseconds $WriteDelayMs
}

# Confirm every link using the native parent endpoint before any body cleanup.
$verified = 0
foreach ($edge in $edges) {
    $actual = Get-CurrentParent -Child $edge.Child
    if (-not (Test-ExpectedParent -Actual $actual -Expected $edge.Parent)) {
        throw "Verification failed for #$($edge.Child); no description cleanup attempted. Rerun after investigating."
    }
    $verified++
}
Write-Host "Native hierarchy verified: $verified/$($edges.Count)." -ForegroundColor Green

$cleaned = 0
if ($RemoveParentReferences) {
    foreach ($edge in $edges) {
        # Read fresh body, preserving any unrelated edits made since preflight.
        $issue = Invoke-GhApi -Arguments @('--method','GET',"$base/issues/$($edge.Child)")
        $old = [string]$issue.body
        $p = $edge.Parent
        # Remove ONLY a standalone leading parent header or parent line matching
        # the verified relationship. Do not rewrite other text or links.
        $pattern = '\A(?:## Parent (?:epic|feature|PBI)[ \t]*\r?\n[ \t]*#' + $p + '[ \t]*\r?\n(?:[ \t]*\r?\n)?|Parent (?:epic|feature|PBI):[ \t]*#' + $p + '[ \t]*\r?\n(?:[ \t]*\r?\n)?)'
        $new = [regex]::Replace($old,$pattern,'',[System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
        if ($new -ceq $old) { continue }
        # Send JSON via a UTF-8 temporary file, avoiding PowerShell quoting issues.
        $tmp = [System.IO.Path]::GetTempFileName()
        try {
            $json = @{body=$new} | ConvertTo-Json -Compress
            [System.IO.File]::WriteAllText($tmp,$json,(New-Object System.Text.UTF8Encoding($false)))
            $updated = Invoke-GhApi -Arguments @('--method','PATCH',"$base/issues/$($edge.Child)",'--input',$tmp)
            if ([string]$updated.body -cne $new) { throw "Body verification failed for #$($edge.Child)." }
        } finally { Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue }
        $cleaned++
        Write-Host "CLEANED redundant parent header from #$($edge.Child)"
        Start-Sleep -Milliseconds $WriteDelayMs
    }
}
Write-Host "Complete: $verified verified, $added newly linked, $existing already linked, $cleaned descriptions cleaned." -ForegroundColor Green
Write-Host 'No issue creation, deletion, closure, label changes, or repository file changes performed.'
