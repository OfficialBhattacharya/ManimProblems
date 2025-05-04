Write-Host "Searching for MiKTeX installation..."

# Common MiKTeX installation locations
$possiblePaths = @(
    "C:\Program Files\MiKTeX\miktex\bin\x64",
    "C:\Program Files (x86)\MiKTeX\miktex\bin",
    "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64",
    "$env:APPDATA\MiKTeX\miktex\bin\x64"
)

$miktexPath = $null

foreach ($path in $possiblePaths) {
    if (Test-Path "$path\latex.exe") {
        $miktexPath = $path
        Write-Host "Found MiKTeX at: $miktexPath"
        break
    }
}

if ($miktexPath -eq $null) {
    Write-Host "MiKTeX installation not found in common locations."
    Write-Host "Please search for 'latex.exe' on your system and note its location."
} else {
    # Check if path is already in PATH
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    if ($currentPath -notlike "*$miktexPath*") {
        # Add to PATH for current session
        $env:Path = "$env:Path;$miktexPath"
        Write-Host "Added MiKTeX to PATH for current session."
        
        # Add to PATH permanently
        [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$miktexPath", "User")
        Write-Host "Added MiKTeX to user PATH permanently."
        Write-Host "Please restart your terminal or computer for the changes to take effect."
    } else {
        Write-Host "MiKTeX is already in your PATH."
    }
}

# Try to verify installation in the current session
Write-Host "`nAttempting to verify LaTeX in current session..."
try {
    $result = & "$miktexPath\latex" --version
    Write-Host "LaTeX is available in the current session.`n$result"
} catch {
    Write-Host "Unable to run LaTeX in the current session.`nPlease restart your terminal or computer."
} 