---
theme: academic
title: Minha Apresentação
info: |
  ## Minha Apresentação
  Criada com [Slidev](https://sli.dev).
class: text-center
transition: slide-left
mdc: true
---

# Minha Apresentação

Slides em Markdown com [Slidev](https://sli.dev)

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Pressione <kbd>espaço</kbd> para o próximo slide <carbon:arrow-right />
  </span>
</div>

<!--
Notas do apresentador ficam aqui (visíveis no modo presenter).
-->

---
transition: fade-out
---

# O que é Slidev?

Slidev é uma ferramenta de slides feita para desenvolvedores:

- 📝 **Markdown** — escreva o conteúdo focando no que importa
- 🎨 **Temas** — visual profissional com um clique
- 🧑‍💻 **Código** — destaque de sintaxe e foco em linhas
- 🤹 **Interativo** — embuta componentes Vue nos slides
- 🎥 **Gravação** — câmera e gravação embutidas
- 📤 **Exportação** — PDF, PNG ou SPA hospedável

<br>

Saiba mais em [sli.dev](https://sli.dev)

---

# Exemplo de código

```ts {2-3|5|all}
function saudacao(nome: string): string {
  const mensagem = `Olá, ${nome}!`
  return mensagem
}

console.log(saudacao('mundo'))
```

Use <kbd>↑</kbd> <kbd>↓</kbd> para navegar e clique para avançar nos passos.

---
layout: center
class: text-center
---

# Obrigado!

[Documentação](https://sli.dev) · [GitHub](https://github.com/slidevjs/slidev)
