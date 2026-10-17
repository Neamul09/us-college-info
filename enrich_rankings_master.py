import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('enriched_colleges.json', 'r', encoding='utf-8') as f:
    colleges = json.load(f)

def get_rankings(c):
    name = c.get('name', '')
    
    # Defaults
    us_rank = 150
    us_cat = "National University"
    us_disp = "US News Top Tier"
    world_rank = 500
    world_disp = "QS World Top Tier"

    # ==========================================
    # NATIONAL UNIVERSITIES
    # ==========================================
    if "Princeton" in name:
        us_rank = 1; us_cat = "National University"; us_disp = "US News #1 National Univ"; world_rank = 22; world_disp = "QS World #22 (THE #6)"
    elif "MIT" in name or "Massachusetts Institute of Technology" in name:
        us_rank = 2; us_cat = "National University"; us_disp = "US News #2 National Univ"; world_rank = 1; world_disp = "QS World #1 (THE #3)"
    elif "Harvard" in name:
        us_rank = 3; us_cat = "National University"; us_disp = "US News #3 National Univ"; world_rank = 4; world_disp = "QS World #4 (THE #4)"
    elif "Stanford" in name:
        us_rank = 3; us_cat = "National University"; us_disp = "US News #3 National Univ"; world_rank = 6; world_disp = "QS World #6 (THE #2)"
    elif "Yale" in name:
        us_rank = 5; us_cat = "National University"; us_disp = "US News #5 National Univ"; world_rank = 23; world_disp = "QS World #23 (THE #10)"
    elif "Caltech" in name or "California Institute of Technology" in name:
        us_rank = 7; us_cat = "National University"; us_disp = "US News #7 National Univ (#1 STEM)"; world_rank = 10; world_disp = "QS World #10 (THE #7)"
    elif "Duke" in name:
        us_rank = 7; us_cat = "National University"; us_disp = "US News #7 National Univ"; world_rank = 61; world_disp = "QS World #61 (THE #26)"
    elif "Johns Hopkins" in name or "JHU" in name:
        us_rank = 9; us_cat = "National University"; us_disp = "US News #9 National Univ"; world_rank = 32; world_disp = "QS World #32 (THE #15)"
    elif "Northwestern" in name:
        us_rank = 9; us_cat = "National University"; us_disp = "US News #9 National Univ"; world_rank = 50; world_disp = "QS World #50 (THE #28)"
    elif "Pennsylvania" in name or "UPenn" in name:
        us_rank = 10; us_cat = "National University"; us_disp = "US News #10 National Univ"; world_rank = 11; world_disp = "QS World #11 (THE #16)"
    elif "Cornell University" in name:
        us_rank = 12; us_cat = "National University"; us_disp = "US News #12 National Univ"; world_rank = 16; world_disp = "QS World #16 (THE #20)"
    elif "University of Chicago" in name or "UChicago" in name:
        us_rank = 12; us_cat = "National University"; us_disp = "US News #12 National Univ"; world_rank = 21; world_disp = "QS World #21 (THE #13)"
    elif "Brown" in name:
        us_rank = 13; us_cat = "National University"; us_disp = "US News #13 National Univ"; world_rank = 79; world_disp = "QS World #79 (THE #64)"
    elif "Columbia University" in name:
        us_rank = 13; us_cat = "National University"; us_disp = "US News #13 National Univ"; world_rank = 34; world_disp = "QS World #34 (THE #17)"
    elif "Dartmouth" in name:
        us_rank = 15; us_cat = "National University"; us_disp = "US News #15 National Univ"; world_rank = 243; world_disp = "QS World #243 (THE #161)"
    elif "Rice" in name:
        us_rank = 17; us_cat = "National University"; us_disp = "US News #17 National Univ"; world_rank = 141; world_disp = "QS World #141 (THE #119)"
    elif "Vanderbilt" in name:
        us_rank = 18; us_cat = "National University"; us_disp = "US News #18 National Univ"; world_rank = 282; world_disp = "QS World #282 (THE #98)"
    elif "Notre Dame" in name:
        us_rank = 19; us_cat = "National University"; us_disp = "US News #19 National Univ"; world_rank = 304; world_disp = "QS World #304 (THE #180)"
    elif "Carnegie Mellon" in name or "CMU" in name:
        us_rank = 22; us_cat = "National University"; us_disp = "US News #22 Nat. Univ (CS #1)"; world_rank = 52; world_disp = "QS World #52 (Global CS #1)"
    elif "Georgetown" in name:
        us_rank = 22; us_cat = "National University"; us_disp = "US News #22 National Univ"; world_rank = 301; world_disp = "QS World #301"
    elif "North Carolina at Chapel Hill" in name or "UNC" in name:
        us_rank = 22; us_cat = "National University"; us_disp = "US News #22 National Univ"; world_rank = 155; world_disp = "QS World #155"
    elif "Washington University in St. Louis" in name or "WashU" in name:
        us_rank = 24; us_cat = "National University"; us_disp = "US News #24 National Univ"; world_rank = 154; world_disp = "QS World #154 (THE #58)"
    elif "Emory" in name:
        us_rank = 24; us_cat = "National University"; us_disp = "US News #24 National Univ"; world_rank = 196; world_disp = "QS World #196 (THE #106)"
    elif "Virginia" in name or "UVA" in name:
        us_rank = 24; us_cat = "National University"; us_disp = "US News #24 National Univ"; world_rank = 250; world_disp = "QS World #250"
    elif "Tufts" in name:
        us_rank = 28; us_cat = "National University"; us_disp = "US News #28 National Univ"; world_rank = 344; world_disp = "QS World #344 (THE #179)"
    elif "Southern California" in name or "USC" in name:
        us_rank = 28; us_cat = "National University"; us_disp = "US News #28 National Univ"; world_rank = 125; world_disp = "QS World #125 (THE #74)"
    elif "NYU" in name and "Abu Dhabi" in name:
        us_rank = 30; us_cat = "Global Honors Portal Campus"; us_disp = "NYU Global Portal (#30 Nat.)"; world_rank = 43; world_disp = "QS World #43 (NYU System)"
    elif "Boston College" in name or "BC" in name:
        us_rank = 39; us_cat = "National University"; us_disp = "US News #39 National Univ"; world_rank = 520; world_disp = "QS World #520"
    elif "Boston University" in name or "BU" in name:
        us_rank = 43; us_cat = "National University"; us_disp = "US News #43 National Univ"; world_rank = 108; world_disp = "QS World #108 (THE #78)"
    elif "Rochester" in name:
        us_rank = 47; us_cat = "National University"; us_disp = "US News #47 National Univ"; world_rank = 224; world_disp = "QS World #224 (THE #147)"
    elif "Wake Forest" in name:
        us_rank = 47; us_cat = "National University"; us_disp = "US News #47 National Univ"; world_rank = 450; world_disp = "QS World #450"
    elif "Lehigh" in name:
        us_rank = 47; us_cat = "National University"; us_disp = "US News #47 National Univ"; world_rank = 550; world_disp = "QS World #550"
    elif "Case Western" in name or "CWRU" in name:
        us_rank = 53; us_cat = "National University"; us_disp = "US News #53 National Univ"; world_rank = 255; world_disp = "QS World #255 (THE #154)"
    elif "Villanova" in name:
        us_rank = 53; us_cat = "National University"; us_disp = "US News #53 National Univ"; world_rank = 650; world_disp = "QS World #650"
    elif "Rensselaer" in name or "RPI" in name:
        us_rank = 60; us_cat = "National University"; us_disp = "US News #60 National Univ"; world_rank = 480; world_disp = "QS World #480"
    elif "Santa Clara" in name or "SCU" in name:
        us_rank = 60; us_cat = "National University"; us_disp = "US News #60 Nat. Univ (Silicon Valley)"; world_rank = 750; world_disp = "QS World #750 / Silicon Valley"
    elif "Michigan State" in name or "MSU" in name:
        us_rank = 60; us_cat = "National University"; us_disp = "US News #60 National Univ"; world_rank = 152; world_disp = "QS World #152 (THE #116)"
    elif "Brandeis" in name:
        us_rank = 63; us_cat = "National University"; us_disp = "US News #63 National Univ"; world_rank = 450; world_disp = "QS World #450"
    elif "Miami" in name and ("Coral Gables" in name or "University of Miami" in name):
        us_rank = 67; us_cat = "National University"; us_disp = "US News #67 National Univ"; world_rank = 300; world_disp = "QS World #300"
    elif "Tulane" in name:
        us_rank = 73; us_cat = "National University"; us_disp = "US News #73 National Univ"; world_rank = 600; world_disp = "QS World #600"
    elif "Stevens Institute" in name:
        us_rank = 76; us_cat = "National University"; us_disp = "US News #76 National Univ"; world_rank = 700; world_disp = "QS World #700"
    elif "Worcester Polytechnic" in name or "WPI" in name:
        us_rank = 82; us_cat = "National University"; us_disp = "US News #82 National Univ"; world_rank = 750; world_disp = "QS World #750"
    elif "Marquette" in name:
        us_rank = 86; us_cat = "National University"; us_disp = "US News #86 National Univ"; world_rank = 800; world_disp = "QS World #800"
    elif "Southern Methodist" in name or "SMU" in name:
        us_rank = 89; us_cat = "National University"; us_disp = "US News #89 National Univ"; world_rank = 800; world_disp = "QS World #800"
    elif "Fordham" in name:
        us_rank = 89; us_cat = "National University"; us_disp = "US News #89 National Univ"; world_rank = 800; world_disp = "QS World #800"
    elif "Temple" in name:
        us_rank = 89; us_cat = "National University"; us_disp = "US News #89 National Univ"; world_rank = 700; world_disp = "QS World #700"
    elif "Loyola Marymount" in name or "LMU" in name:
        us_rank = 93; us_cat = "National University"; us_disp = "US News #93 National Univ"; world_rank = 850; world_disp = "QS World #850"
    elif "Drexel" in name:
        us_rank = 98; us_cat = "National University"; us_disp = "US News #98 National Univ"; world_rank = 650; world_disp = "QS World #650"
    elif "Illinois Institute of Technology" in name or "Illinois Tech" in name:
        us_rank = 98; us_cat = "National University"; us_disp = "US News #98 National Univ"; world_rank = 469; world_disp = "QS World #469"
    elif "Texas at Dallas" in name or "UT Dallas" in name:
        us_rank = 115; us_cat = "National University"; us_disp = "US News #115 National Univ"; world_rank = 520; world_disp = "QS World #520"
    elif "Howard" in name:
        us_rank = 115; us_cat = "National University"; us_disp = "US News #115 Nat. Univ (#1 HBCU)"; world_rank = 800; world_disp = "QS World #800 (#1 HBCU)"
    elif "Fairfield" in name:
        us_rank = 124; us_cat = "National University"; us_disp = "US News #124 National Univ"; world_rank = 900; world_disp = "QS World #900"
    elif "Drake" in name:
        us_rank = 133; us_cat = "National University"; us_disp = "US News #133 National Univ"; world_rank = 950; world_disp = "QS World #950"
    elif "Clark University" in name:
        us_rank = 142; us_cat = "National University"; us_disp = "US News #142 National Univ"; world_rank = 600; world_disp = "QS World #600"
    elif "Clarkson" in name:
        us_rank = 142; us_cat = "National University"; us_disp = "US News #142 National Univ"; world_rank = 800; world_disp = "QS World #800"
    elif "Loyola University Chicago" in name:
        us_rank = 142; us_cat = "National University"; us_disp = "US News #142 National Univ"; world_rank = 850; world_disp = "QS World #850"
    elif "Valparaiso" in name:
        us_rank = 163; us_cat = "National University"; us_disp = "US News #163 National Univ"; world_rank = 1000; world_disp = "QS World 1000+"
    elif "Alabama" in name:
        us_rank = 170; us_cat = "National University"; us_disp = "US News #170 National Univ"; world_rank = 750; world_disp = "QS World #750"
    elif "University of Dallas" in name:
        us_rank = 227; us_cat = "National University"; us_disp = "US News #227 National Univ"; world_rank = 1200; world_disp = "QS World 1200+"
    elif "Florida Institute of Technology" in name or "Florida Tech" in name:
        us_rank = 269; us_cat = "National University"; us_disp = "US News #269 National Univ"; world_rank = 800; world_disp = "QS World #800"

    # ==========================================
    # NATIONAL LIBERAL ARTS COLLEGES (LACs)
    # ==========================================
    elif "Williams" in name:
        us_rank = 1; us_cat = "National LAC"; us_disp = "US News #1 National LAC"; world_rank = 20; world_disp = "THE US Undergrad #1 / Forbes Top 15"
    elif "Amherst" in name:
        us_rank = 2; us_cat = "National LAC"; us_disp = "US News #2 National LAC"; world_rank = 25; world_disp = "THE US Undergrad #2 / Forbes Top 20"
    elif "Swarthmore" in name:
        us_rank = 3; us_cat = "National LAC"; us_disp = "US News #3 National LAC"; world_rank = 28; world_disp = "THE US Undergrad #3 / Forbes Top 20"
    elif "Pomona" in name:
        us_rank = 4; us_cat = "National LAC"; us_disp = "US News #4 National LAC"; world_rank = 30; world_disp = "THE US Undergrad #4 / Forbes Top 20"
    elif "Wellesley" in name:
        us_rank = 5; us_cat = "National LAC"; us_disp = "US News #5 National LAC"; world_rank = 35; world_disp = "THE US Undergrad #5 / #1 Global Women's"
    elif "Bowdoin" in name:
        us_rank = 5; us_cat = "National LAC"; us_disp = "US News #5 National LAC"; world_rank = 35; world_disp = "THE US Undergrad #5 / Forbes Top 25"
    elif "Carleton" in name:
        us_rank = 6; us_cat = "National LAC"; us_disp = "US News #6 National LAC"; world_rank = 40; world_disp = "THE US Undergrad #6 / Forbes Top 30"
    elif "Claremont McKenna" in name or "CMC" in name:
        us_rank = 11; us_cat = "National LAC"; us_disp = "US News #11 National LAC"; world_rank = 55; world_disp = "THE US Top 10 LAC / Forbes Top 30"
    elif "Middlebury" in name:
        us_rank = 11; us_cat = "National LAC"; us_disp = "US News #11 National LAC"; world_rank = 55; world_disp = "THE US Top 10 LAC / Forbes Top 35"
    elif "Grinnell" in name:
        us_rank = 11; us_cat = "National LAC"; us_disp = "US News #11 National LAC"; world_rank = 55; world_disp = "THE US Top 10 LAC / Forbes Top 40"
    elif "Barnard" in name:
        us_rank = 11; us_cat = "National LAC"; us_disp = "US News #11 National LAC"; world_rank = 55; world_disp = "Columbia Affiliate / Forbes Top 35"
    elif "Hobart and William Smith" in name or "HWS" in name:
        us_rank = 60; us_cat = "National LAC"; us_disp = "US News #60 National LAC"; world_rank = 270; world_disp = "Finger Lakes Research Hub"
    elif "Smith College" in name or name.strip() == "Smith":
        us_rank = 14; us_cat = "National LAC"; us_disp = "US News #14 National LAC"; world_rank = 65; world_disp = "Forbes Top 40 / Historic Elite"
    elif "Colby" in name:
        us_rank = 15; us_cat = "National LAC"; us_disp = "US News #15 National LAC"; world_rank = 70; world_disp = "Forbes Top 45 (Davis AI Institute)"
    elif "Davidson" in name:
        us_rank = 16; us_cat = "National LAC"; us_disp = "US News #16 National LAC"; world_rank = 75; world_disp = "Forbes Top 50"
    elif "Hamilton" in name:
        us_rank = 16; us_cat = "National LAC"; us_disp = "US News #16 National LAC"; world_rank = 75; world_disp = "Forbes Top 50"
    elif "Vassar" in name:
        us_rank = 16; us_cat = "National LAC"; us_disp = "US News #16 National LAC"; world_rank = 75; world_disp = "Forbes Top 50"
    elif "Harvey Mudd" in name:
        us_rank = 16; us_cat = "National LAC"; us_disp = "US News #16 Nat. LAC (#1 STEM)"; world_rank = 75; world_disp = "US STEM #1 PhD Feeder"
    elif "Bates" in name:
        us_rank = 18; us_cat = "National LAC"; us_disp = "US News #18 National LAC"; world_rank = 85; world_disp = "Forbes Top 60 (Test-Opt Since 1984)"
    elif "Haverford" in name:
        us_rank = 18; us_cat = "National LAC"; us_disp = "US News #18 National LAC"; world_rank = 85; world_disp = "Forbes Top 60"
    elif "Colgate" in name:
        us_rank = 18; us_cat = "National LAC"; us_disp = "US News #18 National LAC"; world_rank = 85; world_disp = "Forbes Top 60"
    elif "Wesleyan University" in name:
        us_rank = 18; us_cat = "National LAC"; us_disp = "US News #18 National LAC"; world_rank = 85; world_disp = "Forbes Top 60"
    elif "Richmond" in name:
        us_rank = 25; us_cat = "National LAC"; us_disp = "US News #25 National LAC"; world_rank = 110; world_disp = "Forbes Top 70 / Richmond Scholars"
    elif "Macalester" in name:
        us_rank = 27; us_cat = "National LAC"; us_disp = "US News #27 National LAC"; world_rank = 120; world_disp = "Top 1% Global Undergrad Community"
    elif "Colorado College" in name:
        us_rank = 29; us_cat = "National LAC"; us_disp = "US News #29 National LAC"; world_rank = 130; world_disp = "Block Plan Innovator / Forbes Top 80"
    elif "Soka University" in name or "SUA" in name:
        us_rank = 29; us_cat = "National LAC"; us_disp = "US News #29 National LAC"; world_rank = 130; world_disp = "Top 1% Global International Campus"
    elif "Kenyon" in name:
        us_rank = 30; us_cat = "National LAC"; us_disp = "US News #30 National LAC"; world_rank = 140; world_disp = "Premier Academic & Literary LAC"
    elif "Lafayette" in name:
        us_rank = 30; us_cat = "National LAC"; us_disp = "US News #30 National LAC"; world_rank = 140; world_disp = "Top Undergrad Engineering LAC"
    elif "Berea" in name:
        us_rank = 30; us_cat = "National LAC"; us_disp = "US News #30 National LAC"; world_rank = 140; world_disp = "100% Tuition Promise / Work College"
    elif "Bryn Mawr" in name:
        us_rank = 30; us_cat = "National LAC"; us_disp = "US News #30 National LAC"; world_rank = 140; world_disp = "Seven Sisters Historic Elite"
    elif "Mount Holyoke" in name:
        us_rank = 34; us_cat = "National LAC"; us_disp = "US News #34 National LAC"; world_rank = 160; world_disp = "Seven Sisters Historic Elite"
    elif "Franklin & Marshall" in name or "F&M" in name:
        us_rank = 35; us_cat = "National LAC"; us_disp = "US News #35 National LAC"; world_rank = 165; world_disp = "Forbes Top 100 LAC"
    elif "Skidmore" in name:
        us_rank = 38; us_cat = "National LAC"; us_disp = "US News #38 National LAC"; world_rank = 180; world_disp = "Forbes Top 100 LAC"
    elif "Denison" in name:
        us_rank = 38; us_cat = "National LAC"; us_disp = "US News #38 National LAC"; world_rank = 180; world_disp = "Top Career Outcomes / Free ISFAA"
    elif "Pitzer" in name:
        us_rank = 38; us_cat = "National LAC"; us_disp = "US News #38 National LAC"; world_rank = 180; world_disp = "Claremont Consortium Member"
    elif "Scripps" in name:
        us_rank = 38; us_cat = "National LAC"; us_disp = "US News #38 National LAC"; world_rank = 180; world_disp = "Claremont Consortium Member"
    elif "Bucknell" in name:
        us_rank = 38; us_cat = "National LAC"; us_disp = "US News #38 National LAC"; world_rank = 180; world_disp = "Undergrad Engineering Leader"
    elif "Trinity College" in name and "Hartford" in name or "Trinity College" == name:
        us_rank = 38; us_cat = "National LAC"; us_disp = "US News #38 National LAC"; world_rank = 180; world_disp = "Historic New England LAC"
    elif "Occidental" in name:
        us_rank = 38; us_cat = "National LAC"; us_disp = "US News #38 National LAC"; world_rank = 180; world_disp = "Los Angeles Elite LAC"
    elif "Union College" in name:
        us_rank = 43; us_cat = "National LAC"; us_disp = "US News #43 National LAC"; world_rank = 200; world_disp = "Undergrad Engineering Leader"
    elif "Whitman" in name:
        us_rank = 46; us_cat = "National LAC"; us_disp = "US News #46 National LAC"; world_rank = 210; world_disp = "Pacific Northwest Elite"
    elif "Dickinson" in name:
        us_rank = 46; us_cat = "National LAC"; us_disp = "US News #46 National LAC"; world_rank = 210; world_disp = "Global Study & Sustainability Leader"
    elif "DePauw" in name:
        us_rank = 46; us_cat = "National LAC"; us_disp = "US News #46 National LAC"; world_rank = 210; world_disp = "Top Midwest LAC / 58% Test-Opt"
    elif "Connecticut College" in name:
        us_rank = 51; us_cat = "National LAC"; us_disp = "US News #51 National LAC"; world_rank = 230; world_disp = "New England Elite LAC"
    elif "St. Olaf" in name:
        us_rank = 51; us_cat = "National LAC"; us_disp = "US News #51 National LAC"; world_rank = 230; world_disp = "Top STEM & Mathematics LAC"
    elif "Furman" in name:
        us_rank = 51; us_cat = "National LAC"; us_disp = "US News #51 National LAC"; world_rank = 230; world_disp = "Top South LAC"
    elif "Sewanee" in name:
        us_rank = 51; us_cat = "National LAC"; us_disp = "US News #51 National LAC"; world_rank = 230; world_disp = "Domain of the South"
    elif "Oberlin" in name:
        us_rank = 51; us_cat = "National LAC"; us_disp = "US News #51 National LAC"; world_rank = 230; world_disp = "Top STEM PhD Feeder in US"
    elif "Centre" in name:
        us_rank = 55; us_cat = "National LAC"; us_disp = "US News #55 National LAC"; world_rank = 250; world_disp = "Premier Kentucky LAC"
    elif "Rhodes" in name:
        us_rank = 55; us_cat = "National LAC"; us_disp = "US News #55 National LAC"; world_rank = 250; world_disp = "Urban LAC / Memphis Health Hub"
    elif "Gettysburg" in name:
        us_rank = 60; us_cat = "National LAC"; us_disp = "US News #60 National LAC"; world_rank = 270; world_disp = "Historic Pennsylvania LAC"
    elif "College of Wooster" in name or "Wooster" in name:
        us_rank = 60; us_cat = "National LAC"; us_disp = "US News #60 Nat. LAC (#1 Research)"; world_rank = 270; world_disp = "#1 Mentored Senior Research"
    elif "Hobart and William Smith" in name or "HWS" in name:
        us_rank = 60; us_cat = "National LAC"; us_disp = "US News #60 National LAC"; world_rank = 270; world_disp = "Finger Lakes Research Hub"
    elif "Wabash" in name:
        us_rank = 60; us_cat = "National LAC"; us_disp = "US News #60 National LAC"; world_rank = 270; world_disp = "Top Return on Investment LAC"
    elif "Bard" in name:
        us_rank = 60; us_cat = "National LAC"; us_disp = "US News #60 National LAC"; world_rank = 270; world_disp = "New York Research & Arts Titan"
    elif "St. Lawrence" in name:
        us_rank = 60; us_cat = "National LAC"; us_disp = "US News #60 National LAC"; world_rank = 270; world_disp = "Upstate New York Titan"
    elif "Agnes Scott" in name:
        us_rank = 63; us_cat = "National LAC"; us_disp = "US News #63 National LAC"; world_rank = 280; world_disp = "#1 Most Innovative LAC (US News)"
    elif "Trinity University" in name and "San Antonio" in name:
        us_rank = 63; us_cat = "National LAC / Regional"; us_disp = "US News #63 National LAC"; world_rank = 280; world_disp = "Semmes STEM Full-Ride Hub"
    elif "Reed" in name:
        us_rank = 67; us_cat = "National LAC"; us_disp = "US News #67 Nat. LAC (#3 STEM PhDs)"; world_rank = 290; world_disp = "#3 STEM PhD Feeder in US"
    elif "Sarah Lawrence" in name:
        us_rank = 67; us_cat = "National LAC"; us_disp = "US News #67 National LAC"; world_rank = 290; world_disp = "Oxford-Style Don System"
    elif "Lawrence" in name:
        us_rank = 75; us_cat = "National LAC"; us_disp = "US News #75 National LAC"; world_rank = 320; world_disp = "Top Midwest LAC & Conservatory"
    elif "Kalamazoo" in name:
        us_rank = 75; us_cat = "National LAC"; us_disp = "US News #75 National LAC"; world_rank = 320; world_disp = "K-Plan Experiential Titan"
    elif "Knox" in name:
        us_rank = 75; us_cat = "National LAC"; us_disp = "US News #75 National LAC"; world_rank = 320; world_disp = "65% Test-Opt / Free ISFAA"
    elif "Muhlenberg" in name:
        us_rank = 75; us_cat = "National LAC"; us_disp = "US News #75 National LAC"; world_rank = 320; world_disp = "Top Pre-Med & Arts LAC"
    elif "Willamette" in name:
        us_rank = 75; us_cat = "National LAC"; us_disp = "US News #75 National LAC"; world_rank = 320; world_disp = "First University in American West"
    elif "Beloit" in name:
        us_rank = 82; us_cat = "National LAC"; us_disp = "US News #82 National LAC"; world_rank = 350; world_disp = "60% Test-Opt Innovator"
    elif "Allegheny" in name:
        us_rank = 82; us_cat = "National LAC"; us_disp = "US News #82 National LAC"; world_rank = 350; world_disp = "Major & Minor in 2 Disciplines"
    elif "Hendrix" in name:
        us_rank = 82; us_cat = "National LAC"; us_disp = "US News #82 National LAC"; world_rank = 350; world_disp = "Top Southern STEM LAC"
    elif "Juniata" in name:
        us_rank = 82; us_cat = "National LAC"; us_disp = "US News #82 National LAC"; world_rank = 350; world_disp = "Program of Emphasis (POE) Leader"
    elif "Illinois Wesleyan" in name or "IWU" in name:
        us_rank = 82; us_cat = "National LAC"; us_disp = "US News #82 National LAC"; world_rank = 350; world_disp = "Top Illinois Science LAC"
    elif "Lewis & Clark" in name:
        us_rank = 82; us_cat = "National LAC"; us_disp = "US News #82 National LAC"; world_rank = 350; world_disp = "Portland Environmental Leader"
    elif "Earlham" in name:
        us_rank = 86; us_cat = "National LAC"; us_disp = "US News #86 National LAC"; world_rank = 370; world_disp = "Epic Journey Research Leader"
    elif "Gustavus Adolphus" in name:
        us_rank = 89; us_cat = "National LAC"; us_disp = "US News #89 National LAC"; world_rank = 380; world_disp = "Nobel Conference Host LAC"
    elif "Puget Sound" in name:
        us_rank = 89; us_cat = "National LAC"; us_disp = "US News #89 National LAC"; world_rank = 380; world_disp = "Seattle Sound Region Titan"
    elif "Bennington" in name:
        us_rank = 90; us_cat = "National LAC"; us_disp = "US News #90 National LAC"; world_rank = 390; world_disp = "Field Work Term Innovator"
    elif "Southwestern" in name:
        us_rank = 90; us_cat = "National LAC"; us_disp = "US News #90 National LAC"; world_rank = 390; world_disp = "First University in Texas"
    elif "College of the Atlantic" in name or "COA" in name:
        us_rank = 90; us_cat = "National LAC"; us_disp = "US News #90 National LAC"; world_rank = 390; world_disp = "#1 Green / Human Ecology College"
    elif "Augustana College" in name and "Illinois" in name:
        us_rank = 100; us_cat = "National LAC"; us_disp = "US News #100 National LAC"; world_rank = 420; world_disp = "Augie Choice Experiential Leader"
    elif "St. John's" in name:
        us_rank = 100; us_cat = "National LAC"; us_disp = "US News #100 Nat. LAC (Great Books)"; world_rank = 420; world_disp = "The Great Books Curriculum"
    elif "Cornell College" in name:
        us_rank = 100; us_cat = "National LAC"; us_disp = "US News #100 Nat. LAC (Block Plan)"; world_rank = 420; world_disp = "One Course At A Time Pioneer"
    elif "Luther" in name:
        us_rank = 100; us_cat = "National LAC"; us_disp = "US News #100 National LAC"; world_rank = 420; world_disp = "Top Midwest Liberal Arts"
    elif "Hampshire" in name:
        us_rank = 130; us_cat = "National LAC"; us_disp = "US News #130 National LAC"; world_rank = 480; world_disp = "100% Test-Blind Pioneer"
    elif "Illinois College" in name:
        us_rank = 133; us_cat = "National LAC"; us_disp = "US News #133 National LAC"; world_rank = 500; world_disp = "Historic Illinois College"
    elif "Ripon" in name:
        us_rank = 133; us_cat = "National LAC"; us_disp = "US News #133 National LAC"; world_rank = 500; world_disp = "Wisconsin Liberal Arts"
    elif "Coe" in name:
        us_rank = 142; us_cat = "National LAC"; us_disp = "US News #142 National LAC"; world_rank = 550; world_disp = "Urban Cedar Rapids LAC"
    elif "Albion" in name:
        us_rank = 142; us_cat = "National LAC"; us_disp = "US News #142 National LAC"; world_rank = 550; world_disp = "Michigan Experiential LAC"
    elif "Transylvania" in name:
        us_rank = 142; us_cat = "National LAC"; us_disp = "US News #142 National LAC"; world_rank = 550; world_disp = "Historic Lexington LAC"
    elif "Eckerd" in name:
        us_rank = 142; us_cat = "National LAC"; us_disp = "US News #142 National LAC"; world_rank = 550; world_disp = "Waterfront Marine Science Hub"
    elif "Wartburg" in name:
        us_rank = 156; us_cat = "National LAC"; us_disp = "US News #156 National LAC"; world_rank = 600; world_disp = "Top Midwest Science LAC"
    elif "Wittenberg" in name:
        us_rank = 156; us_cat = "National LAC"; us_disp = "US News #156 National LAC"; world_rank = 600; world_disp = "Ohio Liberal Arts"
    elif "Oglethorpe" in name:
        us_rank = 156; us_cat = "National LAC"; us_disp = "US News #156 National LAC"; world_rank = 600; world_disp = "Atlanta Metro LAC"
    elif "Warren Wilson" in name:
        us_rank = 156; us_cat = "National LAC"; us_disp = "US News #156 Nat. LAC (Work College)"; world_rank = 600; world_disp = "National Work College"

    # ==========================================
    # REGIONAL & SPECIALIZED
    # ==========================================
    elif "Cooper Union" in name:
        us_rank = 1; us_cat = "Regional Specialized (Engineering)"; us_disp = "US News #1 Regional Colleges"; world_rank = 150; world_disp = "QS Top 50 Architecture/Art"
    elif "Deep Springs" in name:
        us_rank = 50; us_cat = "Alternative 2-Year Prep"; us_disp = "#1 Alternative Prep (Feeds Ivies)"; world_rank = 200; world_disp = "Feeds Directly to Ivies"
    elif "Providence" in name:
        us_rank = 1; us_cat = "Regional University North"; us_disp = "US News #1 Regional North"; world_rank = 700; world_disp = "QS Americas #181-190"
    elif "Rollins" in name:
        us_rank = 1; us_cat = "Regional University South"; us_disp = "US News #1 Regional South"; world_rank = 750; world_disp = "Forbes Top South Regional"
    elif "College of the Ozarks" in name:
        us_rank = 1; us_cat = "Regional Work College"; us_disp = "US News #1 Regional Midwest"; world_rank = 800; world_disp = "National Work College ($0 Tuition)"
    elif "Whitworth" in name:
        us_rank = 3; us_cat = "Regional University West"; us_disp = "US News #3 Regional West"; world_rank = 850; world_disp = "Pacific Northwest Regional"
    elif "Augustana University" in name and "Sioux Falls" in name:
        us_rank = 15; us_cat = "Regional University Midwest"; us_disp = "US News #15 Regional Midwest"; world_rank = 900; world_disp = "Midwest Health & Tech"
    elif "Wesleyan College (Macon" in name:
        us_rank = 150; us_cat = "Historic Women's College"; us_disp = "#150 Historic Women's College"; world_rank = 1000; world_disp = "Historic Women's College"

    return us_rank, us_cat, us_disp, world_rank, world_disp

