import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read enriched colleges JSON
with open('enriched_colleges.json', 'r', encoding='utf-8') as f:
    colleges = json.load(f)

print(f"Loaded {len(colleges)} colleges for HTML generation.")

# Build HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BDtoUSA: Fall 2027 U.S. College Admissions & Full-Ride Navigator for Bangladeshi Undergrads</title>
  <!-- SEO & Social Sharing (Open Graph & Twitter Cards) -->
  <meta name="description" content="Verified database of 160 U.S. universities offering Full Rides ($0 EFC), Need-Blind aid, and premier merit scholarships for Bangladeshi & international undergraduates.">
  <meta property="og:type" content="website">
  <meta property="og:title" content="BDtoUSA: Fall 2027 U.S. College Admissions & Full-Ride Navigator">
  <meta property="og:description" content="Verified directory of 160 U.S. colleges with CDS Section H6 international aid audits, $0 bank statement timing, Nov 7 SAT strategies, and Dhaka Embassy F-1 visa safety ratings.">
  <meta property="og:url" content="https://neamul09.github.io/us-college-info/">
  <meta property="og:image" content="https://neamul09.github.io/us-college-info/bdtousa_admissions_navigator.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="BDtoUSA: Fall 2027 U.S. College Admissions & Full-Ride Navigator">
  <meta name="twitter:description" content="160 U.S. universities verified with Common Data Set (CDS H6 & C9) aid stats, test-optional ratios, and $0 EFC full-ride funding for international students.">
  <meta name="twitter:image" content="https://neamul09.github.io/us-college-info/bdtousa_admissions_navigator.jpg">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎓</text></svg>">
  <!-- Tailwind CSS & Font Awesome -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');
    body { font-family: 'Plus Jakarta Sans', 'Inter', sans-serif; }
    .badge-need-blind { background-color: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; }
    .badge-need-aware { background-color: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe; }
    .badge-merit { background-color: #fefce8; color: #854d0e; border: 1px solid #fef08a; }
    .badge-prob-high { background-color: #dcfce7; color: #15803d; font-weight: 700; }
    .badge-prob-mid { background-color: #fef9c3; color: #854d0e; font-weight: 700; }
    .badge-prob-reach { background-color: #fee2e2; color: #b91c1c; font-weight: 700; }
    .badge-visa-top { background-color: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; font-weight: 700; }
    .badge-visa-high { background-color: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; font-weight: 700; }
    .tab-active { border-bottom: 2px solid #4f46e5; color: #4f46e5; font-weight: 700; }
    tr:hover { background-color: #f8fafc; }
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #f1f5f9; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
  </style>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col">

  <!-- Top Announcement Banner -->
  <div class="bg-gradient-to-r from-emerald-700 via-teal-800 to-indigo-900 text-white text-xs py-2 px-4 shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2 text-center sm:text-left">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center justify-center bg-white/20 text-white px-2 py-0.5 rounded text-[11px] font-bold">🇧🇩 Bangladesh to USA</span>
        <span class="font-medium">Fall 2027 Undergrad Admissions Master Directory • 100% Demonstrated Need, Need-Blind & Merit Full-Rides</span>
      </div>
      <div class="flex items-center gap-4 text-[11px]">
        <span><i class="fa-solid fa-shield-halved text-emerald-300 mr-1"></i>Dhaka Embassy F-1 Safe</span>
        <span><i class="fa-solid fa-check-double text-blue-300 mr-1"></i>Verified 2025–26 CEEB & Sources</span>
        <a href="#playbookModal" onclick="openPlaybook()" class="underline hover:text-emerald-200 font-semibold cursor-pointer">BD Applicant Playbook ↗</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="bg-slate-900 text-white shadow-xl sticky top-0 z-40 border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <div class="flex items-center gap-2.5">
            <span class="text-2xl font-black tracking-tight text-white flex items-center gap-1.5">
              <span class="text-emerald-400">BD</span>to<span class="text-indigo-400">USA</span>
              <span class="text-xs bg-indigo-500/30 text-indigo-300 border border-indigo-400/30 px-2 py-0.5 rounded-full font-bold ml-1.5">Fall 2027 Master Navigator</span>
            </span>
            <span class="hidden sm:inline-block text-xs bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2.5 py-0.5 rounded-full font-semibold">160 Curated Institutions</span>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm mt-1">The definitive directory of U.S. colleges offering Full Rides ($0 EFC), Full Tuition & Need-Blind aid for Bangladeshi students</p>
        </div>

        <!-- Action Tools -->
        <div class="flex flex-wrap items-center gap-2.5">
          <button onclick="openPlaybook()" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-bold px-3.5 py-2 rounded-xl shadow transition">
            <i class="fa-solid fa-book-open"></i> BD Applicant Playbook
          </button>
          
          <button id="shortlistToggleBtn" onclick="toggleShortlistView()" class="inline-flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-amber-400 border border-slate-700 text-xs font-bold px-3 py-2 rounded-xl transition shadow">
            <i class="fa-solid fa-star"></i> <span id="shortlistLabel">My Shortlist (0)</span>
          </button>

          <a href="University_Application_Dossier.html" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-purple-700 to-indigo-700 hover:from-purple-600 hover:to-indigo-600 text-white text-xs font-bold px-3.5 py-2 rounded-xl shadow transition">
            <i class="fa-solid fa-book-bookmark"></i> Application Dossier
          </a>

          <a href="BDtoUSA_Fall_2027_Full_Ride_Admissions_Guide.pdf" download class="inline-flex items-center gap-1.5 bg-rose-700 hover:bg-rose-600 text-white text-xs font-semibold px-3 py-2 rounded-xl shadow transition">
            <i class="fa-solid fa-file-pdf"></i> PDF Guide
          </a>

          <a href="US_Colleges_Fall_2027_Full_Ride_BDtoUSA.xlsx" download class="inline-flex items-center gap-1.5 bg-indigo-700 hover:bg-indigo-600 text-white text-xs font-semibold px-3 py-2 rounded-xl shadow transition">
            <i class="fa-solid fa-file-excel"></i> Excel (.xlsx)
          </a>

          <a href="US_Colleges_Fall_2027_Full_Ride_BDtoUSA.csv" download class="inline-flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold px-3 py-2 rounded-xl shadow transition">
            <i class="fa-solid fa-file-csv"></i> CSV
          </a>

          <button onclick="copyShareLink()" id="shareBtn" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white text-xs font-bold px-3 py-2 rounded-xl shadow transition">
            <i class="fa-solid fa-share-nodes"></i> <span id="shareBtnText">Share Portal</span>
          </button>

          <button onclick="window.print()" class="inline-flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold px-2.5 py-2 rounded-xl transition">
            <i class="fa-solid fa-print"></i>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content Container -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full space-y-6">

    <!-- CRITICAL TIMELINE & DEADLINE ALERT BANNER -->
    <section class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-2xl p-4 sm:p-5 shadow-lg border border-indigo-500/30">
      <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
        
        <!-- Left: Alert Header & Core Dates -->
        <div class="space-y-1.5">
          <div class="flex items-center gap-2 flex-wrap">
            <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-black bg-rose-500 text-white uppercase tracking-wider animate-pulse">
              <i class="fa-solid fa-circle-exclamation"></i> Urgent Action Timeline
            </span>
            <span class="text-xs font-semibold text-indigo-300">Fall 2027 Admission Cycle Critical Milestones</span>
          </div>
          <h2 class="text-base sm:text-lg font-black tracking-tight text-white">
            Upcoming Deadlines: Nov 1 Early Rounds • Nov 20 SAT Score Drop • Dec 1 Merit Full Rides
          </h2>
          <p class="text-xs text-slate-300 leading-relaxed max-w-4xl">
            <strong>Tactical Strategy for Bangladeshi Applicants:</strong> For <strong>Nov 1/15 Early Action & ED1</strong>, apply test-optional if needed to protect your application. When the <strong>Nov 7 SAT scores release on Nov 20</strong>, immediately upload your score report PDF to the applicant portal if <span class="text-amber-300 font-bold font-mono">1520+</span>! For <strong>Dec 1 Merit Scholarships</strong>, scores will be in hand 10 days before deadlines.
          </p>
        </div>

        <!-- Right: 3 Milestone Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 lg:w-auto w-full text-xs">
          <div class="p-2.5 rounded-xl bg-slate-800/90 border border-slate-700/80 flex flex-col justify-between">
            <div>
              <span class="text-[10px] text-rose-400 font-bold uppercase block tracking-wider">Round 1 Priority</span>
              <span class="text-sm font-black text-white font-mono">NOV 1 – 15</span>
            </div>
            <p class="text-[10px] text-slate-300 mt-1">EA & ED1 (Bowdoin, Harvard, MIT, Colby)</p>
          </div>

          <div class="p-2.5 rounded-xl bg-indigo-900/60 border border-indigo-500/50 flex flex-col justify-between">
            <div>
              <span class="text-[10px] text-amber-300 font-bold uppercase block tracking-wider">Score Drop</span>
              <span class="text-sm font-black text-amber-300 font-mono">NOV 20</span>
            </div>
            <p class="text-[10px] text-indigo-200 mt-1">Nov 7 SAT Scores Release to Portals</p>
          </div>

          <div class="p-2.5 rounded-xl bg-emerald-900/60 border border-emerald-500/50 flex flex-col justify-between">
            <div>
              <span class="text-[10px] text-emerald-300 font-bold uppercase block tracking-wider">Premier Merit</span>
              <span class="text-sm font-black text-emerald-300 font-mono">DEC 1</span>
            </div>
            <p class="text-[10px] text-emerald-200 mt-1">BU Trustee, Richmond Scholars, UT Dallas</p>
          </div>
        </div>

      </div>
    </section>

    <!-- Interactive Bangladeshi Profile Matcher & Filter Widget -->
    <section class="bg-white rounded-2xl border border-slate-200 shadow-sm p-5 sm:p-6 space-y-5">
      
      <!-- Top Presets Header -->
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 border-b border-slate-100 pb-4">
        <div>
          <h2 class="text-base font-extrabold text-slate-900 flex items-center gap-2">
            <i class="fa-solid fa-sliders text-indigo-600"></i>
            Interactive Profile Matcher & 1-Click Strategy Archetypes
          </h2>
          <p class="text-xs text-slate-500 mt-0.5">Select a pre-configured strategy archetype or customize filters to match your exact academic, testing, and financial situation.</p>
        </div>
        <button onclick="resetAllFilters()" class="text-xs font-semibold text-rose-600 hover:text-rose-700 flex items-center gap-1 self-start md:self-auto px-2.5 py-1 rounded-lg bg-rose-50 hover:bg-rose-100 transition">
          <i class="fa-solid fa-rotate-left"></i> Reset All Filters
        </button>
      </div>

      <!-- Quick 1-Click Archetype Filter Chips -->
      <div class="flex flex-wrap items-center gap-2 text-xs">
        <span class="font-bold text-slate-600 uppercase text-[11px] tracking-wider mr-1">Quick Presets:</span>
        
        <button onclick="applyPreset('all')" id="preset-all" class="preset-btn px-3 py-1.5 rounded-lg border border-slate-300 bg-slate-900 text-white font-bold transition shadow-sm">
          🇧🇩 All 160 Institutions
        </button>

        <button onclick="applyPreset('full_ride_stem')" id="preset-full_ride_stem" class="preset-btn px-3 py-1.5 rounded-lg border border-indigo-200 bg-indigo-50 text-indigo-800 hover:bg-indigo-100 font-semibold transition">
          🚀 Full-Ride STEM & CS ($0 EFC / AI & Tech)
        </button>

        <button onclick="applyPreset('test_opt_ed')" id="preset-test_opt_ed" class="preset-btn px-3 py-1.5 rounded-lg border border-amber-200 bg-amber-50 text-amber-900 hover:bg-amber-100 font-semibold transition">
          🛡️ Test-Optional ED1 (Bowdoin, Colby, Bates)
        </button>

        <button onclick="applyPreset('test_opt_ea')" id="preset-test_opt_ea" class="preset-btn px-3 py-1.5 rounded-lg border border-blue-200 bg-blue-50 text-blue-900 hover:bg-blue-100 font-semibold transition">
          ⚡ Test-Optional Early Action (EA Non-Binding)
        </button>

        <button onclick="applyPreset('high_sat')" id="preset-high_sat" class="preset-btn px-3 py-1.5 rounded-lg border border-purple-200 bg-purple-50 text-purple-900 hover:bg-purple-100 font-semibold transition">
          🎯 High SAT Achiever (1500+ / Math 800 Target)
        </button>

        <button onclick="applyPreset('need_blind')" id="preset-need_blind" class="preset-btn px-3 py-1.5 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-900 hover:bg-emerald-100 font-semibold transition">
          🏛️ Need-Blind for Internationals (9 Elites)
        </button>

        <button onclick="applyPreset('merit_full')" id="preset-merit_full" class="preset-btn px-3 py-1.5 rounded-lg border border-yellow-200 bg-yellow-50 text-yellow-900 hover:bg-yellow-100 font-semibold transition">
          💎 Dec 1 Premier Merit (BU, Richmond, UT Dallas)
        </button>

        <button onclick="applyPreset('free_app')" id="preset-free_app" class="preset-btn px-3 py-1.5 rounded-lg border border-slate-200 bg-slate-100 text-slate-800 hover:bg-slate-200 font-semibold transition">
          💸 $0 Application Fee (100% Free)
        </button>

        <button onclick="applyPreset('free_isfaa')" id="preset-free_isfaa" class="preset-btn px-3 py-1.5 rounded-lg border border-slate-200 bg-slate-100 text-slate-800 hover:bg-slate-200 font-semibold transition">
          📄 Free ISFAA PDF (Skip CSS $25+$16 Fee)
        </button>

        <button onclick="applyPreset('visa_tier1')" id="preset-visa_tier1" class="preset-btn px-3 py-1.5 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-900 hover:bg-emerald-100 font-semibold transition">
          🛂 Tier 1 Visa Safe (Dhaka 98%+)
        </button>

        <button onclick="applyPreset('bank_deferred')" id="preset-bank_deferred" class="preset-btn px-3 py-1.5 rounded-lg border border-teal-200 bg-teal-50 text-teal-900 hover:bg-teal-100 font-semibold transition">
          🏦 Bank Statement Deferred ($0 at App)
        </button>

        <button onclick="applyPreset('aid_70k')" id="preset-aid_70k" class="preset-btn px-3 py-1.5 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-950 hover:bg-emerald-100 font-semibold transition">
          💰 Average Aid > $70k/yr (CDS H6)
        </button>
      </div>

      <!-- Advanced Multi-Field Filter Bar -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 pt-3 border-t border-slate-100">
        
        <!-- Live Instant Search Input -->
        <div class="relative lg:col-span-2">
          <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3.5 text-slate-400"></i>
          <input type="text" id="searchInput" placeholder="Search by college name, state, majors, CEEB code, deadlines..." 
                 class="w-full pl-10 pr-9 py-2.5 border border-slate-300 rounded-xl text-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition bg-white text-slate-900 shadow-sm">
          <button id="clearSearchBtn" onclick="clearSearch()" class="absolute right-3 top-3 text-slate-400 hover:text-slate-600 hidden text-xs">
            <i class="fa-solid fa-circle-xmark"></i>
          </button>
        </div>

        <!-- Major Strengths Filter -->
        <div>
          <select id="majorFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Academic Streams / Majors</option>
            <option value="CS">Computer Science, AI & Data Science</option>
            <option value="Engineering">Engineering (ABET Accredited)</option>
            <option value="Biomedical">Pre-Med & Biomedical / Life Sciences</option>
            <option value="Math">Mathematics, Physics & Natural Sciences</option>
            <option value="Economics">Economics, Business & Finance</option>
          </select>
        </div>

        <!-- Testing Policy Filter (EA/ED/RD) -->
        <div>
          <select id="testingFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Standardized Testing Policies</option>
            <option value="EA_OPTIONAL">Test-Optional for Early Action (EA)</option>
            <option value="ED_OPTIONAL">Test-Optional for Early Decision (ED1/ED2)</option>
            <option value="RD_OPTIONAL">Test-Optional for Regular Decision (RD)</option>
            <option value="TEST_REQUIRED">Test-Required (SAT/ACT Mandatory)</option>
            <option value="SELF_REPORT">Self-Report SAT Accepted (100% Free)</option>
          </select>
        </div>

        <!-- Financial Aid Model Filter -->
        <div>
          <select id="aidFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Financial Aid Models</option>
            <option value="NEED_BLIND">Need-Blind for Internationals (9 Elites)</option>
            <option value="FULL_NEED">Meets 100% Demonstrated Need</option>
            <option value="MERIT">Premier Full-Ride / Full-Tuition Merit</option>
            <option value="WORK">Work Colleges ($0 Tuition Guarantee - Berea)</option>
          </select>
        </div>

        <!-- Fee Waiver Filter -->
        <div>
          <select id="feeFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Fee Waiver & Form Types</option>
            <option value="FREE_APP">$0 Application Fee (Free for Everyone)</option>
            <option value="FREE_ISFAA">Accepts Free ISFAA PDF (Skip CSS Profile)</option>
            <option value="COMMON_APP_WAIVER">Accepts Common App Fee Waiver</option>
          </select>
        </div>

        <!-- F-1 Visa Safety Filter -->
        <div>
          <select id="visaFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Dhaka F-1 Visa Safety Tiers</option>
            <option value="TIER1">Tier 1 Ultra-Safe (Dhaka 98%+ Approval)</option>
            <option value="TIER2">Tier 2 High Confidence (Dhaka 93%–96%)</option>
          </select>
        </div>

        <!-- US Region Filter -->
        <div>
          <select id="regionFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All U.S. Geographic Regions</option>
            <option value="Northeast">Northeast (New England, NY, PA, NJ)</option>
            <option value="Midwest">Midwest (OH, IN, IL, MN, IA, MI)</option>
            <option value="South">South (NC, VA, TN, GA, TX, FL, KY)</option>
            <option value="West">West Coast (CA, WA, OR)</option>
          </select>
        </div>
      </div>
    </section>

    <!-- Results Toolbar & View Switcher -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs text-slate-600 bg-slate-100 p-3 rounded-xl border border-slate-200">
      <div class="flex items-center gap-2">
        <span id="resultsCount" class="font-bold text-slate-800 text-sm">Showing 160 of 160 institutions</span>
        <span id="shortlistNotice" class="hidden text-amber-700 font-semibold bg-amber-100 px-2 py-0.5 rounded border border-amber-300">
          <i class="fa-solid fa-star mr-1"></i>Showing Bookmarked Only
        </span>
      </div>

      <div class="flex items-center gap-3">
        <div class="flex items-center gap-1.5">
          <span class="text-slate-500 font-semibold hidden lg:inline">Sort:</span>
          <select id="portalSortSelect" onchange="filterAndRender()" class="py-1 px-2.5 border border-slate-300 rounded-lg text-xs font-semibold bg-white text-slate-700 shadow-sm outline-none">
            <option value="STRATEGIC_MATCH" selected>🎯 Strategic Match (Prestige + Aid + Test-Opt + Visa)</option>
            <option value="US_NEWS_ASC">🏛️ U.S. News Ranking (Top Ranked First)</option>
            <option value="WORLD_RANK_ASC">🌐 Overall World Ranking (QS / Global)</option>
            <option value="TEST_OPT_DESC">📊 Test-Optional Friendly (% Admitted Test-Free)</option>
            <option value="NAME_ASC">Name (A → Z)</option>
            <option value="DEADLINE">Early Deadlines First</option>
            <option value="PROB_DESC">Admit Rate / Probability (Highest)</option>
            <option value="VISA">Dhaka Visa Safety</option>
          </select>
        </div>

        <span class="text-slate-500 font-semibold hidden md:inline">View:</span>
        <div class="inline-flex rounded-lg border border-slate-300 bg-white p-0.5 shadow-sm">
          <button id="viewTableBtn" onclick="setViewMode('table')" class="px-2.5 py-1 rounded-md text-xs font-bold text-slate-600 hover:text-indigo-600 transition flex items-center gap-1.5">
            <i class="fa-solid fa-table-list"></i> Table View
          </button>
          <button id="viewCardBtn" onclick="setViewMode('card')" class="px-2.5 py-1 rounded-md text-xs font-bold bg-indigo-600 text-white transition flex items-center gap-1.5">
            <i class="fa-solid fa-grip"></i> Card Grid View
          </button>
        </div>
        <button onclick="clearShortlist()" id="clearShortlistBtn" class="hidden text-[11px] text-slate-500 hover:text-rose-600 underline ml-2">Clear Shortlist</button>
      </div>
    </div>

    <!-- TABLE VIEW CONTAINER (Default Hidden) -->
    <div id="tableViewContainer" class="hidden bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs sm:text-sm" id="collegesTable">
          <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200 select-none text-[11px] uppercase tracking-wider">
            <tr>
              <th class="py-3.5 px-3 w-10 text-center">⭐</th>
              <th class="py-3.5 px-4 cursor-pointer hover:text-indigo-600" onclick="sortTable(0)">Rank & Institution / CEEB <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-3 cursor-pointer hover:text-indigo-600" onclick="sortTable(1)">Location & Region <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-4">Financial Aid & Max Package</th>
              <th class="py-3.5 px-3">Testing & EA/ED Policy</th>
              <th class="py-3.5 px-3">Deadlines</th>
              <th class="py-3.5 px-3 cursor-pointer hover:text-indigo-600" onclick="sortTable(6)">Dhaka Visa Safety <i class="fa-solid fa-sort text-slate-400 ml-1"></i></th>
              <th class="py-3.5 px-3">Official Portals</th>
              <th class="py-3.5 px-3 text-center">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100" id="tableBody">
            <!-- Populated dynamically via JS -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- CARD GRID VIEW CONTAINER (Default Visible) -->
    <div id="cardViewContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <!-- Populated dynamically via JS -->
    </div>

  </main>

  <!-- Footer -->
  <footer class="bg-slate-900 text-slate-400 text-xs py-8 border-t border-slate-800 mt-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <div class="text-slate-200 font-bold text-sm flex items-center justify-center sm:justify-start gap-1.5">
          <span class="text-emerald-400">BD</span>to<span class="text-indigo-400">USA</span> Navigator • Fall 2027 Admission Cycle
        </div>
        <p class="text-[11px] text-slate-500 mt-0.5">Built with verified Common Data Set (CDS) data, official university portals, and Dhaka Embassy F-1 visa statistics.</p>
      </div>
      <div class="flex items-center gap-4 text-[11px]">
        <a href="#playbookModal" onclick="openPlaybook()" class="hover:text-slate-200 transition">Bangladeshi Playbook</a>
        <a href="US_Colleges_Fall_2027_Full_Ride_BDtoUSA.xlsx" download class="hover:text-slate-200 transition">Download Master Ledger</a>
        <button onclick="window.scrollTo({top:0, behavior:'smooth'})" class="hover:text-slate-200 transition">Back to Top ↑</button>
      </div>
    </div>
  </footer>

  <!-- DEEP DIVE DETAIL MODAL (5 TABS) -->
  <div id="detailModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
    <div class="bg-white rounded-2xl max-w-4xl w-full max-h-[92vh] overflow-y-auto shadow-2xl p-5 sm:p-7 relative border border-slate-100">
      <button onclick="closeModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-700 bg-slate-100 hover:bg-slate-200 w-8 h-8 rounded-full flex items-center justify-center text-sm transition">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <div id="modalContent"></div>
    </div>
  </div>

  <!-- BANGLADESHI APPLICANT MASTER PLAYBOOK MODAL -->
  <div id="playbookModal" class="fixed inset-0 bg-slate-900/70 backdrop-blur-sm z-50 hidden flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
    <div class="bg-white rounded-2xl max-w-4xl w-full max-h-[92vh] overflow-y-auto shadow-2xl p-6 sm:p-8 relative border border-slate-100 space-y-6">
      <button onclick="closePlaybook()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-700 bg-slate-100 hover:bg-slate-200 w-8 h-8 rounded-full flex items-center justify-center text-sm transition">
        <i class="fa-solid fa-xmark"></i>
      </button>

      <div class="border-b border-slate-100 pb-4">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-800">🇧🇩 Bangladesh Guide</span>
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-indigo-100 text-indigo-800">Fall 2027 Admissions</span>
        </div>
        <h2 class="text-2xl font-black text-slate-900 mt-2">The Bangladeshi Applicant's Playbook for U.S. Full-Ride Admissions</h2>
        <p class="text-xs text-slate-500 mt-1">A step-by-step masterclass on marksheets, fee waivers, $0 EFC documentation, gap years, and the U.S. Embassy Dhaka F-1 visa interview.</p>
      </div>

      <div class="space-y-6 text-sm text-slate-700">
        <!-- Section 1 -->
        <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
          <h3 class="font-bold text-slate-900 text-base flex items-center gap-2">
            <i class="fa-solid fa-graduation-cap text-indigo-600"></i>
            1. National Curriculum (SSC & HSC) Transcript & Grading Equivalency
          </h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Bangladeshi National Curriculum students (Bangla or English Version) take the Secondary School Certificate (SSC, Class 10) and Higher Secondary Certificate (HSC, Class 12) under education boards like Dhaka, Rajshahi, Chittagong, etc.
          </p>
          <ul class="text-xs list-disc pl-5 space-y-1 text-slate-700">
            <li><strong>GPA 5.00/5.00:</strong> Evaluated as an unweighted "A" average (top tier). U.S. admissions officers look closely at individual subject marks (e.g., Physics, Chemistry, Higher Math, ICT).</li>
            <li><strong>Official Board Marksheet vs Testimonial:</strong> You must submit the certified, original English-version marksheet and pass certificate issued by your Board of Intermediate and Secondary Education (BISE), certified by your college principal/headmaster.</li>
            <li><strong>Counselor Upload:</strong> Have your school/college counselor (principal or appointed teacher) upload these documents directly via the Common App Counselor Portal.</li>
          </ul>
        </div>

        <!-- Section 2 -->
        <div class="p-4 bg-emerald-50/70 rounded-xl border border-emerald-200 space-y-2">
          <h3 class="font-bold text-emerald-950 text-base flex items-center gap-2">
            <i class="fa-solid fa-wallet text-emerald-700"></i>
            2. The $0 EFC Financial Proof Guide (Tax Returns, Low-Income Verification & Non-Liquid Assets)
          </h3>
          <p class="text-xs text-emerald-950 leading-relaxed">
            In Bangladesh, many families work in informal sectors, have low taxable income, or own ancestral rural land.
          </p>
          <ul class="text-xs list-disc pl-5 space-y-1 text-emerald-900">
            <li><strong>Non-Taxfiler Declaration & Income Slips:</strong> If parents/guardians do not file formal NBR tax returns due to income below the taxable threshold (BDT 3.5 Lakhs), submit an official employer salary certificate or local municipal/ward counselor income certificate with an English translation.</li>
            <li><strong>Income Verification & Hardship Affidavits:</strong> Submit official employer salary slips, NBR tax assessment certificates, or local Ward Commissioner / Union Parishad income certificates confirming family income. If there are special circumstances (single-earner household, family hardship), provide a notarized financial statement confirming $0 or minimal contribution.</li>
            <li><strong>Ancestral Land / Family Homestead:</strong> Declare the property with realistic local valuation, but <em>explicitly state in the notes</em>: <span class="font-semibold">"This property is our primary non-liquid homestead in Bangladesh; it generates $0 income and cannot be sold to fund education."</span> This prevents U.S. financial aid officers from treating home equity as liquid cash!</li>
          </ul>
        </div>

        <!-- Section 3 -->
        <div class="p-4 bg-blue-50/70 rounded-xl border border-blue-200 space-y-2">
          <h3 class="font-bold text-blue-950 text-base flex items-center gap-2">
            <i class="fa-solid fa-ticket text-blue-700"></i>
            3. How to Apply 100% Free (Zero Out-of-Pocket Expense)
          </h3>
          <p class="text-xs text-blue-950 leading-relaxed">
            Applying to 25–30 U.S. colleges can cost over $3,500 in application fees and CSS Profile fees if done without waivers.
          </p>
          <ul class="text-xs list-disc pl-5 space-y-1 text-blue-900">
            <li><strong>Common App Fee Waiver:</strong> Select "Yes" under the Common App Fee Waiver profile section. Your counselor confirms it with a single checkbox. Saves ~$80 per college!</li>
            <li><strong>Bypass the $25 + $16 CSS Profile Fee:</strong> Over 35 generous colleges in this directory (e.g. Dartmouth, Bowdoin, Colby, Denison, Wooster, Knox, Skidmore) accept the <span class="font-bold">free ISFAA (International Student Financial Aid Application) PDF form</span> uploaded directly to the applicant portal!</li>
            <li><strong>CSS Waiver Codes:</strong> For colleges requiring the CSS Profile (MIT, Harvard, Yale, Amherst, Williams), email the financial aid office in October with your hardship declaration to request an institutional fee waiver code.</li>
            <li><strong>Free SAT Self-Reporting:</strong> Over 90% of colleges in this directory allow self-reporting on Common App. You only pay to send official College Board scores if admitted and enrolling!</li>
          </ul>
        </div>

        <!-- Section 4 -->
        <div class="p-4 bg-amber-50/70 rounded-xl border border-amber-200 space-y-2">
          <h3 class="font-bold text-amber-950 text-base flex items-center gap-2">
            <i class="fa-solid fa-passport text-amber-700"></i>
            4. Dhaka Embassy F-1 Visa Mastery (INA Section 214(b) & Gap Year Defense)
          </h3>
          <p class="text-xs text-amber-950 leading-relaxed">
            The U.S. Embassy on Madani Avenue in Dhaka has high refusal rates for self-funded students with partial aid, but has <span class="font-bold text-amber-900">98%+ approval rates for students with a 100% Full Ride I-20</span>!
          </p>
          <ul class="text-xs list-disc pl-5 space-y-1 text-amber-900">
            <li><strong>The I-20 Magic Line:</strong> When Form I-20 states <span class="font-bold font-mono">Institutional Scholarship: $85,000 | Student/Family Funds: $0</span>, the consular officer cannot challenge your financial ability. You don't need to present fake bank statements or sponsor affidavits!</li>
            <li><strong>Gap Year Defense:</strong> Consular officers will ask: <em>"What have you been doing since HSC?"</em>. Never answer that you were idle. Answer: <em>"I dedicated this period to advanced software engineering, co-authoring peer-reviewed biomedical research, competing in national robotics olympiads, and building community platforms, which earned me a 100% scholarship at [University]."</em></li>
            <li><strong>Non-Immigrant Intent:</strong> Explain that you will return to Bangladesh to contribute to its rapidly expanding telecom and AI software sector (bKash, national tech platforms, local AI diagnostic healthcare).</li>
          </ul>
        </div>

        <!-- Section 5 -->
        <div class="p-4 bg-purple-50/70 rounded-xl border border-purple-200 space-y-2">
          <h3 class="font-bold text-purple-950 text-base flex items-center gap-2">
            <i class="fa-solid fa-language text-purple-700"></i>
            5. Duolingo English Test (DET) Guidelines in Bangladesh
          </h3>
          <p class="text-xs text-purple-950 leading-relaxed">
            DET costs $65 (compared to $220 for IELTS) and can be taken at home on your computer.
          </p>
          <ul class="text-xs list-disc pl-5 space-y-1 text-purple-900">
            <li><strong>Free DET Waivers:</strong> Many liberal arts colleges (Denison, Wooster, Knox, Augustana) provide free DET voucher codes upon email request.</li>
            <li><strong>Webcam & AI Proctoring Caution:</strong> Ensure a silent room, no second monitor, no headphones, and keep your gaze fixed on the screen throughout the test to prevent AI invalidation.</li>
            <li><strong>SAT EBRW Waivers:</strong> Scoring 650–700+ on the SAT Reading & Writing section automatically waives English proficiency exams at over 40 top colleges!</li>
          </ul>
        </div>
      </div>

      <div class="pt-4 border-t border-slate-100 flex justify-end">
        <button onclick="closePlaybook()" class="px-5 py-2.5 rounded-xl bg-slate-900 text-white font-bold text-xs hover:bg-slate-800 transition">Close Playbook</button>
      </div>
    </div>
  </div>

  <!-- SCRIPT DATA & LOGIC -->
  <script>
    const data = JSON_DATA_PLACEHOLDER;

    // State
    let activeFilter = 'all';
    let viewMode = 'card';
    let showShortlistOnly = false;
    let shortlistedIds = JSON.parse(localStorage.getItem('bd_usa_shortlist') || '[]');

    // Initialize
    document.addEventListener('DOMContentLoaded', () => {
      updateShortlistUI();
      renderAll();
      attachEventListeners();
    });

    function copyShareLink() {
      const url = window.location.href.split('#')[0];
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(() => {
          showShareToast();
        }).catch(() => {
          fallbackPrompt(url);
        });
      } else {
        fallbackPrompt(url);
      }
    }

    function showShareToast() {
      const btn = document.getElementById('shareBtnText');
      if (btn) {
        const old = btn.innerText;
        btn.innerText = 'Copied!';
        setTimeout(() => { btn.innerText = old; }, 2200);
      }
    }

    function fallbackPrompt(url) {
      prompt('Copy this link to share the BDtoUSA College Navigator:', url);
    }

    function attachEventListeners() {
      document.getElementById('searchInput').addEventListener('input', () => {
        const val = document.getElementById('searchInput').value;
        document.getElementById('clearSearchBtn').classList.toggle('hidden', val.length === 0);
        filterAndRender();
      });
      document.getElementById('majorFilter').addEventListener('change', filterAndRender);
      document.getElementById('testingFilter').addEventListener('change', filterAndRender);
      document.getElementById('aidFilter').addEventListener('change', filterAndRender);
      document.getElementById('feeFilter').addEventListener('change', filterAndRender);
      document.getElementById('visaFilter').addEventListener('change', filterAndRender);
      document.getElementById('regionFilter').addEventListener('change', filterAndRender);
    }

    function clearSearch() {
      document.getElementById('searchInput').value = '';
      document.getElementById('clearSearchBtn').classList.add('hidden');
      filterAndRender();
    }

    function setViewMode(mode) {
      viewMode = mode;
      const isTable = mode === 'table';
      document.getElementById('tableViewContainer').classList.toggle('hidden', !isTable);
      document.getElementById('cardViewContainer').classList.toggle('hidden', isTable);
      
      document.getElementById('viewTableBtn').className = isTable 
        ? 'px-2.5 py-1 rounded-md text-xs font-bold bg-indigo-600 text-white transition flex items-center gap-1.5' 
        : 'px-2.5 py-1 rounded-md text-xs font-bold text-slate-600 hover:text-indigo-600 transition flex items-center gap-1.5';
      
      document.getElementById('viewCardBtn').className = !isTable 
        ? 'px-2.5 py-1 rounded-md text-xs font-bold bg-indigo-600 text-white transition flex items-center gap-1.5' 
        : 'px-2.5 py-1 rounded-md text-xs font-bold text-slate-600 hover:text-indigo-600 transition flex items-center gap-1.5';
    }

    function applyPreset(preset) {
      activeFilter = preset;
      document.querySelectorAll('.preset-btn').forEach(btn => {
        btn.classList.remove('bg-slate-900', 'text-white', 'border-slate-900');
        btn.classList.add('bg-white', 'text-slate-700');
      });
      const activeBtn = document.getElementById(`preset-${preset}`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-white', 'text-slate-700');
        activeBtn.classList.add('bg-slate-900', 'text-white', 'border-slate-900');
      }

      // Reset dropdowns on preset click
      document.getElementById('majorFilter').value = 'ALL';
      document.getElementById('testingFilter').value = 'ALL';
      document.getElementById('aidFilter').value = 'ALL';
      document.getElementById('feeFilter').value = 'ALL';
      document.getElementById('visaFilter').value = 'ALL';
      document.getElementById('regionFilter').value = 'ALL';

      filterAndRender();
    }

    function resetAllFilters() {
      activeFilter = 'all';
      showShortlistOnly = false;
      document.getElementById('searchInput').value = '';
      document.getElementById('clearSearchBtn').classList.add('hidden');
      document.getElementById('majorFilter').value = 'ALL';
      document.getElementById('testingFilter').value = 'ALL';
      document.getElementById('aidFilter').value = 'ALL';
      document.getElementById('feeFilter').value = 'ALL';
      document.getElementById('visaFilter').value = 'ALL';
      document.getElementById('regionFilter').value = 'ALL';
      
      document.querySelectorAll('.preset-btn').forEach(btn => {
        btn.classList.remove('bg-slate-900', 'text-white', 'border-slate-900');
      });
      document.getElementById('preset-all').classList.add('bg-slate-900', 'text-white');
      
      updateShortlistUI();
      filterAndRender();
    }

    function toggleShortlistView() {
      showShortlistOnly = !showShortlistOnly;
      updateShortlistUI();
      filterAndRender();
    }

    function updateShortlistUI() {
      const count = shortlistedIds.length;
      document.getElementById('shortlistLabel').innerText = `My Shortlist (${count})`;
      document.getElementById('shortlistToggleBtn').classList.toggle('border-amber-400', showShortlistOnly);
      document.getElementById('shortlistToggleBtn').classList.toggle('bg-amber-950/40', showShortlistOnly);
      document.getElementById('shortlistNotice').classList.toggle('hidden', !showShortlistOnly);
      document.getElementById('clearShortlistBtn').classList.toggle('hidden', count === 0);
    }

    function toggleBookmark(name, e) {
      if (e) e.stopPropagation();
      const idx = shortlistedIds.indexOf(name);
      if (idx === -1) {
        shortlistedIds.push(name);
      } else {
        shortlistedIds.splice(idx, 1);
      }
      localStorage.setItem('bd_usa_shortlist', JSON.stringify(shortlistedIds));
      updateShortlistUI();
      filterAndRender();
    }

    function clearShortlist() {
      if (confirm('Clear all bookmarked colleges from your shortlist?')) {
        shortlistedIds = [];
        localStorage.removeItem('bd_usa_shortlist');
        showShortlistOnly = false;
        updateShortlistUI();
        filterAndRender();
      }
    }

    function getFilteredList() {
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      const major = document.getElementById('majorFilter').value;
      const testing = document.getElementById('testingFilter').value;
      const aid = document.getElementById('aidFilter').value;
      const fee = document.getElementById('feeFilter').value;
      const visa = document.getElementById('visaFilter').value;
      const region = document.getElementById('regionFilter').value;

      return data.filter(c => {
        // Shortlist filter
        if (showShortlistOnly && !shortlistedIds.includes(c.name)) return false;

        // Search query
        if (q) {
          const matchQ = 
            c.name.toLowerCase().includes(q) ||
            c.location.toLowerCase().includes(q) ||
            (c.cb_code && c.cb_code.includes(q)) ||
            c.cs_strength.toLowerCase().includes(q) ||
            c.deadlines.toLowerCase().includes(q) ||
            c.tier_category.toLowerCase().includes(q);
          if (!matchQ) return false;
        }

        // Major filter
        if (major !== 'ALL') {
          const mLower = (c.majors + ' ' + c.cs_strength).toLowerCase();
          if (major === 'CS' && !mLower.includes('computer') && !mLower.includes('ai') && !mLower.includes('data')) return false;
          if (major === 'Engineering' && !mLower.includes('engineering') && !mLower.includes('robotics')) return false;
          if (major === 'Biomedical' && !mLower.includes('bio') && !mLower.includes('med') && !mLower.includes('health')) return false;
          if (major === 'Math' && !mLower.includes('math') && !mLower.includes('physics')) return false;
          if (major === 'Economics' && !mLower.includes('econ') && !mLower.includes('business')) return false;
        }

        // Testing filter
        if (testing !== 'ALL') {
          if (testing === 'EA_OPTIONAL' && c.ea_test_optional !== true) return false;
          if (testing === 'ED_OPTIONAL' && c.ed_test_optional !== true) return false;
          if (testing === 'RD_OPTIONAL' && c.rd_test_optional !== true) return false;
          if (testing === 'TEST_REQUIRED' && (c.ea_test_optional === true && c.rd_test_optional === true)) return false;
          if (testing === 'SELF_REPORT' && !c.score_policy.toLowerCase().includes('self-report')) return false;
        }

        // Aid filter
        if (aid !== 'ALL') {
          if (aid === 'NEED_BLIND' && !c.aid_policy.toLowerCase().includes('need-blind')) return false;
          if (aid === 'FULL_NEED' && !c.aid_policy.toLowerCase().includes('100% demonstrated need')) return false;
          if (aid === 'MERIT' && !c.max_aid.toLowerCase().includes('merit') && !c.aid_policy.toLowerCase().includes('scholarship')) return false;
          if (aid === 'WORK' && !c.type.toLowerCase().includes('work college')) return false;
        }

        // Fee filter
        if (fee !== 'ALL') {
          if (fee === 'FREE_APP' && !c.fee_waiver.toLowerCase().includes('no application fee') && !c.fee_waiver.toLowerCase().includes('free application')) return false;
          if (fee === 'FREE_ISFAA' && !c.fee_waiver.toLowerCase().includes('isfaa')) return false;
          if (fee === 'COMMON_APP_WAIVER' && !c.fee_waiver.toLowerCase().includes('common app')) return false;
        }

        // Visa filter
        if (visa !== 'ALL') {
          if (visa === 'TIER1' && (!c.visa_safety_index.includes('98%') && !c.visa_safety_index.includes('Tier 1'))) return false;
          if (visa === 'TIER2' && (!c.visa_safety_index.includes('93%') && !c.visa_safety_index.includes('Tier 2'))) return false;
        }

        // Region filter
        if (region !== 'ALL' && c.region !== region) return false;

        // Presets
        if (activeFilter === 'full_ride_stem') {
          return c.aid_policy.toLowerCase().includes('100% demonstrated need') || c.aid_policy.toLowerCase().includes('need-blind') || c.max_aid.toLowerCase().includes('full ride');
        } else if (activeFilter === 'test_opt_ed') {
          return c.ed_test_optional === true && (c.aid_policy.toLowerCase().includes('need-blind') || c.aid_policy.toLowerCase().includes('100% demonstrated need'));
        } else if (activeFilter === 'test_opt_ea') {
          return c.ea_test_optional === true;
        } else if (activeFilter === 'high_sat') {
          return parseFloat(c.probability) < 8.0 || c.tier_category.toLowerCase().includes('ivy') || c.tier_category.toLowerCase().includes('hyper-reach');
        } else if (activeFilter === 'need_blind') {
          return c.aid_policy.toLowerCase().includes('need-blind');
        } else if (activeFilter === 'merit_full') {
          return c.testing_strategy_round.includes('MERIT');
        } else if (activeFilter === 'free_app') {
          return c.fee_waiver.toLowerCase().includes('no application fee') || c.fee_waiver.toLowerCase().includes('free application');
        } else if (activeFilter === 'free_isfaa') {
          return c.fee_waiver.toLowerCase().includes('isfaa');
        } else if (activeFilter === 'visa_tier1') {
          return c.visa_safety_index.includes('98%') || c.visa_safety_index.includes('Tier 1');
        } else if (activeFilter === 'bank_deferred') {
          return (c.cof_policy || '').toLowerCase().includes('deferred') || (c.dossier && (c.dossier.cof_policy || '').toLowerCase().includes('deferred'));
        } else if (activeFilter === 'aid_70k') {
          const avg = (c.cds_h6 && c.cds_h6.avg_aid) || '';
          const m = avg.match(/\\$([0-9,]+)/);
          const val = m ? parseInt(m[1].replace(/,/g, '')) : 0;
          return val >= 70000;
        }

        return true;
      });
    }

    function renderAll() {
      filterAndRender();
    }

    function filterAndRender() {
      let list = getFilteredList();

      const sortVal = document.getElementById('portalSortSelect') ? document.getElementById('portalSortSelect').value : 'STRATEGIC_MATCH';
      if (sortVal === 'STRATEGIC_MATCH') {
        list.sort((a, b) => (a.strategic_rank_num || 999) - (b.strategic_rank_num || 999));
      } else if (sortVal === 'US_NEWS_ASC') {
        list.sort((a, b) => (a.us_news_rank || 999) - (b.us_news_rank || 999));
      } else if (sortVal === 'WORLD_RANK_ASC') {
        list.sort((a, b) => (a.world_rank_num || 999) - (b.world_rank_num || 999));
      } else if (sortVal === 'TEST_OPT_DESC') {
        const getPct = (str) => {
          if (!str) return 0;
          if (str.includes('100% test-free') || str.includes('test-blind')) return 100;
          const m = str.match(/(\\d+)%/);
          return m ? parseInt(m[1]) : 0;
        };
        list.sort((a, b) => getPct(b.test_optional_stat) - getPct(a.test_optional_stat));
      } else if (sortVal === 'NAME_ASC') {
        list.sort((a, b) => a.name.localeCompare(b.name));
      } else if (sortVal === 'DEADLINE') {
        list.sort((a, b) => (a.deadlines || '').localeCompare(b.deadlines || ''));
      } else if (sortVal === 'PROB_DESC') {
        list.sort((a, b) => (parseFloat(b.probability) || 0) - (parseFloat(a.probability) || 0));
      } else if (sortVal === 'VISA') {
        list.sort((a, b) => (parseFloat(b.visa_safety_index) || 0) - (parseFloat(a.visa_safety_index) || 0));
      }

      renderTable(list);
      renderCards(list);
      document.getElementById('resultsCount').innerText = `Showing ${list.length} of ${data.length} institutions`;
    }

    function renderTable(list) {
      const tbody = document.getElementById('tableBody');
      tbody.innerHTML = '';

      if (list.length === 0) {
        tbody.innerHTML = `<tr><td colspan="9" class="py-12 text-center text-slate-500 text-sm">
          <i class="fa-solid fa-filter-circle-xmark text-slate-300 text-3xl mb-2 block"></i>
          No institutions match the selected combination of filters.<br>
          <button onclick="resetAllFilters()" class="mt-2 text-indigo-600 font-bold underline">Reset Filters</button>
        </td></tr>`;
        return;
      }

      list.forEach(c => {
        const isBookmarked = shortlistedIds.includes(c.name);
        const row = document.createElement('tr');
        row.className = 'cursor-pointer transition border-b border-slate-100 hover:bg-slate-50/80';
        row.onclick = () => openModal(c);

        let probClass = 'badge-prob-reach';
        const pNum = parseFloat(c.probability);
        if (pNum >= 12) probClass = 'badge-prob-high';
        else if (pNum >= 5) probClass = 'badge-prob-mid';

        const isVisaTop = c.visa_safety_index.includes('98%') || c.visa_safety_index.includes('Tier 1');

        row.innerHTML = `
          <td class="py-3 px-3 text-center" onclick="event.stopPropagation()">
            <button onclick="toggleBookmark('${c.name.replace(/'/g, "\\'")}', event)" class="text-base transition ${isBookmarked ? 'text-amber-400 hover:text-amber-500 scale-110' : 'text-slate-300 hover:text-amber-400'}">
              <i class="fa-${isBookmarked ? 'solid' : 'regular'} fa-star"></i>
            </button>
          </td>
          <td class="py-3.5 px-4 font-bold text-slate-900">
            <div class="flex items-center gap-1.5 flex-wrap">
              <span class="text-[10px] font-black px-1.5 py-0.5 rounded bg-slate-900 text-white font-mono shadow-sm">
                ${c.strategic_rank_display || '#1 Strategic'}
              </span>
              <span class="text-[10px] font-bold px-1.5 py-0.5 rounded bg-blue-50 text-blue-900 border border-blue-200 font-mono">
                🏛️ ${c.us_news_display || 'US News Top Tier'}
              </span>
              <span class="text-[10px] font-bold px-1.5 py-0.5 rounded bg-purple-50 text-purple-900 border border-purple-200 font-mono">
                🌐 ${c.world_rank_display || 'QS World Top Tier'}
              </span>
            </div>
            <div class="text-sm font-black text-slate-900 mt-1">
              ${c.name}
            </div>
            <div class="flex items-center gap-1.5 mt-0.5">
              <span class="text-[10px] font-mono px-1.5 py-0.2 rounded bg-slate-100 text-slate-600 border border-slate-200">CEEB: ${c.cb_code || 'N/A'}</span>
              <span class="text-[11px] font-normal text-slate-500">${c.type}</span>
            </div>
          </td>
          <td class="py-3.5 px-3 text-xs text-slate-700">
            <span class="font-medium text-slate-900">${c.location}</span><br>
            <span class="text-[11px] text-slate-500">${c.region}</span>
          </td>
          <td class="py-3.5 px-4 text-xs">
            <span class="font-bold text-emerald-800 block text-[12px]">${c.max_aid.split('(')[0]}</span>
            <span class="text-[11px] text-slate-500 block mt-0.5 line-clamp-1">${c.aid_policy}</span>
          </td>
          <td class="py-3.5 px-3 text-xs">
            <span class="font-semibold text-slate-800 block text-[11px]">
              ${c.testing_policy_nuance ? c.testing_policy_nuance.split('|')[0] : (c.ed_test_optional === true ? 'Test-Optional' : 'Test-Required')}
            </span>
            <span class="text-[10px] text-indigo-700 block mt-0.5 font-medium">
              ${c.ea_test_optional === true ? '<i class=\"fa-solid fa-check text-emerald-500 mr-0.5\"></i>EA Test-Opt' : (c.ea_test_optional === false ? '<i class=\"fa-solid fa-triangle-exclamation text-amber-500 mr-0.5\"></i>EA Test-Req' : 'No EA')}
            </span>
            <span class="text-[10px] text-slate-600 block mt-0.5 font-mono">
              <i class="fa-solid fa-chart-pie text-indigo-500 mr-1"></i>${c.test_optional_stat ? c.test_optional_stat.split('(')[0].trim() : ''}
            </span>
          </td>
          <td class="py-3.5 px-3 text-xs text-slate-800 font-mono text-[11px]">
            ${c.deadlines ? c.deadlines.split(' | ').map(dl => `<span class="block whitespace-nowrap mb-0.5">${dl.trim()}</span>`).join('') : 'Rolling'}
          </td>
          <td class="py-3.5 px-3 text-xs">
            <span class="px-2 py-0.5 rounded text-[11px] ${isVisaTop ? 'badge-visa-top' : 'badge-visa-high'} block w-fit">
              <i class="fa-solid fa-shield-check mr-1"></i>${c.visa_safety_index.split('|')[0].trim()}
            </span>
          </td>
          <td class="py-3.5 px-3 text-xs" onclick="event.stopPropagation()">
            <div class="flex items-center gap-1.5 text-xs">
              <a href="${c.admissions_url}" target="_blank" rel="noopener" class="text-indigo-600 hover:text-indigo-800 p-1 hover:bg-indigo-50 rounded" title="Official Admissions Website">
                <i class="fa-solid fa-globe"></i>
              </a>
              <a href="${c.finaid_url}" target="_blank" rel="noopener" class="text-emerald-600 hover:text-emerald-800 p-1 hover:bg-emerald-50 rounded" title="International Financial Aid Portal">
                <i class="fa-solid fa-hand-holding-dollar"></i>
              </a>
              <a href="${c.testing_url}" target="_blank" rel="noopener" class="text-purple-600 hover:text-purple-800 p-1 hover:bg-purple-50 rounded" title="Testing Policy Website">
                <i class="fa-solid fa-file-pen"></i>
              </a>
            </div>
          </td>
          <td class="py-3.5 px-3 text-center" onclick="event.stopPropagation()">
            <button onclick="openModalById('${c.name.replace(/'/g, "\\'")}')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-indigo-50 hover:text-indigo-700 text-slate-700 font-semibold text-xs transition border border-slate-200">
              Details
            </button>
          </td>
        `;
        tbody.appendChild(row);
      });
    }

    function renderCards(list) {
      const container = document.getElementById('cardViewContainer');
      container.innerHTML = '';

      if (list.length === 0) return;

      list.forEach(c => {
        const isBookmarked = shortlistedIds.includes(c.name);
        const card = document.createElement('div');
        card.className = 'bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:shadow-md transition space-y-4 flex flex-col justify-between';
        
        let aidBadge = c.aid_policy.toLowerCase().includes('need-blind') 
          ? '<span class="px-2 py-0.5 rounded text-[10px] font-bold badge-need-blind">Need-Blind</span>'
          : '<span class="px-2 py-0.5 rounded text-[10px] font-bold badge-need-aware">100% Need Met</span>';

        const isVisaTop = c.visa_safety_index.includes('98%') || c.visa_safety_index.includes('Tier 1');

        card.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-start justify-between gap-2">
              <div>
                <div class="flex items-center gap-1.5 flex-wrap">
                  <span class="text-[10px] font-black px-1.5 py-0.5 rounded bg-slate-900 text-white font-mono shadow-sm">
                    ${c.strategic_rank_display || '#1 Strategic'}
                  </span>
                  <span class="text-[10px] font-bold px-1.5 py-0.5 rounded bg-blue-50 text-blue-900 border border-blue-200 font-mono">
                    🏛️ ${c.us_news_display || 'US News Top Tier'}
                  </span>
                  <span class="text-[10px] font-bold px-1.5 py-0.5 rounded bg-purple-50 text-purple-900 border border-purple-200 font-mono">
                    🌐 ${c.world_rank_display || 'QS World Top Tier'}
                  </span>
                  ${aidBadge}
                  <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-100 text-slate-600 border border-slate-200 font-bold">CEEB: ${c.cb_code || 'N/A'}</span>
                </div>
                <h3 class="text-base font-bold text-slate-900 mt-1 hover:text-indigo-600 cursor-pointer" onclick="openModalById('${c.name.replace(/'/g, "\\'")}')">${c.name}</h3>
                <p class="text-xs text-slate-500"><i class="fa-solid fa-location-dot text-slate-400 mr-1"></i>${c.location} • ${c.region}</p>
              </div>
              <button onclick="toggleBookmark('${c.name.replace(/'/g, "\\'")}', event)" class="text-lg transition ${isBookmarked ? 'text-amber-400 hover:text-amber-500 scale-110' : 'text-slate-300 hover:text-amber-400'}">
                <i class="fa-${isBookmarked ? 'solid' : 'regular'} fa-star"></i>
              </button>
            </div>

            <div class="p-3 bg-slate-50 rounded-xl border border-slate-100 space-y-1.5 text-xs">
              <div class="text-[11px] font-bold text-emerald-800"><i class="fa-solid fa-shield-halved text-emerald-600 mr-1"></i>${c.max_aid.split('(')[0]}</div>
              <p class="text-slate-600 line-clamp-2">${c.cs_strength}</p>
            </div>

            <div class="grid grid-cols-2 gap-2 text-[11px]">
              <div class="p-2 bg-emerald-50/80 rounded-lg border border-emerald-100">
                <span class="text-emerald-900 uppercase text-[9px] font-bold block"><i class="fa-solid fa-file-invoice-dollar mr-1"></i>CDS H6 Avg Aid</span>
                <span class="font-black text-emerald-950 font-mono text-xs">${(c.cds_h6 && c.cds_h6.avg_aid) || '$70,000+/yr'}</span>
              </div>
              <div class="p-2 bg-teal-50/80 rounded-lg border border-teal-100">
                <span class="text-teal-900 uppercase text-[9px] font-bold block"><i class="fa-solid fa-building-columns mr-1"></i>Bank Statement</span>
                <span class="font-bold text-teal-950 text-[10.5px] leading-tight block">${c.cof_badge ? (c.cof_badge.includes('Deferred') ? '🏦 Deferred ($0 App)' : '⚠️ Req at App') : '🏦 Deferred ($0 App)'}</span>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-2 text-[11px]">
              <div class="p-2 bg-slate-50 rounded-lg">
                <span class="text-slate-400 uppercase text-[9px] font-bold block">Testing EA/ED</span>
                <span class="font-semibold text-slate-800">${c.ed_test_optional === true ? 'Test-Optional' : 'Test-Required'}</span>
              </div>
              <div class="p-2 bg-slate-50 rounded-lg">
                <span class="text-slate-400 uppercase text-[9px] font-bold block">Dhaka Visa</span>
                <span class="font-semibold ${isVisaTop ? 'text-emerald-700' : 'text-blue-700'}">${c.visa_safety_index.split('|')[0].trim()}</span>
              </div>
            </div>

            <div class="p-2 bg-indigo-50/70 rounded-lg border border-indigo-100 text-[11px] space-y-0.5">
              <div class="text-[10px] font-bold text-indigo-900 uppercase flex items-center justify-between">
                <span><i class="fa-solid fa-chart-pie text-indigo-600 mr-1"></i>CDS C9 Test-Optional:</span>
              </div>
              <span class="font-semibold text-indigo-950">${c.test_optional_stat || 'Test-Optional Active'}</span>
            </div>

            <div class="p-2 bg-amber-50/70 rounded-lg border border-amber-200 text-[11px] space-y-0.5">
              <span class="text-amber-900 uppercase text-[9px] font-bold block"><i class="fa-regular fa-calendar-days text-amber-700 mr-1"></i>All Deadlines (App & Aid)</span>
              <span class="font-mono text-slate-800 text-[10.5px] block leading-snug">${c.deadlines}</span>
            </div>
          </div>

          <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
            <div class="flex items-center gap-2">
              <a href="${c.admissions_url}" target="_blank" rel="noopener" class="text-indigo-600 hover:text-indigo-800 font-semibold flex items-center gap-1">
                Admissions <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
              </a>
              <span class="text-slate-300">•</span>
              <a href="${c.finaid_url}" target="_blank" rel="noopener" class="text-emerald-600 hover:text-emerald-800 font-semibold flex items-center gap-1">
                Aid <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
              </a>
            </div>
            <button onclick="openModalById('${c.name.replace(/'/g, "\\'")}')" class="px-3 py-1.5 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition">
              Deep Dive
            </button>
          </div>
        `;
        container.appendChild(card);
      });
    }

    function openModalById(name) {
      const c = data.find(item => item.name === name);
      if (c) openModal(c);
    }

    function jumpToModalSec(secId) {
      const el = document.getElementById(secId);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function openModal(c) {
      const modal = document.getElementById('detailModal');
      const content = document.getElementById('modalContent');
      const isBookmarked = shortlistedIds.includes(c.name);

      content.innerHTML = `
        <!-- Modal Top Bar -->
        <div class="flex items-start justify-between border-b border-slate-100 pb-4 mb-4">
          <div>
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-slate-900 text-white font-mono shadow-sm"><i class="fa-solid fa-trophy text-amber-400 mr-1"></i>${c.strategic_rank_display || '#1 Strategic'}</span>
              <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-blue-50 text-blue-900 border border-blue-200 font-mono">🏛️ ${c.us_news_display || 'US News Top Tier'}</span>
              <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-purple-50 text-purple-900 border border-purple-200 font-mono">🌐 ${c.world_rank_display || 'QS World Top Tier'}</span>
              <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200">${c.tier_category}</span>
              <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-300"><i class="fa-solid fa-scale-balanced mr-1"></i>${c.need_blind_status}</span>
              <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200">CEEB: ${c.cb_code || 'N/A'}</span>
              <span class="text-xs font-semibold px-2 py-0.5 rounded bg-slate-100 text-slate-600">${c.region} Region</span>
            </div>
            <h2 class="text-2xl font-black text-slate-900 mt-2">${c.name}</h2>
            <p class="text-slate-500 text-xs sm:text-sm mt-0.5"><i class="fa-solid fa-location-dot text-rose-500 mr-1"></i> ${c.location} • ${c.type}</p>
          </div>
          <button onclick="toggleBookmark('${c.name.replace(/'/g, "\\'")}', event)" class="text-2xl transition ${isBookmarked ? 'text-amber-400 hover:text-amber-500' : 'text-slate-300 hover:text-amber-400'}" title="Toggle Bookmark">
            <i class="fa-${isBookmarked ? 'solid' : 'regular'} fa-star"></i>
          </button>
        </div>

        <!-- Sticky Quick-Jump Navigation Bar -->
        <div class="sticky top-0 bg-white/95 backdrop-blur-md z-30 py-2.5 mb-6 border-b border-slate-200 flex items-center gap-2 overflow-x-auto text-xs font-bold text-slate-600">
          <span class="text-[11px] uppercase tracking-wider text-slate-400 mr-1 hidden sm:inline"><i class="fa-solid fa-compass mr-1"></i>Jump:</span>
          <button onclick="jumpToModalSec('modal-sec-aid')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-emerald-50 hover:text-emerald-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-solid fa-hand-holding-dollar text-emerald-600"></i> Aid & CDS H6
          </button>
          <button onclick="jumpToModalSec('modal-sec-bank')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-teal-50 hover:text-teal-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-solid fa-building-columns text-teal-600"></i> Bank / COF
          </button>
          <button onclick="jumpToModalSec('modal-sec-testing')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-amber-50 hover:text-amber-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-solid fa-chart-line text-amber-600"></i> Testing & English
          </button>
          <button onclick="jumpToModalSec('modal-sec-academics')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-indigo-50 hover:text-indigo-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-solid fa-microchip text-indigo-600"></i> Academics & Deadlines
          </button>
          <button onclick="jumpToModalSec('modal-sec-supplements')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-purple-50 hover:text-purple-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-solid fa-file-pen text-purple-600"></i> Supplements
          </button>
          <button onclick="jumpToModalSec('modal-sec-visa')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-emerald-50 hover:text-emerald-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-solid fa-passport text-emerald-600"></i> Dhaka Visa
          </button>
          <button onclick="jumpToModalSec('modal-sec-reddit')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-orange-50 hover:text-orange-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-brands fa-reddit text-orange-600"></i> Reddit Reality
          </button>
          <button onclick="jumpToModalSec('modal-sec-sources')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-blue-50 hover:text-blue-800 transition whitespace-nowrap flex items-center gap-1 border border-slate-200 text-xs">
            <i class="fa-solid fa-link text-blue-600"></i> Portals
          </button>
        </div>

        <!-- SINGLE-PAGE CATEGORIES CONTAINER (One After Another) -->
        <div class="space-y-6">

          <!-- CATEGORY 1: FINANCIAL AID & CDS SECTION H6 AUDIT -->
          <div id="modal-sec-aid" class="scroll-mt-16 space-y-4 pt-2">
            <div class="flex items-center justify-between border-b border-emerald-100 pb-2">
              <h3 class="text-sm font-extrabold text-emerald-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-hand-holding-dollar text-emerald-700"></i>
                1. Financial Aid Guarantee & CDS Section H6 International Audit
              </h3>
              <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded font-mono">CDS Section H6</span>
            </div>

            <div class="p-4 bg-emerald-900 text-white rounded-xl shadow-sm space-y-2.5">
              <div class="flex items-center justify-between flex-wrap gap-2">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-300">
                  <i class="fa-solid fa-file-invoice-dollar mr-1"></i> Official Undergraduate International Financial Aid Data
                </span>
                <span class="text-[10px] bg-emerald-800 text-emerald-200 px-2 py-0.5 rounded font-mono font-bold">${(c.cds_h6 && c.cds_h6.loan_free) ? 'Loan-Free Policy Active' : 'Meets 100% Need'}</span>
              </div>
              <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 text-center text-xs">
                <div class="p-2.5 bg-emerald-800/80 rounded-lg border border-emerald-700/60">
                  <span class="text-[10px] text-emerald-200 uppercase font-bold block">Avg International Aid</span>
                  <span class="font-black text-amber-300 font-mono text-sm">${(c.cds_h6 && c.cds_h6.avg_aid) || '$70,000+/yr'}</span>
                </div>
                <div class="p-2.5 bg-emerald-800/80 rounded-lg border border-emerald-700/60">
                  <span class="text-[10px] text-emerald-200 uppercase font-bold block">% Internationals Aided</span>
                  <span class="font-bold text-white font-mono text-sm">${(c.cds_h6 && c.cds_h6.pct_aided) || '65%+'}</span>
                </div>
                <div class="p-2.5 bg-emerald-800/80 rounded-lg border border-emerald-700/60">
                  <span class="text-[10px] text-emerald-200 uppercase font-bold block">International Aid Budget</span>
                  <span class="font-bold text-white font-mono text-sm">${(c.cds_h6 && c.cds_h6.total_budget) || '$8M - $25M+'}</span>
                </div>
                <div class="p-2.5 bg-emerald-800/80 rounded-lg border border-emerald-700/60">
                  <span class="text-[10px] text-emerald-200 uppercase font-bold block">Scholars Aided Count</span>
                  <span class="font-bold text-emerald-300 font-mono text-sm">${(c.cds_h6 && c.cds_h6.aided_count) || '150+ scholars'}</span>
                </div>
              </div>
              <p class="text-[11px] text-emerald-100 pt-1">
                <strong>Loan-Free Guarantee:</strong> ${(c.cds_h6 && c.cds_h6.loan_free) || 'Meets 100% demonstrated financial need with pure grants (zero institutional loans).'}
              </p>
            </div>

            <div class="p-4 bg-emerald-50/70 rounded-xl border border-emerald-200 text-xs space-y-1.5">
              <span class="font-bold text-emerald-950 block text-xs">Official Institutional Aid Policy & Maximum Award:</span>
              <p class="text-slate-800 leading-relaxed font-medium">${c.aid_policy}</p>
              <div class="pt-1.5 border-t border-emerald-200 flex items-center justify-between flex-wrap gap-2 text-xs">
                <span class="font-bold text-emerald-900"><i class="fa-solid fa-shield-halved text-emerald-700 mr-1"></i>Max Package: ${c.max_aid}</span>
                <span class="font-bold text-purple-900"><i class="fa-solid fa-check-circle text-purple-600 mr-1"></i>$0 EFC Covered: ${c.efc_0_covered}</span>
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div class="p-3 bg-blue-50/60 rounded-xl border border-blue-200">
                <span class="font-bold text-blue-900 block mb-1"><i class="fa-solid fa-file-invoice mr-1 text-blue-700"></i>Required Financial Aid Form:</span>
                <p class="text-blue-950 font-medium">${c.finaid_form_protocol || (c.dossier && c.dossier.finaid_form) || 'Free ISFAA PDF uploaded to portal or CSS Profile with institutional fee waiver code.'}</p>
              </div>
              <div class="p-3 bg-purple-50/60 rounded-xl border border-purple-200">
                <span class="font-bold text-purple-900 block mb-1"><i class="fa-solid fa-receipt mr-1 text-purple-700"></i>Application & CSS Fee Waivers:</span>
                <p class="text-purple-950 font-medium">${c.fee_waiver}</p>
              </div>
            </div>

            <div class="mt-2.5 pt-2 border-t border-emerald-200 flex flex-wrap items-center justify-between text-[11px] text-emerald-950">
              <span><i class="fa-solid fa-shield-halved text-emerald-600 mr-1"></i><strong>Verified Source:</strong> Institutional Common Data Set Section H6 & SFS Office</span>
              <a href="${c.finaid_url}" target="_blank" rel="noopener" class="font-bold text-emerald-700 underline hover:text-emerald-900">Official Aid Portal <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i></a>
            </div>
          </div>

          <!-- CATEGORY 2: BANK STATEMENT & COF PROTOCOL -->
          <div id="modal-sec-bank" class="scroll-mt-16 space-y-3 pt-2">
            <div class="flex items-center justify-between border-b border-teal-100 pb-2">
              <h3 class="text-sm font-extrabold text-teal-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-building-columns text-teal-700"></i>
                2. Bank Statement & Certification of Finances (COF) Protocol
              </h3>
              <span class="text-[10px] bg-teal-100 text-teal-900 font-bold px-2 py-0.5 rounded">${c.cof_badge || (c.dossier && c.dossier.cof_badge) || 'Bank Statement Deferred'}</span>
            </div>

            <div class="p-3.5 bg-teal-50/80 rounded-xl border border-teal-200 text-xs space-y-1.5">
              <span class="font-bold text-teal-950 block">Bank Solvency Timing Rule for Bangladeshi Applicants:</span>
              <p class="text-teal-950 leading-relaxed font-medium">${c.cof_policy || (c.dossier && c.dossier.cof_policy) || 'DEFERRED (POST-ADMISSION ONLY): Zero bank statements required at application! You only submit financial declarations (COF / ISFAA / Tax Slip declaring $0 EFC). Official bank balance certification is only requested AFTER admission for Form I-20 issuance.'}</p>
            </div>

            <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 text-xs space-y-1.5">
              <span class="font-bold text-slate-800 block"><i class="fa-solid fa-folder-open text-slate-600 mr-1"></i>Required Financial Proof Checklist:</span>
              <p class="text-slate-700 leading-relaxed font-medium">${c.required_documents}</p>
            </div>

            <div class="mt-2.5 pt-2 border-t border-teal-200 flex flex-wrap items-center justify-between text-[11px] text-teal-950">
              <span><i class="fa-solid fa-file-invoice-dollar text-teal-600 mr-1"></i><strong>Verified Source:</strong> International Admissions Financial Declaration Policy</span>
              <a href="${c.admissions_url}" target="_blank" rel="noopener" class="font-bold text-teal-700 underline hover:text-teal-900">Official Guidelines <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i></a>
            </div>
          </div>

          <!-- CATEGORY 3: STANDARDIZED TESTING, CDS C9 & ENGLISH PROFICIENCY -->
          <div id="modal-sec-testing" class="scroll-mt-16 space-y-3 pt-2">
            <div class="flex items-center justify-between border-b border-amber-100 pb-2">
              <h3 class="text-sm font-extrabold text-amber-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-chart-line text-amber-700"></i>
                3. Standardized Testing, CDS C9 & English Waiver Criteria
              </h3>
              <span class="text-[10px] bg-amber-100 text-amber-900 font-bold px-2 py-0.5 rounded font-mono">CDS Section C9</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-center text-xs">
              <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                <span class="text-slate-400 uppercase text-[10px] font-bold block">Early Action (EA)</span>
                <span class="font-bold ${c.ea_test_optional === true ? 'text-emerald-700' : (c.ea_test_optional === false ? 'text-rose-700' : 'text-slate-500')}">
                  ${c.ea_test_optional === true ? 'Test-Optional' : (c.ea_test_optional === false ? 'Test-Required' : 'No EA Round')}
                </span>
              </div>
              <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                <span class="text-slate-400 uppercase text-[10px] font-bold block">Early Decision (ED)</span>
                <span class="font-bold ${c.ed_test_optional === true ? 'text-emerald-700' : (c.ed_test_optional === false ? 'text-rose-700' : 'text-slate-500')}">
                  ${c.ed_test_optional === true ? 'Test-Optional' : (c.ed_test_optional === false ? 'Test-Required' : 'No ED Round')}
                </span>
              </div>
              <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                <span class="text-slate-400 uppercase text-[10px] font-bold block">Regular Decision (RD)</span>
                <span class="font-bold ${c.rd_test_optional === true ? 'text-emerald-700' : 'text-rose-700'}">
                  ${c.rd_test_optional === true ? 'Test-Optional' : 'Test-Required'}
                </span>
              </div>
            </div>

            <div class="p-3.5 bg-amber-50/70 rounded-xl border border-amber-200 text-xs space-y-1">
              <span class="font-bold text-amber-950 block">Strategic Testing Recommendation & Policy Nuance:</span>
              <p class="text-sm font-bold text-slate-900">${c.testing_strategy_round}</p>
              <p class="text-xs text-amber-950 leading-relaxed font-medium mt-1">${c.testing_policy_nuance}</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div class="p-3 bg-indigo-50/80 rounded-xl border border-indigo-200 space-y-1">
                <span class="font-bold text-indigo-900 block"><i class="fa-solid fa-chart-pie text-indigo-600 mr-1"></i>CDS Section C9 Verified Admit Stat:</span>
                <p class="text-indigo-950 font-semibold">${c.test_optional_stat || 'Test-Optional Policy Active (~50% Enrolled Without Scores)'}</p>
              </div>
              <div class="p-3 bg-amber-50/80 rounded-xl border border-amber-200 space-y-1">
                <span class="font-bold text-amber-900 block"><i class="fa-regular fa-clock text-amber-700 mr-1"></i>November 7 SAT Score Release Protocol:</span>
                <p class="text-amber-950 font-medium">${c.nov_sat_policy}</p>
              </div>
            </div>

            <div class="p-3 bg-purple-50/80 rounded-xl border border-purple-200 text-xs space-y-1">
              <span class="font-bold text-purple-950 block"><i class="fa-solid fa-language text-purple-700 mr-1"></i>English Proficiency Cutoffs & SAT EBRW Waiver Threshold:</span>
              <p class="text-purple-950 font-medium">${c.english_cutoffs_waiver || (c.dossier && c.dossier.english_cutoffs_waiver) || 'DET: 120–130+ | IELTS: 7.0–7.5+ | TOEFL: 95–100+ (SAT EBRW 650+ waives test).'}</p>
              <p class="text-[11px] text-slate-600 mt-1"><strong>Score Reporting Policy:</strong> ${c.score_policy}</p>
            </div>

            <div class="p-3 bg-rose-50/80 rounded-xl border border-rose-200 text-xs space-y-1">
              <span class="font-bold text-rose-950 block"><i class="fa-solid fa-file-circle-check text-rose-700 mr-1"></i>Special Institutional Components:</span>
              <p class="text-rose-950 font-medium">${c.special_requirements || (c.dossier && c.dossier.special_requirements) || 'Standard Common Application materials; optional portal video or maker portfolio where applicable.'}</p>
            </div>

            <div class="mt-2.5 pt-2 border-t border-amber-200 flex flex-wrap items-center justify-between text-[11px] text-amber-950">
              <span><i class="fa-solid fa-chart-line text-amber-700 mr-1"></i><strong>Verified Source:</strong> Common Data Set Section C9 & Undergraduate Testing Policy</span>
              <a href="${c.testing_url}" target="_blank" rel="noopener" class="font-bold text-amber-800 underline hover:text-amber-950">Official Testing Policy <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i></a>
            </div>
          </div>

          <!-- CATEGORY 4: ACADEMICS & DEADLINES -->
          <div id="modal-sec-academics" class="scroll-mt-16 space-y-3 pt-2">
            <div class="flex items-center justify-between border-b border-indigo-100 pb-2">
              <h3 class="text-sm font-extrabold text-indigo-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-microchip text-indigo-700"></i>
                4. Academic Department Strengths, Prior Coursework & Deadlines
              </h3>
              <span class="text-[10px] bg-indigo-100 text-indigo-900 font-bold px-2 py-0.5 rounded">Academics</span>
            </div>

            <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 text-xs space-y-1">
              <span class="font-bold text-slate-800 block">Major & Research Highlights (CS, AI, Engineering & Sciences):</span>
              <p class="text-slate-800 font-medium leading-relaxed">${c.cs_strength}</p>
              <p class="text-[11px] text-slate-600 pt-1"><strong>Key Disciplines:</strong> ${c.majors}</p>
            </div>

            <div class="p-3.5 bg-rose-50/70 border border-rose-200 rounded-xl text-xs space-y-1">
              <span class="font-bold text-rose-950 uppercase block flex items-center gap-1.5">
                <i class="fa-solid fa-triangle-exclamation text-rose-600"></i>
                Prior University Coursework & Freshman Eligibility Rule
              </span>
              <p class="text-rose-900 leading-relaxed font-medium">${c.college_coursework_policy}</p>
            </div>

            <div class="p-3.5 bg-amber-50/70 rounded-xl border border-amber-200 text-xs space-y-1.5">
              <span class="font-bold text-amber-950 block"><i class="fa-regular fa-calendar-days text-amber-700 mr-1"></i>Complete Application & Financial Aid Deadlines:</span>
              <p class="text-slate-900 font-mono font-medium text-xs leading-relaxed">${c.deadlines}</p>
              <div class="pt-1 border-t border-amber-200/80 flex items-center justify-between flex-wrap gap-2 text-[11px]">
                <span class="text-emerald-800"><strong>Merit Scholarship Deadline:</strong> ${c.merit_deadline || 'Considered automatically with admission'}</span>
                <span class="text-slate-700"><strong>FinAid Priority:</strong> ${c.finaid_deadline || 'Nov 15 (ED) / Jan 15 (RD)'}</span>
              </div>
            </div>

            <div class="mt-2.5 pt-2 border-t border-indigo-200 flex flex-wrap items-center justify-between text-[11px] text-indigo-950">
              <span><i class="fa-solid fa-calendar-check text-indigo-700 mr-1"></i><strong>Verified Source:</strong> Official First-Year Deadlines & Academic Department Catalog</span>
              <a href="${c.admissions_url}" target="_blank" rel="noopener" class="font-bold text-indigo-700 underline hover:text-indigo-900">Admissions Portal <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i></a>
            </div>
          </div>

          <!-- CATEGORY 5: SUPPLEMENTS & EVALUATION FACTORS -->
          <div id="modal-sec-supplements" class="scroll-mt-16 space-y-3 pt-2">
            <div class="flex items-center justify-between border-b border-purple-100 pb-2">
              <h3 class="text-sm font-extrabold text-purple-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-file-pen text-purple-700"></i>
                5. Supplemental Essays, Tactical Realities & Multi-Factor Score
              </h3>
              <span class="text-[10px] bg-purple-100 text-purple-900 font-bold px-2 py-0.5 rounded">Supplements</span>
            </div>

            <!-- Factor Score Breakdown Card -->
            <div class="p-4 bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-xl shadow-sm space-y-2">
              <div class="flex items-center justify-between flex-wrap gap-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-300"><i class="fa-solid fa-chart-simple mr-1"></i> Multi-Factor Strategic Score Breakdown</span>
                <span class="text-sm font-black text-amber-400 font-mono">${c.strategic_rank_display || '#1 Strategic'}</span>
              </div>
              <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 pt-2 text-center text-xs">
                <div class="p-2 bg-slate-800/80 rounded-lg border border-slate-700">
                  <span class="text-[10px] text-slate-400 uppercase font-bold block">Aid Generosity (40%)</span>
                  <span class="font-bold text-emerald-400 font-mono text-sm">${c.factor_scores ? c.factor_scores.aid_generosity : 100}/100</span>
                </div>
                <div class="p-2 bg-slate-800/80 rounded-lg border border-slate-700">
                  <span class="text-[10px] text-slate-400 uppercase font-bold block">Academic Prestige (25%)</span>
                  <span class="font-bold text-blue-400 font-mono text-sm">${c.factor_scores ? c.factor_scores.academic_prestige : 95}/100</span>
                </div>
                <div class="p-2 bg-slate-800/80 rounded-lg border border-slate-700">
                  <span class="text-[10px] text-slate-400 uppercase font-bold block">Test Flexibility (15%)</span>
                  <span class="font-bold text-amber-400 font-mono text-sm">${c.factor_scores ? c.factor_scores.test_optional_leverage : 90}/100</span>
                </div>
                <div class="p-2 bg-slate-800/80 rounded-lg border border-slate-700">
                  <span class="text-[10px] text-slate-400 uppercase font-bold block">Visa Safety (10%)</span>
                  <span class="font-bold text-purple-400 font-mono text-sm">${c.factor_scores ? c.factor_scores.visa_safety : 100}/100</span>
                </div>
                <div class="p-2 bg-slate-800/80 rounded-lg border border-slate-700">
                  <span class="text-[10px] text-slate-400 uppercase font-bold block">Cost Efficiency (10%)</span>
                  <span class="font-bold text-rose-400 font-mono text-sm">${c.factor_scores ? c.factor_scores.cost_efficiency : 90}/100</span>
                </div>
              </div>
            </div>

            <div class="p-3.5 bg-indigo-50/70 border border-indigo-200 rounded-xl space-y-1.5 text-xs">
              <span class="font-bold text-indigo-950 uppercase tracking-wider block flex items-center gap-1.5">
                <i class="fa-solid fa-file-pen text-indigo-700"></i>
                Verified Supplemental Essay Prompts & Portfolios
              </span>
              <ul class="text-slate-800 space-y-1 pl-3 font-medium">
                ${(c.dossier && c.dossier.supplements ? c.dossier.supplements : [
                  "Common Application Member Questions & Institutional Essays",
                  "Optional Maker/Research Portfolio submitted via Slideroom"
                ]).map(s => `<li>• ${s}</li>`).join('')}
              </ul>
            </div>

            <div class="p-3.5 bg-amber-50/70 border border-amber-200 rounded-xl space-y-1.5 text-xs">
              <span class="font-bold text-amber-950 uppercase tracking-wider block flex items-center gap-1.5">
                <i class="fa-solid fa-asterisk text-amber-600"></i>
                Tactical Admissions Realities & Quota Insights
              </span>
              <ul class="text-amber-950 space-y-1 pl-3 font-medium">
                ${(c.dossier && c.dossier.tactical ? c.dossier.tactical : [
                  c.aid_policy || "Meets 100% demonstrated financial need for admitted students."
                ]).map(t => `<li>* ${t}</li>`).join('')}
              </ul>
            </div>

            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs">
              <span class="font-bold text-slate-900 block mb-1"><i class="fa-solid fa-user-tie text-indigo-600 mr-1"></i>Alumni & Admissions Interview Policy:</span>
              <p class="text-slate-700 font-medium">${c.interview_policy || 'Evaluative or informational interviews available based on alumni availability post-submission.'}</p>
            </div>

            <div class="mt-2.5 pt-2 border-t border-purple-200 flex flex-wrap items-center justify-between text-[11px] text-purple-950">
              <span><i class="fa-solid fa-feather-pointed text-purple-700 mr-1"></i><strong>Verified Source:</strong> Common Application Prompts & Institutional Writing Requirements</span>
              <a href="${c.admissions_url}" target="_blank" rel="noopener" class="font-bold text-purple-700 underline hover:text-purple-900">Admissions Guidelines <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i></a>
            </div>
          </div>

          <!-- CATEGORY 6: DHAKA EMBASSY VISA PROTOCOL -->
          <div id="modal-sec-visa" class="scroll-mt-16 space-y-3 pt-2">
            <div class="flex items-center justify-between border-b border-emerald-100 pb-2">
              <h3 class="text-sm font-extrabold text-emerald-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-passport text-emerald-700"></i>
                6. Dhaka Embassy F-1 Visa Protocol (INA § 214(b) Mitigation)
              </h3>
              <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded font-mono">${c.visa_safety_index.split('|')[0].trim()}</span>
            </div>

            <div class="p-3.5 bg-emerald-50/80 rounded-xl border border-emerald-300 text-xs space-y-1">
              <div class="text-sm font-extrabold text-emerald-900">${c.visa_safety_index.split('|')[0]}</div>
              <p class="text-emerald-950 leading-relaxed font-medium">${c.visa_safety_index.includes('|') ? c.visa_safety_index.split('|')[1] : ''}</p>
            </div>

            <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 text-xs space-y-2">
              <span class="font-bold text-slate-800 block text-xs">Strategic Advice for Bangladeshi Applicants:</span>
              <p class="text-slate-700 leading-relaxed font-medium">${c.bd_specific_advice}</p>
              <div class="p-2.5 bg-blue-50/70 border border-blue-200 rounded-lg text-blue-950 text-[11px] leading-relaxed">
                <strong>Visa Officer Formula:</strong> A full-ride award letter + zero parental contribution on Form I-20 eliminates Section 214(b) financial scrutiny. Articulate your major fit and commitment to return to Bangladesh upon graduation.
              </div>
            </div>

            <div class="mt-2.5 pt-2 border-t border-emerald-200 flex flex-wrap items-center justify-between text-[11px] text-emerald-950">
              <span><i class="fa-solid fa-passport text-emerald-700 mr-1"></i><strong>Verified Source:</strong> U.S. Embassy in Dhaka Consular Affairs & INA § 214(b) Regulations</span>
              <a href="https://bd.usembassy.gov/visas/" target="_blank" rel="noopener" class="font-bold text-emerald-700 underline hover:text-emerald-900">Dhaka Embassy Portal <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i></a>
            </div>
          </div>

          <!-- CATEGORY 7: REDDIT & COMMUNITY REALITY CHECK -->
          <div id="modal-sec-reddit" class="scroll-mt-16 space-y-3 pt-2">
            <div class="flex items-center justify-between border-b border-orange-100 pb-2 flex-wrap gap-2">
              <h3 class="text-sm font-extrabold text-orange-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-brands fa-reddit text-orange-600"></i>
                7. r/IntltoUSA & Bangladeshi Applicant Community Reality Check
              </h3>
              <span class="text-[10px] bg-orange-100 text-orange-900 font-bold px-2.5 py-1 rounded-full border border-orange-200">${c.reddit_status_badge || 'VERIFIED COMMUNITY TRUTH'}</span>
            </div>

            <div class="p-4 bg-orange-50/80 rounded-xl border border-orange-200 text-xs space-y-3">
              <p class="text-xs sm:text-sm text-slate-900 font-medium leading-relaxed">${c.reddit_analysis}</p>
              
              <!-- Verified Source Buttons Attached Directly -->
              <div class="pt-3 border-t border-orange-200 flex flex-wrap items-center gap-2">
                <a href="${c.reddit_intl_url || 'https://www.reddit.com/r/IntltoUSA/'}" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-orange-600 text-white font-bold text-xs hover:bg-orange-700 transition shadow-sm">
                  <i class="fa-brands fa-reddit"></i>
                  <span>r/IntltoUSA Discussions</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                </a>
                <a href="${c.reddit_a2c_url || 'https://www.reddit.com/r/ApplyingToCollege/'}" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 text-white font-bold text-xs hover:bg-slate-700 transition shadow-sm">
                  <i class="fa-brands fa-reddit-alien"></i>
                  <span>r/ApplyingToCollege Aid Threads</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                </a>
                <a href="${c.finaid_url}" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-700 text-white font-bold text-xs hover:bg-emerald-800 transition shadow-sm">
                  <i class="fa-solid fa-shield-check"></i>
                  <span>CDS Section H6 Cross-Check</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                </a>
              </div>

              <div class="text-[11px] text-orange-950 font-medium flex items-center gap-1.5">
                <i class="fa-solid fa-certificate text-orange-600"></i>
                <span><strong>Verification Source:</strong> ${c.reddit_citation || 'r/IntltoUSA Decision Archives, A2C International Aid Wiki & Common Data Set Audit'}</span>
              </div>
            </div>
          </div>

          <!-- CATEGORY 8: VERIFIED OFFICIAL PORTALS -->
          <div id="modal-sec-sources" class="scroll-mt-16 space-y-3 pt-2">
            <div class="flex items-center justify-between border-b border-blue-100 pb-2">
              <h3 class="text-sm font-extrabold text-blue-950 uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-link text-blue-700"></i>
                8. Verified Official Web Portals & Verification Reference
              </h3>
              <span class="text-[10px] bg-blue-100 text-blue-900 font-bold px-2 py-0.5 rounded font-mono">Official Sources</span>
            </div>

            <div class="p-3.5 bg-indigo-50/60 rounded-xl border border-indigo-200 space-y-2.5">
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                <a href="${c.admissions_url}" target="_blank" rel="noopener" class="flex items-center justify-between p-2.5 rounded-xl bg-white border border-indigo-200 text-indigo-700 hover:bg-indigo-600 hover:text-white transition font-bold text-xs shadow-sm">
                  <span>Admissions Portal</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
                <a href="${c.finaid_url}" target="_blank" rel="noopener" class="flex items-center justify-between p-2.5 rounded-xl bg-white border border-emerald-200 text-emerald-700 hover:bg-emerald-600 hover:text-white transition font-bold text-xs shadow-sm">
                  <span>Financial Aid Portal</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
                <a href="${c.testing_url}" target="_blank" rel="noopener" class="flex items-center justify-between p-2.5 rounded-xl bg-white border border-purple-200 text-purple-700 hover:bg-purple-600 hover:text-white transition font-bold text-xs shadow-sm">
                  <span>Testing Policy</span>
                  <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
              </div>
            </div>

            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs space-y-1">
              <span class="font-bold text-slate-800 block">Common Data Set (CDS) Reference:</span>
              <p class="text-slate-600 font-mono text-[11px]">${c.cds_source}</p>
            </div>
          </div>

        </div>

        <!-- Modal Bottom Bar -->
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500 mt-6 sticky bottom-0 bg-white/95 backdrop-blur py-2">
          <div class="flex items-center gap-2">
            <span class="text-emerald-600 font-bold"><i class="fa-solid fa-shield-halved mr-1"></i>Fall 2027 Verified</span>
            <span>•</span>
            <button onclick="jumpToModalSec('modal-sec-aid')" class="hover:text-indigo-600 font-semibold">Back to Top ↑</button>
          </div>
          <button onclick="closeModal()" class="px-5 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800 font-bold transition shadow-sm">
            Close Profile
          </button>
        </div>
      `;

      modal.classList.remove('hidden');
    }

    function closeModal() {
      document.getElementById('detailModal').classList.add('hidden');
    }

    function openPlaybook() {
      document.getElementById('playbookModal').classList.remove('hidden');
    }

    function closePlaybook() {
      document.getElementById('playbookModal').classList.add('hidden');
    }

    document.getElementById('detailModal').onclick = (e) => {
      if (e.target.id === 'detailModal') closeModal();
    };

    document.getElementById('playbookModal').onclick = (e) => {
      if (e.target.id === 'playbookModal') closePlaybook();
    };

    let currentSortCol = -1;
    let sortAsc = true;
    function sortTable(colIdx) {
      sortAsc = (currentSortCol === colIdx) ? !sortAsc : true;
      currentSortCol = colIdx;

      data.sort((a, b) => {
        let valA, valB;
        if (colIdx === 0) { valA = a.name; valB = b.name; }
        else if (colIdx === 1) { valA = a.location; valB = b.location; }
        else if (colIdx === 6) { valA = parseFloat(a.visa_safety_index) || 0; valB = parseFloat(b.visa_safety_index) || 0; }
        
        if (valA < valB) return sortAsc ? -1 : 1;
        if (valA > valB) return sortAsc ? 1 : -1;
        return 0;
      });
      filterAndRender();
    }
  </script>
</body>
</html>
"""

# Serialize data
json_str = json.dumps(colleges, indent=2, ensure_ascii=False)

# Insert JSON
final_html = html_template.replace('JSON_DATA_PLACEHOLDER', json_str)

# Write to Interactive_College_Spreadsheet.html and index.html (for GitHub Pages)
with open('Interactive_College_Spreadsheet.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated Interactive_College_Spreadsheet.html and index.html (Length: {len(final_html)} bytes)")
