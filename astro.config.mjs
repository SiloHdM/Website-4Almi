import { defineConfig } from 'astro/config';

// Netlify setzt beim Build URL auf die Hauptadresse der Seite (eigene Domain, sobald verbunden).
// Wird für die Vorschau beim Teilen (og:image) und die Firmendaten für Google gebraucht.
export default defineConfig({
  site: process.env.URL ?? 'http://localhost:4321',
});
