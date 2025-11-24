#!/usr/bin/env python3
"""
CV PDF Generator - Unified Version
Bietet zwei Optionen: Einfache Version (empfohlen) oder Website-basierte Version
"""

import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

async def generate_simple_pdf():
    """Generiert ein einfaches, funktionales PDF (EMPFOHLEN)"""
    print("=> Erstelle einfaches CV PDF...")
    
    # Einfache HTML-Struktur
    simple_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Julian Banek - CV</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: #2c3e50;
            color: white;
        }
        
        .header h1 {
            margin: 0 0 10px 0;
            font-size: 32px;
        }
        
        .header p {
            margin: 0;
            font-size: 18px;
        }
        
        .contact {
            text-align: center;
            margin-bottom: 30px;
            padding: 15px;
            background: #f4f4f4;
        }
        
        .section {
            margin-bottom: 30px;
        }
        
        .section h2 {
            color: #2c3e50;
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 5px;
            margin-bottom: 20px;
            font-size: 20px;
        }
        
        .job {
            margin-bottom: 25px;
            padding: 15px;
            border-left: 4px solid #2c3e50;
            background: #f9f9f9;
        }
        
        .job-title {
            font-weight: bold;
            font-size: 16px;
            color: #2c3e50;
        }
        
        .job-company {
            font-style: italic;
            color: #666;
        }
        
        .job-date {
            font-size: 14px;
            color: #888;
            margin-bottom: 10px;
        }
        
        .job-description {
            margin-top: 10px;
        }
        
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 10px;
        }
        
        .skill {
            background: #2c3e50;
            color: white;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 12px;
        }
        
        .education {
            background: #f9f9f9;
            padding: 15px;
            margin-bottom: 15px;
            border-left: 4px solid #2c3e50;
        }
        
        .education h3 {
            margin: 0 0 5px 0;
            color: #2c3e50;
        }
        
        .education p {
            margin: 5px 0;
        }
        
        .two-columns {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        
        ul {
            margin: 10px 0;
            padding-left: 20px;
        }
        
        li {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Julian Banek</h1>
        <p>Senior Software Engineer</p>
    </div>
    
    <div class="contact">
        <strong>Kontakt:</strong> julian.banek@web.de | 92339 Beilngries | Geboren: 30.05.1989 | Deutsch
    </div>
    
    <div class="section">
        <h2>Berufserfahrung</h2>
        
        <div class="job">
            <div class="job-title">Software Engineer</div>
            <div class="job-company">CARIAD SE, PMT, Ingolstadt</div>
            <div class="job-date">seit 01/2023</div>
            <div class="job-description">
                <ul>
                    <li>Entwicklung und Wartung einer CI/CD-Umgebung für MBSD-Toolchains mittels GitHub Actions</li>
                    <li>Bereitstellung einer automatisierten Anlieferungsschnittstelle für Zulieferer</li>
                    <li>Konzeption und Implementierung einer Schnittstelle zur strukturierten Speicherung von Metadaten über Steuergeräteinformationen</li>
                </ul>
            </div>
        </div>
        
        <div class="job">
            <div class="job-title">Software Architekt</div>
            <div class="job-company">Continental Automotive GmbH, he[a]t SW Technologies, Regensburg</div>
            <div class="job-date">03/2020 - 12/2022</div>
            <div class="job-description">
                <ul>
                    <li>Entwicklung und Wartung der CI/CD Umgebung von AUTOSAR Adaptive Projekten</li>
                    <li>Konzeption, Design und Entwicklung eines Reporting Frameworks</li>
                    <li>Einsatz von Conan.io als System Integrations Werkzeug</li>
                    <li>Entwicklung von REST-APIs als Schnittstelle zu Datenbanken und weiteren Microservices</li>
                </ul>
            </div>
        </div>
        
        <div class="job">
            <div class="job-title">Software Engineer</div>
            <div class="job-company">Continental Automotive GmbH, Software Center of Competence, Regensburg</div>
            <div class="job-date">07/2017 - 03/2020</div>
            <div class="job-description">
                <ul>
                    <li>Automatisierung von Softwareentwicklungsprojekten mit Hilfe von Continuous Integration</li>
                    <li>Automatisiertes Data Reporting und deren Verarbeitung mit Hilfe einer NoSQL-Datenbank</li>
                    <li>Entwicklung einer REST-API mit Spring Boot zur einfachen und automatisierten Interaktion mit der NoSQL-Datenbank</li>
                    <li>Bereitstellung einer Single-Page-Webanwendung mittels JSF zur Visualisierung von Projektkennzahlen</li>
                </ul>
            </div>
        </div>
        
        <div class="job">
            <div class="job-title">Software Engineer</div>
            <div class="job-company">Continental Automotive GmbH, AUTOSAR Center, Regensburg</div>
            <div class="job-date">04/2013 - 06/2017</div>
            <div class="job-description">
                <ul>
                    <li>Erstellung von System- und Akzeptanztest für Ethernet im Automotive und AUTOSAR Umfeld</li>
                    <li>Mitentwicklung eines Testtools zur Erstellung von Integrations- und Systemtests</li>
                    <li>Konfiguration eines Continuous Integration Servers und Automatisierung des CI Prozesses</li>
                    <li>Integration eines Ethernet-Stacks im AUTOSAR Umfeld</li>
                </ul>
            </div>
        </div>
        
        <div class="job">
            <div class="job-title">Masterand</div>
            <div class="job-company">Continental Engineering Services GmbH, AUTOSAR Center, Regensburg</div>
            <div class="job-date">08/2012 - 02/2013</div>
            <div class="job-description">
                <ul>
                    <li>Thema: Konzeption und Entwicklung einer Testumgebung und zugehöriger Testfälle im Bereich der Integration eines TCP/IP-Stacks in AUTOSAR</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="two-columns">
        <div>
            <div class="section">
                <h2>Ausbildung</h2>
                <div class="education">
                    <h3>Masterstudium Informatik</h3>
                    <p><strong>Hochschule Regensburg</strong> | 10/2011 - 02/2013</p>
                    <p>Schwerpunkt: Technical Systems</p>
                </div>
                <div class="education">
                    <h3>Bachelorstudium Informatik</h3>
                    <p><strong>Hochschule Ingolstadt</strong> | 10/2007 - 09/2011</p>
                    <p>Fachrichtung: Allgemein</p>
                </div>
                <div class="education">
                    <h3>Fachhochschulreife</h3>
                    <p><strong>Maximilian-Kolbe-Schule Neumarkt (Fachoberschule)</strong> | 09/2005 - 07/2007</p>
                    <p>Fachrichtung: Wirtschaft</p>
                </div>
            </div>
            
            <div class="section">
                <h2>Technische Fähigkeiten</h2>
                <p><strong>Projektkoordination:</strong><br>
                Agile Softwareentwicklung mit SCRUM und SAFe, Product Ownership, JIRA und Confluence</p>
                
                <p><strong>Software Design und Architektur:</strong><br>
                UML Modellierung, Design Patterns, Objektorientierte Programmierung, Microservices und REST-APIs</p>
                
                <p><strong>Continuous Integration and Delivery:</strong><br>
                CI/CD, Automatisierte Software Tests, Build Automatisierung (Gradle, Maven, Conan), Jenkins, GitHub Actions, Docker, Kubernetes</p>
                
                <p><strong>Programmiersprachen:</strong><br>
                Java/Groovy, Python, C/C++</p>
                
                <p><strong>Tools:</strong><br>
                Git/GitHub, Eclipse/IntelliJ IDEA/VS Code, Enterprise Architect/PlantUML, Spring Boot, Windows und Linux, MS-Office, Atlassian, Artifactory</p>
                
                <p><strong>Datenbanken:</strong><br>
                SQL Datenbanken (Oracle), NoSQL-Datenbanken (MongoDB)</p>
                
                <p><strong>Webentwicklung:</strong><br>
                HTML, CSS, JavaScript, Apache Tomcat, Wildfly, JSF, Primefaces</p>
                
                <p><strong>AUTOSAR Classic:</strong><br>
                Methodologie, Communication Stack (insbesondere Ethernet)</p>
            </div>
            
            <div class="section">
                <h2>Sprachen</h2>
                <ul>
                    <li><strong>Deutsch:</strong> Muttersprache</li>
                    <li><strong>Englisch:</strong> Fließend</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>Hobbys & Interessen</h2>
                <ul>
                    <li><strong>Fußball:</strong> Aktiver Spieler im Verein</li>
                    <li><strong>Laufen:</strong> Marathon-Läufer</li>
                    <li><strong>Radfahren:</strong> Mountain Biking und Rennrad</li>
                    <li><strong>Kochen:</strong> Internationale Küche</li>
                    <li><strong>Heimwerken:</strong> DIY-Projekte</li>
                    <li><strong>Weiterbildung:</strong> Tech-Blogs und Online-Kurse</li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>
    """
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        try:
            page = await browser.new_page()
            await page.set_content(simple_html, wait_until='networkidle')
            
            output_file = 'generated/Julian-Banek-CV.pdf'
            
            # Stelle sicher, dass der generated Ordner existiert
            Path('generated').mkdir(exist_ok=True)
            
            await page.pdf(
                path=output_file,
                format='A4',
                print_background=True,
                margin={
                    'top': '15mm',
                    'right': '15mm',
                    'bottom': '15mm',
                    'left': '15mm'
                }
            )
            
            print(f"=> Einfaches PDF erstellt: {output_file}")
            print(f"=> Speicherort: {Path(output_file).absolute()}")
            
        except Exception as e:
            print(f"=> Fehler: {e}")
            
        finally:
            await browser.close()

async def generate_website_pdf():
    """Generiert PDF von der Website (kann Layout-Probleme haben)"""
    print("=> Erstelle PDF von Website...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-web-security'
            ]
        )
        
        try:
            page = await browser.new_page()
            await page.set_viewport_size({'width': 1920, 'height': 1080})
            
            # HTML-Datei laden
            html_file = Path(__file__).parent / 'index-clean.html'
            html_url = f'file://{html_file.absolute()}'
            
            print(f"=> Lade Website: {html_url}")
            
            await page.goto(html_url, wait_until='networkidle')
            await asyncio.sleep(4)
            
            # CSS für PDF-Layout injizieren
            await page.add_style_tag(content="""
                @media print, screen {
                    * {
                        -webkit-print-color-adjust: exact !important;
                        color-adjust: exact !important;
                        box-sizing: border-box !important;
                    }
                    
                    body { 
                        margin: 0 !important;
                        padding: 0 !important;
                        overflow: visible !important;
                        height: auto !important;
                        font-size: 11px !important;
                        line-height: 1.3 !important;
                        background: white !important;
                    }
                    
                    /* Remove fixed positioning - convert to static layout */
                    .sidebar {
                        position: static !important;
                        width: 100% !important;
                        height: auto !important;
                        max-width: none !important;
                        margin: 0 !important;
                        padding: 15px !important;
                        page-break-inside: avoid !important;
                        background: linear-gradient(135deg, #2c3e50 0%, #3a4d63 100%) !important;
                    }
                    
                    /* Main content adjustments */
                    .main-content {
                        margin-left: 0 !important;
                        width: 100% !important;
                        padding: 15px !important;
                        position: static !important;
                    }
                    
                    /* Hide animations and interactive elements */
                    .banner-animation, .code-line, .typewriter {
                        display: none !important;
                    }
                    
                    /* Section spacing */
                    .section {
                        margin: 10px 0 !important;
                        padding: 8px 0 !important;
                        page-break-inside: avoid !important;
                    }
                    
                    .section h2 {
                        font-size: 14px !important;
                        margin: 8px 0 5px !important;
                        page-break-after: avoid !important;
                    }
                    
                    /* Timeline adjustments */
                    .timeline {
                        margin: 5px 0 !important;
                    }
                    
                    .timeline-item {
                        margin: 5px 0 !important;
                        padding: 5px !important;
                        page-break-inside: avoid !important;
                        font-size: 10px !important;
                    }
                    
                    /* Remove unnecessary spacing */
                    .wrapper, #wrapper {
                        margin: 0 !important;
                        padding: 0 !important;
                        max-width: none !important;
                    }
                    
                    /* Force single column layout */
                    .columns {
                        display: block !important;
                        column-count: 1 !important;
                    }
                }
            """)
            
            output_file = 'generated/Julian-Banek-CV-Website.pdf'
            
            # Stelle sicher, dass der generated Ordner existiert
            Path('generated').mkdir(exist_ok=True)
            
            await page.pdf(
                path=output_file,
                format='A4',
                print_background=True,
                margin={
                    'top': '5mm',
                    'right': '5mm', 
                    'bottom': '5mm',
                    'left': '5mm'
                },
                prefer_css_page_size=False,
                display_header_footer=False,
                scale=0.75
            )
            
            print(f"=> Website-PDF erstellt: {output_file}")
            print(f"=> Speicherort: {Path(output_file).absolute()}")
            
        except Exception as e:
            print(f"=> Fehler beim PDF-Export: {e}")
            
        finally:
            await browser.close()

def show_menu():
    """Zeigt das Auswahlmenü"""
    print("=" * 50)
    print("=> CV PDF Generator")
    print("=" * 50)
    print("Waehle eine Option:")
    print()
    print("1.  Einfaches PDF erstellen (EMPFOHLEN)")
    print("    + Funktioniert garantiert")
    print("    + Kompakte 2 Seiten")
    print("    + Professionelles Design")
    print()
    print("2.  PDF von Website erstellen")
    print("    ! Kann Layout-Probleme haben")
    print("    ! Moeglicherweise leere Seiten")
    print("    + Originales Website-Design")
    print()
    print("3.  Beide Versionen erstellen")
    print("    + Erstellt beide PDFs zum Vergleich")
    print()
    print("0.  Beenden")
    print("=" * 50)

async def main():
    """Hauptfunktion mit Menü"""
    while True:
        show_menu()
        choice = input("Deine Wahl (1-3, 0 zum Beenden): ").strip()
        
        if choice == "1":
            print("\n=> Erstelle einfaches PDF...")
            await generate_simple_pdf()
            print("\n=> Fertig! Druecke Enter um fortzufahren...")
            input()
            
        elif choice == "2":
            print("\n=> Erstelle Website-PDF...")
            await generate_website_pdf()
            print("\n=> Fertig! Druecke Enter um fortzufahren...")
            input()
            
        elif choice == "3":
            print("\n=> Erstelle beide Versionen...")
            await generate_simple_pdf()
            print()
            await generate_website_pdf()
            print("\n=> Beide PDFs erstellt! Druecke Enter um fortzufahren...")
            input()
            
        elif choice == "0":
            print("\n=> Auf Wiedersehen!")
            break
            
        else:
            print("\n=> Ungueltibe Eingabe. Bitte waehle 1, 2, 3 oder 0.")
            input("Druecke Enter um fortzufahren...")

if __name__ == "__main__":
    # Überprüfe Kommandozeilenargumente für direkten Aufruf
    if len(sys.argv) > 1:
        if sys.argv[1] == "simple":
            asyncio.run(generate_simple_pdf())
        elif sys.argv[1] == "website":
            asyncio.run(generate_website_pdf())
        elif sys.argv[1] == "both":
            asyncio.run(generate_simple_pdf())
            asyncio.run(generate_website_pdf())
        else:
            print("Usage: python cv_pdf_generator.py [simple|website|both]")
    else:
        # Interaktives Menü
        asyncio.run(main())
