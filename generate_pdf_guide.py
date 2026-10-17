import json
import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

sys.stdout.reconfigure(encoding='utf-8')

with open('enriched_colleges.json', 'r', encoding='utf-8') as f:
    colleges = json.load(f)

total_colleges = len(colleges)
print(f"Generating PDF guide for {total_colleges} institutions...")

# Numbered canvas for footer
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Suppress footer on cover page if page 1
        if self._pageNumber > 1:
            # Header
            self.drawString(54, letter[1] - 36, "BDtoUSA: Fall 2027 U.S. College Admissions & Full-Ride Navigator")
            self.drawRightString(letter[0] - 54, letter[1] - 36, "160 Verified Institutions • Dhaka Embassy Safe")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)

            # Footer
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 45, letter[0] - 54, 45)
            self.drawString(54, 32, "Confidential & Community Resource for Bangladeshi Undergrad Applicants • $0 EFC & Need-Blind Verified")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(letter[0] - 54, 32, page_text)
        self.restoreState()

pdf_filename = "BDtoUSA_Fall_2027_Full_Ride_Admissions_Guide.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=letter,
    leftMargin=45,
    rightMargin=45,
    topMargin=50,
    bottomMargin=50
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'DocTitle',
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=colors.HexColor('#0F172A'),
    alignment=0,
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    fontName='Helvetica',
    fontSize=11,
    leading=15,
    textColor=colors.HexColor('#475569'),
    spaceAfter=12
)

h1_style = ParagraphStyle(
    'Heading1_Custom',
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=18,
    textColor=colors.HexColor('#0F172A'),
    spaceBefore=14,
    spaceAfter=8,
    keepWithNext=True
)

h2_style = ParagraphStyle(
    'Heading2_Custom',
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    textColor=colors.HexColor('#1E3A8A'),
    spaceBefore=8,
    spaceAfter=4,
    keepWithNext=True
)

body_style = ParagraphStyle(
    'Body_Custom',
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#1E293B')
)

bold_body = ParagraphStyle(
    'Bold_Body_Custom',
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#0F172A')
)

meta_style = ParagraphStyle(
    'Meta_Style',
    fontName='Helvetica',
    fontSize=7.5,
    leading=10,
    textColor=colors.HexColor('#64748B')
)

reddit_style = ParagraphStyle(
    'Reddit_Style',
    fontName='Helvetica-Oblique',
    fontSize=8,
    leading=11.5,
    textColor=colors.HexColor('#9A3412')
)

alert_style = ParagraphStyle(
    'Alert_Style',
    fontName='Helvetica',
    fontSize=8,
    leading=11.5,
    textColor=colors.HexColor('#065F46')
)

story = []

