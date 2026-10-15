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

Personal CV website of Julian Banek. The German version is the default page; the [English CV](index_en.html) is available via the language switch in the sidebar.

---

## Open website locally

Open `index.html` in a browser to view the German CV, or open `index_en.html` for the English version. You can also switch languages using the language switch on the page.

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

# English version (German is the default)
.\generate-pdf.ps1 -Language en

# English version with a custom file name, then open the PDF
.\generate-pdf.ps1 -Language en -OutputName "Julian_Banek_CV_EN.pdf" -Open
```

> **Note:** If the script fails because the file is still open, close your PDF viewer first and run the command again.

---

## Project structure

```
curriculum_vitae/
├── index.html          # German CV
├── index_en.html       # English CV
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
