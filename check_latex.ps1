Write-Host "Checking for LaTeX installation..."
$latex = Get-Command latex -ErrorAction SilentlyContinue
if ($latex) {
    Write-Host "LaTeX is installed at: $($latex.Source)"
    Write-Host "LaTeX version information:"
    & latex --version
} else {
    Write-Host "LaTeX not found. Make sure MiKTeX is installed and in your PATH."
    Write-Host "You may need to restart your terminal or computer for PATH changes to take effect."
}

Write-Host "`nChecking for pdflatex..."
$pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
if ($pdflatex) {
    Write-Host "pdflatex is installed at: $($pdflatex.Source)"
} else {
    Write-Host "pdflatex not found."
}

Write-Host "`nChecking PATH environment variable..."
$env:Path -split ";" | ForEach-Object { 
    if ($_ -like "*tex*" -or $_ -like "*miktex*") {
        Write-Host "Found TeX-related path: $_"
    }
} 