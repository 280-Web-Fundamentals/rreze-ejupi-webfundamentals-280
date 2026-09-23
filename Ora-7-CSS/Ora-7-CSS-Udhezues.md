# Aktiviteti 10 — Njoftimi me CSS
## Udhëzues

---

Orën e kaluar shtuam imazhe dhe lidhje në faqet tona, por deri tani gjithçka ka qenë "e zhveshur" — pa ngjyra, pa madhësi fontesh, pa asnjë stil. Sot njihemi me **CSS**, gjuha që i jep pamje HTML-it: ngjyra, madhësi, rreshtim, dhe shumë e shumë tjera.

Ky udhëzues shpjegon konceptet dhe hapat që i ndoqëm, në rendin e duhur.

---

## 1. Çfarë është CSS?

**CSS** është akronim për **Cascading Style Sheets**. CSS përshkruan **si** duken elementet e HTML-it në ekran — ngjyra, madhësi, hapësira, rreshtim, etj.

Duke e mbajtur CSS-in të ndarë nga HTML, mund të kontrollojmë pamjen e shumë dokumenteve HTML njëkohësisht, pa pasur nevojë të ndryshojmë çdo faqe veç e veç.

Ka **tre mënyra** kryesore për të shtuar CSS brenda një projekti:

1. **Inline CSS**
2. **Internal CSS** (ose Embedded)
3. **External CSS**

---

## 2. Inline CSS (CSS në rresht)

Inline CSS stilizon **një element specifik**, direkt brenda etiketës hapëse, duke përdorur atributin `style`.

```html
<h1 style="color:blue">Titulli im</h1>
<p style="color:orange">Ky është një paragraf.</p>
```

Stilizimi shkon gjithmonë në dyshe **property : value** (p.sh. `color:red` e bën tekstin e kuq).

> 💡 **Property** (karakteristika, p.sh. `color`) dhe **value** (vlera, p.sh. `red`) ndahen me `:`, dhe çdo dyshe mbyllet me `;` kur ka më shumë se një.

**Avantazhet:** e shpejtë dhe e lehtë për t'u shtuar, nuk kërkon file shtesë.

**Disavantazhet:** nëse duhet të stilizosh 10 paragrafë njësoj, duhesh ta përsërisësh 10 herë — struktura e HTML-it bëhet e çrregullt dhe faqja "peshon" më shumë.

---

## 3. CSS sintaksa — Selector + Declaration

Përveç inline CSS, mënyrat e tjera (Internal dhe External) ndjekin një sintaksë të caktuar:

```css
p {
  color: red;
}
```

- **Selector** (`p`) — tregon **cilin** element HTML dëshirojmë ta stilizojmë. Nëse duam të stilizojmë një element tjetër, thjesht ndryshojmë selektorin (p.sh. nga `p` në `h1`).
- **Declaration** (`color: red;`) — vetë rregulli brenda kllapave gjarpëruese `{ }`, i ndërtuar nga **property** (`color`) dhe **value** (`red`).

> 💡 Mund të kesh sa property-value dyshe të duash brenda një selektori — çdo dyshe në rreshtin e vet, e ndarë me `;`.

---

## 4. Internal CSS (CSS i brendshëm)

Internal CSS shkruhet **brenda vetë dokumentit HTML**, jo në një file të veçantë. Shtojmë një element `<style>` brenda `<head>`, dhe brenda tij shkruajmë rregulla sipas sintaksës së mësipërme.

```html
<head>
  <title>Faqja ime</title>
  <style>
    h2 {
      color: green;
    }
  </style>
</head>
```

Këtu të gjitha `<h2>` të faqes do të shfaqen jeshile, pa pasur nevojë të prekim asnjë `<h2>` veç e veç.

---

## 5. External CSS (CSS i jashtëm)

Metoda **më efikase** dhe më e përdorura në industri. CSS-i shkruhet në një **file të veçantë**, plotësisht të ndarë nga HTML-i.

**Hapat:**

1. Brenda folderit të projektit krijojmë një folder të ri me emrin `css`.
2. Brenda tij krijojmë një file `style.css` (ose `main.css`).
3. E lidhim atë file me HTML-in duke përdorur elementin `<link>` brenda `<head>`:

```html
<head>
  <title>Faqja ime</title>
  <link rel="stylesheet" href="css/style.css">
</head>
```

```css
/* css/style.css */
body {
  background-color: #673AB7;
}
```

**Avantazhet:** kontroll i plotë mbi strukturën, HTML-i mbetet i pastër, faqja ngarkohet më shpejt (browser-i e "cache-on" file-in CSS).

**Disavantazhet:** praktikisht asnjë — për këtë arsye është metoda e preferuar.

