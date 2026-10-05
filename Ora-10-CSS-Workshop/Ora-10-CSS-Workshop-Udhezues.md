# Aktiviteti 11 — CSS Properties + Web Typography
## Udhëzues

---

Në orën e CSS-it mësuam si ta shtojmë CSS-in në një faqe dhe përdorëm disa property bazike si `color`, `background-color`, `font-size` dhe `text-align`. Sot e thellojmë: shohim mënyrat e ndryshme si mund të përcaktojmë një ngjyrë, dhe pastaj hyjmë në **Web Typography** — gjithçka që ka të bëjë me pamjen e tekstit në një faqe. Në fund mësojmë si të shtojmë një font të ri nga Google Fonts.

Ky udhëzues shpjegon konceptet dhe hapat që i ndoqëm, në rendin e duhur.

---

## 1. Çfarë është Web Typography?

**Tipografia e web-it** i referohet pamjes së të gjithë tekstit në një faqe. Brenda saj hyjnë disa veti themelore të tekstit — ato përcaktojnë pamjen, stilin, madhësinë, hapësirën mes shkronjave, hapësirën mes fjalëve, etj.

Në këtë orë i kaluam këto property, një nga një:

`color`, `background-color`, `word-spacing`, `letter-spacing`, `text-indent`, `text-align`, `text-decoration`, `text-transform`, `line-height`, pastaj fontet (`font-family`, `font-weight`).

---

## 2. `color` dhe `background-color`

- **`color`** — specifikon ngjyrën e tekstit.
- **`background-color`** — ngjyros prapavijën ku gjendet elementi.

```css
h1 {
  color: white;
  background-color: black;
}
```

Ngjyrën mund ta specifikojmë në disa mënyra. Tri prej tyre i përdorëm sot: **TEXT**, **RGB** dhe **HEX**.

> 💡 Ekzistojnë edhe mënyra të tjera si HSL dhe RGBA, por sot u fokusuam te tre të parat.

### TEXT — emri i ngjyrës

Shkruajmë direkt emrin e ngjyrës (p.sh. `blue`, `red`, `green`). Rreth **140 ngjyra** kanë emra që çdo shfletues i njeh.

### RGB — `rgb(red, green, blue)`

Secili nga tre parametrat specifikon intensitetin e ngjyrës përkatëse, nga **0 deri në 255**. Pra ngjyrat krijohen duke përzierë në mënyra të ndryshme tri ngjyrat kryesore (të kuqe, jeshile, blu) — njëlloj si diodat RGB të një ekrani.

```css
p {
  color: rgb(255, 0, 0); /* e kuqe */
}
```

### HEX — `#rrggbb`

Fillon **gjithmonë** me simbolin `#`, ku `rr` është red, `gg` është green dhe `bb` është blue. Numrat heksadecimalë janë:

```
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Pra A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.

```css
p {
  color: #ff0000; /* e kuqe */
}
```

Të tre shembujt më sipër — `red`, `rgb(255, 0, 0)` dhe `#ff0000` — japin saktësisht të njëjtën ngjyrë.

---

## 3. `word-spacing` — hapësira mes fjalëve

Zgjeron ose ngushton hapësirën **mes fjalëve** brenda një teksti.

```css
p {
  word-spacing: 15px; /* secila fjalë 15px larg tjetrës */
}
```

Për ta **ngushtuar**, mjafton t'i japim vlerë negative, p.sh. `-15px`.

---

## 4. `letter-spacing` — hapësira mes shkronjave

Zgjeron ose ngushton hapësirën **mes shkronjave** brenda një teksti.

```css
h1 {
  letter-spacing: 15px; /* secila shkronjë 15px larg tjetrës */
}
```

Edhe këtu, vlera negative (p.sh. `-15px`) e ngushton.

> 💡 Mos i ngatërro: `word-spacing` punon mes **fjalëve**, `letter-spacing` mes **shkronjave**.

---

## 5. `text-indent` — shtyrja e rreshtit të parë

Shtyn ose tërheq fillimin e **rreshtit të parë** brenda një paragrafi.

```css
p {
  text-indent: 30px; /* rreshti i parë shtyhet 30px djathtas */
}
```

Me vlerë negative (p.sh. `-30px`) rreshti i parë tërhiqet nga ana e majtë.

---

## 6. `text-align` — pozicionimi horizontal

Përdoret për pozicionimin **horizontal** të tekstit. Ka katër vlera kryesore:

- **`left`** — vlera e paracaktuar (by default), teksti sa më majtas.
- **`center`** — teksti në mes të hapësirës.
- **`right`** — teksti sa më djathtas.
- **`justify`** — i shtrin linjat që secila vijë të ketë gjerësi të barabartë.

```css
h1 {
  text-align: center;
}

p {
  text-align: justify;
}
```

---

## 7. `text-decoration` — dekorimi i tekstit

Përdoret për dekorimin e tekstit. Vlerat kryesore:

