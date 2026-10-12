#!/usr/bin/env python3
"""
prompts_chat_tool.py — Local CLI Intelligence Engine for prompts.chat in Poster Studio V3.0
Allows instant searching, inspecting, and adapting 2,400+ prompts from prompts.chat
into standard 18-Block Master Production Prompts for commercial poster design.
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Any

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "library", "prompts_chat", "prompts_community.json")


def load_dataset() -> List[Dict[str, Any]]:
    if not os.path.exists(DATA_FILE):
        print(f"Error: Dataset not found at {DATA_FILE}")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_stats(args: argparse.Namespace):
    data = load_dataset()
    type_counts = {}
    for p in data:
        t = p.get("type", "TEXT")
        type_counts[t] = type_counts.get(t, 0) + 1

    print("=" * 60)
    print("PROMPTS.CHAT LOCAL REPOSITORY STATISTICS")
    print("=" * 60)
    print(f"Total community prompts indexed: {len(data):,}")
    print("Prompt Types Distribution:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  - {t:<15}: {c:>5} prompts ({c/len(data)*100:.1f}%)")
    print(f"Source file: {DATA_FILE}")
    print("License: CC0 1.0 Universal (Public Domain)")
    print("=" * 60)


def cmd_search(args: argparse.Namespace):
    data = load_dataset()
    query = args.query.lower()
    ptype = args.type.upper() if args.type else None
    limit = args.limit

    matches = []
    for p in data:
        if ptype and p.get("type") != ptype:
            continue
        act = p.get("act", "")
        prompt = p.get("prompt", "")
        if query in act.lower() or query in prompt.lower():
            # Calculate a simple match relevance score
            score = 0
            if query == act.lower():
                score += 100
            elif query in act.lower():
                score += 50
            if query in prompt.lower():
                score += 10
            matches.append((score, p))

    matches.sort(key=lambda x: -x[0])
    total_found = len(matches)

    print("=" * 70)
    print(f"PROMPTS.CHAT SEARCH RESULTS FOR: '{args.query}' (Found: {total_found})")
    if ptype:
        print(f"Filtered by type: {ptype}")
    print("=" * 70)

    for idx, (_, p) in enumerate(matches[:limit], 1):
        act = p.get("act")
        pid = p.get("id")
        ptype = p.get("type", "TEXT")
        plen = len(p.get("prompt", ""))
        contributor = p.get("contributor", "community")
        sample = p.get("prompt", "")[:120].replace("\n", " ").strip()
        print(f"[{idx:>2}] ID: {pid:<4} | Type: {ptype:<10} | Act: {act}")
        print(f"     By: {contributor} | Length: {plen} chars")
        print(f"     Preview: {sample}...")
        print("-" * 70)

    if total_found > limit:
        print(f"... and {total_found - limit} more. Use --limit to show more results.")


def cmd_show(args: argparse.Namespace):
    data = load_dataset()
    target = args.target.strip()

    item = None
    if target.isdigit():
        tid = int(target)
        for p in data:
            if p.get("id") == tid:
                item = p
                break
    else:
        for p in data:
            if p.get("act", "").lower() == target.lower():
                item = p
                break
        if not item:
            # Fuzzy match
            for p in data:
                if target.lower() in p.get("act", "").lower():
                    item = p
                    break

    if not item:
        print(f"No prompt found matching '{target}'.")
        return

    print("=" * 70)
    print(f"PROMPT #{item['id']}: {item['act']}")
    print(f"Type: {item.get('type')} | Contributor: {item.get('contributor', 'anonymous')} | For Devs: {item.get('for_devs')}")
    print("=" * 70)
    print(item.get("prompt"))
    print("=" * 70)


def cmd_adapt(args: argparse.Namespace):
    """
    Adapts a prompt from prompts.chat into the 18-Block Master Production Prompt format
    for poster generation in POSTER_PROMPT_SYSTEM_V2.
    """
    data = load_dataset()
    target = args.target.strip()
    topic = args.topic or "Giải pháp bảo vệ tài chính và bình an trọn đời"
    headline = args.headline or "VỮNG BƯỚC TƯƠNG LAI — BẢO AN TOÀN DIỆN"

    item = None
    if target.isdigit():
        tid = int(target)
        for p in data:
            if p.get("id") == tid:
                item = p
                break
    else:
        for p in data:
            if target.lower() in p.get("act", "").lower():
                item = p
                break

    if not item:
        print(f"Prompt '{target}' not found.")
        return

    act = item.get("act")
    original_prompt = item.get("prompt", "")

    # Clean prompt summary for prompt adaptation
    clean_concept = original_prompt[:400].replace("\n", " ").strip()

    master_prompt = f"""# ==============================================================================
# PRODUCTION PROMPT (Adapted from prompts.chat: '{act}')
# POSTER STUDIO V3.1 — 4-FRAME & STREAMLINED SEQUENCE READY
# ==============================================================================

ROLE & OBJECTIVE:
Synthesize a commercial visual poster for {topic}. The composition must achieve instant stopping power on mobile and desktop, integrating authentic art materials and exact Vietnamese typography.

VISUAL THESIS & HERO METAPHOR:
Central visual anchor adapting archetype '{act}':
A meticulously composed centerpiece symbolizing long-term protection, resilience, and family peace of mind. Central motif crafted with hyper-tactile details, authentic physical texture, and zero generic AI plastic finish.

