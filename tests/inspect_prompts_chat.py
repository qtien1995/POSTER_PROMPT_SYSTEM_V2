import urllib.request
import csv
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
csv.field_size_limit(2147483647)
url = 'https://raw.githubusercontent.com/f/prompts.chat/main/prompts.csv'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req, timeout=15)
lines = resp.read().decode('utf-8', errors='ignore')
reader = csv.DictReader(io.StringIO(lines))

targets = [
    'Senior Prompt Engineer Role Guide',
    'Midjourney Prompt Generator',
    'Travel Poster',
    'Predictive Eye Tracking Heatmap Generator',
    'Editorial Winter Poster\ufffdStyle Multi-Panel Collage Generation',
    'Legebdary Exploded View Prompt For nanobanana',
    'Create STYLE_GUIDE.md'
]

found = set()
for row in reader:
    act = row.get('act', '')
    for t in targets:
        if t in act or act in t:
            print('=' * 60)
            print(f"ACT: {row['act']} (Type: {row.get('type')})")
            print('=' * 60)
            print(row['prompt'][:1000])
            print('\n' + '-' * 30 + '\n')
            found.add(t)
            break
