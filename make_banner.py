# Generates banner.svg: name and focus on the left, a field of soft Gaussian splats on the right
# whose opacity ripples outward in an 8-second loop.
import math, numpy as np
W, H = 900, 240
rng = np.random.RandomState(3)
cols = ['#38bdf8', '#818cf8', '#22d3ee', '#a78bfa', '#60a5fa']
X0, X1, Y0, Y1 = 520, 870, 22, 218; cx, cy = (X0+X1)/2, (Y0+Y1)/2
splats = []
for k in range(150):
    x, y = rng.uniform(X0, X1), rng.uniform(Y0, Y1)
    rx, ry = rng.uniform(6, 22), rng.uniform(4, 13); ang = rng.uniform(0, 180)
    d = math.hypot(x-cx, (y-cy)*1.6)/180; begin = -8*d                      # ripple: phase grows with distance from the centre
    f = min(1., max(0., (x-X0)/90))**1.5                                  # fade in from the left edge of the field
    lo, hi = f*rng.uniform(.08, .2), f*rng.uniform(.55, .9)
    splats.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" transform="rotate({ang:.0f} {x:.1f} {y:.1f})" fill="url(#g{k % len(cols)})" opacity="{lo:.2f}">'
                  f'<animate attributeName="opacity" values="{lo:.2f};{hi:.2f};{lo:.2f}" dur="8s" begin="{begin:.2f}s" repeatCount="indefinite"/></ellipse>')
grads = ''.join(f'<radialGradient id="g{i}"><stop offset="0" stop-color="{c}" stop-opacity="1"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>' for i, c in enumerate(cols))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Aryan Achary: 3D computer vision and Gaussian splatting">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1020"/><stop offset="1" stop-color="#131a33"/></linearGradient>
  {grads}
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0b1020" stop-opacity="1"/><stop offset="1" stop-color="#0b1020" stop-opacity="0"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
<g>{''.join(splats)}</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="none" stroke="#24304f"/>
<g font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif">
  <text x="44" y="108" font-size="40" font-weight="700" fill="#e6edf3">Aryan Achary</text>
  <text x="44" y="142" font-size="17" fill="#8fa3c0">3D computer vision · Gaussian splatting</text>
  <text x="44" y="168" font-size="15" fill="#5d6f8f">CSE @ MIT Manipal</text>
</g>
</svg>'''
open('banner.svg', 'w').write(svg); print(len(svg), 'bytes')
