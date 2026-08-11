import re

with open("src/components/Header.astro", "r") as f:
    content = f.read()

# Remove the old script completely
content = re.sub(r'<script is:inline>.*?</script>', '', content, flags=re.DOTALL)

# Add the new standard module script with event delegation
new_script = """
<script>
  // Event delegation to avoid issues with bubbling from SVG children
  document.addEventListener("click", (e) => {
    const toggleBtn = e.target.closest("#theme-toggle, #mobile-theme-toggle");
    if (toggleBtn) {
      e.preventDefault();
      const isDark = document.documentElement.classList.contains("dark");
      if (isDark) {
        document.documentElement.classList.remove("dark");
        localStorage.setItem("theme", "light");
      } else {
        document.documentElement.classList.add("dark");
        localStorage.setItem("theme", "dark");
      }
    }
  });

  // Handle active route highlighting
  const currentPath = window.location.pathname;
  document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("text-text-primary");
      link.classList.remove("text-text-secondary");
      const indicator = link.querySelector(".nav-indicator");
      if (indicator) {
        indicator.classList.remove("scale-x-0");
        indicator.classList.add("scale-x-100");
      }
    }
  });

  document.querySelectorAll(".mobile-nav-link").forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("text-primary");
      link.classList.remove("text-text-secondary");
    }
  });

  // Handle scroll for floating navbar
  const header = document.getElementById("main-header");
  const navContainer = document.getElementById("nav-container");
  
  function handleScroll() {
    if (window.scrollY > 20) {
      if(header) {
        header.classList.add("py-3", "md:py-4");
        header.classList.remove("py-6", "md:py-8");
      }
      if(navContainer) {
        navContainer.classList.add("bg-surface/95", "backdrop-blur-md", "border-border", "shadow-lg", "shadow-black/50", "px-6", "py-3", "rounded-[24px]");
        navContainer.classList.remove("py-0", "px-0", "rounded-none", "border-transparent", "bg-transparent");
      }
    } else {
      if(header) {
        header.classList.add("py-6", "md:py-8");
        header.classList.remove("py-3", "md:py-4");
      }
      if(navContainer) {
        navContainer.classList.remove("bg-surface/95", "backdrop-blur-md", "border-border", "shadow-lg", "shadow-black/50", "px-6", "py-3", "rounded-[24px]");
        navContainer.classList.add("py-0", "px-0", "rounded-none", "border-transparent", "bg-transparent");
      }
    }
  }
  
  window.addEventListener("scroll", handleScroll);
  handleScroll(); // Initialize on load

  // Mobile menu toggle logic
  const menuToggle = document.getElementById("menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");
  const line1 = document.getElementById("hamburger-line-1");
  const line2 = document.getElementById("hamburger-line-2");
  const line3 = document.getElementById("hamburger-line-3");
  
  let isMenuOpen = false;
  
  function toggleMobileMenu() {
    isMenuOpen = !isMenuOpen;
    if(menuToggle) menuToggle.setAttribute("aria-expanded", isMenuOpen ? "true" : "false");
    if(mobileMenu) mobileMenu.setAttribute("aria-hidden", isMenuOpen ? "false" : "true");

    if (isMenuOpen) {
      if(mobileMenu) {
        mobileMenu.classList.remove("opacity-0", "pointer-events-none", "translate-y-[-10px]");
        mobileMenu.classList.add("opacity-100", "pointer-events-auto", "translate-y-0");
      }
      document.body.style.overflow = "hidden";
      if(line1) line1.setAttribute("transform", "rotate(45) translate(6, -6)");
      if(line2) line2.classList.add("opacity-0");
      if(line3) line3.setAttribute("transform", "rotate(-45) translate(-6, -6)");
    } else {
      if(mobileMenu) {
        mobileMenu.classList.add("opacity-0", "pointer-events-none", "translate-y-[-10px]");
        mobileMenu.classList.remove("opacity-100", "pointer-events-auto", "translate-y-0");
      }
      document.body.style.overflow = "";
      if(line1) line1.removeAttribute("transform");
      if(line2) line2.classList.remove("opacity-0");
      if(line3) line3.removeAttribute("transform");
    }
  }

  if (menuToggle) {
    menuToggle.addEventListener("click", toggleMobileMenu);
  }

  document.querySelectorAll(".mobile-nav-link, .mobile-menu-cta").forEach((el) => {
    el.addEventListener("click", () => {
      if (isMenuOpen) toggleMobileMenu();
    });
  });
</script>
"""

content += new_script

with open("src/components/Header.astro", "w") as f:
    f.write(content)
