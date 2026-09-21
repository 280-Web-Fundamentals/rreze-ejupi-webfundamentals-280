# Aktiviteti 6 — Njoftimi me WEB-in
## Udhëzues

---

Deri tani kemi punuar vetëm në Figma, me dizajn. Tani fillojmë të njihemi me vetë web-in — si funksionon, cilat gjuhë e ndërtojnë, dhe cilin editor do të përdorim për të shkruar kod gjatë gjithë vitit.

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

## 9. Editorët

**Editorët** janë programe që na lehtësojnë të shkruajmë kod — shumica janë falas dhe instalohen lehtë. Na ndihmojnë të gjejmë gabimet më lehtë, dhe kanë extensions/shtesa me funksione të veçanta.

Këtë vit do të përdorim **Visual Studio Code (VS Code)**.

### Instalimi i VS Code

1. Vizito **code.visualstudio.com** (ose kërko "Visual Studio Code" në Google).
2. Kliko butonin blu **Download for Windows**.
3. Prit derisa të përfundojë shkarkimi, pastaj hape file-in e shkarkuar dhe ndiq hapat e instalimit.
4. Instalo edhe extension-in **"Live Server"** (na lejon të shohim ndryshimet e kodit tonë menjëherë në browser, pa e ringarkuar faqen manualisht).

---

## Detyra e klasës

1. Hap një folder në Desktop me emrin **"jCoders Viti 1"** (kujdes — ky folder nuk fshihet deri në fund të vitit!).
2. Brenda tij krijo një folder tjetër me emrin **"A6"** (për çdo orë që mbajmë krijohet folderi përkatës: A6, A7, A8, etj.).
3. Klik i djathtë mbi folderin A6 → **Open with Code**.
4. Në VS Code, krijo një file të ri: **index.html** (`.html` është prapashtesa e dokumenteve HTML).
5. Shkruaj diçka brenda file-it. Aktivizo **Auto Save** (menyja File → Auto Save).
6. Me ndihmën e trajnerit, hape file-in duke përdorur **Live Server**.

**Pesha e detyrës: 500 pikë**

---

## Përmbledhje e shpejtë

```
1. Interneti lidh kompjuterët; WWW (Web) lidh njerëzit përmes webfaqeve
2. WWW u zbulua nga Tim Berners-Lee në 1989, në CERN
3. Një webfaqe = HTML (strukturë) + CSS (stil) + JavaScript (interaktivitet)
4. HTML nuk është gjuhë programuese -- është gjuhë shënjuese (markup)
5. Editori ynë: VS Code, + extension Live Server për parapamje të menjëhershme
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

---

## 🎯 Sfida jote (pikë ekstra)

Brenda `index.html` shto edhe një fjali tjetër (çfarëdo teksti). Ruaje file-in (Auto Save duhet të jetë aktiv) dhe kontrollo në browser (me Live Server hapur) nëse ndryshimi shfaqet automatikisht, pa pasur nevojë ta rifreskosh vetë faqen. Shkruaj si koment ç'vure re.
