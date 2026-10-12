import os
import json
import subprocess
import sys

base_dir = r"d:\AI\POSTER_PROMPT_SYSTEM_V2"

def test_prompts_community_json():
    path = os.path.join(base_dir, "library", "prompts_chat", "prompts_community.json")
    assert os.path.exists(path), f"Missing {path}"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) >= 2400, f"Expected at least 2400 records, got {len(data)}"
    print(f"PASS: prompts_community.json has {len(data)} prompts.")

def test_prompts_csv():
    path = os.path.join(base_dir, "library", "prompts_chat", "prompts.csv")
    assert os.path.exists(path), f"Missing {path}"
    size = os.path.getsize(path)
    assert size > 5000000, f"Expected size > 5MB, got {size}"
    print(f"PASS: prompts.csv is present ({size:,} bytes).")

def test_cli_tool():
    tool = os.path.join(base_dir, "scripts", "prompts_chat_tool.py")
    res = subprocess.run([sys.executable, tool, "stats"], capture_output=True, text=True, encoding="utf-8")
    assert res.returncode == 0, f"CLI stats failed: {res.stderr}"
    assert "2,435" in res.stdout, "CLI stats output missing count"
    print("PASS: CLI stats command verified.")

    res_search = subprocess.run([sys.executable, tool, "search", "travel"], capture_output=True, text=True, encoding="utf-8")
    assert res_search.returncode == 0, f"CLI search failed: {res_search.stderr}"
    assert "Travel" in res_search.stdout, "CLI search output missing 'Travel'"
    print("PASS: CLI search command verified.")

    res_adapt = subprocess.run([sys.executable, tool, "adapt", "Travel Poster", "--headline", "TEST HEADLINE"], capture_output=True, text=True, encoding="utf-8")
    assert res_adapt.returncode == 0, f"CLI adapt failed: {res_adapt.stderr}"
    assert "PRODUCTION PROMPT" in res_adapt.stdout, "CLI adapt missing PRODUCTION PROMPT header"
    assert "0935 074 268" in res_adapt.stdout, "CLI adapt missing advisor phone"
    assert "TEST HEADLINE" in res_adapt.stdout, "CLI adapt missing headline"
    print("PASS: CLI adapt command verified (production prompt + advisor signature).")

def test_new_files():
    files = [
        "library/prompts_chat/README.md",
        "library/prompts_chat/CURATED_CREATIVE_PROMPTS.md",
        "library/styles/STYLE_024_ART_DECO_VINTAGE_TRAVEL_POSTER.md",
        "library/styles/STYLE_025_EXPLODED_VIEW_TECHNICAL_INFOGRAPHIC.md",
        "library/styles/STYLE_026_WHIMSICAL_3D_ISOMETRIC_MINIATURE_DIORAMA.md",
        "rules/visual_hierarchy_eyeflow.md",
        "rules/headline_copywriting_formulas.md",
        "rules/qa_completeness_gate.md"
    ]
    for rel in files:
        full = os.path.join(base_dir, rel.replace("/", os.sep))
        assert os.path.exists(full), f"Missing file {rel}"
        with open(full, "r", encoding="utf-8") as f:
            content = f.read()
        assert len(content) > 200, f"File {rel} is suspiciously small"
        print(f"PASS: Verified {rel} ({len(content)} chars)")

if __name__ == "__main__":
    print("Running Integration Tests for prompts.chat Integration...")
    test_prompts_community_json()
    test_prompts_csv()
    test_cli_tool()
    test_new_files()
    print("ALL TESTS PASSED SUCCESSFULLY!")
