# Notebook DDPM — `make_moons`

Implementação didática de um **Denoising Diffusion Probabilistic Model** (Ho et al., 2020)
num dataset 2D. Serve de material de apoio aos slides e **gera o GIF**
`../assets/reverse_diffusion.gif` usado na apresentação.

O notebook cobre: dados e normalização → processo *forward* (noise schedule) →
rede $\epsilon_\theta$ com *time embedding* → treinamento (MSE do ruído) →
amostragem *reverse* → geração do GIF.

## Ambiente

Requer Python 3.12 (CPU já basta — o treino leva ~2 min). Usando [`uv`](https://docs.astral.sh/uv/):

```bash
cd notebook
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

Com `pip` tradicional:

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

## Executar / regenerar o GIF

Abra no Jupyter e rode todas as células:

```bash
jupyter lab DDPM_make_moons_tutorial.ipynb
```

Ou, em modo *headless* (re-treina e regrava o GIF em `../assets/`):

```bash
jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=1200 DDPM_make_moons_tutorial.ipynb
```
