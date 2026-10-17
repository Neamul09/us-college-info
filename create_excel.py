import csv
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Read enriched CSV
with open('US_Colleges_Fall_2027_Full_Ride_Neon.csv', mode='r', encoding='utf-8-sig') as f:
    reader = list(csv.reader(f))

headers = reader[0]
rows = reader[1:]

wb = openpyxl.Workbook()

# Setup Sheet 1: Master Database
ws = wb.active
ws.title = "Master Database (98 Colleges)"

# Palette definition
navy_header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
zebra_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color='E2E8F0'),
    right=Side(style='thin', color='E2E8F0'),
    top=Side(style='thin', color='E2E8F0'),
    bottom=Side(style='thin', color='E2E8F0')
)

# Write headers
for col_idx, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_idx, value=header)
    cell.fill = navy_header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border
ws.row_dimensions[1].height = 42

# Write data rows
for row_idx, row_data in enumerate(rows, 2):
    fill = zebra_fill if row_idx % 2 == 0 else white_fill
    for col_idx, value in enumerate(row_data, 1):
        cell = ws.cell(row=row_idx, column=col_idx, value=value)
        cell.fill = fill
        cell.font = Font(name="Calibri", size=10)
        cell.border = thin_border
        
        # Text alignments
        if col_idx in [1, 2, 3]: # Name, Type, Location
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        elif col_idx in [8, 9, 14, 15, 16, 22]: # Deadlines, Strategy, Probabilities, Visa, Tier
            cell.alignment = Alignment(horizontal="center", vertical="top", wrap_text=True)
        else:
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            
        # Highlight high probability
        if col_idx == 15: # Neon's Prob
            try:
                p_val = float(value.split('%')[0].split('-')[0].strip())
                if p_val >= 12.0:
                    cell.font = Font(name="Calibri", size=10, bold=True, color="166534") # dark green
                elif p_val >= 5.0:
                    cell.font = Font(name="Calibri", size=10, bold=True, color="854D0E") # amber
                else:
                    cell.font = Font(name="Calibri", size=10, color="991B1B") # red
            except:
                pass
                
        # Highlight Primary ED1
        if col_idx == 9 and "PRIMARY ED1" in value:
            cell.fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
            cell.font = Font(name="Calibri", size=10, bold=True, color="92400E")
    ws.row_dimensions[row_idx].height = 70

# Freeze top row
ws.freeze_panes = "A2"

# Auto-adjust column widths with bounds
col_widths = {
    1: 32, # Institution Name
    2: 24, # Type
    3: 18, # Location
    4: 38, # CS Highlights
    5: 35, # Aid Policy
    6: 28, # Max Aid
    7: 15, # $0 EFC Covered
    8: 24, # Deadlines
    9: 32, # Testing Strategy Round
    10: 24, # Nov SAT Policy
    11: 28, # Target SAT
    12: 28, # English Proficiency
    13: 38, # Testing Nuance
    14: 20, # Int'l Admit Rate
    15: 18, # Neon's Prob
    16: 38, # Visa Safety Index
    17: 45, # Required Docs
    18: 35, # Fee Waiver Availability
    19: 25, # Testing Policy
    20: 35, # Prior Coursework
    21: 45, # Extra Info
    22: 25  # Tier Category
}

for col_idx, width in col_widths.items():
    ws.column_dimensions[get_column_letter(col_idx)].width = width

# Enable auto filter
ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(rows)+1}"

# Sheet 2: Application Roadmap & Strategy
ws2 = wb.create_sheet(title="Strategy & Testing Roadmap")
ws2.views.sheetView[0].showGridLines = True

roadmap_headers = ["Strategic Round", "Application Deadline", "Testing Policy & Scores Used", "Recommended Colleges for Neon", "Core Strategy & Action Items"]
for c_idx, h in enumerate(roadmap_headers, 1):
    c = ws2.cell(row=1, column=c_idx, value=h)
    c.fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    c.alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[1].height = 32