def calculate_strategic_score(c, us_rank, us_cat, world_rank):
    aid_policy = c.get('aid_policy', '').lower()
    need_blind = c.get('need_blind_status', '').lower()
    max_aid = c.get('max_aid', '').lower()
    test_opt_stat = c.get('test_optional_stat', '').lower()
    visa = c.get('visa_safety_index', '').lower()

    # Factor 1: Aid (max 40 pts)
    aid_score = 15
    if "need-blind" in need_blind or "need-blind" in aid_policy:
        aid_score = 40
    elif "100% demonstrated need" in aid_policy or "100% full ride" in max_aid or "full ride" in max_aid:
        aid_score = 36
    elif "work college" in c.get('type', '').lower() or "tuition promise" in max_aid:
        aid_score = 33
    elif "merit" in max_aid or "scholarship" in aid_policy:
        aid_score = 30

    # Factor 2: Academic Prestige & Standing (max 25 pts)
    prestige_score = 6
    is_regional = "Regional" in us_cat or "Alternative" in us_cat or "Specialized" in us_cat
    
    if not is_regional:
        if us_rank <= 5 or world_rank <= 10:
            prestige_score = 25
        elif us_rank <= 15 or world_rank <= 35:
            prestige_score = 23
        elif us_rank <= 30 or world_rank <= 70:
            prestige_score = 20
        elif us_rank <= 50 or world_rank <= 150:
            prestige_score = 16
        elif us_rank <= 80:
            prestige_score = 13
        elif us_rank <= 120:
            prestige_score = 10
        else:
            prestige_score = 7
    else:
        # Regional / Alternative institutions
        if "Cooper Union" in c.get('name', ''):
            prestige_score = 17
        elif "Deep Springs" in c.get('name', ''):
            prestige_score = 15
        elif us_rank <= 3:
            prestige_score = 11
        else:
            prestige_score = 8

    # Factor 3: Test-Optional Friendliness (max 20 pts)
    test_score = 10
    if "100% test-free" in test_opt_stat or "test-blind" in test_opt_stat:
        test_score = 20
    elif any(pct in test_opt_stat for pct in ['50%', '51%', '52%', '53%', '54%', '55%', '56%', '58%', '60%', '62%', '65%']):
        test_score = 19
    elif any(pct in test_opt_stat for pct in ['40%', '42%', '44%', '45%', '46%', '47%', '48%', '49%']):
        test_score = 16
    elif any(pct in test_opt_stat for pct in ['30%', '35%', '36%', '37%', '38%', '39%']):
        test_score = 13
    elif "0% test-optional" in test_opt_stat or "test-required" in test_opt_stat:
        test_score = 7

    # Factor 4: Dhaka Visa Safety (max 15 pts)
    visa_score = 10
    if "99%" in visa or "98%" in visa:
        visa_score = 15
    elif "96%" in visa or "95%" in visa:
        visa_score = 13
    elif "93%" in visa or "92%" in visa:
        visa_score = 11

    total = aid_score + prestige_score + test_score + visa_score
    return round(total, 1)

