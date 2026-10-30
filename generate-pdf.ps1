# ============================================================
# generate-pdf.ps1
# Generiert ein PDF des Lebenslaufs via Microsoft Edge (headless)
# Aufruf: pwsh ./generate-pdf.ps1
#         pwsh ./generate-pdf.ps1 -OutputName "MeinCV.pdf"
#         pwsh ./generate-pdf.ps1 -Language en
#         pwsh ./generate-pdf.ps1 -Open
# ============================================================

param(
    [string]$OutputName = "Julian_Banek_CV.pdf",
    [ValidateSet("de", "en")]
    [string]$Language = "de",
    [switch]$Open
)

$edgeCandidates = @()

if ($env:EDGE_PATH) {
    $edgeCandidates += $env:EDGE_PATH
}

if ($IsWindows) {
    $programFilesX86 = [Environment]::GetEnvironmentVariable("ProgramFiles(x86)")
    if ($programFilesX86) {
        $edgeCandidates += Join-Path $programFilesX86 "Microsoft\Edge\Application\msedge.exe"
    }

    $programFiles = [Environment]::GetFolderPath("ProgramFiles")
    if ($programFiles) {
        $edgeCandidates += Join-Path $programFiles "Microsoft\Edge\Application\msedge.exe"
    }
} elseif ($IsMacOS) {
    $edgeCandidates += "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
    $edgeCandidates += Join-Path $HOME "Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
}

$edgeCommand = Get-Command "msedge" -ErrorAction SilentlyContinue
if ($edgeCommand) {
    $edgeCandidates += $edgeCommand.Source
}

$edgePath = $edgeCandidates |
    Where-Object { $_ -and (Test-Path -LiteralPath $_ -PathType Leaf) } |
    Select-Object -First 1

if (-not $edgePath) {
    Write-Error "Microsoft Edge nicht gefunden. Installiere Edge oder setze EDGE_PATH auf den Pfad zur Edge-Anwendung."
    exit 1
}

$scriptDir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$printShortcut = if ($IsMacOS) { "Cmd+P" } else { "Strg+P" }
$htmlFileName = if ($Language -eq "en") { "index_en.html" } else { "index.html" }
$htmlFile   = Join-Path $scriptDir $htmlFileName
$outputPdf  = Join-Path $scriptDir $OutputName

if (-not (Test-Path $htmlFile)) {
    Write-Error "$htmlFileName nicht gefunden: $htmlFile"
    exit 1
}

$fileUrl = ([System.Uri]::new($htmlFile)).AbsoluteUri

Write-Host ""
Write-Host "  📄  Generiere PDF..." -ForegroundColor Cyan
Write-Host "  Sprache: $Language"
Write-Host "  Quelle : $htmlFile"
Write-Host "  Ausgabe: $outputPdf"
Write-Host ""

# Vorhandenes PDF entfernen, damit wir den Erfolg klar prüfen können
if (Test-Path $outputPdf) {
    try {
        Remove-Item $outputPdf -Force -ErrorAction Stop
    } catch {
        Write-Host "  ⚠️  PDF ist noch geöffnet – bitte zuerst den PDF-Viewer schließen und erneut ausführen." -ForegroundColor Yellow
        exit 1
    }
}
$startTime = Get-Date

$edgeArgs = @(
    "--headless=new"
    "--disable-gpu"
    "--no-sandbox"
    "--disable-extensions"
    "--run-all-compositor-stages-before-draw"
    "--virtual-time-budget=8000"          # 8 s warten – Animationen / Fonts
    "--print-to-pdf=$outputPdf"
    "--no-pdf-header-footer"
    $fileUrl
)

& $edgePath @edgeArgs
$edgeExitCode = $LASTEXITCODE
if ($edgeExitCode -ne 0) {
    Write-Error "Microsoft Edge wurde mit Fehlercode $edgeExitCode beendet."
    exit $edgeExitCode
}

$outputFile = $null
$outputDeadline = (Get-Date).AddSeconds(30)
while ((Get-Date) -lt $outputDeadline) {
    $outputFile = Get-Item -LiteralPath $outputPdf -Force -ErrorAction SilentlyContinue
    if ($outputFile -and $outputFile.Length -gt 0) {
        break
    }
    Start-Sleep -Milliseconds 250
}

if ($outputFile -and $outputFile.Length -gt 0) {
    $size = [math]::Round($outputFile.Length / 1KB, 1)
    Write-Host "  ✅  PDF erfolgreich erstellt  ($size KB)" -ForegroundColor Green
    Write-Host "  Pfad: $outputPdf" -ForegroundColor Gray

    if ($Open) {
        Write-Host "  🔍  Öffne PDF..." -ForegroundColor Cyan
        if ($IsWindows) {
            Start-Process -FilePath $outputPdf
        } elseif ($IsMacOS) {
            & open $outputPdf
        }
    }
} else {
    Write-Host "  ❌  PDF-Generierung fehlgeschlagen." -ForegroundColor Red
    Write-Host "      Tipp: Öffne $htmlFileName manuell in Edge und drucke mit $printShortcut → 'Als PDF speichern'." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
