import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\AI\POSTER_PROMPT_SYSTEM_V2\library\prompts_chat\prompts_community.json', encoding='utf-8') as f:
    data = json.load(f)

image_prompts = [p for p in data if p['type'] == 'IMAGE']
structured_visual = [p for p in data if p['type'] == 'STRUCTURED' and any(k in p['act'].lower() for k in ['poster', 'photo', 'image', 'art', 'diorama', 'view', 'tracking', 'design', 'style'])]
prompt_engineering = [p for p in data if any(k in p['act'].lower() for k in ['prompt engineer', 'prompt generator', 'prompt enhancer', 'reverse prompt', 'optimization', 'visual noise', 'midjourney'])]
copywriting_marketing = [p for p in data if any(k in p['act'].lower() for k in ['copywrit', 'advertis', 'branding', 'slogan', 'campaign', 'marketing', 'headline', 'storyteller'])]

print(f'IMAGE prompts: {len(image_prompts)}')
print(f'STRUCTURED visual prompts: {len(structured_visual)}')
print(f'Prompt Engineering prompts: {len(prompt_engineering)}')
print(f'Copywriting & Marketing prompts: {len(copywriting_marketing)}')

print('\nTop Structured Visual Acts:')
for p in structured_visual[:20]:
    print(f"- {p['act']} ({len(p['prompt'])} chars)")

print('\nTop Prompt Engineering Acts:')
for p in prompt_engineering[:20]:
    print(f"- {p['act']} ({len(p['prompt'])} chars)")

print('\nTop Copywriting/Marketing Acts:')
for p in copywriting_marketing[:20]:
    print(f"- {p['act']} ({len(p['prompt'])} chars)")
