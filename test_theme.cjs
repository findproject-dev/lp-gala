const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
  page.on('pageerror', err => console.log('BROWSER ERROR:', err.message));
  
  // Need to serve the dist folder or run the dev server.
  // Since we already ran `bun run build`, let's just serve `dist` temporarily.
  const { exec } = require('child_process');
  const server = exec('bunx serve dist -p 8080');
  
  // Wait a second for server to start
  await new Promise(r => setTimeout(r, 2000));
  
  try {
    await page.goto('http://localhost:8080', { waitUntil: 'networkidle' });
    console.log('Page loaded');
    
    let htmlClass = await page.evaluate(() => document.documentElement.className);
    console.log('Initial HTML class:', htmlClass);
    
    // Click the toggle
    await page.click('#theme-toggle');
    console.log('Clicked theme toggle');
    
    htmlClass = await page.evaluate(() => document.documentElement.className);
    console.log('After click HTML class:', htmlClass);
    
    let localStorageTheme = await page.evaluate(() => localStorage.getItem('theme'));
    console.log('LocalStorage theme:', localStorageTheme);
    
    // Get background color
    let bgColor = await page.evaluate(() => window.getComputedStyle(document.body).backgroundColor);
    console.log('Body background color:', bgColor);
    
  } finally {
    server.kill();
    await browser.close();
  }
})();