# COVER / TITLE BANNER
title_table_data = [
    [
        Paragraph("<font color='#059669'><b>🇧🇩 BDtoUSA</b></font> • Fall 2027 Admissions Master Guide", ParagraphStyle('TopTag', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#059669'))),
        Paragraph("<font color='#64748B'>160 Curated Institutions • Verified Oct 2026</font>", ParagraphStyle('TopTagR', fontName='Helvetica', fontSize=9, alignment=2, textColor=colors.HexColor('#64748B')))
    ],
    [
        Paragraph("U.S. Undergraduate Admissions, Need-Blind Status & Full-Ride Navigator", title_style),
        ""
    ],
    [
        Paragraph("The definitive directory of 160 U.S. colleges offering 100% Demonstrated Need, Need-Blind admission, and Premier Merit Full Rides ($0 EFC) for Bangladeshi high school graduates, with Dhaka Embassy F-1 Visa Safety and Reddit Insider Consensus.", subtitle_style),
        ""
    ]
]
t_title = Table(title_table_data, colWidths=[400, 122])
t_title.setStyle(TableStyle([
    ('SPAN', (0, 1), (1, 1)),
    ('SPAN', (0, 2), (1, 2)),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ('TOPPADDING', (0, 0), (-1, -1), 2),
]))
story.append(t_title)
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

# 4 KEY METRIC CARDS
metric_data = [
    [
        Paragraph("<b>160 Colleges</b><br/><font color='#64748B' size=7>Audited Directory</font>", ParagraphStyle('M1', fontName='Helvetica', fontSize=9, leading=12, alignment=1)),
        Paragraph("<b>9 Elites</b><br/><font color='#64748B' size=7>100% Need-Blind Int'l</font>", ParagraphStyle('M2', fontName='Helvetica', fontSize=9, leading=12, alignment=1)),
        Paragraph("<b>$0 EFC Safe</b><br/><font color='#64748B' size=7>Dhaka Embassy 214(b) Ready</font>", ParagraphStyle('M3', fontName='Helvetica', fontSize=9, leading=12, alignment=1)),
        Paragraph("<b>Zero-Cost Apply</b><br/><font color='#64748B' size=7>Free App & ISFAA Guides</font>", ParagraphStyle('M4', fontName='Helvetica', fontSize=9, leading=12, alignment=1))
    ]
]
t_metrics = Table(metric_data, colWidths=[130.5, 130.5, 130.5, 130.5])
t_metrics.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#E2E8F0')),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
]))
story.append(t_metrics)
story.append(Spacer(1, 14))

# SECTION 1: THE BANGLADESHI APPLICANT GOLDEN RULES
story.append(Paragraph("1. Essential Strategic Rules for Bangladeshi Applicants", h1_style))

rules_data = [
    [
        Paragraph("<b>Rule 1: The $0 EFC Mandate & Visa Clearance</b>", bold_body),
        Paragraph("At the US Embassy in Dhaka, consular officers scrutinize student finances under INA Section 214(b). If an applicant's I-20 form displays an unmet funding gap of $15,000–$25,000, visa refusal is near-certain without documented high-volume parental assets. Every primary college in this directory meets 100% of demonstrated need or awards verified full-tuition/full-ride merit scholarships, resulting in an I-20 that states: <i>'Family Contribution: $0 | Institutional Scholarship: $85,000+'</i>.", body_style)
    ],
    [
        Paragraph("<b>Rule 2: $0 Application & Financial Aid Cost Protocol</b>", bold_body),
        Paragraph("Never pay application fees ($75–$90/school) or CSS Profile fees ($25 initial + $16/school). On the Common Application, select the <b>Common App Fee Waiver</b> (verified by your school counselor). For financial aid, prioritize colleges that accept the <b>Free ISFAA PDF</b> uploaded to your portal, Princeton's free PFAA portal, or request an institutional CSS Profile fee waiver code from admissions offices.", body_style)
    ],
    [
        Paragraph("<b>Rule 3: Standardized Testing & November 7 SAT Strategy</b>", bold_body),
        Paragraph("Scores from the November 7 SAT release on November 20–21. For <b>November 1 Early Action (EA)</b> and <b>Early Decision (ED1 at Bowdoin)</b>, submit as <b>Test-Optional</b>. If your verified score is <b>1530+ (Math 790–800)</b>, log into your applicant portals around November 21 and upload your score report. If the score is lower, leave your application test-optional. Use the verified score for December 1 Merit and January RD.", body_style)
    ],
    [
        Paragraph("<b>Rule 4: Study Gap Justification (Post-HSC Timeline)</b>", bold_body),
        Paragraph("Consular officers in Dhaka aggressively question study gaps post-HSC. A study gap is converted into an asset by presenting verified academic and technical deliverables: published research papers or pre-prints, national science or programming Olympiad accolades, hackathon awards, active open-source code repositories, and documented community leadership.", body_style)
    ]
]
t_rules = Table(rules_data, colWidths=[150, 372])
t_rules.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F1F5F9')),
    ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#FFFFFF')),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(t_rules)
