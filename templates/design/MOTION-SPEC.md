# Motion spec

Um bloco por movimento identificado numa referência ou planejado pro
projeto. Ver `docs/GSAP.md` pra critério de quando usar GSAP.

## M### — <nome do movimento>

Elemento:
Evento:
Estado inicial:
Estado final:
Trigger:
Duração:
Ease:
Delay:
Stagger:
Scrub:
Pin:
Start:
End:
Desktop:
Tablet:
Mobile:
Reduced motion:
Tecnologia:
Motivo:

---

### Exemplo

## M001 — Entrada do headline do hero

Elemento: headline hero
Evento: entrada inicial
Estado inicial: `y: 40, autoAlpha: 0`
Estado final: `y: 0, autoAlpha: 1`
Trigger: carregamento da página
Tecnologia: GSAP Timeline
Ease: power3.out
Reduced motion: remove o deslocamento, mantém só o fade
Motivo: entrada hierárquica sem distrair da leitura.

---

Toda spec com `prefers-reduced-motion` ativo remove scrub intenso,
parallax forte e zoom agressivo, preserva conteúdo e navegação — ver
`docs/GSAP.md`, seção "Acessibilidade".
