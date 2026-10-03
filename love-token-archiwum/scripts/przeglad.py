#!/usr/bin/env python3
"""Export tagged snapshots to an offline gallery, preserving the Git working tree."""
import argparse
import html
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]

STYLE = '''
:root{color-scheme:light;--bg:#f5f2eb;--ink:#29291f;--muted:#747265;--line:#d9d4c5;--gold:#88702b}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,sans-serif}
main{max-width:1240px;margin:auto;padding:36px 24px 70px}header{border-bottom:1px solid var(--line);padding-bottom:25px;margin-bottom:30px}
.eyebrow{letter-spacing:.17em;text-transform:uppercase;font-size:12px;color:var(--gold)}h1{font:clamp(28px,4vw,48px)/1.12 Georgia,serif;margin:14px 0}h2{font:28px Georgia,serif;margin:36px 0 16px}h3{margin:0 0 8px;font-size:17px}p{max-width:850px}
a{color:var(--ink);text-underline-offset:4px}a:hover{color:var(--gold)}.timeline{display:grid;gap:12px}.stage{display:grid;grid-template-columns:165px 1fr;gap:22px;background:#fffdf8;border:1px solid var(--line);padding:18px 22px;border-radius:10px;text-decoration:none}.date,.meta{color:var(--muted);font-size:13px}.pill{display:inline-block;border:1px solid #c8b574;padding:2px 9px;border-radius:20px;font-size:12px;margin-bottom:12px}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.card{margin:0;background:white;border:1px solid var(--line);border-radius:8px;overflow:hidden}.card img{width:100%;height:300px;object-fit:contain;background:white;display:block}.card figcaption{padding:14px;font-size:13px;overflow-wrap:anywhere}.details{font:14px/1.7 ui-monospace,monospace;white-space:pre-wrap;overflow-wrap:anywhere;background:#fffdf8;padding:24px;border:1px solid var(--line);border-radius:10px}.files{display:grid;gap:8px}.note{border-left:3px solid #b19952;padding:10px 16px;background:#ece7d9}.bar{display:flex;gap:18px;flex-wrap:wrap;margin:16px 0}.search{width:100%;padding:13px;border:1px solid var(--line);border-radius:7px;font:inherit;background:white;margin-bottom:18px}
@media(max-width:720px){main{padding:26px 16px}.stage{grid-template-columns:1fr;gap:5px}.grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.card img{height:210px}.card figcaption{padding:10px}}
@media(max-width:440px){.grid{grid-template-columns:1fr}.card img{height:330px}}
'''

def esc(s):
    return html.escape(str(s), quote=True)

def page(title, content):
    return '<!doctype html><html lang="pl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + esc(title) + '</title><style>' + STYLE + '</style><main>' + content + '</main></html>'

def export_snapshot(ref, target):
    result = subprocess.run(['git', '-C', str(ROOT), 'archive', '--format=zip', ref], check=True, stdout=subprocess.PIPE)
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(result.stdout)) as zf:
        for member in zf.infolist():
            if member.is_dir():
                continue
            dest = (target / member.filename).resolve()
            if not dest.is_relative_to(target.resolve()):
                raise ValueError('Nieprawidłowa ścieżka w archiwum Gita')
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(zf.read(member))

def gallery(records, directory, current=False):
    cards = []
    for record in records:
        rel = record.get('path') or 'materialy/' + record['filename']
        if not (directory / rel).is_file():
            raise FileNotFoundError(rel)
        source = record.get('sources', [{}])[0]
        title = record.get('title', record['filename'])
        status = record.get('status', 'propozycja / materiał historyczny')
        detail = (source.get('created_at') or '')[:19].replace('T', ' ') + ' UTC'
        labels = ' '.join(str(x) for x in [title, status, source.get('name'), source.get('member'), record.get('category')])
        cards.append('<figure class="card" data-search="' + esc(labels.lower()) + '"><a href="' + esc(rel) + '"><img loading="lazy" src="' + esc(rel) + '" alt="' + esc(title) + '"></a><figcaption><strong>' + esc(title) + '</strong><br>' + esc(status) + '<br><span class="meta">' + esc(detail) + '</span></figcaption></figure>')
    return '<input class="search" type="search" aria-label="Szukaj obrazów" placeholder="Szukaj: Orbit, Instagram, pierścień..."><div class="grid">' + ''.join(cards) + '</div><script>document.querySelector(".search").addEventListener("input",e=>{const q=e.target.value.toLowerCase();document.querySelectorAll("[data-search]").forEach(x=>x.hidden=!x.dataset.search.includes(q))});</script>'