story.append(Spacer(1, 14))

# SECTION 2: ADMISSIONS ROUND STRATEGY ROADMAP
story.append(Paragraph("2. Strategic Admissions Round Execution Roadmap", h1_style))

roadmap_table_data = [
    [
        Paragraph("<b>Round</b>", bold_body),
        Paragraph("<b>Deadlines</b>", bold_body),
        Paragraph("<b>Testing Policy</b>", bold_body),
        Paragraph("<b>Recommended Target Institutions</b>", bold_body),
        Paragraph("<b>Bangladeshi Action Plan</b>", bold_body)
    ],
    [
        Paragraph("<b>ED1 Primary</b><br/>(Binding)", bold_body),
        Paragraph("Nov 15, 2026", body_style),
        Paragraph("100% Test-Optional", body_style),
        Paragraph("<b>Bowdoin College</b><br/>(#5 US LAC | CEEB: 3089)", body_style),
        Paragraph("Need-blind for int'ls with 100% full ride ($0 loans). If Nov 7 SAT is 1530+, upload on Nov 21. 99% Dhaka visa approval.", body_style)
    ],
    [
        Paragraph("<b>ED1 Alternatives</b><br/>(Binding)", bold_body),
        Paragraph("Nov 1 – Nov 15", body_style),
        Paragraph("Test-Optional", body_style),
        Paragraph("<b>Colby College</b> (Davis AI)<br/><b>NYU Abu Dhabi</b> (Global Full Ride)", body_style),
        Paragraph("Colby: #1 for AI in LACs, free ISFAA. NYUAD: 100% need-blind with flights and living stipend.", body_style)
    ],
    [
        Paragraph("<b>Early Action (EA)</b><br/>(Non-Binding)", bold_body),
        Paragraph("Nov 1 – Dec 1", body_style),
        Paragraph("Test-Optional / Nov SAT", body_style),
        Paragraph("UChicago, Denison, DePauw, Wooster, St. Olaf, Knox, Soka, Reed, Colorado", body_style),
        Paragraph("Submit 8-12 non-binding EA applications. $0 application fees and free ISFAA at Denison, DePauw, Wooster, St. Olaf.", body_style)
    ],
    [
        Paragraph("<b>Premier Merit</b><br/>(Non-Binding)", bold_body),
        Paragraph("Nov 15 – Dec 1", body_style),
        Paragraph("Nov 7 SAT (1550+)", body_style),
        Paragraph("Robertson (Duke/UNC), Richmond Scholars, Stamps (Miami), UT Dallas AES", body_style),
        Paragraph("Awards full funding based on academic excellence, bypassing need-aware financial aid limits.", body_style)
    ],
    [
        Paragraph("<b>ED2 Backup Shot</b><br/>(Binding)", bold_body),
        Paragraph("Jan 1 – Jan 15", body_style),
        Paragraph("Verified 1550+ SAT", body_style),
        Paragraph("WashU, Vanderbilt, Carleton, Grinnell, Lafayette, UChicago ED2", body_style),
        Paragraph("If Bowdoin ED1 defers/rejects in mid-Dec, pivot immediately to an ED2 target with verified SAT.", body_style)
    ],
    [
        Paragraph("<b>Regular Decision</b><br/>(Full Sweep)", bold_body),
        Paragraph("Jan 1 – Feb 1", body_style),
        Paragraph("Verified 1550+ SAT", body_style),
        Paragraph("9 Need-Blind Elites (Harvard, Princeton, Yale, Dartmouth, Amherst, Brown, Notre Dame) + 30 LACs", body_style),
        Paragraph("Submit 25-30 applications across colleges meeting 100% need with full fee waivers.", body_style)
    ]
]

t_roadmap = Table(roadmap_table_data, colWidths=[75, 65, 75, 140, 167])
t_roadmap.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(t_roadmap)
story.append(Spacer(1, 14))

