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
