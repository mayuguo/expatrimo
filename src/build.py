"""Build the expatrimo.com static site.

Articles live in content/actualites/*.md (edited by hand or through /admin).
Static files (images, CSS, JS, the /admin editor) live in static/ and are copied as-is.
Fixed pages live in src/pages.py.

Usage:  python3 src/build.py            -> public/ (production URLs)
        python3 src/build.py preview DIR -> DIR with relative links (works from any sub-path)
No third-party packages needed (Python 3.8+).
"""
import html, json, os, re, shutil, sys, unicodedata
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pages import PAGES, CONTACT_EMAIL

MODE = sys.argv[1] if len(sys.argv) > 1 else 'prod'
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'public')
SITE = 'https://expatrimo.com'
CONTENT = os.path.join(ROOT, 'content', 'actualites')
STATIC = os.path.join(ROOT, 'static')

# Old URLs of removed articles -> where they now point
REDIRECTS = {
    '/actualites/interview-de-vincent-leroy-dans-gestion-de-fortune/': '/actualites/',
    '/actualites/temoignage-de-hugues-martin-dans-connexions/': '/actualites/',
}

def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

# ---------- link helpers ----------
CUR = ['/']
def L(path):
    """Link from the current page to a site path (may carry ?query or #hash)."""
    m = re.match(r'([^?#]*)(.*)', path); p, q = m.group(1), m.group(2)
    if MODE != 'preview' or not p.startswith('/'):
        return p + q
    depth = len([x for x in CUR[0].strip('/').split('/') if x and not x.endswith('.html')])
    tgt = p.lstrip('/') + ('index.html' if p.endswith('/') else '')
    return ('../' * depth + tgt or './index.html') + q
I = L

MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
def fdate(d): return f"{d.day} {MONTHS[d.month-1]} {d.year}"

# ---------- reading articles ----------
def parse_front_matter(text):
    m = re.match(r'---\s*\n(.*?)\n---\s*\n?(.*)', text, re.S)
    if not m:
        return {}, text
    meta, key, block = {}, None, None
    for line in m.group(1).split('\n'):
        if block is not None:  # YAML block scalar (| or >), e.g. a multi-line summary
            if line.startswith((' ', '\t')) or not line.strip():
                block.append(line.strip()); continue
            meta[key] = (' ' if fold else '\n').join(block).strip(); block = None
        if not line.strip():
            continue
        li = re.match(r'\s+-\s+(.*)', line)
        if li and key:
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(unquote(li.group(1)))
            continue
        kv = re.match(r'([A-Za-z_]+):\s*(.*)', line)
        if kv:
            key = kv.group(1); v = kv.group(2).strip()
            if v[:1] in ('|', '>'):
                block, fold = [], v[0] == '>'; continue
            meta[key] = unquote(v) if v else []
    if block is not None:
        meta[key] = (' ' if fold else '\n').join(block).strip()
    return meta, m.group(2)

def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        v = v[1:-1].replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
    return v

def to_date(v):
    v = str(v)[:10]
    y, m, d = v.split('-')
    return date(int(y), int(m), int(d))

articles = []
for fn in sorted(os.listdir(CONTENT)):
    if not fn.endswith('.md'):
        continue
    meta, body = parse_front_matter(open(os.path.join(CONTENT, fn), encoding='utf-8').read())
    if str(meta.get('draft', '')).lower() == 'true':
        continue
    slug = fn[:-3]
    cats = meta.get('categories') or ['Actualités']
    if isinstance(cats, str):
        cats = [cats]
    a = dict(slug=slug, url=f'/actualites/{slug}/', title=meta.get('title') or slug,
             d=to_date(meta.get('date') or date.today().isoformat()), cats=cats,
             image=meta.get('image') or None, description=meta.get('description') or '', body=body)
    if meta.get('updated'):
        a['updated'] = to_date(meta['updated'])
    articles.append(a)
articles.sort(key=lambda a: a['d'], reverse=True)
ALL_CATS = {}
for a in articles:
    for c in a['cats']:
        ALL_CATS[c] = ALL_CATS.get(c, 0) + 1

def norm(s):
    return re.sub(r'\s+', ' ', s).strip().lower()

