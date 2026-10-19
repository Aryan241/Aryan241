# Generates banner.svg: an 8-second loop of the redaction pilot.
# 1) a 16x16 random bit pattern on a sheet (secret 8 from the pilot), 2) "redacted": the sheet goes blank,
# 3) an x-ray sweep shows Gaussian centres, still denser on the old ink cells (the layout residue).
import numpy as np
r = np.random.RandomState(8); b = np.zeros(256, int); b[r.choice(256, 128, replace=False)] = 1; bits = b.reshape(16, 16)
W, H, SX, SY, S = 900, 260, 640, 24, 196; c = S/16
rng = np.random.RandomState(1)
ink = ''.join(f'<rect x="{SX+j*c:.1f}" y="{SY+i*c:.1f}" width="{c+.2:.1f}" height="{c+.2:.1f}"/>' for i in range(16) for j in range(16) if bits[i, j])
dots = []
for i in range(16):
    for j in range(16):
        n = 7 if bits[i, j] else int(rng.rand() < .25)
        for _ in range(n):
            x, y = SX+(j+rng.uniform(.15, .85))*c, SY+(i+rng.uniform(.15, .85))*c
            dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rng.uniform(.9, 1.4):.2f}"/>')
A = 'dur="8s" repeatCount="indefinite"'
def fade(vals, keys): return f'<animate attributeName="opacity" values="{vals}" keyTimes="{keys}" {A}/>'
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Aryan Achary: what a 3D scene file remembers after the picture has forgotten">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1020"/><stop offset="1" stop-color="#131a33"/></linearGradient>
  <clipPath id="sweep"><rect x="{SX}" y="{SY}" width="0" height="{S}"><animate attributeName="width" values="0;0;{S};{S};0" keyTimes="0;0.6;0.84;0.97;1" {A}/></rect></clipPath>
</defs>
<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="none" stroke="#24304f"/>
<g font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif">
  <text x="40" y="78" font-size="36" font-weight="700" fill="#e6edf3">Aryan Achary</text>
  <text x="40" y="108" font-size="16" fill="#8fa3c0">3D computer vision · Gaussian splatting · MIT Manipal</text>
  <text x="40" y="150" font-size="16" fill="#c9d4e3">I study what a 3D scene file still remembers</text>
  <text x="40" y="172" font-size="16" fill="#c9d4e3">after the picture has forgotten it.</text>
</g>
<g font-family="SFMono-Regular, Menlo, Consolas, monospace" font-size="13">
  <text x="40" y="222" fill="#8fa3c0">$ secret on the sheet<tspan fill="#e6edf3">  pattern visible</tspan>{fade("1;1;0;0;1", "0;0.33;0.36;0.97;1")}</text>
  <text x="40" y="222" fill="#8fa3c0" opacity="0">$ redact, read the render<tspan fill="#facc15">  bit accuracy 0.50</tspan>{fade("0;0;1;1;0;0", "0;0.36;0.39;0.58;0.61;1")}</text>
  <text x="40" y="222" fill="#8fa3c0" opacity="0">$ read the file instead<tspan fill="#38bdf8">  bit accuracy 1.00</tspan>{fade("0;0;1;1;0", "0;0.61;0.64;0.97;1")}</text>
</g>
<rect x="{SX-8}" y="{SY-8}" width="{S+16}" height="{S+16}" rx="10" fill="#e9ecf2"/>
<g fill="#111827">{ink}{fade("1;1;0;0;1", "0;0.33;0.45;0.97;1")}</g>
<rect x="{SX-8}" y="{SY-8}" width="{S+16}" height="{S+16}" rx="10" fill="#0b1020" opacity="0">{fade("0;0;0.82;0.82;0", "0;0.58;0.64;0.97;1")}</rect>
<g fill="#38bdf8" clip-path="url(#sweep)">{''.join(dots)}</g>
<line x1="{SX}" y1="{SY-8}" x2="{SX}" y2="{SY+S+8}" stroke="#38bdf8" stroke-width="2" opacity="0">
  <animate attributeName="x1" values="{SX};{SX};{SX+S};{SX+S}" keyTimes="0;0.6;0.84;1" {A}/>
  <animate attributeName="x2" values="{SX};{SX};{SX+S};{SX+S}" keyTimes="0;0.6;0.84;1" {A}/>
  {fade("0;0;1;1;0;0", "0;0.6;0.61;0.84;0.86;1")}
</line>
<text x="{SX+S/2}" y="{SY+S+24}" text-anchor="middle" font-family="SFMono-Regular, Menlo, Consolas, monospace" font-size="11" fill="#5d6f8f">illustration of my 3DGS redaction pilot</text>
</svg>'''
open('banner.svg', 'w').write(svg); print(len(svg), 'bytes,', len(dots), 'dots')