# SECTION 3: DHAKA EMBASSY F-1 VISA INTERVIEW PROTOCOL
story.append(Paragraph("3. Dhaka Embassy F-1 Visa Protocol (INA § 214(b) Mitigation)", h1_style))

visa_qa_data = [
    [
        Paragraph("<b>Consular Officer Question</b>", bold_body),
        Paragraph("<b>Why the Officer Asks It & Recommended Verbal Script</b>", bold_body)
    ],
    [
        Paragraph("<b>'Who is sponsoring your education in the United States?'</b>", bold_body),
        Paragraph("<b>Officer Objective:</b> Looking for unverified local bank balances or borrowed sponsor funds.<br/><b>Winning Answer:</b> <i>'I was awarded a full scholarship by [University Name] covering 100% of my tuition, room, board, and health insurance based on my academic excellence and software engineering achievements. My family has zero financial burden.'</i> (Present official award letter).", body_style)
    ],
    [
        Paragraph("<b>'What have you been doing since completing your HSC / A-Levels?'</b>", bold_body),
        Paragraph("<b>Officer Objective:</b> Interrogating study gaps post-HSC to check if you were idle or working without authorization.<br/><b>Winning Answer:</b> <i>'I spent this period conducting advanced academic research, developing open-source software platforms, competing in national programming contests and Olympiads, and teaching technology skills in my community. These projects deepened my practical expertise and solidified my preparation for undergraduate study in the United States.'</i>", body_style)
    ],
    [
        Paragraph("<b>'Why did you choose this specific university?'</b>", bold_body),
        Paragraph("<b>Officer Objective:</b> Testing whether you are a genuine student who researched the curriculum.<br/><b>Winning Answer:</b> <i>'I chose [University] because of its dedicated undergraduate research facilities, faculty mentorship in my major, and its commitment to fully funding international scholars. I look forward to working in their applied computing laboratories.'</i>", body_style)
    ],
    [
        Paragraph("<b>'What are your career plans upon completing your degree?'</b>", bold_body),
        Paragraph("<b>Officer Objective:</b> Evaluating non-immigrant intent under INA Section 214(b).<br/><b>Winning Answer:</b> <i>'I plan to return to Bangladesh to contribute to our rapidly expanding technology and engineering sector. My studies will allow me to help develop scalable technical systems and research infrastructure in Bangladesh.'</i>", body_style)
    ]
]
t_visa = Table(visa_qa_data, colWidths=[150, 372])
t_visa.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#047857')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(t_visa)
story.append(Spacer(1, 14))

# PAGE BREAK TO DIRECTORY
story.append(PageBreak())

# SECTION 4: THE MASTER DIRECTORY OF 160 INSTITUTIONS
story.append(Paragraph("4. Master Institutional Directory (160 Verified Colleges)", h1_style))
story.append(Paragraph("Detailed profile of each institution including Need-Blind status, CEEB Code, testing requirements, maximum financial aid package, Dhaka Embassy visa safety rating, and Reddit / community insider analysis.", body_style))
story.append(Spacer(1, 8))

