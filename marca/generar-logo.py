import math, os, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

OUT = sys.argv[1]
NAVY = '#0B2A5B'; ACCENT = '#1F7AE0'
_cache = {}
def font(path, wght):
    k = (path, wght)
    if k not in _cache:
        f = TTFont(path); _cache[k] = instantiateVariableFont(f, {'wght': wght}, inplace=False)
    return _cache[k]

def text_path(txt, path, wght, size, tracking=0.0):
    """Devuelve (d, ancho, alto_mayúscula) del texto convertido a trazado, origen en la línea base."""
    f = font(path, wght); gs = f.getGlyphSet(); cmap = f.getBestCmap()
    upm = f['head'].unitsPerEm; s = size / upm
    pen = SVGPathPen(gs); x = 0
    for ch in txt:
        if ch == ' ':
            x += f['hmtx'][cmap[32]][0] + tracking * upm; continue
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (s, 0, 0, -s, x * s, 0))
        gs[g].draw(tp)
        x += f['hmtx'][g][0] + tracking * upm
    x -= tracking * upm
    cap = f['OS/2'].sCapHeight * s
    return pen.getCommands(), x * s, cap

def icon(color=NAVY, accent=ACCENT):
    """Símbolo: libro abierto + 5 pistas de circuito. Caja 0..200 x 0..150."""
    sw = 7  # grosor de las pistas
    r = 7.5  # radio de los nodos
    parts = []
    # Páginas (dos capas por lado), simétricas respecto a x=100
    def side(sign):
        X = lambda x: 100 + sign * (x - 100)
        page = f"M{X(100)},126 C{X(84)},106 {X(56)},90 {X(18)},86 L{X(14)},104 C{X(50)},106 {X(80)},116 {X(100)},134 Z"
        cover = f"M{X(100)},140 C{X(80)},124 {X(48)},114 {X(6)},116 L{X(2)},130 C{X(44)},128 {X(76)},134 {X(100)},148 Z"
        return page, cover
    for sgn in (-1, 1):
        p, c = side(sgn)
        parts.append(f'<path d="{p}" fill="{color}"/>')
        parts.append(f'<path d="{c}" fill="{color}"/>')
    # Pistas: centro + dos por lado
    tr = []
    tr.append(((100, 112), [(100, 34)], (100, 24)))
    for sgn in (-1, 1):
        X = lambda x: 100 + sgn * (x - 100)
        tr.append(((X(88), 106), [(X(88), 66), (X(66), 44)], (X(59), 37)))
        tr.append(((X(76), 100), [(X(76), 84), (X(46), 64)], (X(38), 59)))
    for start, pts, node in tr:
        pl = [start] + pts
        # acortar el último tramo para que la pista toque el anillo del nodo
        (x1, y1), (x2, y2) = pl[-1], node
        d = math.hypot(x2 - x1, y2 - y1)
        k = (d - r) / d if d else 0
        pl[-1] = (x1 + (x2 - x1) * k, y1 + (y2 - y1) * k) if d > r else pl[-1]
        pts_s = ' '.join(f'{x:.2f},{y:.2f}' for x, y in pl)
        parts.append(f'<polyline points="{pts_s}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="butt"/>')
    for i, (start, pts, node) in enumerate(tr):
        c = accent if i == 0 else color
        parts.append(f'<circle cx="{node[0]}" cy="{node[1]}" r="{r}" fill="none" stroke="{c}" stroke-width="{sw-1}"/>')
    return '\n'.join(parts)

FW = '/tmp/claude-0/fonts/Outfit.ttf'
def wordmark(color=NAVY, size=100):
    return text_path('DIDACTEK', FW, 700, size, tracking=0.02)

def svg(w, h, body, bg=None, title='Didactek'):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-label="{title}"><title>{title}</title>{b}{body}</svg>\n'

