# Matriz de decisão de motion

Preencher antes de escolher ferramenta pra qualquer comportamento de
movimento. Pergunta central: **esse comportamento realmente precisa de
GSAP (ou de biblioteca adicional)?** Ver `docs/GSAP.md`.

| Necessidade | Ferramenta | Motivo |
|---|---|---|
| Entrada simples | CSS ou GSAP core | |
| Sequência | GSAP Timeline | |
| Scroll-driven | ScrollTrigger | |
| Texto | SplitText + GSAP quando necessário | |
| Mudança de layout | Flip | |
| SVG morph | MorphSVG | |
| Smooth scroll | Lenis OU ScrollSmoother (nunca as duas juntas) | |
| Parallax simples | CSS/ScrollTrigger | |
| Parallax complexo | ScrollTrigger / Lenis / Locomotive conforme contexto | |
| 3D/WebGL | Avaliar stack específica — não forçar GSAP sozinho | |

## Decisão registrada neste projeto

Necessidade:
Ferramenta escolhida:
Motivo:
Alternativa descartada e por quê:

## Regra

GSAP + recursos nativos primeiro. Biblioteca complementar (Lenis,
Locomotive Scroll) só entra com motivo concreto registrado aqui — nunca
por padrão, e nunca duas engines de smooth scroll ao mesmo tempo sem
justificativa.
