# -*- coding: utf-8 -*-
"""poeskill 原创化：第一轮确定性替换（品牌统一 + 去独断话术）"""
import os

ROOT = r'C:\Users\Administrator\.workbuddy\skills'

# (old, new) 全量确定性替换
REPLS = [
    ('', 'poeskill'),
    ('', 'Poeskill'),
    ('公理', '假设'),
    ('非谈判项', '核心假设'),
    ('（奥派经济学视角）', '（市场秩序学派视角）'),
]

def walk_skill_files():
    for d in sorted(os.listdir(ROOT)):
        if not d.startswith('poe'):
            continue
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p):
            continue
        for base, _, files in os.walk(p):
            for fn in files:
                yield os.path.join(base, fn)

changed = 0
for fp in walk_skill_files():
    try:
        with open(fp, encoding='utf-8') as f:
            s = f.read()
    except Exception:
        continue
    orig = s
    for a, b in REPLS:
        s = s.replace(a, b)
    if s != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(s)
        changed += 1
        print('changed:', os.path.relpath(fp, ROOT))

print(f'\n共修改 {changed} 个文件')
