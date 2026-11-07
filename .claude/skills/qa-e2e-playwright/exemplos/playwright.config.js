// Configuração de exemplo: desktop + mobile, artefatos só em falha.
const { defineConfig, devices } = require("@playwright/test");

module.exports = defineConfig({
  testDir: ".",
  testMatch: /.*\.spec\.js/,
  retries: 1,
  outputDir: "./test-results",
  use: { trace: "on-first-retry", screenshot: "only-on-failure" },
  projects: [
    { name: "desktop", use: { ...devices["Desktop Chrome"] } },
    { name: "mobile", use: { ...devices["Pixel 7"] } },
  ],
});