- **`overline`** — shton një vijë në pjesën e sipërme të tekstit.
- **`line-through`** — shton një vijë përmes tekstit, në mes.
- **`underline`** — shton një nënvizim në pjesën e poshtme.
- **`underline overline`** — kombinim i të dyjave.

```css
h2 {
  text-decoration: underline;
}

p {
  text-decoration: line-through;
}
```

---

## 8. `text-transform` — ndryshimi i shkronjave

Ndryshon shkronjat e një teksti, pa e prekur tekstin në HTML. Tri vlera kryesore:

- **`uppercase`** — i kthen të gjitha shkronjat në të mëdha.
- **`lowercase`** — i kthen të gjitha shkronjat në të vogla.
- **`capitalize`** — shkronjën e parë të çdo fjale e kthen në të madhe.

```css
h1 {
  text-transform: uppercase;
}

p {
  text-transform: capitalize;
}
```

---

## 9. `line-height` — lartësia e rreshtit

Përdoret për të caktuar lartësinë e **secilit rresht** të tekstit. E ndryshojmë duke shtuar një masë me njësi matëse, në rastin tonë `px`:

```css
p {
  line-height: 50px;
}
```

---

## 10. Çfarë janë fontet?

Një **font** është një koleksion karakteresh me dizajn të ngjashëm. Këto karaktere përfshijnë shkronja të vogla dhe të mëdha, numra, shenja pikësimi dhe simbole.

Ndryshimi i fontit mund ta ndryshojë shumë pamjen dhe ndjesinë e një teksti. Disa fonte janë krijuar të jenë të thjeshta dhe të lehta për t'u lexuar, të tjerat për t'i dhënë tekstit një stil unik. Për shembull, **Arial** ka një pamje të thjeshtë, moderne, ndërsa **Palatino** ka një pamje më të vjetër, më tradicionale.

Për të gjetur dhe përdorur fonte të ndryshme këtë vit do të përdorim platformën **Google Fonts** (`fonts.google.com`).

### Font Families & Font Faces

Një **familje fonti** (font family) përbëhet nga disa **fytyra** (font faces). Secila fytyrë dallon nga të tjerat në:

- **peshë** (weight) — trashësia e fytyrës;
- **stil** (style) — a është teksti i tipit roman, italic, etj.

---

## 11. Shtimi i një fonti të ri nga Google Fonts

Hapat që ndoqëm:

1. Vizitojmë `fonts.google.com`.
2. Shohim katrorë të ndryshëm, secili me një font tjetër.
3. Zgjedhim njërin nga fontet. Kur klikojmë mbi të, na hapet faqja me specifikat e tij.
4. **Zgjedhim vetëm peshat që do të na duhen** në faqen tonë (shih paralajmërimin më poshtë).
5. Pasi zgjedhim peshat, hapet një meny në anën e djathtë. Zgjedhim opsionin **Embed**.
6. Aty marrim kodin për ta shtuar fontin në projekt. Ne e përdorëm pjesën me `<link>` — e kopjojmë dhe e vendosim brenda `<head>`, **para CSS-it tonë**.

```html
<head>
  <title>Faqja ime</title>

  <!-- linku nga Google Fonts (shembull me Roboto, peshat 100, 300, 900) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;900&display=swap" rel="stylesheet">

  <!-- CSS-i ynë vjen pas tyre -->
  <link rel="stylesheet" href="css/style.css">
</head>
```

> ⚠️ Mos zgjidh më shumë pesha sesa të duhen! Sa më shumë pesha të zgjedhura, aq më e ngadaltë bëhet faqja jonë gjatë hapjes.

---

## 12. `font-family` — i tregojmë faqes cilin font të përdorë

Edhe pse e shtuam linkun, **nuk do të shohim asnjë ndryshim** te teksti. Pse? Sepse duhet t'i tregojmë faqes **cilat elementë** duhet ta përdorin fontin e ri.

Për këtë përdorim property-n **`font-family`**, që specifikon fontin për një element. Nëse duam që gjithçka në dokument të jetë me fontin e marrë nga Google Fonts, e vendosim te selektori `body`:

```css
body {
  font-family: 'Roboto', sans-serif;
}
```

### Pse shkruajmë disa vlera?

Shohim një shembull klasik:

```css
p {
  font-family: Times, "Times New Roman", serif;
}
```

Kur faqja ngarkohet dhe fonti nuk gjendet, ndodh kjo zinxhir:

1. Browser-i kërkon fontin e parë: `Times`.
2. Nëse nuk e gjen, kërkon të dytin: `Times New Roman`.
3. Nëse as ky nuk gjendet, browser-i merr çfarëdo fonti të familjes së përgjithshme `serif` që ka të instaluar lokalisht.

> 💡 Rregull i mirë: fonti kryesor i parë, pastaj alternativat, dhe në fund gjithmonë një familje e përgjithshme (si `serif` ose `sans-serif`) si "rrjetë sigurie".

---

## 13. `font-weight` — pesha e fontit