roadmap_rows = [
    [
        "Early Decision I (ED1) — PRIMARY",
        "Nov 15, 2026",
        "SAT: 100% OPTIONAL | DET: 100% OPTIONAL (Does not require any standardized test). Optional Nov 7 SAT upload if 1550+.",
        "BOWDOIN COLLEGE (Brunswick, ME) — Ranked #5 US LAC",
        "Bowdoin is Need-Blind for internationals and meets 100% demonstrated need with $0 loans. Submitting test-optional protects your chances. If admitted, I-20 guarantees a 100% full ride, ensuring 99% visa approval at the Dhaka Embassy."
    ],
    [
        "Early Decision I (ED1) — ALTERNATIVE",
        "Nov 15, 2026",
        "SAT: 100% OPTIONAL | DET: Optional / Flexible (waivable via interview).",
        "COLBY COLLEGE (Waterville, ME) — Davis Institute for AI",
        "Colby is home to the first dedicated AI institute at an American LAC. Highly synergistic with your biomedical deep learning research. 3x-4x acceptance boost in ED1. $0 application fee, free ISFAA."
    ],
    [
        "Early Action (EA) — Non-Binding",
        "Nov 1 – Dec 1, 2026",
        "Self-report October SAT + Rushes/Uploads November 7 SAT + DET",
        "MIT (Need-Blind EA - accepts Nov 7 SAT), Denison University (EA: Nov 15), Berea College (Priority EA: Nov 30), DePauw, St. Olaf, Earlham",
        "Non-binding early applications. Berea College provides guaranteed 100% Tuition Promise. MIT reviews November SAT for EA. Free applications and free ISFAA forms."
    ],
    [
        "Premier Full-Ride Merit Deadlines",
        "Nov 15 – Dec 1, 2026",
        "Powered by November 7 SAT (Target 1550+, Math 800) + DET (135+)",
        "University of Richmond (Richmond Scholars - Dec 1), Boston University (Trustee Full Tuition - Dec 1), UT Dallas (AES/McDermott - Dec 1), Miami (Stamps - EA)",
        "Crucial for 100% full-ride funding without need-awareness. These scholarships require separate supplemental essays or early submission. Prestigious named scholarships guarantee smooth Dhaka visa interviews."
    ],
    [
        "Early Decision II (ED2) — Second Shot",
        "Jan 1 – Jan 15, 2027",
        "Powered by November 7 SAT (1550+) + Verified DET (135+)",
        "WashU in St. Louis (Jan 2), Vanderbilt University (Jan 1), Carleton College (Jan 15), Grinnell College (Jan 5), Lafayette College (Jan 15)",
        "If Bowdoin ED1 does not yield an admit, ED2 offers a binding second chance at elite institutions that commit to 100% demonstrated need."
    ],
    [
        "Regular Admission (RA / RD) — Full Broad Sweep",
        "Jan 1 – Feb 1, 2027",
        "Powered by Superscored October + November SAT (1550+) + DET (135+)",
        "Need-Blind Ivies (Harvard, Princeton, Yale, Dartmouth, Amherst) + Johns Hopkins (Biomedical AI) + 25 High-Aid LACs (Wooster, Knox, Denison, Union, Dickinson, etc.)",
        "Cast a broad net across 25–30 institutions. Ensure 100% fee waivers are secured via Common App waiver, ISFAA free uploads, or institutional codes."
    ]
]

for r_idx, r_data in enumerate(roadmap_rows, 2):
    for c_idx, val in enumerate(r_data, 1):
        c = ws2.cell(row=r_idx, column=c_idx, value=val)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ws2.row_dimensions[r_idx].height = 60

ws2.column_dimensions['A'].width = 25
ws2.column_dimensions['B'].width = 18
ws2.column_dimensions['C'].width = 35
ws2.column_dimensions['D'].width = 35
ws2.column_dimensions['E'].width = 48

# Sheet 3: Bangladesh F-1 Visa Guide
ws3 = wb.create_sheet(title="Bangladesh F-1 Visa Guide")
ws3.views.sheetView[0].showGridLines = True

