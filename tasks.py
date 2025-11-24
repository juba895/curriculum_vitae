#!/usr/bin/env python3
"""
Invoke Tasks für CV PDF Generator
Automatisiert Setup, Installation und PDF-Generierung
"""

from invoke import task
import sys
import asyncio
from pathlib import Path

@task
def setup(c):
    """Installiert alle Dependencies und richtet das System ein"""
    print("🚀 CV PDF Generator Setup")
    print("=" * 40)
    
    # Python-Version prüfen
    python_version = sys.version_info
    print(f"=> Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("❌ Python 3.8+ erforderlich!")
        return
    
    # Playwright installieren
    print("=> Installiere Dependencies...")
    result = c.run("pip install -r requirements.txt", warn=True)
    if result.failed:
        print("❌ Dependencies Installation fehlgeschlagen!")
        return
    print("=> Dependencies installiert!")
    
    # Chromium Browser installieren
    print("=> Installiere Chromium Browser...")
    result = c.run("python -m playwright install chromium", warn=True)
    if result.failed:
        print("❌ Chromium Installation fehlgeschlagen!")
        return
    print("=> Chromium Browser installiert!")
    
    # Installation testen
    print("=> Teste Installation...")
    test_result = c.run("python -c 'from playwright.async_api import async_playwright; print(\"=> Playwright funktioniert!\")'", warn=True)
    
    if test_result.ok:
        print("\n=> Setup erfolgreich abgeschlossen!")
        print("\n📋 Verfügbare Kommandos:")
        print("   invoke pdf           # Interaktives Menü")
        print("   invoke pdf-simple    # Einfaches PDF (empfohlen)")
        print("   invoke pdf-website   # Website-PDF")
        print("   invoke pdf-both      # Beide Versionen")
        print("   invoke clean-generated # Generierte PDFs löschen")
        print("\n=> PDFs werden in 'generated/' gespeichert")
    else:
        print("❌ Setup fehlgeschlagen!")

@task
def pdf(c):
    """Startet den interaktiven PDF-Generator"""
    print("=> Starte interaktiven PDF-Generator...")
    c.run("python scripts/cv_pdf_generator.py")

@task
def pdf_simple(c):
    """Erstellt das einfache PDF (empfohlen)"""
    print("=> Erstelle einfaches PDF...")
    c.run("python scripts/cv_pdf_generator.py simple")

@task
def pdf_website(c):
    """Erstellt PDF von der Website"""
    print("=> Erstelle Website-PDF...")
    c.run("python scripts/cv_pdf_generator.py website")

@task
def pdf_both(c):
    """Erstellt beide PDF-Versionen"""
    print("=>=> Erstelle beide PDF-Versionen...")
    c.run("python scripts/cv_pdf_generator.py both")

@task
def clean_generated(c):
    """Löscht alle generierten PDF-Dateien"""
    print("🧹 Lösche generierte PDFs...")
    
    from pathlib import Path
    generated_dir = Path("generated")
    
    if generated_dir.exists():
        pdf_files = list(generated_dir.glob("*.pdf"))
        if pdf_files:
            for pdf in pdf_files:
                pdf.unlink()
                print(f"     =>  Gelöscht: {pdf.name}")
            print(f"=> {len(pdf_files)} PDF-Dateien gelöscht!")
        else:
            print("=> Keine PDF-Dateien zum Löschen gefunden")
    else:
        print("=> Generated-Ordner existiert nicht")

@task
def clean(c):
    """Löscht temporäre Python-Dateien"""
    print("🧹 Räume Python-Dateien auf...")
    
    files_to_clean = [
        "*.pyc",
        "__pycache__",
        ".pytest_cache",
        "*.pyo"
    ]
    
    for pattern in files_to_clean:
        result = c.run(f"Remove-Item {pattern} -Force -Recurse -ErrorAction SilentlyContinue", warn=True, shell="pwsh")
    
    print("=> Python-Aufräumen abgeschlossen!")

@task
def install(c):
    """Alias für setup - installiert alle Dependencies"""
    setup(c)

@task
def test(c):
    """Testet die Playwright-Installation"""
    print("=> Teste Playwright...")
    result = c.run("python -c 'from playwright.async_api import async_playwright; print(\"=> Import erfolgreich!\")'", warn=True)
    
    if result.ok:
        print("=> Playwright funktioniert korrekt!")
    else:
        print("❌ Playwright-Test fehlgeschlagen!")
        print("💡 Führe 'invoke setup' aus um das Problem zu beheben.")

@task
def info(c):
    """Zeigt Systeminformationen und verfügbare Kommandos"""
    print("=>  CV PDF Generator - Systeminformationen")
    print("=" * 50)
    
    # Python-Version
    python_version = sys.version_info
    print(f"=> Python: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Playwright-Status
    try:
        from playwright.async_api import async_playwright
        print("=> Playwright: Installiert")
    except ImportError:
        print("❌ Playwright: Nicht installiert")
    
    # Verfügbare PDFs
    pdf_files = list(Path("generated").glob("*.pdf")) if Path("generated").exists() else []
    if pdf_files:
        print(f"=> Generierte PDFs: {len(pdf_files)}")
        for pdf in pdf_files:
            print(f"   • {pdf.name}")
    else:
        print("=> Keine PDFs vorhanden")
    
    print("\n📋 Verfügbare Kommandos:")
    print("   invoke setup         # Erstinstallation")
    print("   invoke pdf           # Interaktives Menü")
    print("   invoke pdf-simple    # Einfaches PDF")
    print("   invoke pdf-website   # Website-PDF")
    print("   invoke pdf-both      # Beide Versionen")
    print("   invoke test          # Installation testen")
    print("   invoke clean         # Python-Dateien aufräumen")
    print("   invoke clean-generated # Generierte PDFs löschen")
    print("   invoke info          # Diese Information")

@task(default=True)
def help(c):
    """Zeigt Hilfe und verfügbare Kommandos (Standard)"""
    print("=> CV PDF Generator")
    print("=" * 30)
    print("Verwende 'invoke <command>' um Aktionen auszuführen.")
    print()
    print("🚀 Schnellstart:")
    print("   invoke setup      # Erstinstallation")
    print("   invoke pdf        # PDF erstellen")
    print()
    print("📋 Alle Kommandos:")
    print("   invoke info       # Detaillierte Informationen")
    print("   invoke --list     # Alle verfügbaren Tasks")
