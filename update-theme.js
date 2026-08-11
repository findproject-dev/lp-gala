const fs = require('fs');

const tailwindPath = './tailwind.config.mjs';
let tw = fs.readFileSync(tailwindPath, 'utf8');

// Add subtle shadows
tw = tw.replace('extend: {', `extend: {
      boxShadow: {
        'soft': '0 4px 24px -4px rgba(0, 0, 0, 0.2)',
        'soft-lg': '0 12px 48px -12px rgba(0, 0, 0, 0.3)',
      },`);

fs.writeFileSync(tailwindPath, tw);

const globalCssPath = './src/styles/global.css';
let css = fs.readFileSync(globalCssPath, 'utf8');
css = css.replace('--color-border: #E2E8F0;', '--color-border: #E5E7EB;');
css = css.replace('--color-border: rgba(255, 255, 255, 0.08);', '--color-border: rgba(255, 255, 255, 0.05);');
css = css.replace('--color-glass-5: rgba(255, 255, 255, 0.05);', '--color-glass-5: rgba(255, 255, 255, 0.03);');
fs.writeFileSync(globalCssPath, css);

console.log('Updated theme variables');
