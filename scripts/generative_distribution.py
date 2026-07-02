# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy>=1.26",
#   "matplotlib>=3.8",
# ]
# ///
"""
Gera as figuras da distribuição multimodal complexa usadas no slide
"O que é um Modelo Generativo?".

Produz, em `assets/`:
  - multimodal_density.png : a densidade p(x) por curvas de nível
  - multimodal_samples.png : amostras x ~ p(x) sobre as curvas de nível

Execução (autocontido, sem instalar nada global):
    uv run scripts/generative_distribution.py
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ------------------------------------------------------------------ paleta (mesma dos slides)
BG, INK, MUTED = "#0f1117", "#e5e7eb", "#94a3b8"
C_SAMPLE = "#38bdf8"          # amostras (azul) contrastando com o mapa magma
plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": INK, "font.size": 12,
})
ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(exist_ok=True)

# ------------------------------------------------------------------ mistura gaussiana multimodal
rng = np.random.default_rng(7)

def cov(sx, sy, ang_deg):
    a = np.deg2rad(ang_deg)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    return R @ np.diag([sx**2, sy**2]) @ R.T

# (peso, média, sx, sy, ângulo) — modos anisotrópicos e rotacionados => nível "complexo"
COMPONENTS = [
    (1.4, (-2.3,  1.3), 0.55, 0.32, 25),
    (1.0, (-1.4, -1.4), 0.40, 0.85, -15),
    (1.6, ( 0.2,  0.6), 0.95, 0.42, -35),
    (1.1, ( 1.9,  1.6), 0.38, 0.60, 10),
    (1.3, ( 2.4, -0.9), 0.70, 0.34, 55),
    (0.9, ( 0.6, -1.9), 0.50, 0.50, 0),
    (0.7, (-3.0, -0.3), 0.30, 0.30, 0),
]
weights = np.array([c[0] for c in COMPONENTS]); weights /= weights.sum()
means = [np.array(c[1], float) for c in COMPONENTS]
covs = [cov(c[2], c[3], c[4]) for c in COMPONENTS]

def density(pts):
    """p(x) numa malha de pontos (..., 2)."""
    out = np.zeros(pts.shape[:-1])
    for w, mu, C in zip(weights, means, covs):
        d = pts - mu
        inv = np.linalg.inv(C); det = np.linalg.det(C)
        m = np.einsum("...i,ij,...j->...", d, inv, d)
        out += w * np.exp(-0.5 * m) / (2 * np.pi * np.sqrt(det))
    return out

def sample(n):
    idx = rng.choice(len(COMPONENTS), size=n, p=weights)
    out = np.empty((n, 2))
    for k in range(len(COMPONENTS)):
        m = idx == k
        out[m] = rng.multivariate_normal(means[k], covs[k], size=m.sum())
    return out

# ------------------------------------------------------------------ malha e níveis
xlim, ylim = (-4.2, 4.0), (-3.2, 3.2)
gx = np.linspace(*xlim, 400)
gy = np.linspace(*ylim, 400)
GX, GY = np.meshgrid(gx, gy)
Z = density(np.stack([GX, GY], -1))
levels = np.linspace(Z.max() * 0.03, Z.max() * 0.98, 12)

def base_axes(ax, title):
    ax.set(xlim=xlim, ylim=ylim, aspect="equal", xticks=[], yticks=[])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(title, color=INK, fontsize=15, pad=10, fontweight="bold")

# ------------------------------------------------------------------ figura 1: densidade p(x)
fig, ax = plt.subplots(figsize=(6.6, 5.2), dpi=120)
ax.contourf(GX, GY, Z, levels=np.linspace(0, Z.max(), 200), cmap="magma")
cs = ax.contour(GX, GY, Z, levels=levels, colors="white",
                linewidths=0.7, alpha=0.35)
base_axes(ax, r"$p(x)$ — distribuição multimodal complexa")
ax.text(0.5, -0.05, "curvas de nível = regiões de igual densidade",
        transform=ax.transAxes, ha="center", color=MUTED, fontsize=11)
fig.subplots_adjust(left=.04, right=.96, top=.9, bottom=.08)
fig.savefig(ASSETS / "multimodal_density.png", bbox_inches="tight")
plt.close(fig)

# ------------------------------------------------------------------ figura 2: amostras x ~ p(x)
pts = sample(1200)
fig, ax = plt.subplots(figsize=(6.6, 5.2), dpi=120)
ax.contour(GX, GY, Z, levels=levels, cmap="magma", linewidths=1.1, alpha=0.9)
ax.scatter(pts[:, 0], pts[:, 1], s=7, c=C_SAMPLE, alpha=0.55, edgecolors="none")
base_axes(ax, r"amostras  $x \sim p(x)$")
ax.text(0.5, -0.05, "o modelo generativo produz novos pontos onde a densidade é alta",
        transform=ax.transAxes, ha="center", color=MUTED, fontsize=11)
fig.subplots_adjust(left=.04, right=.96, top=.9, bottom=.08)
fig.savefig(ASSETS / "multimodal_samples.png", bbox_inches="tight")
plt.close(fig)

print("salvos:")
print("  ", ASSETS / "multimodal_density.png")
print("  ", ASSETS / "multimodal_samples.png")
