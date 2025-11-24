# CV PDF Generator

Dieses Verzeichnis enthält Skripte zur Generierung von PDF-Versionen des CVs.

## 📄 Hauptskript

### `scripts/cv_pdf_generator.py` (VEREINIGT)
- **Zweck**: Unified PDF Generator mit mehreren Modi
- **Modi**: 
  - `simple`: Erstellt sauberes, professionelles PDF
  - `website`: Generiert PDF von der Website-Version
  - `both`: Erstellt beide Versionen
- **Ausgabe**: Alle PDFs werden in `generated/` gespeichert

**Verwendung:**
```bash
# Interaktives Menü
python scripts/cv_pdf_generator.py

# Direkter Modus
python scripts/cv_pdf_generator.py simple
python scripts/cv_pdf_generator.py website  
python scripts/cv_pdf_generator.py both
```

## 🚀 Empfohlene Nutzung mit Invoke

```bash
# Setup (einmalig)
invoke setup

# PDF-Generierung
invoke pdf           # Interaktives Menü
invoke pdf-simple    # Einfaches PDF (empfohlen)
invoke pdf-website   # Website-PDF
invoke pdf-both      # Beide Versionen

# Aufräumen
invoke clean-generated
```

## 🛠️ Voraussetzungen

```bash
pip install playwright
python -m playwright install chromium
```

## 📋 Generierte Dateien

Alle PDFs werden im `generated/` Ordner gespeichert:
- `Julian-Banek-CV.pdf` - Simple Version (empfohlen)
- `Julian-Banek-CV-Website.pdf` - Website Version

## 💡 Empfehlung

Verwende **`invoke pdf-simple`** für die PDF-Generierung. Diese Version ist optimiert für:
- Keine leeren Seiten
- Professionelle Darstellung
- Kompakte Struktur
- Zuverlässige Ausgabe
