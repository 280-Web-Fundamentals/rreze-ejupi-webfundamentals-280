# Aktiviteti 6 — Njoftimi me WEB-in dhe HTML
## Udhëzues

---

Deri tani kemi punuar vetëm në Figma, me dizajn. Tani fillojmë të njihemi me vetë web-in — si funksionon, cilat gjuhë e ndërtojnë, cilin editor do të përdorim gjatë gjithë vitit — dhe hyjmë menjëherë në gjuhën e parë: **HTML**.

Ky udhëzues shpjegon konceptet dhe hapat që i ndoqëm, në rendin e duhur.

---

## 1. Interneti

Interneti është një rrjet global që lidh miliarda kompjuterë dhe pajisje nga e gjithë bota me njëri-tjetrin, duke përdorur një protokoll (TCP/IP). Arkitektura e tij shtrihet fizikisht përmes kabllove optike nën dete dhe tokë (shiko p.sh. submarinecablemap.com), duke lidhur kontinentet mes vete. Interneti mundëson komunikim dhe shpërndarje të dhënash brenda milisekondave.

---

## 2. WWW (World Wide Web)

**WWW** ("Web") është një koleksion i webfaqeve që ruhen në web server të ndryshëm. Këta server janë të konektuar tek kompjuterët tanë lokalë përmes internetit. Webfaqet përmbajnë tekste, imazhe, audio, video etj., dhe ne u qasemi atyre përmes pajisjeve tona (telefon, tablet, kompjuter, televizor).

### WWW vs Internet — dallimi

Njerëzit shpesh i ngatërrojnë, por dallojnë:

- **Interneti** — rrjeti botëror i pajisjeve kompjuterike, që lejon p.sh. dërgimin e emaileve.
- **WWW** — kur hapim një webfaqe (p.sh. Google.com), ne parashtrojmë një kërkesë për të parë një informacion — kjo është WWW.

> 💡 Thënë shkurt: **Interneti lidh kompjuterët** mes vete, **WWW lidh njerëzit** mes vete.

---

## 3. Historia e Web-it

WWW u zbulua nga shkencëtari britanik **Tim Berners-Lee** në vitin **1989**, ndërkohë që punonte në **CERN** (Organizata Evropiane për Hulumtimet Nukleare). E zhvilloi për ta përmbushur nevojën e automatizimit të shpërndarjes së informacionit mes shkencëtarëve të ndryshëm, pa pasur nevojë për udhëtime dhe mbledhje (të cilat kanë kosto të lartë).

---

## 4. Përbërja e një webfaqeje

Secila webfaqe që shohim mund të përmbajë kode të llojeve: **HTML**, **CSS**, **JavaScript**, etj.

---

## 5. Browsers (Shfletuesit)

Webfaqet zakonisht shikohen me ndihmën e **browser-ëve** — ata luajnë rolin ndërmjetësues mes klientit (vizitorit) dhe webfaqes. Disa browser aktualë: Google Chrome (më i popullarizuari, i preferuari për ne), Mozilla Firefox, Safari, Opera, Brave, Microsoft Edge.

---

## 6. Çfarë është HTML?

**HTML** (HyperText Markup Language) është një lloj kodi që përdoret për të strukturuar një webfaqe dhe përmbajtjen e saj (paragrafë, lista, tabela, imazhe). HTML **nuk** është gjuhë programuese — është një **gjuhë shënjuese** (markup language), që zbaton konventa/rregulla mbi një dokument tekst.

Versionet e HTML-it: 1.0 (1992), 2.0 (1995), 3.2 (1997), 4.01 (1999), **HTML5 (2008)** — versioni aktual, më i qëndrueshmi deri tani.

---

## 7. Çfarë është CSS?

**CSS** (Cascading Style Sheet) na lejon të stilizojmë përmbajtjen e shkruar në HTML — trajton pamjen dhe "ndjenjën" e webfaqes: ngjyra teksti, stili i shkronjave, distancat mes elementeve, fotot në prapavijë, dhe si ndryshon dukja e faqes në pajisje më të vogla.

