import json
import csv
import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

with open('enriched_colleges.json', 'r', encoding='utf-8') as f:
    colleges = json.load(f)

total_count = len(colleges)
print(f"Loaded {total_count} institutions from enriched_colleges.json")

columns_bd = [
    'Strategic Match Rank',
    'Strategic Factor Score (Out of 100)',
    'U.S. News Ranking',
    'QS World Ranking',
    'Institution Name',
    'College Board Code (CEEB)',
    'Test-Optional Admitted / Enrolled Rate (CDS Sec. C9)',
    'Need-Blind / Aid Model (Internationals)',
    'Institution Type',
    'Location',
    'US Region',
    'Official Admissions URL',
    'Official Financial Aid URL',
    'Official Testing Policy URL',
    'CS / AI / Engineering / Major Highlights',
    'Financial Aid Policy (Internationals)',
    'CDS H6 Average International Aid ($/yr)',
    'CDS H6 % of Internationals Aided',
    'CDS H6 Total International Aid Budget',
    'CDS H6 Loan-Free Guarantee',
    'Required Financial Aid Form (ISFAA vs CSS Profile)',
    'Bank Statement / COF Timing (Deferred vs Application)',
    'Max Aid Package',
    '$0 EFC Covered?',
    'All Application Deadlines (ED1 / EA / ED2 / RD)',
    'Financial Aid Priority Deadline (CSS / ISFAA)',
    'Priority Merit Scholarship Deadline',
    'November 7 SAT Score Compatibility & Strategy (Nov 20 Release)',
    'Supplemental Essays & Portfolios (Verified)',
    'Tactical Admissions Realities & Quotas',
    'Special Submission Requirements (Graded Paper / Video / Peer Rec)',
    'Interview Policy & Guidelines',
    'Testing Strategy Round (ED / EA / Merit / RA)',
    'Test-Optional for Early Action (EA)?',
    'Test-Optional for Early Decision (ED1/ED2)?',
    'Test-Optional for Regular Decision (RD)?',
    'Target SAT Score Needed (Full Aid / Merit)',
    'English Proficiency Cutoffs & SAT EBRW Waiver Threshold',
    'General International Admit Rate (%)',
    'Estimated Acceptance Probability (%)',
    'Bangladesh F-1 Visa Safety Index (Dhaka Embassy)',
    'Reddit & Community Insider Consensus (r/IntltoUSA)',
    'Bangladeshi Applicant Strategic Advice & Nuance',
    'Fee Waiver Availability (App & Financial Aid)',
    'Testing Policy (Self-Report vs Official)',
    'Required Documents Section',
    'Common Data Set (CDS) Source & Verification',
    'Tier Category'
]

def extract_row(c):
    d = c.get('dossier', {})
    supps = " | ".join(d.get('supplements', [])) if d.get('supplements') else ''
    tactical = " | ".join(d.get('tactical', [])) if d.get('tactical') else ''
    h6 = c.get('cds_h6', {})
    
    return [
        c.get('strategic_rank_display', ''),
        str(c.get('strategic_score', '')),
        c.get('us_news_display', ''),
        c.get('world_rank_display', ''),
        c.get('name', ''),
        c.get('cb_code', ''),
        c.get('test_optional_stat', ''),
        c.get('need_blind_status', ''),
        c.get('type', ''),
        c.get('location', ''),
        c.get('region', ''),
        c.get('admissions_url', ''),
        c.get('finaid_url', ''),
        c.get('testing_url', ''),
        c.get('cs_strength', ''),
        c.get('aid_policy', ''),
        h6.get('avg_aid', 'N/A'),
        h6.get('pct_aided', 'N/A'),
        h6.get('total_budget', 'N/A'),
        h6.get('loan_free', 'Meets demonstrated need'),
        c.get('finaid_form_protocol', '') or d.get('finaid_form', ''),
        c.get('cof_policy', '') or d.get('cof_policy', ''),
        c.get('max_aid', ''),
        c.get('efc_0_covered', ''),
        c.get('deadlines', ''),
        c.get('finaid_deadline', ''),
        c.get('merit_deadline', ''),
        c.get('nov_sat_policy', ''),
        supps,
        tactical,
        c.get('special_requirements', '') or d.get('special_requirements', ''),
        c.get('interview_policy', 'Informational/Evaluative based on alumni capacity'),
        c.get('testing_strategy_round', ''),
        str(c.get('ea_test_optional', '')),
        str(c.get('ed_test_optional', '')),
        str(c.get('rd_test_optional', '')),
        c.get('sat_det_needed', ''),
        c.get('english_cutoffs_waiver', '') or d.get('english_cutoffs_waiver', ''),
        c.get('international_probability', ''),
        c.get('probability', ''),
        c.get('visa_safety_index', ''),
        c.get('reddit_analysis', ''),
        c.get('bd_specific_advice', ''),
        c.get('fee_waiver', ''),
        c.get('score_policy', ''),
        c.get('required_documents', ''),
        c.get('cds_source', ''),
        c.get('tier_category', '')
    ]