visa_headers = ["Visa Dimension", "Dhaka Embassy Reality", "Why Neon's Profile Wins", "Exact Interview Script / Action Item"]
for c_idx, h in enumerate(visa_headers, 1):
    c = ws3.cell(row=1, column=c_idx, value=h)
    c.fill = PatternFill(start_color="047857", end_color="047857", fill_type="solid")
    c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    c.alignment = Alignment(horizontal="center", vertical="center")
ws3.row_dimensions[1].height = 32

visa_rows = [
    [
        "Section 214(b) Financial Scrutiny",
        "The #1 cause of visa refusals in Dhaka is an unconvincing financial sponsor or a deficit on the I-20 requiring personal bank deposits.",
        "Every recommended university provides a 100% Full Ride or Full Tuition. Your I-20 will state: Institutional Scholarship: $85,000 | Student/Family Funds: $0.",
        "When VO asks 'Who is sponsoring you?': 'I was awarded a full scholarship by [University Name] covering 100% of my tuition, room, board, and health insurance based on my academic and software engineering achievements.'"
    ],
    [
        "Post-2023 HSC Timeline Justification",
        "Dhaka consular officers interrogate study gaps post-high school to determine if the applicant is genuine and academically engaged.",
        "You have tangible, verifiable national technical achievements: Top 40 Android Dev among 100k+, Biomedical AI co-authored paper, CholoSikhi SAT platform, Chitro AI.",
        "When VO asks 'What have you been doing since 2023?': 'I spent this period conducting biomedical deep learning research, co-authoring a paper on medical image classification, building two web platforms with thousands of users, and ranking in the Top 40 nationwide among 100,000 developers in Bangladesh's National Android Bootcamp.'"
    ],
    [
        "Institutional Prestige & Recognition",
        "Consular officers heavily prioritize accredited, top-ranked institutions. Low-tier regional colleges trigger suspicion.",
        "Bowdoin (Ranked #5 US LAC), MIT, Harvard, Dartmouth, Colby, Williams, and Amherst have instant brand equity and near 99% visa issuance rates.",
        "Carry your official award letter and acceptance packet signed by the Dean of Admissions. Consular officers know these institutions do not give full rides lightly."
    ],
    [
        "Non-Immigrant Intent & Ties to Bangladesh",
        "Applicants must demonstrate their degree will be utilized upon graduation rather than seeking permanent migration immediately.",
        "Bangladesh has an exploding tech and telecom ecosystem (national developer platforms, Robi Axiata, bKash). Your campus ambassadorship and tech products prove deep local roots.",
        "When VO asks 'What are your future plans?': 'I plan to return to Bangladesh to work in applied AI and healthcare technology. My research in medical computer vision has shown me the acute need for automated diagnostic tools in our national healthcare infrastructure.'"
    ]
]

for r_idx, r_data in enumerate(visa_rows, 2):
    for c_idx, val in enumerate(r_data, 1):
        c = ws3.cell(row=r_idx, column=c_idx, value=val)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ws3.row_dimensions[r_idx].height = 65

ws3.column_dimensions['A'].width = 24
ws3.column_dimensions['B'].width = 35
ws3.column_dimensions['C'].width = 38
ws3.column_dimensions['D'].width = 50

# Sheet 4: Document & Zero-Cost Checklist
ws4 = wb.create_sheet(title="Document & Zero-Cost Checklist")
ws4.views.sheetView[0].showGridLines = True

checklist_headers = ["Category", "Item / Document Name", "Issuing Body / Platform", "Zero-Cost Protocol / Waiver Instructions", "Strategic Notes for Neon"]
for c_idx, h in enumerate(checklist_headers, 1):
    c = ws4.cell(row=1, column=c_idx, value=h)
    c.fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
    c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    c.alignment = Alignment(horizontal="center", vertical="center")
ws4.row_dimensions[1].height = 30