Kur kemi zgjedhur pesha të ndryshme te Google Fonts, mund t'ia ndryshojmë peshën çdo elementi me property-n **`font-weight`**.

Për shembull, nëse kemi zgjedhur peshat 100, 300 dhe 900, dhe duam që një paragraf të ketë peshën 100:

```css
p {
  font-weight: 100;
}

h1 {
  font-weight: 900;
}
```

> ⚠️ Mund të përdorim vetëm peshat që i kemi zgjedhur te Google Fonts. Nëse kërkojmë një peshë që nuk e kemi shtuar në link, browser-i nuk do ta ketë atë fytyrë të fontit.

---

## Ushtrimet që bëmë në klasë

### Detyra 1 — Tipografia e një faqeje

Punuam mbi një faqe me tekst dhe praktikuam gjithçka që mësuam sot:

1. Zgjodhëm një font nga Google Fonts, me vetëm peshat që na duheshin, dhe e shtuam me `<link>` brenda `<head>`, para CSS-it tonë.
2. Me `font-family` te `body`, e aplikuam fontin në gjithë faqen (me një familje të përgjithshme si alternativë).
3. Me `font-weight`, i dhamë peshë të ndryshme titullit dhe paragrafit.
4. Provuam property-t e tekstit: `letter-spacing`, `word-spacing`, `text-indent`, `text-align`, `text-decoration`, `text-transform` dhe `line-height`.
5. Ngjyrat i vendosëm me `color` dhe `background-color`, duke provuar të tria mënyrat: emër, `rgb()` dhe hex.

---

## Përmbledhje e shpejtë

```
1. Web Typography = pamja e gjithë tekstit në faqe
2. color = ngjyra e tekstit; background-color = ngjyra e prapavijës
3. Ngjyrat: TEXT (red), RGB (rgb(255, 0, 0)), HEX (#ff0000) -- të tria japin të kuqe
4. word-spacing = hapësira mes fjalëve; letter-spacing = mes shkronjave
   (vlera negative i ngushton)
5. text-indent = shtyn rreshtin e parë të paragrafit
6. text-align: left | center | right | justify
7. text-decoration: overline | line-through | underline | underline overline
8. text-transform: uppercase | lowercase | capitalize
9. line-height = lartësia e secilit rresht (p.sh. 50px)
10. Font = koleksion karakteresh; family = disa fytyra (peshë + stil)
11. Google Fonts: zgjedh vetëm peshat që të duhen -> Embed -> <link> në <head>,
    para CSS-it
12. font-family (te body) = cilin font përdorim; vlera të shumta = fallback
13. font-weight = trashësia, vetëm nga peshat që i kemi zgjedhur
```

---

## Fjalë të shkurtra

- **Web Typography** — pamja e gjithë tekstit në një faqe web
- **color** — property që specifikon ngjyrën e tekstit
- **background-color** — property që ngjyros prapavijën e një elementi
- **RGB** — ngjyrë e krijuar nga përzierja e red, green, blue, secila nga 0 deri në 255
- **HEX** — vlerë heksadecimale e ngjyrës, `#rrggbb`
- **word-spacing** — hapësira mes fjalëve
- **letter-spacing** — hapësira mes shkronjave
- **text-indent** — shtyrja e rreshtit të parë të paragrafit
- **text-align** — pozicionimi horizontal i tekstit (`left`, `center`, `right`, `justify`)
- **text-decoration** — dekorimi i tekstit (`overline`, `line-through`, `underline`)
- **text-transform** — ndryshimi i shkronjave (`uppercase`, `lowercase`, `capitalize`)
- **line-height** — lartësia e një rreshti teksti
- **Font** — koleksion karakteresh me dizajn të ngjashëm
- **Font family** — familje fonti, e përbërë nga disa fytyra
- **Font face** — një fytyrë e vetme e familjes, që dallon nga pesha ose stili
- **Google Fonts** — platforma ku gjejmë dhe marrim fonte për faqet tona
- **font-family** — property që tregon cilin font përdor një element
- **font-weight** — property që cakton trashësinë e fontit

---

## 🎯 Sfida jote (pikë ekstra)

Ndërto një faqe të vogël "poster" me një `<h1>`, një `<h2>` dhe dy paragrafë, dhe përdor sa më shumë nga property-t e sotme:

- Shto një font nga Google Fonts me **dy ose tri pesha** dhe aplikoje te `body` me një fallback.
- Titulli me `text-transform: uppercase`, `letter-spacing` dhe `text-align: center`.
- Njëri paragraf me `text-indent` dhe `line-height`, tjetri me `text-align: justify`.
- Përdor të tri mënyrat e ngjyrave (emër, `rgb()` dhe hex) për elementë të ndryshëm.

Pastaj ndrysho qëllimisht emrin e fontit te `font-family` me një që nuk ekziston, dhe vër re çfarë fonti shfaq browser-i — a përputhet me atë çka mësuam për fallback?