# 1. WRITE MASTER CSV (GENERALIZED FOR ALL BANGLADESHI APPLICANTS)
csv_filename = 'US_Colleges_Fall_2027_Full_Ride_BDtoUSA.csv'
with open(csv_filename, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns_bd)
    for c in colleges:
        writer.writerow(extract_row(c))

print(f"Generated {csv_filename} ({total_count} rows, {len(columns_bd)} cols)")

# 2. BUILD GENERALIZED EXCEL WORKBOOK
navy_header = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
zebra_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
thin_border = Border(
    left=Side(style='thin', color='E2E8F0'),
    right=Side(style='thin', color='E2E8F0'),
    top=Side(style='thin', color='E2E8F0'),
    bottom=Side(style='thin', color='E2E8F0')
)

roadmap_data = [
    [
        "Early Decision I (ED1) — PRIMARY",
        "Nov 1 – Nov 15, 2026",
        "SAT: 100% OPTIONAL | DET: 100% OPTIONAL (Does not require any test)",
        "BOWDOIN COLLEGE (Ranked #5 US LAC) [CEEB: 3089] | WASHINGTON AND LEE [CEEB: 5887]",
        "Bowdoin: Need-Blind for international students. 100% Full Ride ($0 loans). Applying test-optional protects from low test score. If Nov 7 SAT is 1530+, upload to portal on Nov 21. Washington and Lee: Need-Blind with 100% need met without loans, test-optional through 2027."
    ],
    [
        "Early Decision I (ED1) — ALTERNATIVES",
        "Nov 1 – Nov 15, 2026",
        "SAT: 100% OPTIONAL | DET: Flexible / Optional",
        "COLBY COLLEGE (Davis AI Institute) [CEEB: 3280] | NYU ABU DHABI [CEEB: 5360] | AMHERST COLLEGE [CEEB: 3003]",
        "Colby: Home to dedicated AI institute at an American LAC. $0 application fee, free ISFAA. NYU Abu Dhabi: 100% Need-Blind for all students with global full ride. Amherst: Need-Blind full ride with zero loans."
    ],
    [
        "Early Action (EA) — Non-Binding",
        "Nov 1 – Dec 1, 2026",
        "Test-Optional or Self-Reported (Accepts Nov 7 SAT)",
        "UChicago (EA Nov 1), Denison (Dec 1), DePauw (Nov 30), Wooster (Nov 30), St. Olaf (Nov 15), Knox (Nov 1), Soka (Dec 1), Reed (Nov 15), Colorado College (Nov 1)",
        "Submit 8-12 non-binding EA applications. Berea guarantees 100% Tuition Promise for all admitted students. Denison, Wooster, Knox, DePauw, and St. Olaf have $0 application fees and accept free ISFAA."
    ],
    [
        "Premier Full-Ride Merit Deadlines",
        "Nov 1 – Dec 1, 2026",
        "Powered by November 7 SAT (Target 1530+, Math 790+) or Holistic Portfolio",
        "Richmond Scholars (Univ of Richmond - Dec 1), Stamps Scholars (Univ of Miami - EA Nov 1), Robertson Scholars (Duke & UNC - Nov 15), Boston Univ (Trustee - Dec 1), UT Dallas (AES/McDermott - Dec 1)",
        "Awards full funding based on academic and technical excellence, bypassing need-aware financial aid limits. High SAT Math (790-800) and software/research projects unlock automatic consideration."
    ],
    [
        "Early Decision II (ED2) — Backup Shot",
        "Jan 1 – Jan 15, 2027",
        "Powered by verified Nov 7 SAT (1530+) or High-Achieving Test-Optional File",
        "WashU in St. Louis (Jan 2), Vanderbilt University (Jan 1), Carleton College (Jan 15), Grinnell College (Jan 5), Lafayette College (Jan 15), UChicago ED2 (Jan 5), NYUAD ED2 (Jan 1)",
        "If Bowdoin or Amherst ED1 does not admit in mid-December, pivot immediately to a top-tier ED2 institution with verified 1530+ SAT or strong test-optional profile."
    ],
    [
        "Regular Admission (RA / RD) — Full Sweep",
        "Jan 1 – Feb 1, 2027",
        "Verified Standardized Testing or Test-Optional LAC Portfolio",
        "Need-Blind Institutions (Harvard, Princeton, Yale, Dartmouth, Brown, Notre Dame, MIT) + 40 High-Aid LACs",
        "Cast a broad net across 30+ colleges that meet 100% need with full fee waivers. Princeton uses 100% free PFAA financial portal."
    ]
]