def stage_page(stage, directory, current=False):
    manifest_file = directory / ('meta/stan-aktualny.json' if current else 'manifest.json')
    manifest = json.loads(manifest_file.read_text())
    body = (directory / ('AKTUALNE.md' if current else 'STAN.md')).read_text()
    content = '<header><div class="eyebrow">Love Token / YOSE - archiwum</div><h1>' + esc(stage['title']) + '</h1><div class="date">' + esc(stage['date']) + '</div><div class="bar"><a href="../index.html">Wszystkie etapy</a><a href="' + ('AKTUALNE.md' if current else 'STAN.md') + '">Podsumowanie jako plik</a></div></header>'
    content += '<div class="pill">' + ('Bieżący potwierdzony stan' if current else 'Historyczny etap - czytaj statusy w podsumowaniu') + '</div>'
    content += '<h2>Co było ustalone</h2><div class="details">' + esc(body) + '</div>'
    documents = manifest.get('documents', [])
    if documents:
        content += '<h2>Dokumenty źródłowe</h2><div class="files">' + ''.join('<a href="dokumenty/' + esc(d['filename']) + '">' + esc(d['title']) + '</a>' for d in documents) + '</div>'
    if (directory / 'kod_sklepu').is_dir():
        content += '<h2>Historyczny kod sklepu</h2><p>Tekstowe źródła są w folderze <code>kod_sklepu/</code>. Manifest opisuje pierwotne ścieżki skompresowanych obrazów.</p>'
    content += '<h2>Obrazy i rendery (' + str(len(manifest['assets'])) + ')</h2>' + gallery(manifest['assets'], directory, current)
    (directory / 'index.html').write_text(page(stage['title'], content))

def main():
    parser = argparse.ArgumentParser(description='Wyeksportuj podgląd historii bez zmiany bieżącej gałęzi.')
    parser.add_argument('--output', default='podglad', help='Folder wyniku, domyślnie podglad/')
    args = parser.parse_args()
    out = (ROOT / args.output).resolve()
    if out == ROOT or not out.is_relative_to(ROOT):
        parser.error('Folder podglądu musi być podfolderem repozytorium.')
    out.mkdir(parents=True, exist_ok=True)
    history = json.loads((ROOT / 'meta/historia.json').read_text())
    stages = history['stages']
    for stage in stages:
        if not re.fullmatch(r'etap-[a-zA-Z0-9-]+|stan-aktualny', stage['tag']):
            raise ValueError('Nieprawidłowy tag')
        dest = out / stage['tag']
        export_snapshot(stage['tag'], dest)
        stage_page(stage, dest, stage['tag'] == 'stan-aktualny')
    links = []
    for stage in reversed(stages):
        links.append('<a class="stage" href="' + esc(stage['tag']) + '/index.html"><div class="date">' + esc(stage['date']) + '<br>' + str(stage['asset_count']) + ' obrazów</div><div><h3>' + esc(stage['title']) + '</h3><span class="meta">' + esc(stage['tag']) + '</span></div></a>')
    content = '<header><div class="eyebrow">Love Token / YOSE</div><h1>Historia pomysłu i designu</h1><p>Od symbolu relacji, przez Fibula i Taken Token, do obecnej kolekcji Love Token. Datowane podsumowania, renderingi, Instagram i dokumenty.</p><div class="pill">' + str(len(stages)) + ' etapów / ' + str(history['historical_asset_count']) + ' odzyskanych obrazów</div></header><p class="note">Historia została odtworzona 3 października 2026. To podsumowanie odzyskanych materiałów, nie pełny zapis rozmów. Status propozycji, badań i odrzuceń opisano w każdym etapie. Pierwsza pozycja pokazuje wyłącznie ostatni potwierdzony stan.</p><div class="timeline">' + ''.join(links) + '</div>'
    (out / 'index.html').write_text(page('Love Token - historia projektu', content))
    print(out / 'index.html')
    print(f'Wyeksportowano {len(stages)} etapów. Historia Gita i bieżąca gałąź pozostają bez zmian.')

if __name__ == '__main__':
    main()