checklist_rows = [
    ["Application Fee", "Common Application Fee Waiver", "Common App Profile", "Select 'Yes' under Common App Fee Waiver (Eligible based on orphan status / zero family income). Counselor checks confirmation box.", "Saves ~$75–$90 per university across all 50+ schools ($4,000+ total savings)."],
    ["Financial Aid Form", "CSS Profile Fee Waiver", "College Board / University Financial Aid Offices", "Email admissions/financial aid offices in October requesting an institutional CSS Profile Fee Waiver Code. If unavailable, submit free ISFAA PDF.", "Never pay the $25 + $16 per school fee. Colleges like Dartmouth, Colby, Bowdoin, Skidmore, Denison accept free ISFAA directly on portal."],
    ["Financial Form", "Free ISFAA / PFAA", "College Websites / Portals", "Download the International Student Financial Aid Application (ISFAA) PDF form, complete it, and upload directly to applicant portal.", "Princeton uses its own free PFAA portal. Many LACs accept paper/PDF ISFAA for free."],
    ["Financial Proof", "Parental Loss & Non-Income Affidavit", "Notary Public / Bangladesh Local Government", "Official death certificates of both parents translated into English, accompanied by an affidavit stating zero parental support and legal orphan status.", "Critical for establishing $0 Expected Family Contribution (EFC) without dispute."],
    ["Financial Proof", "Asset Declaration (Land/House)", "Local Land Authority / Valuation", "Declare the residential house/land with realistic local municipal valuation, explicitly noting that it generates $0 income and is non-liquid.", "Prevents financial aid officers from assuming hidden rental income."],
    ["Academic Records", "SSC & HSC Official Marksheets & Certificates", "BISE (Bangladesh Education Board)", "Certified copies of SSC 2021 (GPA 5.00) and HSC 2023 (GPA 5.00) official marksheets and certificates.", "Must be officially attested by school principal/headmaster and uploaded by counselor."],
    ["Recommendations", "School Counselor Recommendation", "High School / College Counselor or Principal", "Comprehensive letter detailing Neon's extreme resilience, leadership, and national accolades despite tragic parental loss.", "Counselor must confirm fee waiver eligibility on Common App."],
    ["Recommendations", "2 Academic Teacher Evaluations", "High School Teachers", "Letter 1: Mathematics or Physics teacher (highlighting 184/200 Physics, Olympiad Bronze, and problem solving). Letter 2: ICT/English teacher (highlighting software passion).", "Letters should emphasize independent intellectual curiosity and perseverance."],
    ["Testing", "SAT Score Report", "College Board", "Self-report scores on Common App and university portals (100% free at 90%+ of universities).", "Only send official College Board score reports to the few schools requiring them upon admission or enrollment."],
    ["Testing", "English Proficiency (DET / IELTS)", "Duolingo / British Council", "Request Duolingo fee waiver coupon from college admissions, or request SAT EBRW waiver (EBRW 650–700+ waives DET at most colleges).", "Duolingo allows testing from home at zero cost if waiver coupon is granted."],
    ["Supplemental", "Biomedical AI Research Abstract", "Published Paper / Manuscript", "Upload a 1–2 page PDF abstract + manuscript link in the application portal (Monkeypox/Chickenpox deep learning with Grad-CAM & ConvNeXt, 93% accuracy).", "Third author publication proves collegiate-level research readiness in AI."],
    ["Supplemental", "Maker Portfolio / Project Showcase", "GitHub / Live Project Links", "Submit Slideroom maker portfolio or add links to CholoSikhi (SAT platform), Chitro AI, MedVision AI, and Top 40 Android Bootcamp certificate.", "Concrete evidence of product-building ability and massive real-world impact."]
]

for r_idx, r_data in enumerate(checklist_rows, 2):
    for c_idx, val in enumerate(r_data, 1):
        c = ws4.cell(row=r_idx, column=c_idx, value=val)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ws4.row_dimensions[r_idx].height = 45

ws4.column_dimensions['A'].width = 18
ws4.column_dimensions['B'].width = 30
ws4.column_dimensions['C'].width = 25
ws4.column_dimensions['D'].width = 42
ws4.column_dimensions['E'].width = 45

# Save workbook
wb.save('US_Colleges_Fall_2027_Full_Ride_Neon.xlsx')
print("Successfully generated updated Excel workbook with Bangladesh Visa Guide & Testing Roadmap: US_Colleges_Fall_2027_Full_Ride_Neon.xlsx")