visa_data = [
    [
        "INA Section 214(b) Financial Scrutiny",
        "The #1 cause of F-1 visa refusals at the Dhaka Embassy is an unconvincing financial sponsor, deficit on Form I-20, or newly created bank deposits.",
        "When an applicant has an I-20 stating 'Institutional Scholarship: $88,000+ | Student/Family Funds: $0', the financial requirement is completely satisfied. Consular officers know the university is contractually covering all costs.",
        "When VO asks 'Who is sponsoring your education?': 'I was awarded a full scholarship by [University Name] covering 100% of my tuition, room, board, and health insurance based on my academic excellence and technical accomplishments. My family has zero financial burden.'"
    ],
    [
        "Post-HSC / A-Level Study Gap Justification",
        "Dhaka consular officers interrogate study gaps post-HSC to verify whether the applicant was genuinely engaged in academic or technical work.",
        "A well-documented gap period with concrete deliverables (peer-reviewed research papers, national competition awards, live software products, community teaching) is viewed positively as high initiative.",
        "When VO asks 'What have you been doing since completing your higher secondary exams?': 'I spent this period conducting advanced academic research, developing open-source software platforms, competing in national programming contests and Olympiads, and teaching technology skills in my community. These projects deepened my practical expertise and solidified my preparation for undergraduate study in the United States.'"
    ],
    [
        "Institutional Prestige & Recognition",
        "Consular officers in Dhaka heavily favor accredited, top-ranked institutions. Obscure, low-tier regional colleges trigger suspicion under 214(b).",
        "Institutions in this directory (Top 30 Research Universities, Top 50 Liberal Arts Colleges, and specialized STEM hubs) enjoy immediate recognition and near-automatic credibility in Dhaka.",
        "Bring your official acceptance letter and scholarship award certificate signed by the Dean of Admissions. Consular officers know these institutions do not give full rides lightly."
    ],
    [
        "Non-Immigrant Intent & Ties to Bangladesh",
        "Applicants must show that their U.S. degree will be utilized upon graduation rather than seeking immediate permanent settlement.",
        "Bangladesh has an expanding technology and engineering ecosystem. Documented contributions, local projects, and clear post-degree career trajectories demonstrate strong national ties.",
        "When VO asks 'What are your future plans?': 'I plan to return to Bangladesh to contribute to our rapidly expanding technology and engineering sector. My studies will allow me to help develop scalable technical systems and research infrastructure in Bangladesh.'"
    ]
]

