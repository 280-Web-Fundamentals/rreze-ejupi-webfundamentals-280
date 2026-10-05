# Rifreskim i Orëve 1–7
## Udhëzues

---

Para se të vazhdojmë përpara, ndalemi një orë të tërë për të rikujtuar çka mësuam deri tani — nga themelet e UI/UX-it e Figma-s, tek hapat e parë në HTML dhe CSS. Ky udhëzues përmbledh konceptet kryesore të çdo ore, në rendin e duhur, si përgatitje për pyetjet praktike që vijojnë.

---

## 1. UI/UX & Frontend vs Backend (Ora 1)

**Front-end Development** është pjesa e web-it që e sheh dhe e përdor useri direkt në browser. **Back-end Development** është logjika "prapa skenave" — serveri, të dhënat, gjithçka që s'shihet drejtpërdrejt.

**UI (User Interface)** është pamja vizuale e një produkti — ngjyrat, fontet, butonat, layout-i. **UX (User Experience)** është si ndihet useri teksa e përdor atë produkt — a është e lehtë, e kuptueshme, pa konfuzion.

Kur zgjedhim ngjyra për një dizajn, mbahemi zakonisht pranë një palete të ngjashme me logon e produktit. Kur zgjedhim fonte, përdorim maksimumi 1–2 stile, që faqja të mbetet e qartë dhe konsistente.

---

## 2. Figma — Hapësira dhe format bazike (Ora 2)

**Figma** është aplikacioni web që përdorim për të dizajnuar — punon direkt në browser, pa instalim.

**Frame** (shkurtorja `F`) është "faqja" ku dizajnojmë — çdo projekt fillon me një Frame.

Format bazike që përdorëm:

- **Rectangle** (`R`) dhe **Ellipse** (`O`) — duke mbajtur `Shift` gjatë vizatimit, forma ruan proporcionin (p.sh. katror i përsosur ose rreth i përsosur).

Parametrat kryesorë të një elementi:

- **Fill** — ngjyra e brendshme e formës.
- **Corner radius** — sa të rrumbullakosura janë qoshet.
- **Opacity** — sa transparent është elementi.

**Layer** është çdo element që shtojmë në Figma; renditja e layer-ave (lart/poshtë) përcakton çfarë shfaqet përpara e çfarë prapa.

---

## 3. Figma — Stroke, Effects, Text (Ora 3)

**Stroke** është kufiri (konturi) i një forme — ka trashësi, dhe mund të vendoset nga tri anë: **inside**, **outside**, ose **center**.

**Effects → Drop Shadow** i shton një hije formës, e kontrollueshme nga katër parametra: **X**, **Y**, **Blur**, dhe **Spread**, plus transparenca e vetë hijes.

**Text Tool** (shkurtorja `T`) mund të përdoret në dy mënyra: duke tërhequr një kuti me gjerësi fikse, ose thjesht duke klikuar një herë (teksti zgjerohet vetë). Parametrat kryesorë të tekstit janë font-i, trashësia (weight), madhësia, line height, dhe letter spacing.

**Groups** (grupet): `CTRL + G` grupon disa elementë (layers) të përzgjedhura në një njësi të vetme, që lëvizin/modifikohen bashkë. `ALT` + zvarritje (drag) mbi një grup krijon një duplikatë të shpejtë të tij.

---

## 4. Figma — Projekt Based (Ora 4)

Një sfidë **"Project Based"** do të thotë rikrijimi i një dizajni ekzistues sa më saktë të jetë e mundur, element pas elementi.

Për ta bërë këtë saktë:

1. Klikojmë mbi elementet e dizajnit origjinal për të lexuar vlerat e sakta (ngjyrë, madhësi, font, distancë).
2. Fillojmë nga struktura e madhe (Frame-i, format kryesore), pastaj shtojmë detajet.
3. Krahasojmë vazhdimisht me origjinalin gjatë punës — jo vetëm në fund.
4. Kontrollojmë çdo element kundrejt origjinalit: ngjyrë, font, distancë, renditje.

Qëllimi është një dizajn **"pixel-perfect"** — një kopje që nuk dallohet nga origjinali.

---

## 5. Interneti, Web-i, dhe struktura e HTML-it (Ora 5)

**Interneti** lidh kompjuterët me njëri-tjetrin; **World Wide Web (WWW)** lidh njerëzit përmes webfaqeve, mbi rrjetin e internetit. WWW-i u zbulua nga **Tim Berners-Lee** në **1989**, në CERN.

Një webfaqe ndërtohet zakonisht nga tri shtresa:

- **HTML** — struktura e përmbajtjes.
- **CSS** — stili / pamja.
- **JavaScript** — interaktiviteti.

**HTML** nuk është gjuhë programuese, është gjuhë **shënjuese (markup)** — përshkruan strukturën e përmbajtjes, jo logjikë.