> 💡 Rregull i përgjithshëm: sa më i madh projekti, aq më e domosdoshme bëhet External CSS. Inline dhe Internal janë të mira për t'u mësuar, por në praktikë përdoret External.

---

## 6. Cascading — pse "Cascading" Style Sheets?

Çka ndodh nëse i njëjti element ka **dy** rregulla që përplasen me njëra-tjetrën?

```css
p {
  color: red;
}

p {
  color: orange;
}
```

Këtu të dy selektorët synojnë `<p>`. Fiton rregulli i shkruar **më poshtë** — pra paragrafi do të jetë portokalli, jo i kuq.

> ⚠️ Kjo është pikërisht ideja e "Cascading" (rrjedhje/kaskadë): kur ka konflikt mes rregullave, browser-i i "rrjedh" nga lart-poshtë dhe zbaton të fundit.

---

## Ushtrimet që bëmë në klasë

### Detyra 1 — Inline CSS

1. Krijo një `<h1>` me përmbajtje sipas dëshirës.
2. Shto një `<p>` me përmbajtje sipas dëshirës.
3. Me atributin `style`, bëj `<h1>` me ngjyrë **blu** dhe `<p>` me ngjyrë **portokalli**.

**Pesha e detyrës: 100 pikë**

### Detyra 2 — Internal CSS

1. Shto edhe një `<h2>` me përmbajtje sipas dëshirës.
2. Shto Internal CSS (elementin `<style>` brenda `<head>`).
3. Bëj që `<h2>` të shfaqet me ngjyrë **jeshile**.

**Pesha e detyrës: 100 pikë**

### Detyra 3 — External CSS: Lyrics Page

Vazhduam Lyrics Page-n dhe i shtuam CSS për herë të parë, këtë herë si file i jashtëm:

- Krijuam një file CSS dhe e lidhëm me `<link>` te HTML-i.
- **`body`** — ngjyra e prapavijës `#673AB7`.
- **`h1`** (titulli i këngës) — madhësia e fontit `40px`, ngjyra `#FFEB3B`.
- **`h2`** (emri i këngëtarit/es) — madhësia e fontit `25px`, ngjyra `#FFC107`.
- **`p`** (teksti i këngës) — madhësia e fontit `18px`, ngjyra `#CDDC39`.
- **`em`** (refreni) — ngjyra `#FF5722`.
- Tek `p`, `h1` dhe `h2` përdorëm edhe `text-align: center;`, që i vendos në qendër horizontalisht.

**Pesha e detyrës: 300 pikë**

---

## Përmbledhje e shpejtë

```
1. CSS = Cascading Style Sheets -- përshkruan si duken elementet e HTML-it
2. Tre mënyra: Inline (style="..." brenda etiketës), Internal (<style> brenda head),
   External (file .css i veçantë, i lidhur me <link>)
3. Sintaksa: selector { property: value; } -- selektori zgjedh elementin
4. External CSS = metoda e preferuar: HTML i pastër, faqe më e shpejtë
5. "Cascading" = kur dy rregulla përplasen për të njëjtin element, fiton ai
   që gjendet më poshtë
6. CSS Mini Cheat Sheet: color, background-color, font-size, text-align
```

---

## Fjalë të shkurtra

- **CSS** — Cascading Style Sheets, gjuha që stilizon HTML-in
- **Inline CSS** — stil i vendosur direkt brenda etiketës, me atributin `style`
- **Internal CSS** — stil i vendosur brenda `<style>`, tek `<head>` i dokumentit
- **External CSS** — stil i vendosur në një file `.css` të veçantë, i lidhur me `<link>`
- **Selector** — pjesa që tregon cilin element HTML po stilizojmë (p.sh. `p`, `h1`)
- **Declaration** — rregulli brenda `{ }`, i ndërtuar nga property + value
- **Property** — karakteristika që ndryshojmë (p.sh. `color`, `font-size`)
- **Value** — vlera që i japim një property-je (p.sh. `red`, `18px`)
- **Cascading** — parimi sipas të cilit rregulli i fundit i shkruar fiton kur ka konflikt

---

## 🎯 Sfida jote (pikë ekstra)

Tek Lyrics Page-n që ndërtove, shto edhe një selektor për `<strong>` (nëse e ke përdorur diku në tekst) me një ngjyrë sipas dëshirës. Pastaj, provo qëllimisht të shkruash **dy herë** të njëjtin selektor (p.sh. dy herë `p { color: ...; }`) me ngjyra të ndryshme, dhe vër re vetë cila ngjyrë "fiton" — a përputhet me atë çka mësuam te Cascading?
