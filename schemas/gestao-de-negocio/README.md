# Schemas — Gestão de negócio (especialização food service)

17 entidades usadas pelas skills de `catalogo/modulos/gestao-de-negocio/` e
`catalogo/modulos/gestao-de-negocio/food-service/`: `negocio`, `produto`,
`ingrediente`, `ficha-tecnica`, `rendimento`, `perda`, `estoque`,
`movimento`, `inventario`, `pedido`, `item-pedido`, `cupom`, `canal`,
`campanha`, `teste-de-produto`, `projecao`, `plano-de-acao`.

`pedido`/`item-pedido` são o contrato de dados genérico que
`cardapio-digital` usa para integração futura com qualquer plataforma
(própria ou de terceiro, incluindo mas não exigindo OlaClick) — uma
integração nova é um adaptador que popula esse contrato, não uma mudança
na skill.