# ---------- minimal Markdown ----------
def inline(text):
    """Escape text and render links, images, **bold**, *italic*, bare URLs."""
    out, pos = [], 0
    pat = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)\)|\[([^\]]+)\]\(([^)\s]+)\)|(https?://[^\s)<»]+)|\*\*(.+?)\*\*|(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])')
    for m in pat.finditer(text):
        out.append(html.escape(text[pos:m.start()], quote=False))
        if m.group(2):
            out.append(f'<img src="{html.escape(L(m.group(2)))}" alt="{html.escape(m.group(1))}" loading="lazy">')
        elif m.group(4):
            u = m.group(4); ext = '' if u.startswith('/') else ' rel="noopener"'
            out.append(f'<a href="{html.escape(L(u))}"{ext}>{inline(m.group(3))}</a>')
        elif m.group(5):
            u = m.group(5).rstrip('.,;'); tail = m.group(5)[len(u):]
            out.append(f'<a href="{html.escape(u)}" rel="noopener">{html.escape(u)}</a>{tail}')
        elif m.group(6):
            out.append(f'<strong>{inline(m.group(6))}</strong>')
        else:
            out.append(f'<em>{inline(m.group(7))}</em>')
        pos = m.end()
    out.append(html.escape(text[pos:], quote=False))
    return ''.join(out)

def markdown(md):
    md = md.replace('\r\n', '\n')
    blocks = re.split(r'\n\s*\n', md.strip())
    out = []
    for b in blocks:
        lines = [l.rstrip() for l in b.split('\n') if l.strip()]
        if not lines:
            continue
        first = lines[0]
        h = re.match(r'(#{1,4})\s+(.*)', first)
        if h and len(lines) == 1:
            lvl = max(2, len(h.group(1)))
            out.append(f'<h{lvl}>{inline(h.group(2).strip())}</h{lvl}>'); continue
        im = re.fullmatch(r'!\[([^\]]*)\]\(([^)\s]+)\)', first.strip())
        if im and len(lines) == 1:
            alt = html.escape(im.group(1))
            cap = f'<figcaption>{alt}</figcaption>' if im.group(1) else ''
            out.append(f'<figure><img src="{html.escape(L(im.group(2)))}" alt="{alt}" loading="lazy">{cap}</figure>'); continue
        if all(re.match(r'\s*[-*+]\s+', l) for l in lines):
            out.append('<ul>' + ''.join('<li>' + inline(re.sub(r'^\s*[-*+]\s+', '', l)) + '</li>' for l in lines) + '</ul>'); continue
        if all(re.match(r'\s*\d+[.)]\s+', l) for l in lines):
            out.append('<ol>' + ''.join('<li>' + inline(re.sub(r'^\s*\d+[.)]\s+', '', l)) + '</li>' for l in lines) + '</ol>'); continue
        if all(l.startswith('>') for l in lines):
            out.append('<blockquote><p>' + inline(' '.join(l.lstrip('> ') for l in lines)) + '</p></blockquote>'); continue
        if h:  # heading followed by text without blank line
            lvl = max(2, len(h.group(1)))
            out.append(f'<h{lvl}>{inline(h.group(2).strip())}</h{lvl}>'); lines = lines[1:]
        out.append('<p>' + '<br>'.join(inline(l.rstrip('\\').strip()) for l in lines) + '</p>')
    return '\n'.join(out)

def plain(md):
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    t = re.sub(r'[#*>`]', '', t)
    return re.sub(r'\s+', ' ', t).strip()

def excerpt(a, n=170):
    if a['description']:
        t = a['description']
    else:
        paras = [p for p in re.split(r'\n\s*\n', a['body']) if p.strip() and not p.lstrip().startswith(('#', '!', '-', '*'))]
        t = plain(next((p for p in paras if len(plain(p)) > 80), paras[0] if paras else ''))
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'

def card(a):
    img = f'<div class="thumb"><img src="{L(a["image"])}" alt="" loading="lazy"></div>' if a['image'] else ''
    cats = ' · '.join(html.escape(c) for c in a['cats'][:2])
    return (f'<a class="card" href="{L(a["url"])}" data-cats="{"|".join(slugify(c) for c in a["cats"])}" '
            f'data-text="{html.escape(norm(a["title"] + " " + excerpt(a, 400)))}">{img}'
            f'<div class="card-body"><p class="meta">{cats} · <time datetime="{a["d"].isoformat()}">{fdate(a["d"])}</time></p>'
            f'<h3>{html.escape(a["title"])}</h3><p>{html.escape(excerpt(a))}</p></div></a>')

def grid(items):
    return '<div class="cards grid">' + ''.join(card(a) for a in items) + '</div>'

def cta():
    return f'''<aside class="cta"><div class="wrap cta-inner">
<div><h2>Besoin d'un conseil adapté à votre situation&nbsp;?</h2>
<p>Expatrimo publie une information générale et ne fournit pas de conseil personnalisé. Nous pouvons vous orienter vers un partenaire, basé en France ou à l'étranger, qui pourra vous conseiller et mettre en place des solutions d'investissement.</p></div>
<a class="btn light" href="{L('/contact/')}">Être mis en relation</a></div></aside>'''

# ---------- layout ----------
GA_ID = 'G-R2RDVRD7B9'  # Google Analytics 4
GA = '' if MODE == 'preview' else f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
"""
CSS_V = '5'
def layout(path, title, desc, body, lang='fr', og_image=None, extra_head=''):
    CUR[0] = path
    nav = [('/actualites/', 'Actualités'), ('/prestations/investissement-immobilier/', 'Immobilier'),
           ('/prestations/epargne-et-finance/', 'Épargne & Finance'), ('/prestations/conseil-patrimonial/', 'Patrimoine'),
           ('/a-propos/', 'À propos')]
    def cur(p): return ' aria-current="page"' if path == p else ''
    navh = ''.join(f'<a href="{L(p)}"{cur(p)}>{t}</a>' for p, t in nav)
    canon = SITE + path
    ogi = f'<meta property="og:image" content="{SITE}{og_image}">' if og_image else ''
    year = date.today().year
    body_html = body
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{GA}<title>{html.escape(title)} | Expatrimo</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="Expatrimo">
{ogi}
<link rel="icon" href="{L('/assets/favicon.png')}">
<link rel="stylesheet" href="{L('/assets/style.css')}?v={CSS_V}">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Aller au contenu</a>
<header class="site-header"><div class="wrap bar">
<a class="logo" href="{L('/')}" aria-label="Expatrimo, accueil"><img src="{L('/assets/expatrimo-logo.png')}" alt="Expatrimo" width="56" height="56"><span><b>EXPATRIMO</b><small>Expatriation &amp; Patrimoine</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav">{navh}<a class="nav-cta" href="{L('/contact/')}">Mise en relation</a></nav>
</div></header>
<main id="main">
{body_html}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><p class="foot-brand">EXPATRIMO</p><p>L'investissement pour les Français en Asie, depuis 2012.</p></div>
<div><p class="foot-h">Thématiques</p><a href="{L('/prestations/investissement-immobilier/')}">Investissement immobilier</a><a href="{L('/prestations/epargne-et-finance/')}">Épargne et finance</a><a href="{L('/prestations/conseil-patrimonial/')}">Stratégie patrimoniale</a><a href="{L('/projets/')}">Projets immobiliers</a></div>
<div><p class="foot-h">Expatrimo</p><a href="{L('/actualites/')}">Actualités</a><a href="{L('/a-propos/')}">À propos</a><a href="{L('/documents/')}">Documents</a><a href="{L('/contact/')}">Mise en relation</a><a href="{L('/expatrimo-en/')}">English</a><a href="{L('/expatrimo-cn/')}">中文</a></div>
</div>
<p class="disclaimer">Les informations publiées sur ce site ont un caractère général et ne constituent pas un conseil en investissement personnalisé. Expatrimo ne commercialise aucun produit et peut orienter ses lecteurs vers des partenaires tiers, en France ou à l'étranger, qui agissent sous leur propre responsabilité. <a href="{L('/mentions-legales/')}">Mentions légales</a></p>
<p class="copy">© 2012–{year} expatrimo.com</p>
</div></footer>
<script src="{L('/assets/site.js')}?v={CSS_V}" defer></script>
</body>
</html>
'''


def write(path, content):
    fp = os.path.join(OUT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(OUT, path.strip('/'))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w', encoding='utf-8').write(content)

def related(a, n=3):
    scored = [(len(set(a['cats']) & set(b['cats'])), b['d'], b) for b in articles if b is not a]
    scored = [x for x in scored if x[0]]
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return [b for _, _, b in scored[:n]] or [b for b in articles if b is not a][:n]

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
# ---------- static files ----------
shutil.copytree(STATIC, OUT)

# ---------- article pages ----------
for a in articles:
    CUR[0] = a['url']
    hero_html = f'<figure class="art-hero"><img src="{L(a["image"])}" alt="" loading="eager"></figure>' if a['image'] else ''
    cats = ', '.join(f'<a href="{L("/actualites/")}?cat={slugify(c)}">{html.escape(c)}</a>' for c in a['cats'])
    upd = f' · mis à jour le {fdate(a["updated"])}' if a.get('updated') and a['updated'] > a['d'] else ''
    body = f'''<article class="article">
<header class="wrap narrow art-head"><p class="meta">{cats}</p><h1>{html.escape(a['title'])}</h1>
<p class="meta"><time datetime="{a['d'].isoformat()}">{fdate(a['d'])}</time>{upd}</p></header>
<div class="wrap narrow">{hero_html}
<div class="prose">
{markdown(a['body'])}
</div>
<p class="art-note">Cet article présente une information générale à la date de sa publication. Il ne constitue pas un conseil en investissement personnalisé.</p>
</div></article>
{cta()}
<section class="wrap"><div class="section-head"><h2>Dans la même thématique</h2><a href="{L('/actualites/')}">Tous les articles →</a></div>{grid(related(a))}</section>'''
    ld = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": a['title'],
                     "datePublished": a['d'].isoformat(), "publisher": {"@type": "Organization", "name": "Expatrimo"},
                     "mainEntityOfPage": SITE + a['url']}, ensure_ascii=False)
    write(a['url'], layout(a['url'], a['title'], excerpt(a, 155), body, og_image=a['image'],
                           extra_head=f'<script type="application/ld+json">{ld}</script>'))

# ---------- blog index ----------
CUR[0] = '/actualites/'
cat_btns = '<button class="chip" data-cat="" aria-pressed="true">Tous les articles</button>' + ''.join(
    f'<button class="chip" data-cat="{slugify(c)}" aria-pressed="false">{html.escape(c)} ({n})</button>'
    for c, n in sorted(ALL_CATS.items(), key=lambda x: -x[1]))
blog = f'''<header class="page-head wrap"><h1>Actualités</h1><p class="lead">Tous nos articles sur l'investissement et le patrimoine des Français d'Asie, depuis 2012.</p></header>
<section class="wrap">
<div class="filters"><input type="search" id="q" placeholder="Rechercher un article…" aria-label="Rechercher"><div class="chips">{cat_btns}</div></div>
<p id="count" class="small"></p>
<div id="list">{grid(articles)}</div>
</section>{cta()}'''
write('/actualites/', layout('/actualites/', 'Actualités', "Tous les articles d'Expatrimo sur l'investissement immobilier et financier pour les Français expatriés en Asie.", blog))

# ---------- fixed pages ----------
def expand(body):
    body = re.sub(r'\{L:([^}]+)\}', lambda m: L(m.group(1)), body)
    body = re.sub(r'\{I:([^}]+)\}', lambda m: I(m.group(1)), body)
    body = body.replace('{CTA}', cta()).replace('{EMAIL}', CONTACT_EMAIL)
    body = re.sub(r'\{LATEST:(\d+)\}', lambda m: grid(articles[:int(m.group(1))]), body)
    body = re.sub(r'\{CAT:([^:}]+):(\d+)\}', lambda m: grid([a for a in articles if m.group(1) in a['cats']][:int(m.group(2))]), body)
    return body

for path, p in PAGES.items():
    CUR[0] = path
    write(path, layout(path, p['title'], p['desc'], expand(p['body']), lang=p.get('lang', 'fr'),
                       og_image='/wp-content/uploads/EXPATRIMO-CHINE-ASIE-BLOG.jpg'))

# ---------- redirects for removed articles ----------
for old, new in REDIRECTS.items():
    CUR[0] = old
    tgt = L(new)
    write(old, f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Expatrimo</title>'
               f'<meta name="robots" content="noindex"><link rel="canonical" href="{SITE}{new}">'
               f'<meta http-equiv="refresh" content="0; url={tgt}">{GA}</head><body><p><a href="{tgt}">Voir les actualités</a></p></body></html>')

# ---------- 404 ----------
CUR[0] = '/404.html'
write('/404.html', layout('/404.html', 'Page introuvable', 'Page introuvable',
      f'<header class="page-head wrap"><h1>Page introuvable</h1><p class="lead">Cette page n\'existe pas ou plus. Retrouvez nos derniers articles ci-dessous.</p></header><section class="wrap">{grid(articles[:6])}</section>'))

# ---------- sitemap, robots, redirects ----------
urls = ['/'] + [p for p in PAGES if p != '/'] + ['/actualites/'] + [a['url'] for a in articles]
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'<url><loc>{SITE}{u}</loc></url>\n' for u in urls) + '</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nDisallow: /admin/\nSitemap: {SITE}/sitemap.xml\n')
if MODE != 'preview':
    red = ''.join(f'{o} {n} 301\n' for o, n in REDIRECTS.items())
    red += '/actualites/page/* /actualites/ 301\n/category/* /actualites/ 301\n/feed/* /actualites/ 301\n/projet/* /projets/ 301\n'
    open(os.path.join(OUT, '_redirects'), 'w').write(red)
    ht = 'ErrorDocument 404 /404.html\nRewriteEngine On\n' + ''.join(
        f'RewriteRule ^{o.strip("/")}/?$ {n} [R=301,L]\n' for o, n in REDIRECTS.items()) + \
        'RewriteRule ^actualites/page/ /actualites/ [R=301,L]\nRewriteRule ^category/ /actualites/ [R=301,L]\nRewriteRule ^projet/ /projets/ [R=301,L]\n'
    open(os.path.join(OUT, '.htaccess'), 'w').write(ht)
else:
    shutil.rmtree(os.path.join(OUT, 'admin'), ignore_errors=True)

print(f'{len(articles)} articles, {len(PAGES)} pages -> {OUT} ({MODE})')
