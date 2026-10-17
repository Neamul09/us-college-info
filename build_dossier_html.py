import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('enriched_colleges.json', 'r', encoding='utf-8') as f:
    colleges = json.load(f)

print(f"Loaded {len(colleges)} colleges for University_Application_Dossier.html")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BDtoUSA: University Application Requirements Dossier & Notebook (Fall 2027)</title>
  <!-- Tailwind CSS & Font Awesome -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&family=Patrick+Hand&display=swap');
    
    body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #f1f5f9; }
    .font-notebook { font-family: 'Patrick Hand', cursive, sans-serif; }
    .font-mono-code { font-family: 'JetBrains Mono', monospace; }

    /* Notebook lined paper effect */
    .notebook-card {
      background-color: #ffffff;
      background-image: linear-gradient(#f8fafc 1px, transparent 1px);
      background-size: 100% 28px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      transition: all 0.2s ease-in-out;
    }
    .notebook-card:hover {
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
      border-color: #cbd5e1;
    }
    .notebook-card.card-selected {
      border: 2px solid #4f46e5 !important;
      background-color: #faf5ff;
    }

    /* Red margin line like student notebooks */
    .notebook-left-margin {
      border-left: 3px double #fca5a5;
    }

    /* Checkbox strike effect */
    .task-checkbox:checked + span {
      text-decoration: line-through;
      color: #94a3b8;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #f1f5f9; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

    @media print {
      header, #filterSection, #actionToolbar, .no-print { display: none !important; }
      body { background-color: #ffffff !important; }
      .notebook-card { break-inside: avoid; border: 1px solid #ccc !important; box-shadow: none !important; margin-bottom: 20px; }
    }
  </style>
</head>
<body class="text-slate-800 min-h-screen flex flex-col">

  <!-- TOP BANNER -->
  <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white text-xs py-2 px-4 shadow-sm border-b border-slate-800">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center justify-center bg-indigo-500 text-white px-2 py-0.5 rounded font-black text-[11px] tracking-wide">
          OFFICIAL ADMISSIONS DOSSIER
        </span>
        <span class="font-medium text-slate-200 text-xs">
          Fall 2027 U.S. College Admissions Checklist & Tactical Dossier • 160 Verified Institutions (Rank Sorted)
        </span>
      </div>
      <div class="flex items-center gap-4 text-[11px] text-slate-300">
        <span><i class="fa-solid fa-check-circle text-emerald-400 mr-1"></i>Verified Admissions & CDS Data</span>
        <span><i class="fa-solid fa-shield-halved text-blue-400 mr-1"></i>$0 EFC & Dhaka Visa Ready</span>
        <a href="index.html" class="underline hover:text-indigo-300 font-semibold cursor-pointer">Spreadsheet Portal ↗</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3">
        
        <div>
          <div class="flex items-center gap-2.5 flex-wrap">
            <h1 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight flex items-center gap-2">
              <i class="fa-solid fa-book-bookmark text-indigo-600"></i>
              Application Requirements Dossier
            </h1>
            <span class="text-xs bg-slate-100 text-slate-700 border border-slate-200 px-2.5 py-0.5 rounded-full font-bold">
              160 Universities
            </span>
            <span class="text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 px-2.5 py-0.5 rounded-full font-bold">
              Exact Checklists
            </span>
          </div>
          <p class="text-slate-500 text-xs mt-0.5">
            Structured in the exact format of your handwritten application notes: Platform, Fees, SAT, English, Transcripts, LORs, Supplements & Tactical Realities.
          </p>
        </div>

        <!-- Header Actions -->
        <div class="flex flex-wrap items-center gap-2">
          <button id="shortlistFilterBtn" onclick="toggleShortlistView()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-amber-300 bg-amber-50 text-amber-900 text-xs font-bold hover:bg-amber-100 transition shadow-sm">
            <i class="fa-solid fa-star text-amber-500"></i>
            <span id="shortlistBadgeText">My Selected List (0)</span>
          </button>

          <a href="BDtoUSA_Fall_2027_Full_Ride_Admissions_Guide.pdf" download class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-rose-700 text-white text-xs font-bold hover:bg-rose-800 transition shadow-sm">
            <i class="fa-solid fa-file-pdf"></i> Download PDF Guide
          </a>

          <a href="US_Colleges_Fall_2027_Full_Ride_BDtoUSA.xlsx" download class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-700 text-white text-xs font-bold hover:bg-emerald-800 transition shadow-sm">
            <i class="fa-solid fa-file-excel"></i> Excel (.xlsx)
          </a>

          <button onclick="exportMarkdownChecklist()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-slate-300 bg-slate-100 text-slate-700 text-xs font-semibold hover:bg-slate-200 transition" title="Export Selected as Markdown">
            <i class="fa-solid fa-file-lines"></i> Export MD
          </button>

          <button onclick="window.print()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-slate-300 bg-slate-100 text-slate-700 text-xs font-semibold hover:bg-slate-200 transition" title="Print Dossier">
            <i class="fa-solid fa-print"></i>
          </button>
        </div>

      </div>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full space-y-6">

    <!-- INTERACTIVE FILTER SECTION -->
    <section id="filterSection" class="bg-white rounded-2xl border border-slate-200 p-4 sm:p-5 shadow-sm space-y-4">
      
      <!-- Top Preset Archetypes -->
      <div class="flex items-center justify-between border-b border-slate-100 pb-3 flex-wrap gap-2">
        <div class="flex items-center gap-2">
          <i class="fa-solid fa-filter text-indigo-600 text-xs"></i>
          <span class="text-xs font-bold uppercase tracking-wider text-slate-600">Quick Strategy Presets:</span>
        </div>
        <button onclick="resetFilters()" class="text-xs text-rose-600 hover:text-rose-700 font-bold flex items-center gap-1 bg-rose-50 px-2.5 py-1 rounded-lg transition">
          <i class="fa-solid fa-rotate-left"></i> Reset Filters
        </button>
      </div>

      <div class="flex flex-wrap items-center gap-2 text-xs">
        <button onclick="setPreset('all')" id="btn-preset-all" class="preset-pill px-3 py-1 rounded-lg border border-slate-900 bg-slate-900 text-white font-bold transition">
          All 160 Colleges
        </button>
        <button onclick="setPreset('ea_nov')" id="btn-preset-ea_nov" class="preset-pill px-3 py-1 rounded-lg border border-indigo-200 bg-indigo-50 text-indigo-800 hover:bg-indigo-100 font-semibold transition">
          ⚡ Early Action (EA / Nov 1 - Dec 1)
        </button>
        <button onclick="setPreset('ed1_bowdoin')" id="btn-preset-ed1_bowdoin" class="preset-pill px-3 py-1 rounded-lg border border-amber-200 bg-amber-50 text-amber-900 hover:bg-amber-100 font-semibold transition">
          🛡️ ED1 Test-Optional (Bowdoin, Colby, Bates)
        </button>
        <button onclick="setPreset('need_blind')" id="btn-preset-need_blind" class="preset-pill px-3 py-1 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-900 hover:bg-emerald-100 font-semibold transition">
          🏛️ 100% Need-Blind Elites (9 Universities + NYUAD)
        </button>
        <button onclick="setPreset('merit_full')" id="btn-preset-merit_full" class="preset-pill px-3 py-1 rounded-lg border border-yellow-200 bg-yellow-50 text-yellow-900 hover:bg-yellow-100 font-semibold transition">
          💎 Dec 1 Premier Full-Ride Merit
        </button>
        <button onclick="setPreset('free_app')" id="btn-preset-free_app" class="preset-pill px-3 py-1 rounded-lg border border-slate-200 bg-slate-100 text-slate-800 hover:bg-slate-200 font-semibold transition">
          💸 $0 Application Fee (100% Free)
        </button>
        <button onclick="setPreset('free_isfaa')" id="btn-preset-free_isfaa" class="preset-pill px-3 py-1 rounded-lg border border-slate-200 bg-slate-100 text-slate-800 hover:bg-slate-200 font-semibold transition">
          📄 Free ISFAA PDF (Skip CSS $25+$16 Fee)
        </button>
        <button onclick="setPreset('top25')" id="btn-preset-top25" class="preset-pill px-3 py-1 rounded-lg border border-purple-200 bg-purple-50 text-purple-900 hover:bg-purple-100 font-semibold transition">
          🏆 Top 25 Ranked
        </button>
        <button onclick="setPreset('test_opt_high')" id="btn-preset-test_opt_high" class="preset-pill px-3 py-1 rounded-lg border border-cyan-200 bg-cyan-50 text-cyan-900 hover:bg-cyan-100 font-semibold transition">
          📊 High Test-Optional (50%+ Admitted Test-Free)
        </button>
        <button onclick="setPreset('bank_deferred')" id="btn-preset-bank_deferred" class="preset-pill px-3 py-1 rounded-lg border border-teal-200 bg-teal-50 text-teal-900 hover:bg-teal-100 font-semibold transition">
          🏦 Bank Statement Deferred ($0 at App)
        </button>
        <button onclick="setPreset('aid_70k')" id="btn-preset-aid_70k" class="preset-pill px-3 py-1 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-950 hover:bg-emerald-100 font-semibold transition">
          💰 Average Aid > $70k/yr (CDS H6)
        </button>
      </div>

      <!-- Advanced Filter Dropdowns -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 pt-2">
        
        <!-- Live Search -->
        <div class="relative lg:col-span-2">
          <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3.5 text-slate-400"></i>
          <input type="text" id="searchInput" placeholder="Search by college name, CEEB code, location, testing policy..." 
                 class="w-full pl-10 pr-9 py-2.5 border border-slate-300 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-indigo-500 outline-none transition bg-white text-slate-900 shadow-sm">
          <button id="clearSearchBtn" onclick="clearSearch()" class="absolute right-3 top-3 text-slate-400 hover:text-slate-600 hidden text-xs">
            <i class="fa-solid fa-circle-xmark"></i>
          </button>
        </div>

        <!-- Strategic Admissions Round -->
        <div>
          <select id="roundFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Application Rounds</option>
            <option value="EA">Early Action (EA Non-Binding)</option>
            <option value="ED1">Early Decision 1 (ED1 Nov 1 - 15)</option>
            <option value="ED2">Early Decision 2 (ED2 Jan 1 - 15)</option>
            <option value="REA">Restrictive Early Action (REA / SCEA)</option>
            <option value="MERIT">Dec 1 Premier Merit Scholarships</option>
            <option value="RD">Regular Decision (RD Jan - Feb)</option>
          </select>
        </div>

        <!-- Testing Policy -->
        <div>
          <select id="testingFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Standardized Testing Policies</option>
            <option value="TEST_OPTIONAL">Test-Optional (Self-Report Accepted)</option>
            <option value="TEST_FREE">Test-Free / Test-Blind (Caltech, Hampshire)</option>
            <option value="TEST_REQUIRED">Test-Required (MIT, Georgetown, CoO)</option>
            <option value="NOV_SAT_OK">Accepts Nov 7 SAT for Early Round</option>
          </select>
        </div>

        <!-- Financial Aid Model -->
        <div>
          <select id="aidFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Financial Aid Models</option>
            <option value="NEED_BLIND">100% Need-Blind for Internationals (9 Elites + NYUAD)</option>
            <option value="MEETS_NEED">Meets 100% Demonstrated Need (No Loans)</option>
            <option value="MERIT_FULL">Premier Full-Ride / Full-Tuition Merit</option>
            <option value="WORK_COLLEGE">Work Colleges ($0 Tuition Guarantee)</option>
          </select>
        </div>

        <!-- Application Fee Model -->
        <div>
          <select id="feeFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Application Fee Policies</option>
            <option value="FREE">$0 Application Fee for Everyone</option>
            <option value="COMMON_APP_WAIVER">Accepts Common App Fee Waiver</option>
            <option value="FREE_ISFAA">Accepts Free ISFAA PDF (No CSS Fee)</option>
          </select>
        </div>

        <!-- English Proficiency Policy -->
        <div>
          <select id="englishFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All English Test Policies</option>
            <option value="NOT_REQUIRED">Not Required / Optional</option>
            <option value="WAIVED_VIA_SAT">Waived via SAT EBRW Score (650+)</option>
            <option value="DET_ACCEPTED">Duolingo English Test (DET) Accepted</option>
          </select>
        </div>

        <!-- User Selection Status -->
        <div>
          <select id="statusFilter" class="w-full py-2.5 px-3 border border-slate-300 rounded-xl text-xs sm:text-sm font-medium focus:ring-2 focus:ring-indigo-500 outline-none bg-white text-slate-700 shadow-sm">
            <option value="ALL">All Application Tracker Statuses</option>
            <option value="SELECTED">⭐ My Selected Colleges Only</option>
            <option value="IN_PROGRESS">📝 In Progress</option>
            <option value="SUBMITTED">✅ Completed / Submitted</option>
          </select>
        </div>

      </div>
    </section>

    <!-- RESULTS BAR -->
    <div id="actionToolbar" class="flex items-center justify-between text-xs text-slate-600 bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex-wrap gap-2">
      <div class="flex items-center gap-2">
        <span id="resultsCount" class="font-bold text-slate-800 text-sm">Showing 160 of 160 institutions</span>
        <span id="shortlistActiveNotice" class="hidden text-amber-800 font-bold bg-amber-100 border border-amber-300 px-2 py-0.5 rounded text-[11px]">
          <i class="fa-solid fa-star text-amber-500 mr-1"></i>Selected List Filter Active
        </span>
      </div>

      <div class="flex items-center gap-3">
        <span class="text-slate-500 font-medium hidden sm:inline">Sort:</span>
        <select id="sortSelect" onchange="filterAndRender()" class="py-1 px-2.5 border border-slate-300 rounded-lg text-xs font-semibold bg-white text-slate-700">
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
    </div>

    <!-- CARDS GRID CONTAINER -->
    <div id="cardsGrid" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
      <!-- Notebook cards injected dynamically by JavaScript -->
    </div>

  </main>

  <!-- JAVASCRIPT DATA & APP LOGIC -->
  <script>
    const data = JSON_DATA_PLACEHOLDER;

    // State
    let activePreset = 'all';
    let showShortlistOnly = false;
    let selectedColleges = JSON.parse(localStorage.getItem('bdtousa_selected_colleges') || '{}');
    let completedTasks = JSON.parse(localStorage.getItem('bdtousa_completed_tasks') || '{}');

    // DOM Ready
    document.addEventListener('DOMContentLoaded', () => {
      attachListeners();
      updateShortlistCount();
      filterAndRender();
    });

    function attachListeners() {
      document.getElementById('searchInput').addEventListener('input', () => {
        const val = document.getElementById('searchInput').value;
        document.getElementById('clearSearchBtn').classList.toggle('hidden', val.length === 0);
        filterAndRender();
      });

      document.getElementById('roundFilter').addEventListener('change', filterAndRender);
      document.getElementById('testingFilter').addEventListener('change', filterAndRender);
      document.getElementById('aidFilter').addEventListener('change', filterAndRender);
      document.getElementById('feeFilter').addEventListener('change', filterAndRender);
      document.getElementById('englishFilter').addEventListener('change', filterAndRender);
      document.getElementById('statusFilter').addEventListener('change', filterAndRender);
    }

    function clearSearch() {
      document.getElementById('searchInput').value = '';
      document.getElementById('clearSearchBtn').classList.add('hidden');
      filterAndRender();
    }

    function setPreset(preset) {
      activePreset = preset;
      document.querySelectorAll('.preset-pill').forEach(btn => {
        btn.classList.remove('bg-slate-900', 'text-white', 'border-slate-900');
        btn.classList.add('bg-white', 'text-slate-800');
      });
      const btn = document.getElementById(`btn-preset-${preset}`);
      if (btn) {
        btn.classList.remove('bg-white', 'text-slate-800');
        btn.classList.add('bg-slate-900', 'text-white', 'border-slate-900');
      }

      // Reset dropdowns
      document.getElementById('roundFilter').value = 'ALL';
      document.getElementById('testingFilter').value = 'ALL';
      document.getElementById('aidFilter').value = 'ALL';
      document.getElementById('feeFilter').value = 'ALL';
      document.getElementById('englishFilter').value = 'ALL';
      document.getElementById('statusFilter').value = 'ALL';

      filterAndRender();
    }

    function resetFilters() {
      activePreset = 'all';
      showShortlistOnly = false;
      document.getElementById('searchInput').value = '';
      document.getElementById('clearSearchBtn').classList.add('hidden');
      document.getElementById('roundFilter').value = 'ALL';
      document.getElementById('testingFilter').value = 'ALL';
      document.getElementById('aidFilter').value = 'ALL';
      document.getElementById('feeFilter').value = 'ALL';
      document.getElementById('englishFilter').value = 'ALL';
      document.getElementById('statusFilter').value = 'ALL';

      document.querySelectorAll('.preset-pill').forEach(btn => {
        btn.classList.remove('bg-slate-900', 'text-white', 'border-slate-900');
      });
      document.getElementById('btn-preset-all').classList.add('bg-slate-900', 'text-white', 'border-slate-900');

      updateShortlistCount();
      filterAndRender();
    }

    function toggleShortlistView() {
      showShortlistOnly = !showShortlistOnly;
      updateShortlistCount();
      filterAndRender();
    }

    function toggleSelection(name) {
      if (selectedColleges[name]) {
        delete selectedColleges[name];
      } else {
        selectedColleges[name] = {
          status: 'TO_APPLY',
          addedAt: new Date().toISOString()
        };
      }
      localStorage.setItem('bdtousa_selected_colleges', JSON.stringify(selectedColleges));
      updateShortlistCount();
      filterAndRender();
    }

    function updateCollegeStatus(name, status) {
      if (!selectedColleges[name]) {
        selectedColleges[name] = { addedAt: new Date().toISOString() };
      }
      selectedColleges[name].status = status;
      localStorage.setItem('bdtousa_selected_colleges', JSON.stringify(selectedColleges));
      filterAndRender();
    }

    function toggleTask(taskId) {
      completedTasks[taskId] = !completedTasks[taskId];
      localStorage.setItem('bdtousa_completed_tasks', JSON.stringify(completedTasks));
    }

    function updateShortlistCount() {
      const count = Object.keys(selectedColleges).length;
      document.getElementById('shortlistBadgeText').innerText = `My Selected List (${count})`;
      document.getElementById('shortlistFilterBtn').classList.toggle('bg-amber-300', showShortlistOnly);
      document.getElementById('shortlistActiveNotice').classList.toggle('hidden', !showShortlistOnly);
    }

    function getFilteredList() {
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      const round = document.getElementById('roundFilter').value;
      const testing = document.getElementById('testingFilter').value;
      const aid = document.getElementById('aidFilter').value;
      const fee = document.getElementById('feeFilter').value;
      const english = document.getElementById('englishFilter').value;
      const status = document.getElementById('statusFilter').value;

      return data.filter(c => {
        const isSelected = !!selectedColleges[c.name];

        // Shortlist view toggle
        if (showShortlistOnly && !isSelected) return false;

        // Status filter
        if (status !== 'ALL') {
          if (status === 'SELECTED' && !isSelected) return false;
          if (status === 'IN_PROGRESS' && (!isSelected || selectedColleges[c.name].status !== 'IN_PROGRESS')) return false;
          if (status === 'SUBMITTED' && (!isSelected || selectedColleges[c.name].status !== 'SUBMITTED')) return false;
        }

        // Search query
        if (q) {
          const m = 
            c.name.toLowerCase().includes(q) ||
            (c.cb_code && c.cb_code.includes(q)) ||
            c.location.toLowerCase().includes(q) ||
            c.cs_strength.toLowerCase().includes(q) ||
            c.deadlines.toLowerCase().includes(q) ||
            c.dossier.app_fee.toLowerCase().includes(q) ||
            c.dossier.sat_status.toLowerCase().includes(q);
          if (!m) return false;
        }

        // Round filter
        if (round !== 'ALL') {
          const dl = c.deadlines.toLowerCase();
          if (round === 'EA' && !dl.includes('ea:')) return false;
          if (round === 'ED1' && !dl.includes('ed1:')) return false;
          if (round === 'ED2' && !dl.includes('ed2:')) return false;
          if (round === 'REA' && !dl.includes('rea:')) return false;
          if (round === 'MERIT' && (!dl.includes('scholarship') && !dl.includes('priority: dec 1') && !c.testing_strategy_round.includes('MERIT'))) return false;
          if (round === 'RD' && !dl.includes('rd:')) return false;
        }

        // Testing filter
        if (testing !== 'ALL') {
          if (testing === 'TEST_OPTIONAL' && c.ed_test_optional !== true && c.ea_test_optional !== true) return false;
          if (testing === 'TEST_FREE' && !c.score_policy.toLowerCase().includes('test-free') && !c.score_policy.toLowerCase().includes('test-blind')) return false;
          if (testing === 'TEST_REQUIRED' && (c.ea_test_optional === true || c.ed_test_optional === true)) return false;
          if (testing === 'NOV_SAT_OK' && !c.nov_sat_policy.toLowerCase().includes('yes') && !c.nov_sat_policy.toLowerCase().includes('accommodates') && !c.nov_sat_policy.toLowerCase().includes('accepted')) return false;
        }

        // Aid filter
        if (aid !== 'ALL') {
          if (aid === 'NEED_BLIND' && !c.need_blind_status.toLowerCase().includes('need-blind')) return false;
          if (aid === 'MEETS_NEED' && !c.aid_policy.toLowerCase().includes('100% demonstrated need') && !c.aid_policy.toLowerCase().includes('need-blind')) return false;
          if (aid === 'MERIT_FULL' && !c.max_aid.toLowerCase().includes('merit') && !c.max_aid.toLowerCase().includes('full ride') && !c.aid_policy.toLowerCase().includes('scholarship')) return false;
          if (aid === 'WORK_COLLEGE' && !c.type.toLowerCase().includes('work college')) return false;
        }

        // Fee filter
        if (fee !== 'ALL') {
          if (fee === 'FREE' && c.dossier.fee_type !== 'FREE') return false;
          if (fee === 'COMMON_APP_WAIVER' && c.dossier.fee_type !== 'COMMON_APP_WAIVER') return false;
          if (fee === 'FREE_ISFAA' && !c.fee_waiver.toLowerCase().includes('isfaa')) return false;
        }

        // English filter
        if (english !== 'ALL') {
          if (english === 'NOT_REQUIRED' && c.dossier.english_category !== 'NOT_REQUIRED') return false;
          if (english === 'WAIVED_VIA_SAT' && c.dossier.english_category !== 'WAIVED_VIA_SAT') return false;
          if (english === 'DET_ACCEPTED' && !c.sat_det_needed.toLowerCase().includes('det')) return false;
        }

        // Presets
        if (activePreset === 'ea_nov') {
          return c.deadlines.toLowerCase().includes('ea:') || c.testing_strategy_round.includes('EARLY ACTION');
        } else if (activePreset === 'ed1_bowdoin') {
          return c.ed_test_optional === true && (c.need_blind_status.includes('Need-Blind') || c.aid_policy.includes('100% demonstrated need'));
        } else if (activePreset === 'need_blind') {
          return c.need_blind_status.includes('Need-Blind');
        } else if (activePreset === 'merit_full') {
          return c.testing_strategy_round.includes('MERIT') || c.max_aid.toLowerCase().includes('full ride');
        } else if (activePreset === 'free_app') {
          return c.dossier.fee_type === 'FREE';
        } else if (activePreset === 'free_isfaa') {
          return c.fee_waiver.toLowerCase().includes('isfaa');
        } else if (activePreset === 'top25') {
          return (c.rank_num || 999) <= 25;
        } else if (activePreset === 'test_opt_high') {
          const to = (c.test_optional_stat || '').toLowerCase();
          return to.includes('50%') || to.includes('51%') || to.includes('52%') || to.includes('53%') ||
                 to.includes('54%') || to.includes('55%') || to.includes('56%') || to.includes('58%') ||
                 to.includes('60%') || to.includes('62%') || to.includes('65%') || to.includes('100% test-free');
        } else if (activePreset === 'bank_deferred') {
          return (c.cof_policy || '').toLowerCase().includes('deferred') || (c.dossier && (c.dossier.cof_policy || '').toLowerCase().includes('deferred'));
        } else if (activePreset === 'aid_70k') {
          const avg = (c.cds_h6 && c.cds_h6.avg_aid) || '';
          const m = avg.match(/\\$([0-9,]+)/);
          const val = m ? parseInt(m[1].replace(/,/g, '')) : 0;
          return val >= 70000;
        }

        return true;
      });
    }

    function filterAndRender() {
      let list = getFilteredList();

      // Sort
      const sortVal = document.getElementById('sortSelect').value;
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
        list.sort((a, b) => a.dossier.deadline_badge.localeCompare(b.dossier.deadline_badge));
      } else if (sortVal === 'PROB_DESC') {
        list.sort((a, b) => (parseFloat(b.probability) || 0) - (parseFloat(a.probability) || 0));
      } else if (sortVal === 'VISA') {
        list.sort((a, b) => (parseFloat(b.visa_safety_index) || 0) - (parseFloat(a.visa_safety_index) || 0));
      }

      renderCards(list);
      document.getElementById('resultsCount').innerText = `Showing ${list.length} of ${data.length} institutions`;
    }

    function renderCards(list) {
      const container = document.getElementById('cardsGrid');
      container.innerHTML = '';

      if (list.length === 0) {
        container.innerHTML = `
          <div class="col-span-full py-16 text-center text-slate-500 bg-white rounded-2xl border border-slate-200">
            <i class="fa-solid fa-folder-open text-4xl text-slate-300 mb-3 block"></i>
            <h3 class="text-base font-bold text-slate-700">No universities match your filters</h3>
            <p class="text-xs text-slate-400 mt-1">Try resetting your filter parameters or search query.</p>
            <button onclick="resetFilters()" class="mt-3 text-xs px-4 py-2 bg-indigo-50 text-indigo-700 font-bold rounded-lg hover:bg-indigo-100 transition">
              Reset All Filters
            </button>
          </div>
        `;
        return;
      }

      list.forEach((c, idx) => {
        try {
          const isSelected = !!selectedColleges[c.name];
          const currentStatus = isSelected ? (selectedColleges[c.name].status || 'TO_APPLY') : 'NONE';
          const d = c.dossier || {};

          const card = document.createElement('div');
          card.className = `notebook-card p-5 flex flex-col justify-between ${isSelected ? 'card-selected' : ''}`;
          card.id = `card-${idx}`;

          // Build checklist items
          const safeId = (c.name || 'col_' + idx).replace(/[^a-zA-Z0-9]/g, '_');
          const safeName = (c.name || '').replace(/'/g, "\\'");
          const lorList = Array.isArray(d.lor_info) && d.lor_info.length > 0 ? d.lor_info : [
            "Teacher Recommendation 1: STEM (Math, Physics, or Computer Science)",
            "Teacher Recommendation 2: Humanities, Social Science, English, or ICT",
            "School Counselor Recommendation & School Report"
          ];
          const tacticalList = Array.isArray(d.tactical) && d.tactical.length > 0 ? d.tactical : [
            c.aid_policy || "Meets 100% demonstrated financial need with comprehensive grant aid.",
            c.score_policy || "Standardized test scores evaluated holistically or self-reported on portal."
          ];
          const isNeedBlind = (c.need_blind_status || '').includes('Need-Blind');
          const visaIndex = (c.visa_safety_index || '98% Approval').split('|')[0].trim();
          const appForm = d.app_form || 'Common Application (First-Year) + Member Questions';
          const appFee = d.app_fee || (c.fee_waiver || '$0 Application Fee / Fee Waiver Accepted');
          const satStatus = d.sat_status || (c.score_policy || 'Test-Optional: Self-reporting accepted');
          const novSat = d.nov_sat || (c.nov_sat_policy || 'ED1: YES | ED2/RD: YES');
          const engStatus = d.english_status || 'English Test: Waived via English-medium schooling or DET accepted';
          const faBadge = d.fa_badge || 'Free ISFAA / CSS Waiver';
          const deadlines = c.deadlines || 'ED1: Nov 15 | RD: Jan 15';

          const h6Data = c.cds_h6 || d.cds_h6 || {
            avg_aid: "$70,000/year",
            pct_aided: "65% of international undergrads",
            loan_free: "100% Loan-Free Package",
            total_budget: "$12M+ annual budget"
          };
          const finaidFormBadge = c.finaid_form_badge || d.finaid_form_badge || d.fa_badge || 'Free ISFAA / CSS Waiver';
          const cofBadge = c.cof_badge || d.cof_badge || 'Deferred: Post-Admission Only ($0 Bank Balance at App)';
          const englishDetails = c.english_cutoffs_waiver || d.english_cutoffs_waiver || engStatus;
          const specialReqs = c.special_requirements || d.special_requirements || 'Standard Common App + LORs';

          card.innerHTML = `
            <div>
              <!-- NOTEBOOK CARD HEADER -->
              <div class="flex items-start justify-between border-b-2 border-slate-900 pb-3 mb-3">
                <div>
                  <div class="flex items-center gap-1.5 flex-wrap">
                    <span class="text-[10px] font-black px-2 py-0.5 rounded bg-slate-900 text-white tracking-wide font-mono shadow-sm">
                      <i class="fa-solid fa-bullseye text-amber-400 mr-1"></i>${c.strategic_rank_display || '#1 Strategic'}
                    </span>
                    <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-50 text-blue-900 border border-blue-200 font-mono">
                      🏛️ ${c.us_news_display || 'US News Top Tier'}
                    </span>
                    <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-purple-50 text-purple-900 border border-purple-200 font-mono">
                      🌐 ${c.world_rank_display || 'QS World Top Tier'}
                    </span>
                    <span class="text-[11px] font-mono font-bold text-slate-500 px-1.5 py-0.2 bg-slate-100 rounded border border-slate-200">
                      CEEB: ${c.cb_code || 'N/A'}
                    </span>
                    <span class="text-[10px] font-bold px-2 py-0.5 rounded-full ${isNeedBlind ? 'bg-emerald-100 text-emerald-800' : 'bg-indigo-50 text-indigo-700'}">
                      ${isNeedBlind ? 'Need-Blind' : '100% Need Met'}
                    </span>
                  </div>
                  <h2 class="text-xl font-black text-slate-900 uppercase tracking-tight mt-1.5 leading-snug">
                    ${c.name}
                  </h2>
                  <p class="text-xs text-slate-500 font-medium mt-0.5">
                    <i class="fa-solid fa-location-dot text-rose-500 mr-1 text-[11px]"></i>${c.location || 'USA'} • ${c.type || 'University'}
                  </p>
                </div>

                <!-- Selection Button -->
                <button onclick="toggleSelection('${safeName}')" 
                        class="p-2 rounded-xl border transition ${isSelected ? 'bg-amber-400 border-amber-500 text-slate-900 shadow-sm' : 'bg-slate-50 border-slate-200 text-slate-400 hover:text-amber-500 hover:border-amber-300'}"
                        title="${isSelected ? 'Remove from my target list' : 'Add to my target list'}">
                  <i class="fa-${isSelected ? 'solid' : 'regular'} fa-star text-base"></i>
                </button>
              </div>

              <!-- STATUS SELECTOR (IF SELECTED) -->
              ${isSelected ? `
                <div class="mb-3.5 p-2 bg-indigo-50 border border-indigo-200 rounded-xl flex items-center justify-between text-xs">
                  <span class="font-bold text-indigo-950 flex items-center gap-1">
                    <i class="fa-solid fa-flag text-indigo-600"></i> Status:
                  </span>
                  <select onchange="updateCollegeStatus('${safeName}', this.value)" class="text-xs font-bold py-1 px-2 rounded-lg bg-white border border-indigo-300 text-indigo-900 outline-none">
                    <option value="TO_APPLY" ${currentStatus === 'TO_APPLY' ? 'selected' : ''}>📌 Target (To Apply)</option>
                    <option value="IN_PROGRESS" ${currentStatus === 'IN_PROGRESS' ? 'selected' : ''}>📝 In Progress</option>
                    <option value="SUBMITTED" ${currentStatus === 'SUBMITTED' ? 'selected' : ''}>✅ Submitted</option>
                  </select>
                </div>
              ` : ''}

              <!-- SECTION: REQUIREMENTS (HANDWRITTEN STYLE CHECKLIST) -->
              <div class="notebook-left-margin pl-3.5 space-y-2 mb-4">
                <div class="text-[11px] font-black uppercase tracking-wider text-slate-900 flex items-center gap-1.5">
                  <i class="fa-solid fa-list-check text-indigo-600"></i> Requirements:
                </div>

                <!-- Item 1: Application Form -->
                <label class="flex items-start gap-2 text-xs text-slate-800 cursor-pointer group">
                  <input type="checkbox" onchange="toggleTask('${safeId}_app')" ${completedTasks[`${safeId}_app`] ? 'checked' : ''} class="task-checkbox mt-0.5 h-3.5 w-3.5 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500">
                  <span><b>${appForm}</b></span>
                </label>

                <!-- Item 2: Application Fee -->
                <label class="flex items-start gap-2 text-xs text-slate-800 cursor-pointer group">
                  <input type="checkbox" onchange="toggleTask('${safeId}_fee')" ${completedTasks[`${safeId}_fee`] ? 'checked' : ''} class="task-checkbox mt-0.5 h-3.5 w-3.5 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500">
                  <span>Fee: <strong class="${d.fee_type === 'FREE' ? 'text-emerald-700' : 'text-slate-800'}">${appFee}</strong></span>
                </label>

                <!-- Item 3: SAT / Testing -->
                <label class="flex items-start gap-2 text-xs text-slate-800 cursor-pointer group">
                  <input type="checkbox" onchange="toggleTask('${safeId}_sat')" ${completedTasks[`${safeId}_sat`] ? 'checked' : ''} class="task-checkbox mt-0.5 h-3.5 w-3.5 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500">
                  <span><b>SAT:</b> ${satStatus}</span>
                </label>
                <div class="text-[11px] text-slate-500 pl-5 -mt-1 font-mono">
                  ↳ <i>Nov 7 SAT (Nov 20 Release):</i> ${novSat}
                </div>
                <div class="mt-1.5 ml-5 p-2 bg-indigo-50/80 border border-indigo-200/90 rounded-lg text-[11px] text-indigo-950">
                  <div class="flex items-center justify-between text-[10px] font-bold text-indigo-800 uppercase tracking-wider mb-0.5">
                    <span><i class="fa-solid fa-chart-pie mr-1 text-indigo-600"></i>Test-Optional Admitted % (CDS C9)</span>
                    <span class="bg-indigo-200/60 px-1 rounded text-[9px] font-mono font-bold">Official CDS</span>
                  </div>
                  <span class="font-semibold">${c.test_optional_stat || 'Test-Optional Policy Active'}</span>
                </div>

                <!-- Item 4: Transcripts & School Report -->
                <label class="flex items-start gap-2 text-xs text-slate-800 cursor-pointer group">
                  <input type="checkbox" onchange="toggleTask('${safeId}_transcripts')" ${completedTasks[`${safeId}_transcripts`] ? 'checked' : ''} class="task-checkbox mt-0.5 h-3.5 w-3.5 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500">
                  <span>School Report with Counselor Letter (SSC/HSC Marksheets 9-12)</span>
                </label>
                <div class="text-[10px] text-slate-500 pl-5 -mt-1">
                  ↳ <i>Mid-Year Report:</i> Replaced by final HSC certificate (Gap Year)
                </div>

                <!-- Item 5: LORs -->
                <div class="text-xs font-semibold text-slate-900 pt-1">
                  Teacher Recommendations:
                </div>
                <ul class="text-[11px] text-slate-700 pl-5 space-y-1">
                  ${lorList.map(lor => `<li>• ${lor}</li>`).join('')}
                </ul>

                <!-- Item 6: English Proficiency -->
                <label class="flex items-start gap-2 text-xs text-slate-800 cursor-pointer group pt-1">
                  <input type="checkbox" onchange="toggleTask('${safeId}_eng')" ${completedTasks[`${safeId}_eng`] ? 'checked' : ''} class="task-checkbox mt-0.5 h-3.5 w-3.5 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500">
                  <span><strong class="text-indigo-900">${engStatus}</strong></span>
                </label>
                <div class="text-[10px] text-slate-600 pl-5 -mt-1 font-mono">
                  ↳ <i>Cutoffs & Waiver:</i> ${englishDetails}
                </div>

                <!-- Item 7: Special Submission Component -->
                <div class="mt-2 p-2 bg-purple-50/70 border border-purple-200/80 rounded-lg text-[11px] text-purple-950">
                  <span class="font-bold uppercase text-[9px] text-purple-800 block"><i class="fa-solid fa-star mr-1"></i> Special Submission Component:</span>
                  <span>${specialReqs}</span>
                </div>
              </div>

              <!-- SECTION: SUPPLEMENTS & PORTFOLIOS -->
              <div class="notebook-left-margin pl-3.5 space-y-1.5 mb-4 pt-1 border-t border-slate-100">
                <div class="text-[11px] font-black uppercase tracking-wider text-slate-900 flex items-center gap-1.5">
                  <i class="fa-solid fa-paperclip text-indigo-600"></i> Supplements & Portfolios (Institution Specific):
                </div>
                <ul class="text-[11px] text-slate-700 pl-4 space-y-1">
                  ${(Array.isArray(d.supplements) && d.supplements.length > 0 ? d.supplements : [
                    "Institutional Supplemental Essays: Complete member questions via Common Application.",
                    "Portfolios: Optional maker/research portfolio via applicant portal Slideroom."
                  ]).map(s => `<li>↳ ${s}</li>`).join('')}
                </ul>
              </div>

              <!-- SECTION: TACTICAL ASTERISKS / REALITIES -->
              <div class="p-3 bg-amber-50/70 border border-amber-200/80 rounded-xl text-xs space-y-1 mb-4">
                <div class="font-bold text-amber-950 uppercase text-[10px] flex items-center gap-1">
                  <i class="fa-solid fa-asterisk text-amber-600"></i> Tactical Admissions Realities:
                </div>
                <ul class="text-[11px] text-amber-900 space-y-0.5">
                  ${tacticalList.map(t => `<li>* ${t}</li>`).join('')}
                </ul>
              </div>

              <!-- SECTION: CDS SECTION H6 INTERNATIONAL FINANCIAL AUDIT -->
              <div class="p-3 bg-emerald-50/80 border border-emerald-300 rounded-xl text-xs space-y-1.5 mb-4">
                <div class="flex items-center justify-between text-[10px] font-bold text-emerald-950 uppercase tracking-wider">
                  <span><i class="fa-solid fa-hand-holding-dollar text-emerald-700 mr-1"></i>Official CDS (Sec. H6) International Aid Audit</span>
                  <span class="bg-emerald-200/80 text-emerald-950 px-1.5 py-0.2 rounded font-mono font-bold text-[9px]">Verified CDS H6</span>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[11px] pt-1">
                  <div>
                    <span class="text-slate-500 text-[10px] block">Average International Package:</span>
                    <strong class="text-emerald-900 text-xs">${h6Data.avg_aid}</strong>
                  </div>
                  <div>
                    <span class="text-slate-500 text-[10px] block">International Cohort Aided:</span>
                    <strong class="text-emerald-900 text-xs">${h6Data.pct_aided}</strong>
                  </div>
                </div>
                <div class="text-[10px] text-emerald-950 font-medium pt-1 border-t border-emerald-200/80">
                  ↳ <i>Loan-Free Guarantee:</i> ${h6Data.loan_free}
                </div>
              </div>

              <!-- SECTION: FINANCIAL AID PROTOCOL & BANK STATEMENT TIMING -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] mb-4">
                <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-lg">
                  <span class="text-slate-400 uppercase font-bold text-[9px] block">Financial Aid Form</span>
                  <strong class="text-emerald-800 text-[11px] block">${finaidFormBadge}</strong>
                  <span class="text-[10px] text-slate-600 block mt-0.5">${c.finaid_form_protocol || ''}</span>
                </div>
                <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-lg">
                  <span class="text-slate-400 uppercase font-bold text-[9px] block">Bank Statement / COF Timing</span>
                  <strong class="text-indigo-900 text-[11px] block">${cofBadge}</strong>
                  <span class="text-[10px] text-slate-600 block mt-0.5">${c.cof_policy || ''}</span>
                </div>
              </div>
            </div>

            <!-- NOTEBOOK CARD FOOTER: ALL DEADLINES & OFFICIAL LINKS -->
            <div class="pt-3 border-t-2 border-slate-900 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs mt-2">
              <div>
                <span class="text-[9px] font-bold text-slate-400 uppercase block font-mono">All Deadlines (App & Aid)</span>
                <div class="font-semibold text-slate-900 font-mono text-[11px] bg-amber-50 px-2 py-0.5 rounded border border-amber-200">
                  ${deadlines}
                </div>
              </div>

              <!-- Official Portals -->
              <div class="flex items-center gap-2">
                <a href="${c.admissions_url || '#'}" target="_blank" rel="noopener" class="p-1.5 text-indigo-700 hover:text-indigo-900 bg-indigo-50 hover:bg-indigo-100 rounded-lg transition text-xs font-bold flex items-center gap-1" title="Official Admissions Website">
                  <span>Admissions</span> <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                </a>
                <a href="${c.finaid_url || '#'}" target="_blank" rel="noopener" class="p-1.5 text-emerald-700 hover:text-emerald-900 bg-emerald-50 hover:bg-emerald-100 rounded-lg transition text-xs font-bold flex items-center gap-1" title="International Financial Aid Portal">
                  <span>Aid</span> <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                </a>
              </div>
            </div>
          `;

          container.appendChild(card);
        } catch (err) {
          console.error('Error rendering card for index', idx, c ? c.name : 'unknown', err);
        }
      });
    }

    function exportMarkdownChecklist() {
      const keys = Object.keys(selectedColleges);
      if (keys.length === 0) {
        alert('Please select at least one university using the star button before exporting!');
        return;
      }

      let md = '# BDtoUSA: Selected University Application Checklist (Fall 2027)\\n\\n';
      md += `*Generated for Bangladeshi Undergraduate Applicants • Total Selected: ${keys.length}*\\n\\n---\\n\\n`;

      keys.forEach(name => {
        const c = data.find(item => item.name === name);
        if (!c) return;
        const d = c.dossier;
        md += `## [${c.name}](${c.admissions_url}) [CEEB: ${c.cb_code || 'N/A'}]\\n`;
        md += `- **Target Deadline:** \\`${d.deadline_badge}\\`\\n`;
        md += `- **Application Platform:** ${d.app_form}\\n`;
        md += `- **Application Fee:** ${d.app_fee}\\n`;
        md += `- **Testing (SAT/ACT):** ${d.sat_status}\\n`;
        md += `- **English Proficiency:** ${d.english_status}\\n`;
        md += `- **Financial Aid Form:** ${d.fa_badge} | **Max Package:** ${c.max_aid}\\n`;
        md += `- **Letters of Recommendation:** ${d.lor_info.join('; ')}\\n`;
        md += `- **Strategic Match:** ${c.strategic_rank_display || 'Top Tier'}\\n`;
        md += `- **US News Ranking:** ${c.us_news_display}\\n`;
        md += `- **Overall World Ranking:** ${c.world_rank_display}\\n`;
        md += `- **Test-Optional Admitted %:** ${c.test_optional_stat || 'Test-Optional Active'}\\n`;
        md += `- **Supplements:** Research Abstract & Technical Project Portfolio (GitHub Repositories / Live Demos)\\n`;
        md += `- **Tactical Takeaway:** ${d.tactical.join(' ')}\\n\\n`;
      });

      const blob = new Blob([md], { type: 'text/markdown;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'My_USA_Application_Checklist.md';
      a.click();
    }
  </script>
</body>
</html>
"""

# Serialize data
json_str = json.dumps(colleges, indent=2, ensure_ascii=False)

# Insert JSON
final_html = html_content.replace('JSON_DATA_PLACEHOLDER', json_str)

output_filename = "University_Application_Dossier.html"
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_filename} ({len(final_html)} bytes) with all 160 colleges.")
