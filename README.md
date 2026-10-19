<p align="center">
  <img src="banner.svg" alt="Aryan Achary: what a 3D scene file still remembers after the picture has forgotten it" width="100%" />
</p>

I'm a second-year CSE student at **MIT Manipal** working on **3D computer vision**, mostly 3D Gaussian Splatting: reconstructing scenes, lifting 2D masks into them, and checking what the trained file actually keeps.

### What I'm working on

- **Does redaction really forget?** If a private detail is edited out of a 3DGS scene so that no render shows it, can it still be read from the scene file? In a synthetic pilot and on a real phone capture, fine-tuning made the renders clean but left a hidden pattern readable from the Gaussians themselves; only rebuilding the whole region brought it down to a clean retrain's level. *(AAAI-27 Undergraduate Consortium proposal, decision pending.)*
- **Object landmarks for dense 3DGS SLAM**, with [@W-OK-E](https://github.com/W-OK-E): lifting and cleaning object masks on a Gaussian map so they can correct the trajectory. *(Manuscript in preparation.)*

### Things I've built

| Project | What it does |
|---|---|
| [**Heimdall**](https://github.com/Aryan241/Heimdall) | One aerial photo in, a metric height map and a 3D flythrough out. A small decoder on a frozen Depth Anything V2, checked against LiDAR on held-out sites. Built for Smart India Hackathon 2026 (ISRO/SAC problem). |
| [**Distractor removal for 3DGS**](https://github.com/Aryan241/SplatSplot) | Cleans an already-trained splat without retraining: SAM 2 masks from a text prompt, then a multi-view vote keeps or prunes each Gaussian. Tested on 12 Nerfbusters scenes. |

### Toolbox

<p>
  <img src="https://skillicons.dev/icons?i=python,pytorch,cpp,java,opencv,linux,git,latex&perline=8" alt="Python, PyTorch, C++, Java, OpenCV, Linux, Git, LaTeX" />
</p>
<p>
  <img src="https://img.shields.io/badge/gsplat-1f2937" alt="gsplat" />
  <img src="https://img.shields.io/badge/OpenSplat-1f2937" alt="OpenSplat" />
  <img src="https://img.shields.io/badge/COLMAP-1f2937" alt="COLMAP" />
  <img src="https://img.shields.io/badge/SAM%202-1f2937" alt="SAM 2" />
  <img src="https://img.shields.io/badge/Depth%20Anything-1f2937" alt="Depth Anything" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=black" alt="Hugging Face" />
</p>

### Around

- Mentoring juniors in ML at [Project MANAS](https://projectmanas.in/), the AI and robotics team of MAHE
- Leading a four-person team in e-Yantra (IIT Bombay)

[Website](https://aryan241.github.io) · [CV](https://aryan241.github.io/files/Aryan_Achary_CV.pdf) · [Email](mailto:aryanachary77@gmail.com)
