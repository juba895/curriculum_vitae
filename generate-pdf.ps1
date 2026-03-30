# ============================================================
# generate-pdf.ps1
# Generiert ein PDF des Lebenslaufs via Microsoft Edge (headless)
# Aufruf: .\generate-pdf.ps1
#         .\generate-pdf.ps1 -OutputName "MeinCV.pdf"
#         .\generate-pdf.ps1 -Open
# ============================================================

param(
    [string]$OutputName = "Julian_Banek_CV.pdf",
    [switch]$Open
)

$edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if (-not (Test-Path $edgePath)) {
    Write-Error "Microsoft Edge nicht gefunden: $edgePath"
    exit 1
}

$scriptDir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlFile   = Join-Path $scriptDir "index.html"
$outputPdf  = Join-Path $scriptDir $OutputName

if (-not (Test-Path $htmlFile)) {
    Write-Error "index.html nicht gefunden: $htmlFile"
    exit 1
}

# Pfad als file:// URL formatieren (Backslashes → Slashes)
$fileUrl = "file:///" + ($htmlFile -replace '\\', '/')

Write-Host ""
Write-Host "  📄  Generiere PDF..." -ForegroundColor Cyan
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
    "--print-to-pdf=`"$outputPdf`""
    "--no-pdf-header-footer"
    "`"$fileUrl`""
)

Start-Process -FilePath $edgePath -ArgumentList $edgeArgs -Wait -NoNewWindow

if (Test-Path $outputPdf) {
    $fileTime = (Get-Item $outputPdf).LastWriteTime
    if ($fileTime -lt $startTime) {
        Write-Host "  ❌  PDF-Generierung fehlgeschlagen (Datei wurde nicht aktualisiert)." -ForegroundColor Red
        Write-Host "      Tipp: Öffne index.html manuell in Edge und drucke mit Strg+P → 'Als PDF speichern'." -ForegroundColor Yellow
        exit 1
    }
    $size = [math]::Round((Get-Item $outputPdf).Length / 1KB, 1)
    Write-Host "  ✅  PDF erfolgreich erstellt  ($size KB)" -ForegroundColor Green
    Write-Host "  Pfad: $outputPdf" -ForegroundColor Gray

    if ($Open) {
        Write-Host "  🔍  Öffne PDF..." -ForegroundColor Cyan
        Start-Process $outputPdf
    }
} else {
    Write-Host "  ❌  PDF-Generierung fehlgeschlagen." -ForegroundColor Red
    Write-Host "      Tipp: Öffne index.html manuell in Edge und drucke mit Strg+P → 'Als PDF speichern'." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