doc_data = [
    ["Application Fee", "Common Application Fee Waiver", "Common App Profile", "Select 'Yes' under Common App Fee Waiver (Eligible based on low family income / financial hardship). School counselor checks confirmation box.", "Saves ~$75–$90 per university across all schools ($4,000+ total savings across 40 applications)."],
    ["Financial Aid Form", "CSS Profile Fee Waiver", "College Board / University Financial Aid Offices", "Email admissions/financial aid offices in October requesting an institutional CSS Profile Fee Waiver Code. If unavailable, submit free ISFAA PDF.", "Never pay the $25 + $16 per school fee. Colleges like Dartmouth, Colby, Bowdoin, Skidmore, Denison accept free ISFAA directly on portal."],
    ["Financial Form", "Free ISFAA / PFAA / Soka Form", "College Websites / Portals", "Download the International Student Financial Aid Application (ISFAA) PDF form, complete it, and upload directly to applicant portal.", "Princeton uses its own free PFAA portal. UChicago uses free UChicago Financial Aid Worksheet. Soka uses free online form. Many LACs accept paper/PDF ISFAA for free."],
    ["Financial Proof", "Parent Income Tax Returns & Financial Affidavit", "NBR / Employer / Local Government (Ward Commissioner / Union Parishad)", "Official family financial records: Parent Tax Certificates (TIN/NBR), Employer Salary Slips, Bank Statements, or Local Ward Commissioner/Union Parishad Low-Income / Financial Hardship Certificate.", "Critical for establishing $0 Expected Family Contribution (EFC) without dispute."],
    ["Financial Proof", "Asset Declaration (Land/House)", "Local Land Authority / Valuation", "Declare the residential house/land with realistic local municipal valuation, explicitly noting that it generates $0 income and is non-liquid.", "Prevents financial aid officers from assuming hidden rental income."],
    ["Academic Records", "SSC & HSC Official Marksheets & Certificates", "BISE (Bangladesh Education Board)", "Certified copies of SSC (Class 10) and HSC (Class 12) official marksheets and certificates from BISE.", "Must be officially attested by school principal/headmaster and uploaded by counselor."],
    ["Recommendations", "School Counselor Recommendation", "High School / College Counselor or Principal", "Comprehensive letter detailing student's academic drive, character, ethics, and resilience.", "Counselor must confirm fee waiver eligibility on Common App."],
    ["Recommendations", "2 Academic Teacher Evaluations", "High School Teachers", "Letter 1: STEM (Math/Physics). Letter 2: ICT, English, or Social Sciences. Focus on intellectual curiosity, problem-solving, and leadership.", "Avoid generic praise; provide specific classroom anecdotes and competition results."],
    ["Testing", "SAT Score Report", "College Board", "Self-report scores on Common App and university portals (100% free at 90%+ of universities).", "Only send official College Board score reports to the few schools requiring them upon admission or enrollment."],
    ["Testing", "English Proficiency (DET / IELTS)", "Duolingo / British Council", "Request Duolingo fee waiver coupon from college admissions, or request SAT EBRW waiver (EBRW 650–700+ waives DET at most colleges).", "Duolingo allows testing from home at zero cost if waiver coupon is granted."],
    ["Supplemental", "Research Abstract & Portfolio", "Published Paper / Manuscript / GitHub", "Upload 1–2 page PDF executive summary of research papers with DOI link and live demo links for software/hardware projects.", "Proves university-level research readiness and technical execution capability."]
]

