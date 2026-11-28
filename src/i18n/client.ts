import {
  translations,
  getLocalizedPath,
  type Locale,
  type TranslationKey,
} from "./index";

const STORAGE_KEY = "galacode_lang";
const WA_BASE = "https://wa.me/6281919564548?text=";

export function getCurrentLanguage(): Locale {
  if (typeof document !== "undefined") {
    const htmlLang = document.documentElement.lang;
    if (htmlLang === "en" || htmlLang === "id") return htmlLang;
  }
  if (typeof localStorage !== "undefined") {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === "en" || saved === "id") return saved;
  }
  return "id";
}

export function applyLanguage(
  lang: Locale,
  options: { updateUrl?: boolean } = {}
): void {
  const dict = translations[lang] || translations.id;

  if (typeof localStorage !== "undefined") {
    localStorage.setItem(STORAGE_KEY, lang);
  }
  document.documentElement.lang = lang;

  // 1. Update textContent
  document.querySelectorAll<HTMLElement>("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n") as TranslationKey | null;
    if (key && key in dict) {
      el.textContent = dict[key];
    }
  });

  // 2. Update innerHTML (for headings with inline spans/br)
  document.querySelectorAll<HTMLElement>("[data-i18n-html]").forEach((el) => {
    const key = el.getAttribute("data-i18n-html") as TranslationKey | null;
    if (key && key in dict) {
      el.innerHTML = dict[key];
    }
  });

  // 3. Update placeholders
  document
    .querySelectorAll<HTMLInputElement | HTMLTextAreaElement>(
      "[data-i18n-placeholder]"
    )
    .forEach((el) => {
      const key = el.getAttribute(
        "data-i18n-placeholder"
      ) as TranslationKey | null;
      if (key && key in dict) {
        el.placeholder = dict[key];
      }
    });

  // 4. Update aria-labels
  document.querySelectorAll<HTMLElement>("[data-i18n-aria]").forEach((el) => {
    const key = el.getAttribute("data-i18n-aria") as TranslationKey | null;
    if (key && key in dict) {
      el.setAttribute("aria-label", dict[key]);
    }
  });

  // 5. Update WhatsApp links
  document.querySelectorAll<HTMLAnchorElement>("[data-i18n-wa]").forEach((el) => {
    const key = el.getAttribute("data-i18n-wa") as TranslationKey | null;
    if (key && key in dict) {
      el.href = `${WA_BASE}${encodeURIComponent(dict[key])}`;
    }
  });

  // 6. Update internal navigation links
  document.querySelectorAll<HTMLAnchorElement>('a[href^="/"]').forEach((a) => {
    const baseHref =
      a.getAttribute("data-base-href") || a.getAttribute("href") || "/";
    if (!a.hasAttribute("data-base-href")) {
      a.setAttribute("data-base-href", baseHref);
    }
    const [pathPart, hashPart] = baseHref.split("#");
    const localized = getLocalizedPath(pathPart || "/", lang);
    a.setAttribute("href", hashPart ? `${localized}#${hashPart}` : localized);
  });

  // 7. Update <title>, meta description, og tags & canonical
  const pageKey = document.documentElement.getAttribute("data-page-key");
  if (pageKey) {
    const titleKey = `meta.${pageKey}.title` as TranslationKey;
    const descKey = `meta.${pageKey}.description` as TranslationKey;
    if (titleKey in dict) {
      document.title = dict[titleKey];
      const ogTitle = document.querySelector('meta[property="og:title"]');
      if (ogTitle) ogTitle.setAttribute("content", dict[titleKey]);
    }
    if (descKey in dict) {
      const metaDesc = document.querySelector('meta[name="description"]');
      if (metaDesc) metaDesc.setAttribute("content", dict[descKey]);
      const ogDesc = document.querySelector('meta[property="og:description"]');
      if (ogDesc) ogDesc.setAttribute("content", dict[descKey]);
    }
  }

  // 8. Update switcher UI
  document.querySelectorAll<HTMLElement>(".lang-current-label").forEach((el) => {
    el.textContent = lang.toUpperCase();
  });

  document.querySelectorAll<HTMLElement>(".lang-option").forEach((btn) => {
    const btnLang = btn.getAttribute("data-lang");
    const isActive = btnLang === lang;
    btn.setAttribute("aria-checked", isActive ? "true" : "false");
    const check = btn.querySelector(".lang-check");
    if (isActive) {
      btn.classList.add("text-primary", "bg-primary/10", "font-bold");
      btn.classList.remove("text-text-secondary");
      if (check) check.classList.remove("opacity-0");
    } else {
      btn.classList.remove("text-primary", "bg-primary/10", "font-bold");
      btn.classList.add("text-text-secondary");
      if (check) check.classList.add("opacity-0");
    }
  });

  // 9. Update browser URL without reload
  if (options.updateUrl) {
    const newPath = getLocalizedPath(window.location.pathname, lang);
    const nextUrl = `${newPath}${window.location.search}${window.location.hash}`;
    if (window.location.pathname + window.location.search + window.location.hash !== nextUrl) {
      window.history.replaceState({}, "", nextUrl);
    }
    const canonical = document.querySelector('link[rel="canonical"]');
    if (canonical) {
      canonical.setAttribute("href", `${window.location.origin}${newPath}`);
    }
  }

  window.dispatchEvent(
    new CustomEvent("galacode:langchange", { detail: { lang } })
  );
}
