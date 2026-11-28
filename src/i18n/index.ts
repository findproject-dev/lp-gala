import { id, type TranslationKey, type TranslationDict } from "./id";
import { en } from "./en";

export type Locale = "id" | "en";

export const DEFAULT_LOCALE: Locale = "id";
export const LOCALES: Locale[] = ["id", "en"];

export const translations: Record<Locale, TranslationDict> = {
  id,
  en,
};

export function t(locale: Locale, key: TranslationKey): string {
  return translations[locale]?.[key] ?? translations[DEFAULT_LOCALE][key];
}

export function stripLocalePrefix(pathname: string): string {
  if (pathname === "/en" || pathname === "/en/") return "/";
  if (pathname.startsWith("/en/")) return pathname.slice(3);
  return pathname || "/";
}

export function getLocalizedPath(pathname: string, targetLocale: Locale): string {
  const cleanPath = stripLocalePrefix(pathname);
  if (targetLocale === "id") {
    return cleanPath === "" ? "/" : cleanPath;
  }
  return cleanPath === "/" ? "/en" : `/en${cleanPath}`;
}

export type { TranslationKey, TranslationDict };