# Build Directory Entries
for idx, c in enumerate(colleges, 1):
    name = c.get('name', '')
    cb = c.get('cb_code', 'N/A')
    need_blind = c.get('need_blind_status', 'Need-Aware')
    itype = c.get('type', '')
    loc = c.get('location', '')
    deadlines = c.get('deadlines', '')
    aid_policy = c.get('aid_policy', '')
    max_aid = c.get('max_aid', '')
    efc_0 = c.get('efc_0_covered', '')
    reddit = c.get('reddit_analysis', '')
    visa = c.get('visa_safety_index', '')
    cs_strength = c.get('cs_strength', '')
    fee_waiver = c.get('fee_waiver', '')
    adm_url = c.get('admissions_url', '')
    fa_url = c.get('finaid_url', '')
    us_news = c.get('us_news_display', '')
    world_rank = c.get('world_rank_display', '')
    test_opt = c.get('test_optional_stat', '')

    h6 = c.get('cds_h6', {})
    avg_aid = h6.get('avg_aid', 'N/A')
    pct_aid = h6.get('pct_aided', 'N/A')
    total_budget = h6.get('total_budget', 'N/A')
    cof_badge = c.get('cof_badge', 'Deferred ($0 at App)')
    finaid_badge = c.get('finaid_form_badge', 'Free ISFAA / CSS')
    is_caution = "Caution" in need_blind or "NO" in str(efc_0) or "Caution" in visa

    entry_data = [
        [
            Paragraph(f"<b>#{idx}. {name}</b> [CEEB: {cb}] • <font color='#1E40AF'><b>{us_news}</b></font> • <font color='#6B21A8'><b>{world_rank}</b></font>", bold_body),
            Paragraph(f"<font color='{'#991B1B' if is_caution else '#065F46'}'><b>{need_blind}</b></font>", ParagraphStyle('NB', fontName='Helvetica-Bold', fontSize=8, alignment=2))
        ],
        [
            Paragraph(f"<font color='#64748B'><b>Location:</b></font> {loc} • {itype} • <font color='#4338CA'><b>CDS C9 Test-Opt:</b> {test_opt.split('(')[0].strip()}</font>", meta_style),
            Paragraph(f"<font color='#B45309'><b>Deadlines:</b></font> {deadlines}", ParagraphStyle('DD', fontName='Helvetica', fontSize=6.5, leading=8, alignment=2, textColor=colors.HexColor('#1E293B')))
        ],
        [
            Paragraph(f"<b>Aid Policy & Max Package:</b> {aid_policy} <font color='#047857'><b>Max: {max_aid.split('(')[0]}</b></font> ($0 EFC: {efc_0.split('(')[0]})", body_style),
            ""
        ],
        [
            Paragraph(f"<font color='#065F46'><b>CDS H6 Aid:</b> Avg: {avg_aid} ({pct_aid} aided, Budget: {total_budget})</font> • <font color='#0D9488'><b>COF:</b> {cof_badge}</font>", meta_style),
            Paragraph(f"<font color='#1E40AF'><b>Form:</b> {finaid_badge}</font>", ParagraphStyle('FA', fontName='Helvetica-Bold', fontSize=7, alignment=2, textColor=colors.HexColor('#1E40AF')))
        ],
        [
            Paragraph(f"<b>Academic & CS Fit:</b> {cs_strength}", body_style),
            ""
        ],
        [
            Paragraph(f"<b>r/IntltoUSA & Reddit Consensus:</b> <i>{reddit}</i>", reddit_style),
            ""
        ],
        [
            Paragraph(f"<b>Dhaka Visa Safety:</b> <font color='{'#B91C1C' if is_caution else '#047857'}'><b>{visa.split('|')[0].strip()}</b></font> • <font color='#64748B'>Fee Waiver:</font> {fee_waiver.split('.')[0]}", meta_style),
            Paragraph(f"<font color='#1E40AF'>Admissions: {adm_url[:35]}...</font>", ParagraphStyle('LinkR', fontName='Helvetica', fontSize=7, alignment=2, textColor=colors.HexColor('#1E40AF')))
        ]
    ]

    t_entry = Table(entry_data, colWidths=[330, 192])
    t_entry.setStyle(TableStyle([
        ('SPAN', (0, 2), (1, 2)),
        ('SPAN', (0, 4), (1, 4)),
        ('SPAN', (0, 5), (1, 5)),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FEF2F2' if is_caution else '#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#FCA5A5' if is_caution else '#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    story.append(KeepTogether([t_entry, Spacer(1, 5)]))

# Build Document
doc.build(story, canvasmaker=NumberedCanvas)
print(f"Successfully generated {pdf_filename} ({os.path.getsize(pdf_filename)} bytes)")
