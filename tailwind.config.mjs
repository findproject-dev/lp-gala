/** @type {import("tailwindcss").Config} */
export default {
  darkMode: 'class',
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      boxShadow: {
        'soft': '0 4px 24px -4px rgba(0, 0, 0, 0.2)',
        'soft-lg': '0 12px 48px -12px rgba(0, 0, 0, 0.3)',
      },
      colors: {
        background: "var(--color-background)",
        surface: "var(--color-surface)",
        "surface-elevated": "var(--color-surface-elevated)",
        primary: "var(--color-primary)",
        secondary: "var(--color-secondary)",
        accent: "var(--color-accent)",
        "accent-pink": "var(--color-accent-pink)",
        "primary-foreground": "var(--color-primary-foreground)",
        "secondary-foreground": "var(--color-secondary-foreground)",
        "accent-foreground": "var(--color-accent-foreground)",
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
        poller: ["'Poller One'", "cursive"],
      },
    },
  },
  plugins: [],
};