Struktura bazë e një dokumenti HTML:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Titulli i faqes</title>
  </head>
  <body>
    <!-- gjithçka që shihet në browser shkon këtu -->
  </body>
</html>
```

- `<!DOCTYPE html>` i thotë browser-it çfarë versioni HTML-i të presë.
- `<html>` është "ena" që mbështjell gjithçka.
- `<head>` përmban informacione **rreth** dokumentit (nuk shfaqet vizualisht).
- `<title>` shfaqet tek tab-i i browser-it.
- `<body>` përmban **gjithë përmbajtjen vizuale** të faqes — vetëm një `<body>` për dokument.

Një **element** HTML ndërtohet zakonisht nga etiketa hapëse + përmbajtje + etiketa mbyllëse: `<p>Përmbajtja...</p>`.

- `<h1>` deri `<h6>` — titujt, nga më i madhi (`<h1>`) tek më i vogli (`<h6>`).
- `<p>` — paragraf; injoron automatikisht hapësirat shtesë dhe rreshtat e rinj në kod.
- `<strong>` — e bën tekstin **bold**; `<em>` — e bën tekstin *italic*. Këto mund të vendosen brenda elementeve të tjera (nesting).
- `<br>` — ndërprerje rreshti (line break); **nuk ka etiketë mbyllëse**.

---

## 6. Lidhjet dhe Imazhet (Ora 6)

Elementet si `<br>` që nuk kanë etiketë mbyllëse quhen **void elements** (p.sh. `<br>`, `<hr>`, `<img>`).

Një **atribut** shton informacion shtesë brenda etiketës hapëse, në formën `emri="vlera"`.

**Imazhet** shtohen me `<img>`:

```html
<img src="foto.jpg" alt="Përshkrim i shkurtër i fotos">
```

- `src` — rruga (adresa) drejt imazhit; i domosdoshëm.
- `alt` — tekst alternativ, që përshkruan imazhin; nuk duhet lënë kurrë bosh (ndihmon nëse imazhi nuk ngarkohet, dhe për qasshmëri).

**Lidhjet** shtohen me `<a>`:

```html
<a href="https://www.jcoders.al" target="_blank">Vizito jCoders</a>
```

- `href` — adresa ku çon lidhja.
- `target="_blank"` — e hap lidhjen në një tab të re.

Lidhjet mund të jenë **absolute** (adresë e plotë, p.sh. `https://...`, zakonisht drejt një webfaqeje tjetër) ose **relative** (brenda të njëjtit projekt, p.sh. drejt një faqeje tjetër në të njëjtin folder).

---

## 7. Njoftimi me CSS (Ora 7)

**CSS** është akronim për **Cascading Style Sheets** — përshkruan **si** duken elementet e HTML-it (ngjyra, madhësi, hapësira, rreshtim).

Tri mënyrat për të shtuar CSS:

1. **Inline CSS** — direkt brenda etiketës, me atributin `style`: `<h1 style="color:blue">...</h1>`
2. **Internal CSS** — brenda `<style>`, tek `<head>` i dokumentit.
3. **External CSS** — file `.css` i veçantë, i lidhur me `<link>` tek `<head>`. Kjo është metoda e **preferuar**, sepse mban HTML-in të pastër dhe faqen më të shpejtë.

Sintaksa bazë:

```css
selector {
  property: value;
}
```

Selektori zgjedh cilin element HTML po stilizojmë; brenda `{ }` shkruajmë dyshe **property: value**, secila e mbyllur me `;`.

**"Cascading"** i referohet parimit: kur dy rregulla përplasen për të njëjtin element, fiton ai që gjendet **më poshtë** në kod (ose i lidhur i fundit).

CSS Mini Cheat Sheet: `color`, `background-color`, `font-size`, `text-align`.

---

## Përmbledhje e shpejtë

```
1. UI = pamja, UX = ndjesia e përdorimit; Frontend = çka sheh useri, Backend = logjika
2. Figma: Frame = faqja, Fill/Corner radius/Opacity = parametrat bazë të një forme
3. Stroke = konturi; CTRL+G = grupim; ALT+drag = duplikim i shpejtë
4. Project Based = rikrijo një dizajn ekzistues sa më saktë (pixel-perfect)
5. HTML = struktura; CSS = stili; JavaScript = interaktiviteti
6. <h1>-<h6> = tituj, <p> = paragraf, <strong> = bold, <em> = italic, <br> = rresht i ri
7. <img src="..." alt="...">, <a href="..." target="_blank">...</a>
8. CSS: Inline (style="..."), Internal (<style>), External (.css + <link>) -- External = e preferuar
9. Cascading: rregulli i fundit/më poshtë fiton kur ka konflikt
```

---

## Vazhdo me pyetjet praktike

Ky rifreskim shoqërohet nga një grup pyetjesh praktike që mbulojnë të shtatë orët — gjendet në të njëjtin folder si ky udhëzues.
