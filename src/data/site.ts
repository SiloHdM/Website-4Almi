// Alle Fakten zu 4Almi an einer Stelle. Was hier steht, ist bestätigt;
// offene Punkte sind als TODO markiert.

export const site = {
  name: '4Almi',
  claim: 'Nicht nur ein gewöhnlicher Kiosk!',
  owner: 'Taylan „Almi“ Tepeoglu',
  ownerLegal: 'Taylan Tepeoglu',
  street: 'Lindenstraße 8',
  zip: '71634',
  city: 'Ludwigsburg',
  hoursShort: 'Mo–Sa 9:30–0 Uhr',
  hours: [
    { days: 'Montag – Samstag', time: '9:30 – 0:00 Uhr' },
    { days: 'Sonntag', time: 'geschlossen' },
  ],
  wolt: 'https://wolt.com/de/deu/ludwigsburg/venue/4almi-kiosk',
  maps: 'https://www.google.com/maps/search/?api=1&query=4Almi%2C+Lindenstra%C3%9Fe+8%2C+71634+Ludwigsburg',
  mapsEmbed: 'https://maps.google.com/maps?q=Lindenstra%C3%9Fe%208%2C%2071634%20Ludwigsburg&z=16&output=embed',
  press: {
    stuttgarterZeitung:
      'https://www.stuttgarter-zeitung.de/lokales/ludwigsburg/4almi-in-ludwigsburg-der-spaeti-mann-der-alles-besorgen-kann-78955235.html',
  },
  socials: [
    { label: 'TikTok', handle: '@4almilb', url: 'https://www.tiktok.com/@4almilb' },
    { label: 'TikTok', handle: '@4_almi', url: 'https://www.tiktok.com/@4_almi' },
    { label: 'Instagram', handle: '@4_almi', url: 'https://www.instagram.com/4_almi/' },
  ],
  // TODO: Telefon, E-Mail und USt-IdNr. für das Impressum
  phone: '[TODO: Telefonnummer]',
  email: '[TODO: E-Mail-Adresse]',
  vatId: '[TODO: USt-IdNr., falls vorhanden]',
};
