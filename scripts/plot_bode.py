#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
plot_bode.py — plot de cinco gráficos Bode preconfigurados y guardados en docs/figures/.

Uso típico:
  python plot_bode.py r20
  python plot_bode.py r2100
  python plot_bode.py all                # guarda los cinco
Opciones:
  --no-save       No guardar archivo (por defecto SÍ guarda en docs/figures/)
  --save PATH     Guardar en una ruta/archivo específico (anula la ruta por defecto)
  --save-prefix P Al usar 'all', prefijo para los 5 archivos (e.g., figs/bode_)
  --dpi 180       DPI para los PNG (150 por defecto)
  --no-show       No mostrar ventana de figura
  --fmarks ...    Sobrescribe los marcadores de frecuencia (Hz)
"""

import argparse
from dataclasses import dataclass
from typing import Dict, List, Optional
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# -------- Tema visual (coincide con tus capturas) --------
BG = "#344A72"
FG = "#B1B9C9"
LINE = "#BF9000"
PT_FILL = "#203864"
PT_EDGE = "#BF9000"

# Carpeta y nombres por defecto
OUTPUT_DIR = Path("docs/figures")
DEFAULT_FILENAMES = {
    "r20":   "bode_r2_0.png",
    "r2100": "bode_r2_100.png",
    "low":   "bode_low.png",
    "mid":   "bode_mid.png",
    "high":  "bode_high.png",
}

@dataclass
class DataSet:
    key: str
    title: str
    freq: np.ndarray
    vout_db: np.ndarray
    default_marks_hz: List[float]

# -------------------- DATASETS --------------------

def ds_r20() -> DataSet:
    # Imagen 1: R2 al 0%
    freq = np.array([2.511886432, 3.162277117, 3.981071022, 5.011871475, 6.309572361, 7.943280983,
                     9.999998282, 12.58925196, 15.8489292, 19.95261972, 25.11886, 31.62277117,
                     39.81071022, 50.11871475, 63.09572361, 79.43280983, 99.99998282, 125.8925196,
                     158.489292, 199.5261972, 251.1886, 316.2277117, 398.1071022, 501.1871475,
                     630.9572361, 794.3280983, 999.9998282, 1258.925196, 1584.89292, 1995.261972,
                     2511.886, 3162.277117, 3981.071022, 5011.871475, 6309.572361, 7943.280983,
                     9999.998282, 12589.25196, 15848.9292, 19952.61972, 25118.86, 31622.77117,
                     39810.71022, 50118.71475, 63095.72361, 79432.80983, 99999.98282, 125892.5196,
                     158489.292, 199526.1972, 251188.6, 316227.7117, 398107.1022, 501187.1475,
                     630957.2361, 794328.0983, 999999.8282])
    vout = np.array([-0.000562495, -0.000562642, -0.000562873, -0.000563238, -0.00056381, -0.000564701,
                     -0.000566074, -0.000568162, -0.000571262, -0.000575713, -0.000581805, -0.000589618,
                     -0.000598842, -0.00060873, -0.0006183, -0.0006267, -0.000633495, -0.000638685,
                     -0.000642565, -0.000645551, -0.000648085, -0.000650614, -0.000653612, -0.000657627,
                     -0.000663332, -0.000671553, -0.000683258, -0.000699533, -0.000721635, -0.000751353,
                     -0.000791814, -0.000848716, -0.000931864, -0.00105715, -0.00124954, -0.00154799,
                     -0.00201361, -0.00274307, -0.00389001, -0.00569838, -0.00855454, -0.0130686,
                     -0.0202011, -0.0314579, -0.0491859, -0.077007, -0.120426, -0.187609, -0.290215,
                     -0.443923, -0.667916, -0.982355, -1.40357, -1.93906, -2.58701, -3.34365, -4.21401])
    return DataSet("r20", "Gráfica de Bode con R2 al 0%", freq, vout, [79, 3162, 15849, 100000])

def ds_r2100() -> DataSet:
    # Imagen 2: R2 al 100%
    freq = np.array([1.00000000e+01, 1.25892541e+01, 1.58489319e+01, 1.99526232e+01,
                     2.51188643e+01, 3.16227766e+01, 3.98107171e+01, 5.01187234e+01,
                     6.30957345e+01, 7.94328235e+01, 1.00000000e+02, 1.25892541e+02,
                     1.58489319e+02, 1.99526231e+02, 2.51188643e+02, 3.16227766e+02,
                     3.98107171e+02, 5.01187234e+02, 6.30957344e+02, 7.94328235e+02,
                     1.00000000e+03, 1.25892541e+03, 1.58489319e+03, 1.99526231e+03,
                     2.51188643e+03, 3.16227766e+03, 3.98107171e+03, 5.01187234e+03,
                     6.30957344e+03, 7.94328235e+03, 1.00000000e+04, 1.25892541e+04,
                     1.58489319e+04, 1.99526231e+04, 2.51188643e+04, 3.16227766e+04,
                     3.98107171e+04, 5.01187234e+04, 6.30957345e+04, 7.94328235e+04,
                     1.00000000e+05, 1.25892541e+05, 1.58489319e+05, 1.99526231e+05,
                     2.51188643e+05, 3.16227766e+05, 3.98107171e+05, 5.01187234e+05,
                     6.30957345e+05, 7.94328235e+05, 1.00000000e+06])
    vout = np.array([ -0.792345,  -1.20303 ,  -1.79234 ,  -2.60643 ,  -3.68289 ,
                      -5.04227 ,  -6.68171 ,  -8.55807 , -10.5159  , -12.1     ,
                     -12.5253  , -11.5632  ,  -9.93794 ,  -8.30714 ,  -6.94143 ,
                      -5.92308 ,  -5.26797 ,  -4.9664  ,  -4.99669 ,  -5.32838 ,
                      -5.91961 ,  -6.71552 ,  -7.65507 ,  -8.68655 ,  -9.78081 ,
                     -10.9234  , -12.0642  , -13.0161  , -13.4087  , -12.9681  ,
                     -11.8856  , -10.5678  ,  -9.25894 ,  -8.02288 ,  -6.84895 ,
                      -5.72478 ,  -4.66413 ,  -3.7037  ,  -2.88479 ,  -2.23496 ,
                      -1.76026 ,  -1.4494  ,  -1.28428 ,  -1.24951 ,  -1.3371  ,
                      -1.54586 ,  -1.87689 ,  -2.32852 ,  -2.89581 ,  -3.57686 ,
                      -4.38101 ])
    return DataSet("r2100", "Gráfica de Bode con R2 al 100%", freq, vout,
                   [79, 3162, 6310, 15849, 100000])

def ds_low() -> DataSet:
    # Imagen 3: Frecuencias bajas
    freq = np.array([2.070730591, 2.606895877, 3.281887465, 4.131651529, 5.201441102, 6.548226382,
                     8.243728594, 10.37823941, 13.06542933, 16.448401, 20.70731, 26.06895877,
                     32.81887465, 41.31651529, 52.01441102, 65.48226382, 82.43728594, 103.7823941,
                     130.6542933, 164.48401, 207.0731, 260.6895877, 328.1887465, 413.1651529,
                     520.1441102, 654.8226382, 824.3728594, 1037.823941, 1306.542933, 1644.8401,
                     2070.731, 2606.895877, 3281.887465, 4131.651529, 5201.441102, 6548.226382,
                     8243.728594, 10378.23941, 13065.42933, 16448.401, 20707.31, 26068.95877,
                     32818.87465, 41316.51529, 52014.41102, 65482.26382, 82437.28594, 103782.3941,
                     130654.2933, 164484.01, 207073.1, 260689.5877, 328188.7465, 413165.1529])
    vout = np.array([-0.0387136, -0.0609018, -0.0958787, -0.150846, -0.236817, -0.370301,
                     -0.575291, -0.885079, -1.34283, -1.99939, -2.90747, -4.11357,
                     -5.65066, -7.52672, -9.66792, -11.6821, -12.4885, -11.3569,
                     -9.25958, -7.15339, -5.33912, -3.86556, -2.71821, -1.86102,
                     -1.24573, -0.819374, -0.532205, -0.342846, -0.219844, -0.140763,
                     -0.0902707, -0.0581855, -0.0378737, -0.0250678, -0.0170496, -0.0121056,
                     -0.00917363, -0.00762065, -0.00710887, -0.0075246, -0.00895424, -0.0117023,
                     -0.0163549, -0.0239004, -0.0359286, -0.05494, -0.0848016, -0.131382,
                     -0.203348, -0.312981, -0.476593, -0.71375, -1.04436, -1.48361])
    return DataSet("low", "Gráfica de Bode para frecuencias bajas", freq, vout,
                   [82, 3282, 16448, 103782])

def ds_mid() -> DataSet:
    # Imagen 4: Frecuencias medias
    freq = np.array([10, 12.58925412, 15.84893192, 19.95262315, 25.11886432, 31.6227766,
                     39.81071706, 50.11872336, 63.09573445, 79.43282347, 100, 125.8925412,
                     158.4893192, 199.5262315, 251.1886432, 316.227766, 398.1071706, 501.1872336,
                     630.9573445, 794.3282347, 1000, 1258.925412, 1584.893192, 1995.262315,
                     2511.886432, 3162.27766, 3981.071706, 5011.872336, 6309.573445, 7943.282347,
                     10000, 12589.25412, 15848.93192, 19952.62315, 25118.86432, 31622.7766,
                     39810.71706, 50118.72336, 63095.73445, 79432.82347, 100000, 125892.5412,
                     158489.3192, 199526.2315, 251188.6432, 316227.766, 398107.1706, 501187.2336,
                     630957.3445, 794328.2347, 1000000, 1258925.412, 1584893.192, 1995262.315,
                     2511886.432, 3162277.66, 3981071.706])
    vout = np.array([-0.00119019, -0.00155761, -0.00213968, -0.00306162, -0.00452156, -0.00683283,
                     -0.0104909, -0.0162787, -0.0254332, -0.0399031, -0.0627494, -0.098752,
                     -0.155311, -0.243732, -0.380927, -0.591409, -0.909049, -1.37749,
                     -2.0477, -2.97184, -4.19515, -5.74861, -7.6368, -9.77702,
                     -11.7544, -12.4792, -11.2972, -9.20459, -7.1196, -5.32722,
                     -3.87366, -2.74415, -1.90251, -1.30047, -0.885546, -0.608977,
                     -0.430867, -0.321775, -0.262008, -0.240125, -0.251596, -0.297983,
                     -0.386601, -0.530226, -0.746044, -1.05281, -1.46592, -1.9924,
                     -2.63056, -3.37728, -4.23852, -5.23288, -6.38328, -7.70301,
                     -9.18716, -10.8143, -12.5543])
    return DataSet("mid", "Gráfica de Bode para frecuencias medias", freq, vout,
                   [79, 3162, 15849, 100000])

def ds_high() -> DataSet:
    # Imagen 5: Frecuencias altas
    freq = np.array([10, 12.58925412, 15.84893192, 19.95262315, 25.11886432, 31.6227766,
                     39.81071706, 50.11872336, 63.09573445, 79.43282347, 100, 125.8925412,
                     158.4893192, 199.5262315, 251.1886432, 316.227766, 398.1071706, 501.1872336,
                     630.9573445, 794.3282347, 1000, 1258.925412, 1584.893192, 1995.262315,
                     2511.886432, 3162.27766, 3981.071706, 5011.872336, 6309.573445, 7943.282347,
                     10000, 12589.25412, 15848.93192, 19952.62315, 25118.86432, 31622.7766,
                     39810.71706, 50118.72336, 63095.73445, 79432.82347, 100000, 125892.5412,
                     158489.3192, 199526.2315, 251188.6432, 316227.766, 398107.1706, 501187.2336,
                     630957.3445, 794328.2347, 1000000, 1258925.412, 1584893.192, 1995262.315,
                     2511886.432, 3162277.66, 3981071.706])
    vout = np.array([-0.000586375, -0.000600655, -0.000623081, -0.000658165, -0.000712813, -0.000797597,
                     -0.000928834, -0.00113213, -0.00144827, -0.00194257, -0.00271942, -0.00394487,
                     -0.00588219, -0.00894801, -0.0138011, -0.0214821, -0.0336313, -0.0528278,
                     -0.083107, -0.130737, -0.205345, -0.321447, -0.500346, -0.772016,
                     -1.17609, -1.7605, -2.57644, -3.67036, -5.07588, -6.80601,
                     -8.82513, -10.9197, -12.3609, -12.0957, -10.378, -8.30064,
                     -6.40523, -4.82832, -3.5841, -2.65107, -1.99186, -1.56274,
                     -1.3231, -1.24258, -1.30358, -1.49887, -1.82566, -2.2796,
                     -2.85346, -3.54314, -4.35609, -5.3124, -6.43504, -7.73582,
                     -9.20765, -10.827, -12.5623])
    return DataSet("high", "Gráfica de Bode para frecuencias altas", freq, vout,
                   [79, 3162, 15849, 100000])

# ---------------- Registro y helpers ----------------

def registry() -> Dict[str, DataSet]:
    # Orden lógico para 'all'
    return {d.key: d for d in [ds_r20(), ds_r2100(), ds_low(), ds_mid(), ds_high()]}

def nearest_indices(freq: np.ndarray, marks_hz: List[float]) -> List[int]:
    return [int(np.argmin(np.abs(freq - f))) for f in marks_hz]

def default_save_path(key: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR / DEFAULT_FILENAMES[key]

def plot_one(ds: DataSet, marks_hz: Optional[List[float]],
             save_path: Optional[Path], dpi: int, show: bool, do_save: bool) -> None:
    fig = plt.figure(figsize=(15, 8))
    ax = plt.gca()

    ax.plot(ds.freq, ds.vout_db, color=LINE)

    # Marcadores
    if marks_hz is None:
        marks_hz = ds.default_marks_hz
    idxs = nearest_indices(ds.freq, marks_hz)
    for i in idxs:
        ax.plot(ds.freq[i], ds.vout_db[i], 'o', markersize=12,
                color=PT_FILL, markeredgewidth=2, markeredgecolor=PT_EDGE)
        ax.annotate(f'{ds.freq[i]:.0f} Hz', (ds.freq[i], ds.vout_db[i]),
                    textcoords="offset points", xytext=(0, 10),
                    ha='center', fontsize=12, color=PT_EDGE, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='none',
                              facecolor=PT_FILL, alpha=0.8))

    # Estilo
    ax.set_title(ds.title, fontsize=20, color=FG, fontweight='bold')
    ax.set_xlabel('Frequency (Hz)', fontsize=18, color=FG, fontweight='bold')
    ax.set_ylabel('Gain (dB)', fontsize=18, color=FG, fontweight='bold')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color=FG)
    ax.set_xscale('log'); ax.set_yscale('linear')
    for sp in ('top', 'bottom', 'left', 'right'):
        ax.spines[sp].set_color(FG)
    ax.tick_params(axis='x', colors=FG); ax.tick_params(axis='y', colors=FG)
    fig.set_facecolor(BG); ax.set_facecolor(BG)
    plt.xticks(color=FG, fontsize=14, fontweight='bold')
    plt.yticks(color=FG, fontsize=14, fontweight='bold')

    # Guardado
    if do_save:
        if save_path is None:
            save_path = default_save_path(ds.key)
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
        print(f"[saved] {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)

# ---------------- CLI ----------------

def main():
    p = argparse.ArgumentParser(description="Plot Bode curves and save to docs/figures by default.")
    p.add_argument("which", choices=["r20", "r2100", "low", "mid", "high", "all"])
    p.add_argument("--save", help="Ruta/archivo para guardar (anula la ruta por defecto).")
    p.add_argument("--save-prefix", help="Prefijo para 'all' (e.g., figs/bode_)")
    p.add_argument("--dpi", type=int, default=150)
    p.add_argument("--no-show", action="store_true")
    p.add_argument("--no-save", action="store_true", help="No guardar archivos.")
    p.add_argument("--fmarks", nargs="*", type=float, help="Marcadores de frecuencia en Hz.")
    args = p.parse_args()

    reg = registry()
    do_save = not args.no_save

    if args.which != "all":
        ds = reg[args.which]
        save_path = Path(args.save) if args.save else (default_save_path(ds.key) if do_save else None)
        plot_one(ds, args.fmarks, save_path, args.dpi, show=not args.no_show, do_save=do_save)
    else:
        for key, ds in reg.items():
            if args.save_prefix:
                save_path = Path(f"{args.save_prefix}{key}.png") if do_save else None
            else:
                save_path = default_save_path(key) if do_save else None
            plot_one(ds, args.fmarks, save_path, args.dpi, show=not args.no_show, do_save=do_save)

if __name__ == "__main__":
    main()
