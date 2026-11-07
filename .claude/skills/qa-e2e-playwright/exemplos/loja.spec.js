// Smoke test de exemplo. Roda só contra o arquivo local loja-ficticia.html.
// Qualquer requisição de rede real é abortada e faz o teste falhar.
const { test, expect } = require("@playwright/test");
const path = require("path");
const { pathToFileURL } = require("url");

const PAGINA = pathToFileURL(path.join(__dirname, "loja-ficticia.html")).href;

let externas = [];

test.beforeEach(async ({ page }) => {
  externas = [];
  await page.route(/^https?:\/\//, (route) => {
    externas.push(route.request().url());
    return route.abort();
  });
  await page.goto(PAGINA);
});

test.afterEach(() => {
  expect(externas, "nenhuma requisição de rede real durante o teste").toEqual([]);
});

test("lista produtos e filtra por categoria", async ({ page }) => {
  await expect(page.getByRole("heading", { level: 2 })).toHaveCount(2);
  await page.getByLabel("Categoria").selectOption("corrida");
  await expect(page.getByRole("heading", { name: "Tênis Corrida Modelo A" })).toBeVisible();
  await expect(page.getByRole("heading", { level: 2 })).toHaveCount(1);
});

test("estado vazio aparece quando a categoria não tem produto", async ({ page }) => {
  await page.getByLabel("Categoria").selectOption("trilha");
  await expect(page.getByText("Nenhum produto nesta categoria.")).toBeVisible();
});

test("link do WhatsApp leva produto e SKU, sem ser aberto", async ({ page }) => {
  const link = page.getByRole("link", { name: "Consultar disponibilidade de Tênis Corrida Modelo A" });
  const href = await link.getAttribute("href");
  expect(href).toContain("https://wa.me/5500000000000?text=");
  expect(decodeURIComponent(href.split("text=")[1])).toContain("SKU MODA-PRT-38");
});

test("sem rolagem horizontal e CTA alcançável por teclado", async ({ page }) => {
  const largura = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]);
  expect(largura[0]).toBeLessThanOrEqual(largura[1]);
  for (let i = 0; i < 5; i++) {
    await page.keyboard.press("Tab");
    const foco = await page.evaluate(() => document.activeElement && document.activeElement.textContent);
    if (foco && foco.startsWith("Consultar disponibilidade")) return;
  }
  throw new Error("CTA não alcançado por teclado em 5 tabs");
});
