# Website 4Almi

Die Website für 4Almi, den Späti in der Lindenstraße 8 in Ludwigsburg. Gebaut mit [Astro](https://astro.build) als statische Seite.

## Lokal starten

Voraussetzung: Node.js 18.20 oder neuer.

```bash
npm install
npm run dev       # Entwicklungsserver auf http://localhost:4321
npm run build     # fertige Seite nach dist/ bauen
npm run preview   # gebaute Seite lokal ansehen
```

Den Ordner `dist/` kann man bei jedem statischen Hoster hochladen, zum Beispiel Netlify, Vercel oder Cloudflare Pages.

## Wo was steht

- `src/data/site.ts`: Adresse, Öffnungszeiten, Links und Impressumsdaten an einer Stelle
- `src/components/`: die einzelnen Abschnitte der Startseite
- `src/pages/`: Startseite, Impressum, Datenschutz
- `src/assets/media/`: alle Originalfotos; Astro macht daraus beim Build WebP und AVIF
- `src/assets/hero-almi.jpg`, `src/assets/logo-4almi.png`: aus den Originalen erzeugt (Schwarz-Weiß-Porträt, freigestelltes Logo)
- `src/styles/global.css`: Farben aus dem Logo und Grundstil

## Offene Punkte vor dem Livegang

- Telefon, E-Mail und USt-IdNr. in `src/data/site.ts` eintragen
- Echte Domain in `astro.config.mjs` eintragen
- Hosting-Anbieter und Speicherdauer der Logfiles in der Datenschutzerklärung ergänzen
- Impressum und Datenschutzerklärung rechtlich prüfen lassen
