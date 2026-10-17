# 🎓 U.S. College Admissions & Full-Ride Navigator (Fall 2027)

> **Verified Database & Strategic Dossier of 160 U.S. Universities Offering Full Rides ($0 EFC), Need-Blind Financial Aid, and Full-Tuition Merit Scholarships for Bangladeshi & International Undergraduates.**

[![Deploy GitHub Pages](https://github.com/Neamul09/us-college-info/actions/workflows/pages.yml/badge.svg)](https://github.com/Neamul09/us-college-info/actions/workflows/pages.yml)
[![Live Site](https://img.shields.io/badge/GitHub%20Pages-Live%20Portal-success?style=flat&logo=github)](https://neamul09.github.io/us-college-info/)
[![Colleges](https://img.shields.io/badge/Verified%20Institutions-160-blue?style=flat)](https://neamul09.github.io/us-college-info/)
[![CDS Verified](https://img.shields.io/badge/Common%20Data%20Set-CDS%20Sec.%20C9%20%26%20H6-purple?style=flat)](https://neamul09.github.io/us-college-info/)

---

## 🌐 Live Web Portals & Deliverables

| Deliverable | Format | Access Link / Download |
| :--- | :---: | :--- |
| **Interactive Admissions & Scholarship Portal** | Web App | [🔗 Open Live Portal](https://neamul09.github.io/us-college-info/) |
| **University Application Checklist & Dossier** | Web App | [📋 Open Application Dossier](https://neamul09.github.io/us-college-info/University_Application_Dossier.html) |
| **BDtoUSA Fall 2027 Admissions Guide** | PDF | [📄 Download Admissions Guide (PDF)](https://neamul09.github.io/us-college-info/BDtoUSA_Fall_2027_Full_Ride_Admissions_Guide.pdf) |
| **Master Institutional Directory & Strategy Workbook** | Excel (.xlsx) | [📊 Download Excel Directory](https://raw.githubusercontent.com/Neamul09/us-college-info/main/US_Colleges_Fall_2027_Full_Ride_BDtoUSA.xlsx) |
| **Master Dataset (48 Verified Columns)** | CSV (.csv) | [📑 Download Dataset (CSV)](https://raw.githubusercontent.com/Neamul09/us-college-info/main/US_Colleges_Fall_2027_Full_Ride_BDtoUSA.csv) |
| **Complete Enriched JSON Database** | JSON | [💾 View raw JSON](https://raw.githubusercontent.com/Neamul09/us-college-info/main/enriched_colleges.json) |

---

## 🚀 Key Features

### 1. Common Data Set (CDS Section H6) International Aid Verification
- **Average International Financial Aid Award ($/year):** Verified institutional grant amounts awarded strictly to undergraduate non-resident international scholars.
- **Percentage (%) and Count of International Students Aided:** Exactly what fraction of international undergraduates receive institutional scholarship funds.
- **Total International Aid Budget:** Institutional annual grant allocations (e.g. Harvard $41M+, Amherst $16.5M+, Bowdoin $12.3M+).
- **Loan-Free Guarantee:** Institutions meeting 100% demonstrated financial need without student loans.

### 2. Bank Statement / Certification of Finances (COF) Timing Protocol
- **Deferred Bank Statement ($0 Balance at Application):** Clear identification of institutions that only require financial declarations at submission (e.g., Bowdoin, Colby, Amherst, Princeton) and defer formal bank balance solvency certificates until **after admission** for Form I-20 issuance.
- **Required at Application:** Colleges that mandate a certified bank solvency statement showing sponsor balances before application review.

### 3. November 7 SAT Score Release Strategy (November 20 Release Date)
- **Dec 1 Priority & Merit Deadlines (100% Compatible):** Boston University Trustee, Richmond Scholars, UT Dallas AES/McDermott. Scores arrive 10 days before deadlines.
- **Nov 15 ED1 Deadlines (Conditional Portal Upload):** Apply by Nov 15 as test-optional/pending Nov SAT (e.g., Bowdoin, Colby, Bates); upload official score report PDF to the applicant portal immediately upon release on Nov 20 before December committee review.
- **Nov 1 Early Deadlines (Tactical Safety Policy):** Submit Common App on Nov 1 as test-optional; upload score on Nov 20 to portal only if score is $\ge 1520$.
- **ED2 & Regular Decision (100% Compatible):** Complete scores are in hand 6 weeks prior to January deadlines.

### 4. Application Costs & Fee Waivers
- **$0 Application Fee:** Institutions with no application fees for anyone (e.g., Colby, Carleton, St. Olaf, Denison, Kenyon, Grinnell, Macalester).
- **Free ISFAA / PFAA / BSAA:** Institutions accepting free PDF financial aid forms uploaded directly to their portal, saving the College Board CSS Profile fee ($25 + $16 per school).

### 5. Dhaka Embassy F-1 Visa Safety & INA § 214(b) Mitigation
- Complete formula on how a verified full-ride award letter showing $0 parental contribution on Form I-20 eliminates consular financial scrutiny at the U.S. Embassy in Dhaka.
- Scripts for handling post-HSC study gaps, academic research, and non-immigrant intent.

---

## 📂 Repository File Structure

```text
├── .github/
│   └── workflows/
│       └── pages.yml                           # Automated GitHub Pages CI/CD workflow
├── .gitignore                                  # Standard Git ignore rules
├── .nojekyll                                   # Disables Jekyll processing for raw static hosting
├── index.html                                  # Primary Interactive Spreadsheet & Portal (GitHub Pages Root)
├── Interactive_College_Spreadsheet.html         # Interactive Directory Web Application
├── University_Application_Dossier.html         # Application Checklist & Requirements Dossier
├── BDtoUSA_Fall_2027_Full_Ride_Admissions_Guide.pdf # Printable PDF Admissions Handbook
├── US_Colleges_Fall_2027_Full_Ride_BDtoUSA.xlsx# 4-Sheet Comprehensive Excel Workbook
├── US_Colleges_Fall_2027_Full_Ride_BDtoUSA.csv # 48-Column Clean CSV Dataset
├── enriched_colleges.json                      # Master JSON database (160 colleges)
├── build_html_portal.py                        # Compiler script for Interactive Spreadsheet & index.html
├── build_dossier_html.py                       # Compiler script for University Application Dossier
├── build_all_deliverables.py                   # Compiler script for Excel & CSV files
├── generate_pdf_guide.py                       # ReportLab script for PDF Guide generation
└── README.md                                   # Comprehensive documentation
```

---

## 🛠️ Local Development & Regeneration

To regenerate any deliverable locally from `enriched_colleges.json`:

```bash
# Rebuild Interactive Spreadsheet and index.html
py build_html_portal.py

# Rebuild Application Requirements Dossier
py build_dossier_html.py

# Rebuild Excel (.xlsx) and CSV (.csv) Deliverables
py build_all_deliverables.py

# Rebuild Admissions Guide PDF
py generate_pdf_guide.py
```

---

## ⚖️ License & Attribution

Compiled and maintained for Bangladeshi and high-need international undergraduate applicants pursuing full-ride funding in the United States. All institutional testing and financial aid data verified against official institutional Common Data Set (CDS) publications and admissions portals.
