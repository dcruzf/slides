# slides

Apresentações feitas com [Slidev](https://sli.dev), publicadas no GitHub Pages.

## Desenvolvimento

```bash
npm install
npm run dev      # abre em http://localhost:3030
```

Edite [`slides.md`](slides.md) — as alterações recarregam automaticamente.

## Build local

```bash
npm run build    # gera a SPA em dist/
```

## Deploy

O deploy é automático: cada `push` na branch `main` dispara o workflow
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), que faz o build
e publica no GitHub Pages.

> **Configuração única no GitHub:** em **Settings → Pages → Build and
> deployment**, defina **Source** como **GitHub Actions**.

A URL final será `https://<usuario>.github.io/slides/`.

## Exportar para PDF

```bash
npm run export
```

## Material gerado (notebook DDPM)

Os gráficos e o GIF usados nos slides são produzidos por um notebook versionado:

- [`notebook/DDPM_make_moons_tutorial.ipynb`](notebook/DDPM_make_moons_tutorial.ipynb) —
  implementa um DDPM em 2D (`make_moons`) e gera os assets em [`assets/`](assets/)
  (`reverse_diffusion.gif`, `comparison.png`, `forward.png`).
- Ambiente e instruções de reprodução: [`notebook/README.md`](notebook/README.md).
- [`scripts/generative_distribution.py`](scripts/generative_distribution.py) — script
  autocontido (executável via `uv run scripts/generative_distribution.py`, declara as
  próprias dependências) que gera `multimodal_density.png` e `multimodal_samples.png`
  (a distribuição multimodal em curvas de nível, usada no slide "Modelo Generativo").

Os slides referenciam esses arquivos por caminho relativo (ex.: `./assets/reverse_diffusion.gif`),
empacotados pelo Vite/Slidev no build (com o `--base` correto para o GitHub Pages).
