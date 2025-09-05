# TriBandEQ — 3-Band Graphic Equalizer (Analog Electronics Lab)

**Languages:** English · [Informe en español](docs/report/TriBand-EQ_Report-ES.pdf)

This repository contains the full design, simulation, analysis, code, and figures for a **3‑band graphic equalizer** built with active filters (op‑amps). You’ll find the complete report in both English and Spanish, Bode plot data/figures, the Proteus project, a Mathematica notebook, and a Python script to reproduce the plots.

---

## 📄 Reports

* **English:** [`docs/report/TriBand-EQ_Report-EN.pdf`](docs/report/TriBand-EQ_Report-EN.pdf)
* **Español:** [`docs/report/TriBand-EQ_Report-ES.pdf`](docs/report/TriBand-EQ_Report-ES.pdf)

The reports cover the theoretical background (differentiator, integrator, active low‑pass), target band centers (≈ 81 Hz, ≈ 3.06 kHz, ≈ 16.7 kHz), transfer functions, design procedure, Bode analysis, Proteus simulations, and bench results.

---

## 🎬 Video Demo

A short demo of the prototype in operation is included here:

* **MP4:** [`docs/video_demo/TriBandEQ-Demo.mp4`](docs/video_demo/TriBandEQ-Demo.mp4)

<details>
<summary>Inline player (GitHub may not preview on all devices)</summary>

<video src="docs/video_demo/TriBandEQ-Demo.mp4" controls preload="metadata" width="720">
  Your browser does not support the video tag. Download the file instead:
  <a href="docs/video_demo/TriBandEQ-Demo.mp4">TriBandEQ-Demo.mp4</a>
</video>

</details>

> If the video doesn’t preview on GitHub’s web UI, use the direct link or clone the repo locally.

---

## 🖼 Project Images (Gallery)

> If an image does not render, make sure the file name matches the path below, or run `scripts/plot_bode.py all --no-show` to (re)generate the Bode figures with the canonical names.

<p align="center">
  <!-- Schematic + Hardware -->
  <img src="docs/figures/Figure_11_Schematic.png" alt="Figure 11 — Schematic diagram of the graphic equalizer" width="31%"/>
  <img src="docs/figures/Figure_17_Physical_Implementation.jpg" alt="Figure 17 — Physical implementation on breadboard" width="31%"/>
  <img src="docs/figures/Figure_18_Physical_Circuit_Closeup.jpg" alt="Figure 18 — Circuit close‑up" width="31%"/>
</p>

<p align="center">
  <!-- Bode overview & R2 sweeps -->
  <img src="docs/figures/Figure_09_Bode_AllBands.png" alt="Figure 9 — Bode plot for the full equalizer (bands combined)" width="31%"/>
  <img src="docs/figures/Figure_12_Bode_R2_0.png" alt="Figure 12 — Bode with R2 at 0%" width="31%"/>
  <img src="docs/figures/Figure_13_Bode_R2_100.png" alt="Figure 13 — Bode with R2 at 100%" width="31%"/>
</p>

<p align="center">
  <!-- Per‑band attenuation views -->
  <img src="docs/figures/Figure_14_Bode_LowOnly.png" alt="Figure 14 — Low‑band attenuation" width="31%"/>
  <img src="docs/figures/Figure_15_Bode_MidOnly.png" alt="Figure 15 — Mid‑band attenuation" width="31%"/>
  <img src="docs/figures/Figure_16_Bode_HighOnly.png" alt="Figure 16 — High‑band attenuation" width="31%"/>
</p>

> **Tip:** Keep image widths at \~31% for a clean 3‑column grid on desktop while gracefully stacking on mobile.

---

## 📦 Repository Structure

```
TriBandEQ/
├─ docs/
│  ├─ report/
│  │  ├─ TriBand-EQ_Report-EN.pdf
│  │  ├─ TriBand-EQ_Report-ES.pdf
│  │  └─ (source .docx files)
│  ├─ figures/
│  │  ├─ Figure 06–10: Bode plots per band & combined (theory)
│  │  ├─ Figure 11: Schematic diagram
│  │  ├─ Figure 12: Bode graph with R2 at 0%
│  │  ├─ Figure 13: Bode graph with R2 at 100%
│  │  ├─ Figure 14: Bode graph for Low-band attenuation
│  │  ├─ Figure 15: Bode graph for Mid-band attenuation
│  │  └─ Figure 16: Bode graph for High-band attenuation
│  └─ video_demo/
│     └─ TriBandEQ-Demo.mp4         ← demo video (place here)
├─ simulations/                      ← raw/processed data exported from Proteus
├─ mathematica/
│  └─ 3Practica5_ElectronicaAnalogica.nb
├─ proteus/
│  └─ Practica5_Ecualizador Grafico.pdsprj
├─ scripts/
│  └─ plot_bode.py                   ← main plotting script
└─ plot_bode.py                      ← (optional duplicate; prefer scripts/plot_bode.py)
```

