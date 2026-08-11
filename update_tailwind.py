with open("tailwind.config.mjs", "r") as f:
    config = f.read()

import re
replacement = """      colors: {
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
        "glass-10": "var(--color-white-opacity-10)",
        "glass-5": "var(--color-white-opacity-5)",
      },"""

config = re.sub(r'colors:\s*\{.*?(?=\},).*?\},', replacement, config, flags=re.DOTALL)

with open("tailwind.config.mjs", "w") as f:
    f.write(config)