for c in colleges:
    us_r, us_cat, us_d, w_r, w_d = get_rankings(c)
    c['us_news_rank'] = us_r
    c['us_news_category'] = us_cat
    c['us_news_display'] = us_d
    c['world_rank_num'] = w_r
    c['world_rank_display'] = w_d
    c['strategic_score'] = calculate_strategic_score(c, us_r, us_cat, w_r)

# Sort primarily by strategic_score descending
colleges.sort(key=lambda x: (-x['strategic_score'], x['us_news_rank'], x['world_rank_num']))

for idx, c in enumerate(colleges):
    c['strategic_rank_num'] = idx + 1
    c['strategic_rank_display'] = f"#{idx + 1} Strategic Match (Score: {c['strategic_score']}/100)"
    c['rank_num'] = c['strategic_rank_num']
    
    # Combined clean display for cards and headers
    c['rank_display'] = f"{c['us_news_display']} • {c['world_rank_display']}"
    
    if 'dossier' in c:
        c['dossier']['us_news_display'] = c['us_news_display']
        c['dossier']['world_rank_display'] = c['world_rank_display']
        c['dossier']['strategic_rank_display'] = c['strategic_rank_display']
        c['dossier']['rank_display'] = c['rank_display']

print("\n=== TOP 25 REVISED STRATEGIC TARGETS ===")
for i in range(25):
    c = colleges[i]
    print(f"#{i+1:2d}: {c['name']} | Score: {c['strategic_score']} | {c['us_news_display']} | {c['world_rank_display']}")

with open('enriched_colleges.json', 'w', encoding='utf-8') as f:
    json.dump(colleges, f, indent=2, ensure_ascii=False)

print("\nEnriched enriched_colleges.json successfully!")
