# Julian Banek – Curriculum Vitae

[![GitHub Pages](https://img.shields.io/badge/Live-GitHub%20Pages-blue?logo=github)](https://juba895.github.io/curriculum_vitae/)

---

## Table of Contents

- [Description](#description)
- [Open website locally](#open-website-locally)
- [Generate PDF](#generate-pdf)
- [Project structure](#project-structure)
- [License](#license)

---

## Description

Personal CV website of Julian Banek.

---

## Open website locally

**Option A – Open directly in browser (simplest method)**

1. Clone or download the repository:
   ```bash
   git clone https://github.com/juba895/curriculum_vitae.git
   cd curriculum_vitae
   ```
2. Double-click `index.html` to open it in your browser
   *(or right-click → "Open with" → select browser)*

**Option B – Start a local web server (recommended)**

With Python (version 3+):
```bash
python -m http.server 8080
```
Then open in your browser: [http://localhost:8080](http://localhost:8080)

With Node.js (`npx`):
```bash
npx serve .
```

---

## Generate PDF

Requirements: **Microsoft Edge** must be installed.

```powershell
# Default – creates "Julian_Banek_CV.pdf"
.\generate-pdf.ps1

# Open PDF immediately after creation
.\generate-pdf.ps1 -Open

# Custom file name
.\generate-pdf.ps1 -OutputName "Banek_Julian_CV.pdf"
```

> **Note:** If the script fails because the file is still open, close your PDF viewer first and run the command again.

---

## Project structure

```
curriculum_vitae/
├── index.html          # Main page
├── generate-pdf.ps1    # PDF generation script (PowerShell / Edge)
├── images/             # Avatar & banner images
└── assets/
    ├── css/            # Stylesheets
    ├── js/             # JavaScript
    └── sass/           # SASS source files
```

---

## License

Design based on [Read Only](https://html5up.net/read-only) by [HTML5 UP](https://html5up.net) – [CCA 3.0 license](https://html5up.net/license).
