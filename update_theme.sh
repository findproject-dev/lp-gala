#!/bin/bash

# Update global.css
cat << 'CSS' > src/styles/global.css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --color-background: #FFFFFF;
    --color-surface: #F8FAFC;
    --color-surface-elevated: #FFFFFF;
    --color-primary: #6D5EF7;
    --color-secondary: #8B5CF6;
    --color-accent: #38BDF8;
    --color-accent-pink: #EC4899;
    --color-foreground: #0F172A;
    --color-foreground-secondary: #475569;
    --color-foreground-muted: #64748B;
    --color-border: #E2E8F0;
    
    /* Semantic Glass/Translucent tokens for Light Mode (uses black) */
    --color-glass-5: rgba(0, 0, 0, 0.02);
    --color-glass-10: rgba(0, 0, 0, 0.05);
    --color-glass-20: rgba(0, 0, 0, 0.1);
    --color-glass-30: rgba(0, 0, 0, 0.15);
    --color-glass-40: rgba(0, 0, 0, 0.2);
    --color-glass-50: rgba(0, 0, 0, 0.25);
  }

  .dark {
    --color-background: #020617;
    --color-surface: #0F172A;
    --color-surface-elevated: #111827;
    --color-primary: #6D5EF7;
    --color-secondary: #8B5CF6;
    --color-accent: #38BDF8;
    --color-accent-pink: #EC4899;
    --color-foreground: #F8FAFC;
    --color-foreground-secondary: #CBD5E1;
    --color-foreground-muted: #94A3B8;
    --color-border: rgba(255, 255, 255, 0.08);
    
    /* Semantic Glass/Translucent tokens for Dark Mode (uses white) */
    --color-glass-5: rgba(255, 255, 255, 0.05);
    --color-glass-10: rgba(255, 255, 255, 0.1);
    --color-glass-20: rgba(255, 255, 255, 0.2);
    --color-glass-30: rgba(255, 255, 255, 0.3);
    --color-glass-40: rgba(255, 255, 255, 0.4);
    --color-glass-50: rgba(255, 255, 255, 0.5);
  }

  /* Transition for theme switching */
  body {
    @apply transition-colors duration-300;
  }
}
CSS

# Update tailwind.config.mjs
cat << 'JS' > tailwind.config.mjs
/** @type {import("tailwindcss").Config} */
export default {
  darkMode: 'class',
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        background: "var(--color-background)",
        surface: "var(--color-surface)",
        "surface-elevated": "var(--color-surface-elevated)",
        primary: "var(--color-primary)",
        secondary: "var(--color-secondary)",
        accent: "var(--color-accent)",
        "accent-pink": "var(--color-accent-pink)",
        "text-primary": "var(--color-foreground)",
        "text-secondary": "var(--color-foreground-secondary)",
        "text-muted": "var(--color-foreground-muted)",
        border: "var(--color-border)",
        divider: "var(--color-border)",
        "glass-5": "var(--color-glass-5)",
        "glass-10": "var(--color-glass-10)",
        "glass-20": "var(--color-glass-20)",
        "glass-30": "var(--color-glass-30)",
        "glass-40": "var(--color-glass-40)",
        "glass-50": "var(--color-glass-50)",
      },
      keyframes: {
        twinkle: {
          "0%, 100%": { opacity: "0.1", transform: "scale(0.8)" },
          "50%": { opacity: "0.6", transform: "scale(1.2)" },
        },
      },
      animation: {
        twinkle: "twinkle 5s ease-in-out infinite",
      },
      fontFamily: {
        inter: ["Inter", "sans-serif"],
      },
    },
  },
  plugins: [],
};
JS