Versionet: CSS1 (1996), CSS2 (1998), CSS3 (1999).

---

## 8. Çfarë është JavaScript?

**JavaScript** është gjuhë programuese që bashkëpunon ngushtë me HTML dhe CSS. Përdoret kryesisht për të shtuar **interaktivitet** dhe përmbajtje dinamike brenda një webfaqeje; përdoret gjithashtu për Backend (me korniza/librari të ndryshme) dhe animacione. Këtë vit do të fokusohemi më shumë në HTML dhe CSS, dhe do t'i prekim vetëm themelet e JavaScript-it.

---

## 9. Editorët + Instalimi i VS Code

**Editorët** janë programe që na lehtësojnë të shkruajmë kod — shumica janë falas dhe instalohen lehtë. Na ndihmojnë të gjejmë gabimet më lehtë, dhe kanë extensions/shtesa me funksione të veçanta.

Këtë vit do të përdorim **Visual Studio Code (VS Code)**.

1. Vizito **code.visualstudio.com** (ose kërko "Visual Studio Code" në Google).
2. Kliko butonin blu **Download for Windows**.
3. Prit derisa të përfundojë shkarkimi, pastaj hape file-in e shkarkuar dhe ndiq hapat e instalimit.
4. Instalo edhe extension-in **"Live Server"** (na lejon të shohim ndryshimet e kodit tonë menjëherë në browser, pa e ringarkuar faqen manualisht).

---

## 10. Struktura e një dokumenti HTML

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

## 11. HTML Elements & Tags

Çdo dokument HTML përbëhet nga **elementet**, dhe secili element zakonisht ka **etiketa (tags)**:

- **Etiketa hapëse** (opening tag): `<p>`
- **Etiketa mbyllëse** (closing tag): `</p>` (ka një `/` para emrit)

Formula e një elementi:

```html
<tagname>Përmbajtja shkon këtu...</tagname>
```

> ⚠️ Një prej gabimeve më të shpeshta të fillestarëve është **mos-mbyllja** e elementit me tag-un mbyllës — kjo mund të prishë pamjen e gjithë faqes.

---

## 12. Headings (Titujt) — `<h1>` … `<h6>`

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

## 13. Paragraphs (Paragrafët) — `<p>`

```html
<p>Ky është paragrafi ynë i parë.</p>
```

Numri i paragrafëve nuk është i limituar. Paragrafët kanë dy rregulla të veçanta:

- **Injorojnë** çdo hapësirë shtesë (më shumë se një hapësirë boshe trajtohet si një e vetme).
- **Injorojnë** rreshtat e rinj — edhe nëse në kod dalim në rresht të ri, paragrafi vazhdon ta shfaqë gjithçka në një rresht të vetëm (derisa të mbarojë hapësira e disponueshme).

---

## 14. Nesting elements (Elementet e ndërthurura) + `<strong>` dhe `<em>`

HTML mbështet **ndërthurjen** (nesting) — një element brenda tjetrit.

- **`<strong>`** — e bën pjesën e tekstit **bold**.
- **`<em>`** — e bën pjesën e tekstit *italic*.

```html
<p>Unë jam <strong>nxënës</strong> në Akademinë <em>jCoders</em></p>
```

---

## 15. `<br>` — element pa etiketë mbyllëse

`<br>` shton një ndërprerje rreshti (line break). Ndryshe nga `<p>` apo `<h1>`, **`<br>` nuk ka etiketë mbyllëse** — thjesht `<br>`, pa `</br>`.

> 💡 Do të hasim edhe elemente të tjera si `<br>` që nuk kanë nevojë për etiketë mbyllëse — për to do të flasim më konkretisht orën tjetër.

---

## Ushtrimet që bëmë në klasë

### Detyra 1 — VS Code + index.html