def logo_vertical(color=NAVY, accent=ACCENT, sub=True, bg=None):
    d, ww, cap = wordmark(size=120)
    W = max(ww, 600) + 80
    ic_scale = 1.55; icw = 200 * ic_scale
    body = f'<g transform="translate({(W-icw)/2:.1f},20) scale({ic_scale})">{icon(color, accent)}</g>'
    y = 20 + 150 * ic_scale + 40 + cap
    body += f'<path transform="translate({(W-ww)/2:.1f},{y:.1f})" d="{d}" fill="{color}"/>'
    H = y + 30
    if sub:
        t1, w1, c1 = text_path('MAQUETAS DIDÁCTICAS DE AUTOMATIZACIÓN', FW, 500, 25, tracking=0.16)
        y2 = y + 34 + c1
        body += f'<path transform="translate({(W-w1)/2:.1f},{y2:.1f})" d="{t1}" fill="{color}"/>'
        H = y2 + 30
    return svg(W, H, body, bg)

def logo_horizontal(color=NAVY, accent=ACCENT, sub=True, bg=None):
    d, ww, cap = wordmark(size=110)
    ic_scale = 1.15; icw, ich = 200 * ic_scale, 150 * ic_scale
    pad = 20; gap = 36
    tx = pad + icw + gap
    W = tx + ww + pad
    H = ich + 2 * pad
    if sub:
        t1, w1, c1 = text_path('MAQUETAS DIDÁCTICAS DE AUTOMATIZACIÓN', FW, 500, 21.5, tracking=0.12)
        sc = min(1, ww / w1)
        block = cap + 26 + c1
        y = pad + (ich - block) / 2 + cap
        body = f'<path transform="translate({tx:.1f},{y:.1f})" d="{d}" fill="{color}"/>'
        y2 = y + 26 + c1
        body += f'<path transform="translate({tx:.1f},{y2:.1f}) scale({sc:.4f})" d="{t1}" fill="{color}"/>'
    else:
        y = pad + (ich + cap) / 2
        body = f'<path transform="translate({tx:.1f},{y:.1f})" d="{d}" fill="{color}"/>'
    body = f'<g transform="translate({pad},{pad}) scale({ic_scale})">{icon(color, accent)}</g>' + body
    return svg(W, H, body, bg)

def logo_icon(color=NAVY, accent=ACCENT, bg=None, pad=20):
    W = 200 + 2 * pad; H = 150 + 2 * pad
    return svg(W, H, f'<g transform="translate({pad},{pad})">{icon(color, accent)}</g>', bg)

def icon_simple(color, accent):
    """Versión simplificada para tamaños pequeños: libro + 3 pistas."""
    parts=[]
    for sgn in (-1,1):
        X=lambda x:100+sgn*(x-100)
        parts.append(f'<path d="M{X(100)},118 C{X(80)},98 {X(50)},86 {X(10)},84 L{X(6)},110 C{X(46)},110 {X(78)},120 {X(100)},140 Z" fill="{color}"/>')
    sw=13; r=12
    parts.append(f'<line x1="100" y1="104" x2="100" y2="{30+r}" stroke="{color}" stroke-width="{sw}"/>')
    parts.append(f'<circle cx="100" cy="30" r="{r}" fill="none" stroke="{accent}" stroke-width="{sw-2}"/>')
    for sgn in (-1,1):
        X=lambda x:100+sgn*(x-100)
        parts.append(f'<polyline points="{X(76)},94 {X(76)},74 {X(56)},58" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>')
        parts.append(f'<circle cx="{X(46)}" cy="50" r="{r}" fill="none" stroke="{color}" stroke-width="{sw-2}"/>')
    return '\n'.join(parts)

def favicon():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="%s"/>'
            '<g transform="translate(6,9) scale(0.26)">%s</g></svg>\n') % (NAVY, icon_simple('#ffffff', '#7CC4FF'))

os.makedirs(OUT, exist_ok=True)
files = {
 'didactek-vertical.svg': logo_vertical(),
 'didactek-horizontal.svg': logo_horizontal(),
 'didactek-horizontal-sin-lema.svg': logo_horizontal(sub=False),
 'didactek-horizontal-blanco.svg': logo_horizontal('#ffffff', '#7CC4FF'),
 'didactek-vertical-blanco.svg': logo_vertical('#ffffff', '#7CC4FF'),
 'didactek-horizontal-sin-lema-blanco.svg': logo_horizontal('#ffffff', '#7CC4FF', sub=False),
 'didactek-simbolo.svg': logo_icon(),
 'favicon.svg': favicon(),
}
for n, s in files.items(): open(os.path.join(OUT, n), 'w').write(s)
print('ok', list(files))
