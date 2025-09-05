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


<table>
  <tr>
    <td align="center"><img src="docs/figures/Figure%2011%20Graphic%20equalizer%20schematic%20diagram.png" alt="Figure 11 — Schematic diagram of the graphic equalizer" height="180"/><br><sub><b>Figure 11</b> — Schematic</sub></td>
    <td align="center"><img src="docs/figures/Figure%2017%20Physical%20implementation%20of%20the%20graphic%20equalizer.jpg" alt="Figure 17 — Physical implementation on breadboard" height="180"/><br><sub><b>Figure 17</b> — Breadboard setup</sub></td>
    <td align="center"><img src="docs/figures/Figure 18 Physical circuit of the graphic equalizer.jpg" alt="Figure 18 — Circuit close‑up (landscape)" height="180"/><br><sub><b>Figure 18</b> — Circuit close‑up</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/figures/Figure 9 Bode graph for the full filtered block of the graphic equalizer.png" alt="Figure 9 — Bode plot for the full equalizer (bands combined)" height="180"/><br><sub><b>Figure 9</b> — All bands (combined)</sub></td>
    <td align="center"><img src="docs/figures/Figure%2012%20Bode%20graph%20with%20R_2%200%25.png" alt="Figure 12 — Bode with R2 at 0%" height="180"/><br><sub><b>Figure 12</b> — R2 = 0%</sub></td>
    <td align="center"><img src="docs/figures/Figure 13 Bode graph with 100 R2.png" alt="Figure 13 — Bode with R2 at 100%" height="180"/><br><sub><b>Figure 13</b> — R2 = 100%</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/figures/Figure%2014%20Bode%20Graph%20for%20Low%20Frequency%20Attenuation.png" alt="Figure 14 — Low‑band attenuation" height="180"/><br><sub><b>Figure 14</b> — Low band only</sub></td>
    <td align="center"><img src="docs/figures/Figure%2015%20Bode%20Graph%20for%20Mid%20Frequency%20Attenuation.png" alt="Figure 15 — Mid‑band attenuation" height="180"/><br><sub><b>Figure 15</b> — Mid band only</sub></td>
    <td align="center"><img src="docs/figures/Figure%2016%20Bode%20Graph%20for%20High%20Frequency%20Attenuation.png" alt="Figure 16 — High‑band attenuation" height="180"/><br><sub><b>Figure 16</b> — High band only</sub></td>
  </tr>
</table>

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
│  ├─ mathematica/
│  │  └─ 3Practica5_ElectronicaAnalogica.nb
│  └─ proteus/
│     └─ Practica5_Ecualizador Grafico.pdsprj
├─ scripts/
└─  └─ plot_bode.py                   ← main plotting script
```

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
