import re

with open("src/components/Header.astro", "r") as f:
    content = f.read()

# Add imports
if 'import { Sun, Moon } from "lucide-astro";' not in content:
    content = content.replace("---\n// src/components/Header.astro\n", "---\n// src/components/Header.astro\nimport { Sun, Moon } from \"lucide-astro\";\n")

# Desktop Theme Toggle & CTA
desktop_replacement = """      <div class="hidden md:flex items-center gap-4">
        <!-- Theme Toggle -->
        <button
          id="theme-toggle"
          class="flex items-center justify-center w-10 h-10 rounded-full border border-border bg-surface text-text-primary transition-all duration-300 hover:border-white/20 hover:bg-surface-elevated hover:shadow-lg focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary group"
          aria-label="Toggle Theme"
        >
          <Sun class="w-5 h-5 hidden dark:block text-text-primary group-hover:text-accent transition-colors" />
          <Moon class="w-5 h-5 block dark:hidden text-text-primary group-hover:text-primary transition-colors" />
        </button>

        <!-- CTA Button -->
        <a
          href="#contact"
          class="inline-block bg-gradient-to-r from-primary to-secondary text-white border border-white/10 shadow-lg shadow-primary/25 text-white text-sm font-semibold py-3 px-6 rounded-xl shadow-lg shadow-primary/25 transition-all duration-300 hover:scale-[1.02] hover:brightness-110 hover:shadow-xl shadow-primary/40 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary"
        >
          Konsultasi Gratis
        </a>
      </div>"""

# Find desktop CTA
content = re.sub(r'<!-- Desktop CTA Button -->.*?</div>', desktop_replacement, content, flags=re.DOTALL)

# Mobile Theme Toggle next to Hamburger
mobile_toggle = """      <div class="md:hidden flex items-center gap-3">
        <!-- Mobile Theme Toggle -->
        <button
          id="mobile-theme-toggle"
          class="flex items-center justify-center w-10 h-10 rounded-full border border-border bg-surface text-text-primary transition-all duration-300 hover:border-white/20 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary group"
          aria-label="Toggle Theme"
        >
          <Sun class="w-5 h-5 hidden dark:block text-text-primary group-hover:text-accent transition-colors" />
          <Moon class="w-5 h-5 block dark:hidden text-text-primary group-hover:text-primary transition-colors" />
        </button>

        <!-- Hamburger Button -->"""

content = content.replace('<!-- Hamburger Button (Mobile Only) -->', mobile_toggle)
content = content.replace('      </button>\n    </div>', '      </button>\n      </div>\n    </div>')

# Add script
script_addition = """
  // Theme Toggle Logic
  const themeToggle = document.getElementById("theme-toggle");
  const mobileThemeToggle = document.getElementById("mobile-theme-toggle");

  function toggleTheme() {
    const isDark = document.documentElement.classList.contains("dark");
    if (isDark) {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("theme", "light");
    } else {
      document.documentElement.classList.add("dark");
      localStorage.setItem("theme", "dark");
    }
  }

  themeToggle?.addEventListener("click", toggleTheme);
  mobileThemeToggle?.addEventListener("click", toggleTheme);
"""

content = content.replace('// Event Listeners', script_addition + '\n  // Event Listeners')

with open("src/components/Header.astro", "w") as f:
    f.write(content)