> If you keep **both** `plot_bode.py` at the repo root and in `scripts/`, use the one in `scripts/` and remove the root copy to avoid confusion.

---

## 🧪 Reproducing the Bode Figures

The Python script plots exported magnitude (dB) vs frequency (Hz) data from Proteus and annotates key frequencies. It’s pre‑configured to save into `docs/figures/` using the same blue/gold theme as the report.

### 1) Environment

```bash
# (optional) create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# install deps
pip install -U numpy matplotlib
```

### 2) Usage

The script accepts a **dataset key** and will save the PNG into `docs/figures/` by default.

```bash
python scripts/plot_bode.py <which> [--no-show] [--no-save] [--save PATH] [--dpi 180]
```

**Dataset ↔ figure mapping** (as used in the English/Spanish reports):

| Key     | Meaning                                       | Report figure |
| ------- | --------------------------------------------- | ------------- |
| `r20`   | All 3 sections with **R2 = 0 %** (≈ 0 Ω)      | Figure 12     |
| `r2100` | All 3 sections with **R2 = 100 %** (≈ 100 kΩ) | Figure 13     |
| `low`   | Only **Low band** R2 = 100 %; others at 0 %   | Figure 14     |
| `mid`   | Only **Mid band** R2 = 100 %; others at 0 %   | Figure 15     |
| `high`  | Only **High band** R2 = 100 %; others at 0 %  | Figure 16     |
| `all`   | Generate **all five** plots                   | —             |

**Examples**

```bash
# Generate and save all five figures into docs/figures/
python scripts/plot_bode.py all --no-show

# Individual figures
python scripts/plot_bode.py r20   --no-show    # → Figure 12
python scripts/plot_bode.py r2100 --no-show    # → Figure 13
python scripts/plot_bode.py low   --no-show    # → Figure 14
python scripts/plot_bode.py mid   --no-show    # → Figure 15
python scripts/plot_bode.py high  --no-show    # → Figure 16

# Override output path and DPI if needed
python scripts/plot_bode.py mid --save docs/figures/Figure_15_Bode_MidOnly.png --dpi 200 --no-show
```

> The script sets **log‑scale** on X, uses the blue/gold theme, and annotates reference frequencies (≈ 81 Hz, ≈ 3162 Hz, ≈ 15849 Hz, ≈ 100 kHz) with labeled markers for consistency with Figures 12–16.

---

## 🛠️ Simulation & Design Files

* **Proteus 8 Professional:** open `proteus/Practica5_Ecualizador Grafico.pdsprj` to run the analog simulation and export new datasets.
* **Mathematica:** `mathematica/3Practica5_ElectronicaAnalogica.nb` contains the second‑order modeling and theoretical Bode plots.
* **Schematic & photos:** see `docs/figures/` (Figure 11 schematic; Figures 17–18 implementation photos).

---

## 🔍 Highlights

* Three narrow‑band sections centered near **≈ 81 Hz**, **≈ 3.06 kHz**, and **≈ 16.7 kHz**.
* Inverting mixer behavior explains **boost** (theory overlays) vs **cut** (Proteus setups with R2 polarity/setting).
* Practical notes: per‑section isolation, optional buffers, and small compensation across the mix resistor to reduce interaction near ≈ 6.31 kHz.

For full derivations, design choices, and lab results, read the reports in `docs/report/`.

---

## 📜 License

If you intend to make it open source, we recommend MIT:

```
MIT License — © 2024 <Your Name>
```

Place this text into a top‑level `LICENSE` file.

---

## 🙌 Acknowledgments

* Course: Analog Electronics
* Tools: Proteus, Wolfram Mathematica, Python (NumPy/Matplotlib)
* Hardware tests on breadboard with ±12 V supply and oscilloscope verification

---

## 🤝 How to cite

If you use this repository, please cite the report:

> *TriBandEQ — 3‑Band Graphic Equalizer.* Report (EN/ES), 2024. Available in `docs/report/`.
