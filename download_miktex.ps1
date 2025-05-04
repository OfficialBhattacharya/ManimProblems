$url = "https://miktex.org/download/ctan/systems/win32/miktex/setup/windows-x64/basic-miktex-24.1-x64.exe"
$output = "$PSScriptRoot\miktex-installer.exe"
Write-Host "Downloading MiKTeX installer..."
(New-Object System.Net.WebClient).DownloadFile($url, $output)
Write-Host "Download complete: $output"
Write-Host "Please run the installer manually from your file explorer"
Write-Host "After installation, please run 'where latex' to verify the installation" 