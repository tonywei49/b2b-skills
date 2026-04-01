#Requires -RunAsAdministrator
<#
.SYNOPSIS
    tavily-search skill dependency installer.
    Checks for Python 3 and installs it if missing.

.DESCRIPTION
    Run this script after installing the tavily-search skill to ensure
    Python 3 is available on the system. Uses winget for silent install.
    Must be run as Administrator.

.NOTES
    Output encoding: UTF-8 with BOM
#>

$ErrorActionPreference = "Stop"
$PythonCommand = $null
$PythonAvailable = $false
$PythonVersion = $null

# Step 1: Detect existing Python
Write-Host "[tavily-search] Checking for Python 3..." -ForegroundColor Cyan

foreach ($candidate in @("python3", "python", "py")) {
    try {
        $cmd = Get-Command $candidate -ErrorAction SilentlyContinue
        if ($null -ne $cmd) {
            $rawVersion = & $candidate --version 2>&1
            if ($rawVersion -match "Python (\d+)\.(\d+)") {
                $PythonCommand = $candidate
                $PythonVersion = $rawVersion.ToString().Trim()
                $PythonAvailable = $true
                Write-Host "[FOUND] $PythonVersion at $(($cmd.Source))" -ForegroundColor Green
                break
            }
        }
    }
    catch {
        continue
    }
}

if ($PythonAvailable) {
    Write-Host "[OK] Python is already installed. No action needed." -ForegroundColor Green
    Write-Host "Python command: $PythonCommand" -ForegroundColor Gray
    exit 0
}

# Step 2: Python not found
Write-Host ""
Write-Host "[MISSING] Python 3 was not found on this system." -ForegroundColor Yellow
Write-Host "The tavily-search skill requires Python 3 to run." -ForegroundColor Yellow
Write-Host ""

$InstallChoice = Read-Host "Install Python 3 now? [Y]es / [N]o (default: Y)"

if ($InstallChoice -eq "N") {
    Write-Host "Skipping installation. The tavily-search skill will not work without Python." -ForegroundColor Red
    Write-Host "To install manually: https://python.org/downloads" -ForegroundColor Gray
    exit 1
}

# Step 3: Try winget
Write-Host ""
Write-Host "[INSTALL] Attempting to install Python 3 via winget..." -ForegroundColor Cyan

$wingetCmd = Get-Command winget -ErrorAction SilentlyContinue
if ($null -eq $wingetCmd) {
    Write-Host "[ERROR] winget not found. Please install Python manually." -ForegroundColor Red
    Write-Host "Download: https://python.org/downloads" -ForegroundColor Gray
    exit 1
}

try {
    $installResult = Start-Process -FilePath "winget" `
        -ArgumentList "install","Python.Python.3.11","--silent","--accept-package-agreements","--accept-source-agreements" `
        -NoNewWindow -Wait -PassThru

    if ($installResult.ExitCode -eq 0) {
        Write-Host "[OK] Python installed successfully via winget." -ForegroundColor Green
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

        $python3Cmd = Get-Command python3 -ErrorAction SilentlyContinue
        if ($null -eq $python3Cmd) { $python3Cmd = Get-Command python -ErrorAction SilentlyContinue }
        if ($null -ne $python3Cmd) {
            $v = & python3 --version 2>&1
            Write-Host "[OK] Python is now available: $v" -ForegroundColor Green
        }
        else {
            Write-Host "[WARN] Python installed but not detected in current session. Restart terminal and re-run to verify." -ForegroundColor Yellow
        }
    }
    else {
        throw "winget install returned exit code $($installResult.ExitCode)"
    }
}
catch {
    Write-Host ""
    Write-Host "[ERROR] Failed to install Python automatically." -ForegroundColor Red
    Write-Host "Please install Python manually:" -ForegroundColor Yellow
    Write-Host "  Option 1: https://python.org/downloads" -ForegroundColor Gray
    Write-Host "  Option 2: Microsoft Store -> search 'Python 3.11'" -ForegroundColor Gray
    Write-Host "  Option 3: choco install python --version=3.11 (if Chocolatey is installed)" -ForegroundColor Gray
    exit 1
}

Write-Host ""
Write-Host "[DONE] Dependency check complete." -ForegroundColor Green