STYLE & MATERIALITY:
Archetype DNA: '{act}'.
Tactile physical rendering, high aesthetic discipline, micro-surface paper/ceramic/wood textures, museum-grade material lighting. Total elimination of cheesy stock photo cliches.

COMPOSITION & ASPECT RATIO:
Aspect ratio 1:1 (or 4:5). Breathable 35-45% negative space reserved for integrated headline typography and advisor signature. High-contrast focal point.

ON-IMAGE COPY (EXACT VIETNAMESE):
Headline:
"{headline}"
Subhead:
"Giải pháp tài chính bảo vệ trọn vẹn tương lai gia đình"

SIGNATURE & IDENTITY (DƯƠNG QUANG TIẾN):
Line 1: Handwritten signature 'Tiến'
Line 2: 'Dương Quang Tiến'
Line 3: 'Trưởng nhóm kinh doanh Manulife'
Line 4: '0935 074 268'

ALLOWED_TEXT WHITELIST:
["{headline}", "Giải pháp tài chính bảo vệ trọn vẹn tương lai gia đình", "Tiến", "Dương Quang Tiến", "Trưởng nhóm kinh doanh Manulife", "0935 074 268"]

NEGATIVE CONSTRAINTS & ANTI-NOISE:
No plastic CGI skin, no uncanny smiling models, no symbolic clutter (###, ░, [placeholder]), no gibberish floating text.
"""
    print(master_prompt)


def cmd_curated(args: argparse.Namespace):
    curated_list = [
        # (ID/Act, Category, Highlight)
        ("Predictive Eye Tracking Heatmap Generator", "Visual Attention", "Simulates user eye movements and visual hierarchy (Nielsen Norman / Gestalt)"),
        ("Travel Poster", "Poster Architecture", "Modern flat vector travel poster with clean geometric balance"),
        ("Legebdary Exploded View Prompt For nanobanana", "Technical Infographic", "3D CAD exploded-view layout with callout lines"),
        ("Whimsical 3D Brand Miniatures", "3D Diorama", "Cinema 4D chibi miniature concept store with warm lighting"),
        ("Removing visual noise in the neural network's response", "Prompt Engineering", "Purges text clutter, symbol noise, and token hallucinations"),
        ("Director Variation Grid: One Still, Eight Auteur Re-Shoots", "Art Direction", "3x3 auteur director visual style matrixing"),
        ("Isometric 3D Weather Cityscapes (PBR Textures)", "3D Architecture", "PBR textured isometric cityscapes with weather dynamics"),
        ("Time Layer Photography", "Visual Concept", "Time progression and multi-phase photographic layering"),
        ("Senior Prompt Engineer Role Guide", "Meta-Prompting", "Structured prompt construction: Persona, Context, Task, Constraints"),
        ("Chimera AI-Powered Prompt Optimization System", "Prompt Optimization", "Multi-provider LLM prompt enhancement engine"),
        ("Landing page copywriting", "Direct-Response Copy", "13-section conversion framework and 10 headline formulas"),
        ("Advertiser", "Marketing Strategy", "Direct advertising campaign creative angles"),
        ("Creative Branding Strategist", "Brand Identity", "Brand positioning, aesthetic voice, and visual storytelling"),
        ("Editorial Winter Poster–Style Multi-Panel Collage Generation", "Poster Layout", "Multi-panel editorial collage composition"),
        ("High-End Beauty Editorial Photo Shoot Specification", "Photorealism", "High-fashion editorial lighting, skin shaders, and optics")
    ]

    print("=" * 75)
    print("TOP CURATED PROMPTS FROM PROMPTS.CHAT FOR POSTER STUDIO V3.0")
    print("=" * 75)
    for idx, (act, cat, desc) in enumerate(curated_list, 1):
        print(f"[{idx:>2}] [{cat:<22}] {act}")
        print(f"     -> {desc}")
    print("=" * 75)
    print("To inspect any prompt: python scripts/prompts_chat_tool.py show \"<act_name>\"")
    print("To adapt into Master Prompt: python scripts/prompts_chat_tool.py adapt \"<act_name>\"")


def main():
    parser = argparse.ArgumentParser(description="prompts.chat CLI Tool for Poster Studio V3.0")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # stats
    subparsers.add_parser("stats", help="Display prompts.chat dataset statistics")

    # search
    search_p = subparsers.add_parser("search", help="Search community prompts")
    search_p.add_argument("query", help="Keywords to search in act or prompt body")
    search_p.add_argument("--type", choices=["TEXT", "STRUCTURED", "IMAGE"], help="Filter by prompt type")
    search_p.add_argument("--limit", type=int, default=10, help="Maximum number of results (default: 10)")

    # show
    show_p = subparsers.add_parser("show", help="Display full prompt content")
    show_p.add_argument("target", help="Prompt ID number or act name")

    # adapt
    adapt_p = subparsers.add_parser("adapt", help="Adapt prompt into 18-Block Master Production Prompt")
    adapt_p.add_argument("target", help="Prompt ID number or act name")
    adapt_p.add_argument("--topic", help="Poster topic / campaign message")
    adapt_p.add_argument("--headline", help="Custom Vietnamese headline")

    # curated
    subparsers.add_parser("list-curated", help="List curated top creative prompts")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "stats":
        cmd_stats(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "show":
        cmd_show(args)
    elif args.command == "adapt":
        cmd_adapt(args)
    elif args.command == "list-curated":
        cmd_curated(args)


if __name__ == "__main__":
    main()
