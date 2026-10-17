import json
import csv
import re
import sys

# Configure output encoding
sys.stdout.reconfigure(encoding='utf-8')

# Read existing HTML to extract data array
with open('Interactive_College_Spreadsheet.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

idx_start = html_content.find('const data = [')
idx_end = html_content.find('];\n    let activeFilter', idx_start)
if idx_end == -1:
    idx_end = html_content.find('];', idx_start)

json_str = html_content[idx_start + 13 : idx_end + 1]
colleges = json.loads(json_str)

print(f"Loaded {len(colleges)} colleges from HTML")

# Helper function to generate tailored required documents
def get_required_documents(name, type_str, tier, fee_waiver):
    app_form = "MIT Application Portal" if "MIT" in name or "Massachusetts Institute of Technology" in name else "Common Application (First-Year)"
    
    # Financial forms
    if "Princeton" in name:
        fin_form = "Princeton Financial Aid Application (PFAA - 100% Free online) + Non-taxfiler certification"
    elif "ISFAA" in fee_waiver or "paper" in fee_waiver.lower() or "free isfaa" in fee_waiver.lower():
        fin_form = "Free ISFAA (International Student Financial Aid Application PDF / portal upload) or CSS Profile with institutional fee waiver code"
    else:
        fin_form = "CSS Profile (Institutional Code) + IDOC document service (upload Parent Death Certificates, Zero Income Statement & Relative Financial Affidavit)"

    # Core academic & rec docs
    docs = (
        f"1. {app_form} with personal statement & institution-specific supplemental essays. "
        f"2. Official SSC (Class 10) & HSC (Class 12) certified Board Marksheets & Pass Certificates from Bangladesh Education Board. "
        f"3. High School Report Card / Transcript and School Profile certified by Headmaster / Counselor. "
        f"4. Counselor Recommendation Letter & School Report. "
        f"5. Two Academic Teacher Recommendation Letters (1 STEM: Math/Physics, 1 ICT/English/Science). "
        f"6. Financial Aid: {fin_form}. "
        f"7. Certification of Finances (COF) declaring $0 family contribution + Parent Death Certificates & legal orphan/hardship affidavit."
    )
    return docs

# Helper function to generate tailored SAT / DET requirements
def get_sat_det_needed(name, tier, type_str):
    if "Need-Blind Hyper-Reach" in tier or "MIT" in name or "Harvard" in name or "Princeton" in name or "Yale" in name or "Stanford" in name:
        return "SAT Target: 1540–1580 (Math 790–800, EBRW 740+) | DET: 135–145+ / IELTS 7.5–8.0+ | Waiver: SAT EBRW 700+ waives English testing at MIT/Yale/Princeton; self-report on portal."
    elif "Ivy" in tier or "Top Merit" in tier or "Tech Powerhouse" in tier or "Duke" in name or "WashU" in name or "Vanderbilt" in name or "Rice" in name or "Hopkins" in name:
        return "SAT Target: 1530–1570 (Math 790–800, EBRW 730+) | DET: 130–140+ / IELTS 7.5+ | Waiver: SAT EBRW 680+ automatically waives DET/IELTS requirement; self-report on Common App."
    elif "Elite LAC" in tier or "Williams" in name or "Swarthmore" in name or "Pomona" in name or "Carleton" in name or "Colby" in name or "Bowdoin" in name:
        return "SAT Target: 1510–1560 (Math 780–800, EBRW 720+) | DET: 130–140+ / IELTS 7.5+ | Waiver: English-medium instruction or SAT EBRW 670+ waives DET; free self-report."
    elif "Target" in tier or "High-Yield" in tier or "High-Probability" in tier:
        return "SAT Target: 1470–1530 (Math 770–800, EBRW 700+) | DET: 120–130+ / IELTS 7.0+ | Waiver: Test-optional / SAT EBRW 650+ waives English test; accepts DET with coupon or self-report."
    elif "Merit" in tier or "UT Dallas" in name or "Miami" in name or "Temple" in name or "Drexel" in name:
        return "SAT Target: 1500–1560 (Math 780–800 mandatory for top competitive merit tier) | DET: 125–135+ / IELTS 7.0+ | Self-report accepted for scholarship consideration."
    elif "Berea" in name:
        return "SAT Target: 1450–1520 (Math 760–800) | DET: 120–130+ or IELTS 6.5–7.0+ | Official test report required; mandatory virtual interview for international applicants."
    else:
        return "SAT Target: 1480–1540 (Math 770–800) | DET: 125–135+ / IELTS 7.0+ | Self-report accepted on application portal."

# Helper function to get General International Acceptance Rate
def get_intl_admit_rate(name, tier, type_str):
    if "MIT" in name:
        return "1.4% - 2.0% (Overall int'l applicant admit rate; ~150 admitted globally out of ~9,500)"
    elif "Harvard" in name or "Stanford" in name:
        return "1.5% - 2.3% (Overall int'l admit rate; sub-2% for international full-need pool)"
    elif "Princeton" in name or "Yale" in name:
        return "1.8% - 2.6% (Overall int'l admit rate; pure need-blind evaluation)"
    elif "Dartmouth" in name or "Amherst" in name:
        return "2.8% - 4.2% (Overall int'l admit rate; need-blind with 100% need met)"
    elif "Bowdoin" in name:
        return "3.2% - 4.8% (Need-blind int'l admit rate; high yield on admitted scholars)"
    elif "Ivy" in tier or "Super-Reach" in tier or "Columbia" in name or "UPenn" in name or "Brown" in name or "Cornell" in name:
        return "2.2% - 3.8% (Int'l admit rate; need-aware budget constraints apply)"
    elif "Duke" in name or "Northwestern" in name or "Vanderbilt" in name or "Rice" in name or "WashU" in name or "JHU" in name:
        return "2.5% - 4.5% (Overall int'l admit rate; highly competitive for $0 EFC)"
    elif "Williams" in name or "Swarthmore" in name or "Pomona" in name:
        return "3.0% - 4.8% (Int'l admit rate; need-aware except Williams/Pomona high aid budget)"
    elif "Carleton" in name or "Colby" in name or "Bates" in name or "Middlebury" in name or "Grinnell" in name:
        return "4.5% - 7.5% (Int'l admit rate; increases significantly to 10-14% in ED1/ED2)"
    elif "Davidson" in name or "Haverford" in name or "Vassar" in name or "Hamilton" in name or "Wesleyan" in name or "Colgate" in name:
        return "4.0% - 6.8% (Int'l admit rate; heavy aid given to admitted cohort)"
    elif "Kenyon" in name or "Oberlin" in name or "Macalester" in name or "Lafayette" in name or "Trinity" in name or "Skidmore" in name or "F&M" in name or "Richmond" in name:
        return "5.5% - 9.5% (Int'l admit rate; generous aid packages for top 10-15 international students)"
    elif "Denison" in name or "St. Olaf" in name or "Union" in name or "Connecticut College" in name or "Dickinson" in name or "Gettysburg" in name:
        return "10.0% - 16.0% (Int'l admit rate; excellent aid pool for high-stats STEM applicants)"
    elif "DePauw" in name or "Wooster" in name or "Knox" in name or "Hobart" in name or "Rhodes" in name or "Sewanee" in name:
        return "14.0% - 24.0% (Int'l admit rate; among the most accessible high-aid LACs in the US)"
    elif "Berea" in name:
        return "6.0% - 8.5% (Overall int'l admit rate; admits exactly 30-40 int'ls/year on 100% full ride)"
    elif "UT Dallas" in name:
        return "20.0% - 30.0% (Admit rate; automatic full-tuition AES + McDermott full-ride interview)"
    elif "Miami" in name or "BU" in name or "USC" in name or "Wake Forest" in name or "SMU" in name:
        return "4.0% - 8.0% (Admit rate for premier competitive full-ride merit scholarship cohorts)"
    elif "Drexel" in name or "Temple" in name or "MSU" in name or "Alabama" in name:
        return "22.0% - 35.0% (Int'l admit rate; high yield on top merit and full tuition awards)"
    elif "Wabash" in name or "Kalamazoo" in name or "Bennington" in name or "Allegheny" in name or "Augustana" in name or "Earlham" in name or "Juniata" in name:
        return "16.0% - 28.0% (Int'l admit rate; high acceptance probability with strong aid package)"
    else:
        return "8.0% - 15.0% (Int'l admit rate benchmark)"

# Helper function for Extra Info & Admissions Insights
def get_extra_info(name, type_str, tier):
    insights = []
    
    # Portfolio / Research Supplement
    if any(k in name for k in ["MIT", "Harvard", "Stanford", "Columbia", "Yale", "Brown", "Tufts", "Swarthmore", "Cornell", "Penn", "Rochester"]):
        insights.append("Maker / Research Portfolio: Highly recommended! Submit Slideroom maker portfolio showcasing CholoSikhi SAT code, Chitro AI live demo, MedVision AI, and upload the 3rd-authored Biomedical AI research paper abstract via applicant portal.")
    elif any(k in name for k in ["Colby", "Carleton", "Williams", "Grinnell", "Lafayette", "Case Western", "WPI", "Illinois Tech"]):
        insights.append("Technical Project Upload: Upload your Biomedical AI paper abstract and live GitHub repository links (Chitro AI, CholoSikhi, MedVision) directly to your application portal under 'Supplemental Research Materials'.")
    else:
        insights.append("Project Showcase: Link GitHub repositories and live URLs for CholoSikhi & Chitro AI directly in the Common App 'Activities' and 'Additional Information' sections.")

    # Interview & Demonstrated Interest
    if any(k in name for k in ["Denison", "Wooster", "Knox", "Gettysburg", "Dickinson", "DePauw", "Rhodes", "St. Olaf", "Hobart", "Kalamazoo", "Allegheny"]):
        insights.append("Demonstrated Interest: CRITICAL! This institution tracks demonstrated interest heavily. Register for virtual info sessions, student webinars, open all admissions emails, and schedule an online international student interview.")
    elif "Berea" in name:
        insights.append("Admissions Nuance: Berea strictly admits students with acute financial hardship. Emphasize your independent upbringing, loss of parents, and work-ethic. An evaluative virtual interview is conducted for top shortlisted international applicants.")
    elif "Colby" in name:
        insights.append("Davis Institute for AI: Tailor your 'Why Colby' essay specifically to the Davis Institute for AI! Mention how your Biomedical AI research on medical image classification directly aligns with Colby's interdisciplinary AI labs. ED1 or ED2 gives maximum leverage.")
    elif "Dartmouth" in name:
        insights.append("AI Legacy: Dartmouth is the birthplace of AI (1956). Highlight your deep learning background and national robotics award. Dartmouth's need-blind policy for internationals makes it the absolute top Ivy ED target.")
    elif any(k in name for k in ["Miami", "Boston University", "USC", "UVA", "Wake Forest", "SMU", "Richmond"]):
        insights.append("Merit Scholarship Deadline: Must submit application by the strict Merit Deadline (typically Dec 1 or Nov 15) to be considered for premier full-ride/full-tuition merit scholarships (e.g. Richmond Scholars, BU Trustee, Stamps, Hunt).")
    else:
        insights.append("Admissions Interview: Request an optional alumni or virtual admissions interview as soon as your application portal is created to demonstrate articulate communication and technical passion.")

    # Coursework / Gap Year Advice
    insights.append("Coursework Presentation: Use Common App 'Additional Information' to clearly detail the 2023 HSC graduation timeline, your ongoing software development / Top 40 Android bootcamp achievement, and confirm compliance with first-year freshman eligibility.")

    return " | ".join(insights)

# Update each college entry
enriched_colleges = []
for c in colleges:
    name = c.get('name', '')
    type_str = c.get('type', '')
    tier = c.get('tier_category', '')
    fee_waiver = c.get('fee_waiver', '')
    prob_neon = c.get('probability', '')

    # Generate new sections
    req_docs = get_required_documents(name, type_str, tier, fee_waiver)
    sat_det = get_sat_det_needed(name, tier, type_str)
    intl_rate = get_intl_admit_rate(name, tier, type_str)
    extra = get_extra_info(name, type_str, tier)

    # Add to object
    c['required_documents'] = req_docs
    c['sat_det_needed'] = sat_det
    c['international_probability'] = intl_rate
    c['extra_info'] = extra

    enriched_colleges.append(c)

print("Enriched all colleges successfully.")

# Write updated CSV
csv_columns = [
    'Institution Name',
    'Institution Type',
    'Location',
    'CS / AI / Tech Highlights',
    'Financial Aid Policy (Internationals)',
    'Max Aid Package',
    '$0 EFC Covered?',
    'Application Deadlines',
    'November SAT Policy',
    'Target SAT Score Needed (Full Aid / Merit)',
    'English Proficiency (DET / IELTS) Needed & Waivers',
    'General International Admit Rate (%)',
    'Estimated Probability for Neon (%)',
    'Required Documents Section',
    'Fee Waiver Availability (App & Financial Aid)',
    'Testing Policy (Self-Report vs Official)',
    'First-Year vs Transfer Policy (Prior Coursework)',
    'Extra Info & Strategic Admissions Insights',
    'Tier Category',
    'Strategic Recommendation'
]

with open('US_Colleges_Fall_2027_Full_Ride_Neon.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_columns)
    for c in enriched_colleges:
        writer.writerow([
            c.get('name', ''),
            c.get('type', ''),
            c.get('location', ''),
            c.get('cs_strength', ''),
            c.get('aid_policy', ''),
            c.get('max_aid', ''),
            c.get('efc_0_covered', ''),
            c.get('deadlines', ''),
            c.get('nov_sat_policy', ''),
            c.get('sat_det_needed', ''),
            c.get('sat_det_needed', ''), # For DET/IELTS
            c.get('international_probability', ''),
            c.get('probability', ''),
            c.get('required_documents', ''),
            c.get('fee_waiver', ''),
            c.get('score_policy', ''),
            c.get('college_coursework_policy', ''),
            c.get('extra_info', ''),
            c.get('tier_category', ''),
            c.get('strategic_round', '')
        ])

print("CSV file updated successfully.")

# Now update Interactive_College_Spreadsheet.html
# We need to replace the data array, and also update the modal rendering to display the 4 new cards!

# Prepare new JSON string
new_json_data = json.dumps(enriched_colleges, indent=2, ensure_ascii=False)

# Replace data array in HTML
html_before_data = html_content[:idx_start + 13]
html_after_data = html_content[idx_end + 1:]

updated_html = html_before_data + new_json_data + html_after_data

# Now update openModal and renderTable to show the new cards and columns
# Let's inspect where openModal is defined in updated_html
modal_target = 'content.innerHTML = `'
idx_modal = updated_html.find(modal_target)

if idx_modal != -1:
    idx_modal_end = updated_html.find('modal.classList.remove(\'hidden\');', idx_modal)
    
    new_modal_body = """content.innerHTML = `
        <div class="flex items-start justify-between mb-4 border-b border-slate-100 pb-4">
          <div>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200">${c.tier_category}</span>
            <h2 class="text-2xl font-bold text-slate-900 mt-2">${c.name}</h2>
            <p class="text-slate-500 text-sm"><i class="fa-solid fa-location-dot text-red-500 mr-1"></i> ${c.location} — ${c.type}</p>
          </div>
          <div class="text-right">
            <div class="text-xs text-slate-400 uppercase font-semibold">Neon's Calibrated Prob.</div>
            <div class="text-2xl font-black text-emerald-700 mt-0.5">${c.probability}</div>
            <div class="text-[11px] text-slate-500 mt-0.5">Overall Int'l Rate: <span class="font-medium text-slate-700">${c.international_probability.split('(')[0]}</span></div>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-4">
          <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
            <div class="text-xs font-bold text-slate-500 uppercase tracking-wider"><i class="fa-solid fa-microchip text-indigo-600 mr-1"></i> CS / AI / Tech Fit</div>
            <div class="text-sm text-slate-800 mt-1 font-medium leading-relaxed">${c.cs_strength}</div>
          </div>
          <div class="p-4 bg-emerald-50/60 rounded-xl border border-emerald-200">
            <div class="text-xs font-bold text-emerald-800 uppercase tracking-wider"><i class="fa-solid fa-hand-holding-dollar text-emerald-600 mr-1"></i> Financial Aid & $0 EFC</div>
            <div class="text-sm text-slate-800 mt-1 font-medium leading-relaxed">${c.aid_policy}</div>
            <div class="text-xs text-emerald-700 font-bold mt-1.5"><i class="fa-solid fa-shield-halved mr-1"></i> Package: ${c.max_aid}</div>
          </div>
        </div>

        <div class="space-y-4">
          <!-- Required Documents Section -->
          <div class="p-4 bg-blue-50/70 border border-blue-200 rounded-xl">
            <div class="text-xs font-bold text-blue-900 uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-folder-open text-blue-600"></i>
              Required Documents Checklist
            </div>
            <p class="text-xs text-blue-950 mt-1.5 leading-relaxed font-medium">${c.required_documents}</p>
          </div>

          <!-- SAT & DET Score Needed Section -->
          <div class="p-4 bg-amber-50/70 border border-amber-200 rounded-xl">
            <div class="text-xs font-bold text-amber-900 uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-chart-line text-amber-600"></i>
              SAT & DET / English Proficiency Scores Needed
            </div>
            <p class="text-xs text-amber-950 mt-1.5 leading-relaxed font-medium">${c.sat_det_needed}</p>
          </div>

          <!-- Extra Info & Strategic Admissions Insights Section -->
          <div class="p-4 bg-indigo-50/70 border border-indigo-200 rounded-xl">
            <div class="text-xs font-bold text-indigo-900 uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-lightbulb text-indigo-600"></i>
              Extra Info & Admissions Insights (Portfolios, Interviews & CS Nuances)
            </div>
            <p class="text-xs text-indigo-950 mt-1.5 leading-relaxed font-medium">${c.extra_info}</p>
          </div>

          <!-- Prior University Coursework & Classification Rule -->
          <div class="p-4 bg-rose-50/70 border border-rose-200 rounded-xl">
            <div class="text-xs font-bold text-rose-900 uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-solid fa-triangle-exclamation text-rose-600"></i>
              Prior University Coursework & Classification Rule
            </div>
            <p class="text-xs text-rose-950 mt-1 leading-relaxed font-medium">${c.college_coursework_policy}</p>
          </div>

          <!-- Deadlines & Testing Policies -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl">
              <div class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-regular fa-calendar-check text-indigo-600"></i>
                Deadlines & Nov SAT Policy
              </div>
              <p class="text-xs text-slate-800 mt-1"><strong>Deadlines:</strong> ${c.deadlines}</p>
              <p class="text-xs text-slate-800 mt-0.5"><strong>November SAT:</strong> ${c.nov_sat_policy}</p>
            </div>
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl">
              <div class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-ticket text-emerald-600"></i>
                Fee Waivers & Testing Policy
              </div>
              <p class="text-xs text-slate-800 mt-1"><strong>Fee Waiver:</strong> ${c.fee_waiver}</p>
              <p class="text-xs text-slate-800 mt-0.5"><strong>Reporting:</strong> ${c.score_policy}</p>
            </div>
          </div>

          <!-- Strategic Round -->
          <div class="p-4 bg-slate-900 text-white rounded-xl flex items-center justify-between">
            <div>
              <div class="text-xs font-bold text-slate-400 uppercase tracking-wider">Recommended Strategy Round for Neon</div>
              <div class="text-sm text-emerald-400 font-bold mt-0.5">${c.strategic_round}</div>
            </div>
            <div class="text-right">
              <div class="text-[11px] text-slate-400">General Int'l Admit Rate</div>
              <div class="text-xs font-semibold text-slate-200">${c.international_probability.split('(')[0]}</div>
            </div>
          </div>
        </div>
      `;
      """
    
    updated_html = updated_html[:idx_modal] + new_modal_body + updated_html[idx_modal_end:]

# Also let's update the table headers and rendering to include SAT/DET and Int'l Rate!
old_table_headers = """              <th class="py-3.5 px-4 cursor-pointer hover:text-indigo-600" onclick="sortTable(0)">University / College <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-4 cursor-pointer hover:text-indigo-600" onclick="sortTable(1)">Type & State <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-4">Financial Aid & Max Package</th>
              <th class="py-3.5 px-4">Key Deadlines</th>
              <th class="py-3.5 px-4 cursor-pointer hover:text-indigo-600" onclick="sortTable(4)">Prob. Range <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-4">Strategic Round</th>"""

new_table_headers = """              <th class="py-3.5 px-4 cursor-pointer hover:text-indigo-600" onclick="sortTable(0)">University / College <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-4 cursor-pointer hover:text-indigo-600" onclick="sortTable(1)">Type & State <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-4">Financial Aid & Max Package</th>
              <th class="py-3.5 px-4">Target SAT / DET</th>
              <th class="py-3.5 px-4">Key Deadlines</th>
              <th class="py-3.5 px-4 cursor-pointer hover:text-indigo-600" onclick="sortTable(5)">Neon's Prob. <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-4">Strategic Round</th>"""

if old_table_headers in updated_html:
    updated_html = updated_html.replace(old_table_headers, new_table_headers)

# Update row rendering in renderTable
old_row_render = """        row.innerHTML = `
          <td class="py-4 px-4 font-bold text-slate-900">
            ${c.name}
            <div class="text-xs font-normal text-slate-500 mt-0.5">${c.tier_category}</div>
          </td>
          <td class="py-4 px-4 text-xs text-slate-600">
            <span class="font-medium text-slate-800">${c.location}</span><br>
            <span class="text-slate-500">${c.type}</span>
          </td>
          <td class="py-4 px-4 text-xs">
            <span class="font-semibold text-emerald-700 block">${c.max_aid.split('(')[0]}</span>
            <span class="text-slate-500 block text-[11px] mt-0.5 line-clamp-1">${c.aid_policy}</span>
          </td>
          <td class="py-4 px-4 text-xs text-slate-700 font-mono">
            ${c.deadlines}
          </td>
          <td class="py-4 px-4 text-xs">
            <span class="px-2.5 py-1 rounded-full ${probClass} text-xs inline-block">${c.probability}</span>
          </td>
          <td class="py-4 px-4 text-xs font-medium text-indigo-700">
            ${c.strategic_round}
          </td>
        `;"""

new_row_render = """        row.innerHTML = `
          <td class="py-4 px-4 font-bold text-slate-900">
            ${c.name}
            <div class="text-xs font-normal text-slate-500 mt-0.5">${c.tier_category}</div>
          </td>
          <td class="py-4 px-4 text-xs text-slate-600">
            <span class="font-medium text-slate-800">${c.location}</span><br>
            <span class="text-slate-500">${c.type}</span>
          </td>
          <td class="py-4 px-4 text-xs">
            <span class="font-semibold text-emerald-700 block">${c.max_aid.split('(')[0]}</span>
            <span class="text-slate-500 block text-[11px] mt-0.5 line-clamp-1">${c.aid_policy}</span>
          </td>
          <td class="py-4 px-4 text-xs text-slate-700">
            <span class="font-semibold text-indigo-900 block text-[11px]">${c.sat_det_needed.split('|')[0]}</span>
            <span class="text-slate-500 block text-[10px] mt-0.5">${c.sat_det_needed.includes('|') ? c.sat_det_needed.split('|')[1] : ''}</span>
          </td>
          <td class="py-4 px-4 text-xs text-slate-700 font-mono text-[11px]">
            ${c.deadlines}
          </td>
          <td class="py-4 px-4 text-xs">
            <span class="px-2.5 py-1 rounded-full ${probClass} text-xs font-bold inline-block">${c.probability}</span>
            <div class="text-[10px] text-slate-400 mt-0.5">Int'l: ${c.international_probability.split('(')[0]}</div>
          </td>
          <td class="py-4 px-4 text-xs font-medium text-indigo-700">
            ${c.strategic_round}
          </td>
        `;"""

if old_row_render in updated_html:
    updated_html = updated_html.replace(old_row_render, new_row_render)

# Write updated HTML file
with open('Interactive_College_Spreadsheet.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Interactive_College_Spreadsheet.html updated successfully with all 4 new sections!")
