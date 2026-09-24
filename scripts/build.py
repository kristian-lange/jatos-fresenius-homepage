#!/usr/bin/env python3
"""Build the self-contained JATOS fragment and an offline preview (Python 3)."""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'home.template.html').read_text()
logo = base64.b64encode((ROOT / 'assets/charlotte-fresenius-logo.svg').read_bytes()).decode()
fragment = source.replace('LOGO_DATA_URI', 'data:image/svg+xml;base64,' + logo)
(ROOT / 'fresenius-welcome.html').write_text(fragment)
preview = fragment.replace('@USER_NAME', 'Alex Morgan').replace('@JATOS_VERSION', '3.11.3')
(ROOT / 'preview.html').write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preview · JATOS at Charlotte Fresenius University</title>
<style>body{margin:0;background:#edf0f3;font-family:Arial,sans-serif}.preview-note{padding:14px 24px;background:#fff;color:#545965;border-bottom:1px solid #dde0e5;font-size:13px}.preview-stage{max-width:1120px;margin:40px auto;padding:0 24px 40px}#branding{padding:48px;text-align:center;border-radius:8px}@media(max-width:600px){.preview-stage{padding:0 12px;margin:16px auto}}</style>
</head><body><div class="preview-note">Design preview · The name and version shown here are sample data.</div>
<main class="preview-stage"><div id="branding">''' + preview + '</div></main></body></html>\n')
print('Built fresenius-welcome.html and preview.html')
