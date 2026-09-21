# Aktiviteti 7 — Njoftimi me HTML
## Udhëzues

---

## Rikujtim i shpejtë

Interneti lidh kompjuterët; WWW (Web) lidh njerëzit përmes webfaqeve, të cilat shikohen me ndihmën e browser-ëve. HTML strukturon përmbajtjen e një webfaqeje, CSS e stilizon, dhe kodin e shkruajmë në një editor si VS Code. Tani hyjmë thellë në **HTML**.

Ky udhëzues shpjegon konceptet dhe hapat që i ndoqëm, në rendin e duhur.

---

## 1. Struktura e një dokumenti HTML

Një webfaqe është një dokument që zakonisht shkruhet në HTML dhe "përkthehet" nga një browser. HTML është gjuha shënjuese që përdoret për të krijuar faqe tërheqëse, duke i dhënë përmbajtjes një strukturë të qartë.

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

- **`<!DOCTYPE html>`** — përcakton llojin e dokumentit / i thotë browser-it cilin version të HTML-it të presë.
- **`<html>`** — informon browser-in që ky është një dokument HTML; është "ena" që mbështjell gjithçka tjetër.
- **`<head>`** — elementi i parë brenda `<html>`; përmban informacione **rreth** dokumentit (jo përmbajtje të dukshme).
- **`<title>`** — titulli i faqes, shfaqet tek "tab"-i i browser-it. Vendoset brenda `<head>`.
- **`<body>`** — elementi më i rëndësishëm; brenda tij vendoset **gjithë përmbajtja vizuale** e faqes. Mund të ketë vetëm **një** `<body>` në një dokument.

> 💡 Mbaje mend kështu: dokumenti HTML është si trupi i njeriut — koka (`head`, informacione) dhe trupi (`body`, çka shihet).

---

## 2. HTML Elements & Tags

Çdo dokument HTML përbëhet nga **elementet**, dhe secili element zakonisht ka **etiketa (tags)**:

- **Etiketa hapëse** (opening tag): `<p>`
- **Etiketa mbyllëse** (closing tag): `</p>` (ka një `/` para emrit)

Formula e një elementi:

```html
<tagname>Përmbajtja shkon këtu...</tagname>
```

> ⚠️ Një prej gabimeve më të shpeshta të fillestarëve është **mos-mbyllja** e elementit me tag-un mbyllës — kjo mund të prishë pamjen e gjithë faqes.

---

## 3. Headings (Titujt) — `<h1>` … `<h6>`

Ekzistojnë **6 lloje** titujsh: `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`.

```html
<h1>Titulli më i madh</h1>
<h2>Titull më i vogël</h2>
<h6>Titulli më i vogël nga të gjithë</h6>
```

- `<h1>` jep titullin më të madh/më të theksuar; sa më i madh numri, aq më e vogël madhësia.
- Titujt i ndihmojnë motorët e kërkimit (search engines) të kuptojnë strukturën/temën e faqes.

> ⚠️ Titujt (headings) përdoren **vetëm për tituj**, jo si mënyrë për të bërë ndonjë tekst bold — për këtë ekziston `<strong>` (shih më poshtë).

---

## 4. Paragraphs (Paragrafët) — `<p>`

```html
<p>Ky është paragrafi ynë i parë.</p>
```

Numri i paragrafëve nuk është i limituar. Paragrafët kanë dy rregulla të veçanta:

- **Injorojnë** çdo hapësirë shtesë (më shumë se një hapësirë boshe trajtohet si një e vetme).
- **Injorojnë** rreshtat e rinj — edhe nëse në kod dalim në rresht të ri, paragrafi vazhdon ta shfaqë gjithçka në një rresht të vetëm (derisa të mbarojë hapësira e disponueshme).

---

## 5. Nesting elements (Elementet e ndërthurura) + `<strong>` dhe `<em>`

HTML mbështet **ndërthurjen** (nesting) — një element brenda tjetrit.

- **`<strong>`** — e bën pjesën e tekstit **bold**.
- **`<em>`** — e bën pjesën e tekstit *italic*.

```html
<p>Unë jam <strong>nxënës</strong> në Akademinë <em>jCoders</em></p>
```

---

## 6. `<br>` — element pa etiketë mbyllëse

`<br>` shton një ndërprerje rreshti (line break). Ndryshe nga `<p>` apo `<h1>`, **`<br>` nuk ka etiketë mbyllëse** — thjesht `<br>`, pa `</br>`.

> 💡 Do të hasim edhe elemente të tjera si `<br>` që nuk kanë nevojë për etiketë mbyllëse — për to do të flasim më konkretisht orën tjetër.

---

## Ushtrimet që bëmë në klasë

### Detyra 1 — Rikrijo pamjen

Duke përdorur `<h1>`…`<h6>`, `<p>`, `<strong>` dhe `<em>`, rikrijuam një pamje të dhënë nga trajneri (tituj + paragrafë me pjesë bold/italic).

### Detyra 2 — Lyrics Page në HTML

Vazhduam projektin që e dizajnuam në Figma (Ora 4–5), duke e ndërtuar tani në kod të vërtetë:

- **Titulli i këngës** → brenda `<h1>`
- **Emri i këngëtarit/es** → brenda `<h2>`
- **Teksti i këngës** → disa paragrafë, ku pjesa e refrenit është e mbështjellë me `<em>` (ose `<i>`)
- Pas çdo fundrreshti të paragrafit shtuam një `<br>`

Pas përfundimit diskutuam: çfarë funksioni kryen `<br>`?

---

## Përmbledhje e shpejtë

```
1. <!DOCTYPE html> <html> <head><title></title></head> <body>...</body> </html>
2. Element = etiketë hapëse + përmbajtje + etiketë mbyllëse: <p>...</p>
3. <h1> deri <h6> = titujt (nga më i madhi tek më i vogli)
4. <p> = paragraf; injoron hapësira shtesë dhe rreshta të rinj
5. <strong> = bold, <em> = italic -- mund të vendosen brenda njëri-tjetrit (nesting)
6. <br> = ndërprerje rreshti, PA etiketë mbyllëse
```

---

## Fjalë të shkurtra

- **DOCTYPE** — deklarata që i thotë browser-it çfarë lloj/versioni dokumenti të presë
- **Element** — etiketa hapëse + përmbajtja + etiketa mbyllëse
- **Tag (etiketë)** — pjesa `<...>` që shënon fillimin ose mbarimin e një elementi
- **Nesting** — vendosja e një elementi brenda tjetrit
- **Void element** — element pa etiketë mbyllëse (p.sh. `<br>`) — do ta zgjerojmë orën e ardhshme

---

## 🎯 Sfida jote (pikë ekstra)

Përfundo plotësisht Lyrics Page-n në HTML dhe krahasoje me dizajnin që bëre në Figma (Ora 4–5) — a përputhet renditja e titullit, nëntitullit dhe paragrafëve? Shkruaj si koment çdo dallim që vure re mes dizajnit dhe kodit.