1. Hap një folder në Desktop me emrin **"jCoders Viti 1"** (kujdes — ky folder nuk fshihet deri në fund të vitit!).
2. Brenda tij krijo një folder tjetër me emrin **"A6"** (për çdo orë që mbajmë krijohet folderi përkatës: A6, A7, A8, etj.).
3. Klik i djathtë mbi folderin A6 → **Open with Code**.
4. Në VS Code, krijo një file të ri: **index.html** (`.html` është prapashtesa e dokumenteve HTML).
5. Shkruaj diçka brenda file-it. Aktivizo **Auto Save** (menyja File → Auto Save).
6. Me ndihmën e trajnerit, hape file-in duke përdorur **Live Server**.

**Pesha e detyrës: 500 pikë**

### Detyra 2 — Rikrijo pamjen

Duke përdorur `<h1>`…`<h6>`, `<p>`, `<strong>` dhe `<em>`, rikrijuam një pamje të dhënë nga trajneri (tituj + paragrafë me pjesë bold/italic).

### Detyra 3 — Lyrics Page në HTML

Vazhduam projektin që e dizajnuam në Figma (Ora 4), duke e ndërtuar tani në kod të vërtetë:

- **Titulli i këngës** → brenda `<h1>`
- **Emri i këngëtarit/es** → brenda `<h2>`
- **Teksti i këngës** → disa paragrafë, ku pjesa e refrenit është e mbështjellë me `<em>` (ose `<i>`)
- Pas çdo fundrreshti të paragrafit shtuam një `<br>`

Pas përfundimit diskutuam: çfarë funksioni kryen `<br>`?

---

## Përmbledhje e shpejtë

```
1. Interneti lidh kompjuterët; WWW (Web) lidh njerëzit përmes webfaqeve
2. WWW u zbulua nga Tim Berners-Lee në 1989, në CERN
3. Një webfaqe = HTML (strukturë) + CSS (stil) + JavaScript (interaktivitet)
4. HTML nuk është gjuhë programuese -- është gjuhë shënjuese (markup)
5. Editori ynë: VS Code, + extension Live Server për parapamje të menjëhershme
6. <!DOCTYPE html> <html> <head><title></title></head> <body>...</body> </html>
7. Element = etiketë hapëse + përmbajtje + etiketë mbyllëse: <p>...</p>
8. <h1> deri <h6> = titujt (nga më i madhi tek më i vogli)
9. <p> = paragraf; injoron hapësira shtesë dhe rreshta të rinj
10. <strong> = bold, <em> = italic -- mund të vendosen brenda njëri-tjetrit (nesting)
11. <br> = ndërprerje rreshti, PA etiketë mbyllëse
```

---

## Fjalë të shkurtra

- **Internet** — rrjeti global i pajisjeve kompjuterike të lidhura mes vete
- **WWW (Web)** — koleksioni i webfaqeve të qasshme përmes internetit
- **Browser** — programi që na lejon të shohim webfaqet (Chrome, Firefox, etj.)
- **HTML** — gjuha shënjuese që strukturon përmbajtjen e një webfaqeje
- **CSS** — gjuha që stilizon (dizajnon) përmbajtjen e HTML-it
- **JavaScript** — gjuha programuese që i shton webfaqes logjikë dhe interaktivitet
- **Editor / IDE** — programi ku shkruajmë kod (ne përdorim VS Code)
- **DOCTYPE** — deklarata që i thotë browser-it çfarë lloj/versioni dokumenti të presë
- **Element** — etiketa hapëse + përmbajtja + etiketa mbyllëse
- **Tag (etiketë)** — pjesa `<...>` që shënon fillimin ose mbarimin e një elementi
- **Nesting** — vendosja e një elementi brenda tjetrit
- **Void element** — element pa etiketë mbyllëse (p.sh. `<br>`) — do ta zgjerojmë orën e ardhshme

---

## 🎯 Sfida jote (pikë ekstra)

Përfundo plotësisht Lyrics Page-n në HTML dhe krahasoje me dizajnin që bëre në Figma (Ora 4) — a përputhet renditja e titullit, nëntitullit dhe paragrafëve? Shkruaj si koment çdo dallim që vure re mes dizajnit dhe kodit. Nëse ke kohë, shto edhe një fjali tjetër tek `index.html` dhe kontrollo në browser (me Live Server hapur) nëse ndryshimi shfaqet automatikisht, pa e rifreskuar faqen vetë.