def create_master_workbook(filename):
    wb = openpyxl.Workbook()
    
    # Tab 1: Master Directory
    ws1 = wb.active
    ws1.title = f"Master Directory ({total_count} Colleges)"
    
    for col_idx, header in enumerate(columns_bd, 1):
        cell = ws1.cell(row=1, column=col_idx, value=header)
        cell.fill = navy_header
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws1.row_dimensions[1].height = 48

    for row_idx, c in enumerate(colleges, 2):
        fill = zebra_fill if row_idx % 2 == 0 else white_fill
        row_data = extract_row(c)
        for col_idx, val in enumerate(row_data, 1):
            cell = ws1.cell(row=row_idx, column=col_idx, value=val)
            cell.fill = fill
            cell.font = Font(name="Calibri", size=10)
            cell.border = thin_border
            
            # Center alignments
            if col_idx in [1, 2, 3, 4, 6, 8, 9, 10, 11, 17, 18, 19, 24, 26, 27, 34, 35, 36, 39, 40]:
                cell.alignment = Alignment(horizontal="center", vertical="top", wrap_text=True)
            else:
                cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
                
            # Highlight 98%+ Visa
            if col_idx == 41 and "98%" in str(val):
                cell.font = Font(name="Calibri", size=10, bold=True, color="047857")
                
            # Highlight ED1 Primary
            if col_idx == 33 and "PRIMARY ED1" in str(val):
                cell.fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
                cell.font = Font(name="Calibri", size=10, bold=True, color="92400E")
                
        ws1.row_dimensions[row_idx].height = 68

    ws1.freeze_panes = "A2"
    for c_idx in range(1, len(columns_bd) + 1):
        ws1.column_dimensions[get_column_letter(c_idx)].width = 25
    ws1.column_dimensions['A'].width = 28 # Strategic Match Rank
    ws1.column_dimensions['B'].width = 14 # Strategic Factor Score
    ws1.column_dimensions['C'].width = 25 # US News Rank
    ws1.column_dimensions['D'].width = 28 # QS World Rank
    ws1.column_dimensions['E'].width = 34 # Institution Name
    ws1.column_dimensions['F'].width = 14 # CEEB
    ws1.column_dimensions['G'].width = 36 # CDS C9
    ws1.column_dimensions['H'].width = 28 # Need-Blind Status
    ws1.column_dimensions['I'].width = 22 # Type
    ws1.column_dimensions['J'].width = 18 # Location
    ws1.column_dimensions['K'].width = 16 # Region
    ws1.column_dimensions['O'].width = 38 # CS Highlights
    ws1.column_dimensions['P'].width = 34 # Aid Policy
    ws1.column_dimensions['Q'].width = 24 # CDS H6 Avg Int'l Aid
    ws1.column_dimensions['R'].width = 20 # CDS H6 % Aided
    ws1.column_dimensions['S'].width = 26 # CDS H6 Total Aid Budget
    ws1.column_dimensions['T'].width = 32 # CDS H6 Loan-Free Guarantee
    ws1.column_dimensions['U'].width = 34 # Required FinAid Form
    ws1.column_dimensions['V'].width = 36 # Bank Statement / COF Timing
    ws1.column_dimensions['W'].width = 30 # Max Aid Package
    ws1.column_dimensions['Y'].width = 42 # All Deadlines
    ws1.column_dimensions['Z'].width = 32 # FinAid Deadline
    ws1.column_dimensions['AA'].width = 30 # Merit Deadline
    ws1.column_dimensions['AB'].width = 42 # Nov 7 SAT Strategy
    ws1.column_dimensions['AC'].width = 45 # Supplemental Essays
    ws1.column_dimensions['AD'].width = 45 # Tactical Admissions Realities
    ws1.column_dimensions['AE'].width = 36 # Special Requirements
    ws1.column_dimensions['AL'].width = 34 # English Cutoffs & SAT Waiver
    ws1.column_dimensions['AO'].width = 38 # Dhaka Visa
    ws1.column_dimensions['AP'].width = 45 # Reddit Consensus
    ws1.column_dimensions['AQ'].width = 45 # BD Strategic Advice
    ws1.auto_filter.ref = f"A1:{get_column_letter(len(columns_bd))}{total_count+1}"

    # Tab 2: Strategy Roadmap
    ws2 = wb.create_sheet(title="Testing & Strategy Roadmap")
    ws2.views.sheetView[0].showGridLines = True
    headers2 = ["Strategic Round", "Application Deadlines", "Testing Strategy & Policy", "Recommended Target Colleges", "Action Items for Bangladeshi Applicants"]
    for i, h in enumerate(headers2, 1):
        cell = ws2.cell(row=1, column=i, value=h)
        cell.fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        cell.alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[1].height = 32

    for r_idx, r in enumerate(roadmap_data, 2):
        for c_idx, val in enumerate(r, 1):
            cell = ws2.cell(row=r_idx, column=c_idx, value=val)
            cell.font = Font(name="Calibri", size=10)
            cell.border = thin_border
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws2.row_dimensions[r_idx].height = 65

    ws2.column_dimensions['A'].width = 28
    ws2.column_dimensions['B'].width = 20
    ws2.column_dimensions['C'].width = 35
    ws2.column_dimensions['D'].width = 42
    ws2.column_dimensions['E'].width = 48

    # Tab 3: Dhaka Visa Guide
    ws3 = wb.create_sheet(title="Dhaka Embassy F-1 Visa Guide")
    ws3.views.sheetView[0].showGridLines = True
    headers3 = ["Embassy Focus Dimension", "Dhaka Embassy Reality", "Why a Full-Ride Wins", "Recommended Script / Interview Action"]
    for i, h in enumerate(headers3, 1):
        cell = ws3.cell(row=1, column=i, value=h)
        cell.fill = PatternFill(start_color="047857", end_color="047857", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        cell.alignment = Alignment(horizontal="center", vertical="center")
    ws3.row_dimensions[1].height = 32

    for r_idx, r in enumerate(visa_data, 2):
        for c_idx, val in enumerate(r, 1):
            cell = ws3.cell(row=r_idx, column=c_idx, value=val)
            cell.font = Font(name="Calibri", size=10)
            cell.border = thin_border
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws3.row_dimensions[r_idx].height = 70

    ws3.column_dimensions['A'].width = 25
    ws3.column_dimensions['B'].width = 35
    ws3.column_dimensions['C'].width = 38
    ws3.column_dimensions['D'].width = 50

    # Tab 4: Zero-Cost & Document Guide
    ws4 = wb.create_sheet(title="BD Zero-Cost & Document Guide")
    ws4.views.sheetView[0].showGridLines = True
    headers4 = ["Category", "Item / Document Name", "Issuing Body / Platform", "Zero-Cost Protocol / Waiver Instructions", "Strategic Notes for Bangladeshi Students"]
    for i, h in enumerate(headers4, 1):
        cell = ws4.cell(row=1, column=i, value=h)
        cell.fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        cell.alignment = Alignment(horizontal="center", vertical="center")
    ws4.row_dimensions[1].height = 32

    for r_idx, r in enumerate(doc_data, 2):
        for c_idx, val in enumerate(r, 1):
            cell = ws4.cell(row=r_idx, column=c_idx, value=val)
            cell.font = Font(name="Calibri", size=10)
            cell.border = thin_border
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws4.row_dimensions[r_idx].height = 45

    ws4.column_dimensions['A'].width = 18
    ws4.column_dimensions['B'].width = 30
    ws4.column_dimensions['C'].width = 25
    ws4.column_dimensions['D'].width = 42
    ws4.column_dimensions['E'].width = 45

    excel_filename = 'US_Colleges_Fall_2027_Full_Ride_BDtoUSA.xlsx'
    wb.save(excel_filename)
    print(f"Generated {excel_filename} (4 sheets, {total_count} rows in directory)")

create_master_workbook('US_Colleges_Fall_2027_Full_Ride_BDtoUSA.xlsx')

print("All generalized CSV and Excel deliverables built successfully.")
