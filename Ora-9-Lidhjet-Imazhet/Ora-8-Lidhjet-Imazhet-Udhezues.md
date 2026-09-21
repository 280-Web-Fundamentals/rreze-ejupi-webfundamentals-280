> ⚠️ **Shënim:** Skeda origjinale e sllajdeve "A9 - Lidhjet dhe Imazhet.pptx" nuk u gjet më në Drive (është shënuar për rikrijim në planin e ri të kurrikulës). Ky udhëzues është rindërtuar në bazë të përshkrimit ekzistues të aktivitetit (Void Elementet, Atributet, Imazhet, Linqet) dhe njohurive standarde të HTML-it. Rishikoje dhe përshtate nëse diçka nuk përputhet me çka u mësua realisht në klasë.

# Aktiviteti 9 — Lidhjet dhe Imazhet
## Udhëzues

---

## Rikujtim i shpejtë

Orën e kaluar mësuam strukturën e HTML-it, elementet/etiketat, titujt, paragrafët, dhe `<br>` — një element që s'ka etiketë mbyllëse. Sot zgjerojmë atë ide me **void elements**, mësojmë çka janë **atributet**, dhe shtojmë dy elemente shumë të përdorura: **imazhet** dhe **lidhjet**.

Ky udhëzues shpjegon konceptet dhe hapat që i ndoqëm, në rendin e duhur.

---

## 1. Void Elements (Elementet pa etiketë mbyllëse)

Siç e pamë me `<br>`, disa elemente **nuk kanë** etiketë mbyllëse — quhen **void elements**. Nuk kanë përmbajtje brenda tyre (nuk "mbyllin" asgjë), kështu që nuk u nevojitet `</...>`.

```html
<br>
<hr>
<img src="foto.jpg" alt="Përshkrim i fotos">
```

- **`<br>`** — ndërprerje rreshti (e pamë orën e kaluar)
- **`<hr>`** — një vijë horizontale ndarëse
- **`<img>`** — një imazh (shih pikën 3)

> 💡 Rregull i thjeshtë: nëse elementi nuk "mbështjell" ndonjë përmbajtje (tekst, elemente të tjera), ka shumë gjasa të jetë void element.

---

## 2. Atributet

Një **atribut** i shton informacion shtesë një elementi — vendoset **brenda etiketës hapëse**, në formatin `emri="vlera"`.

```html
<tagname atribut1="vlera1" atribut2="vlera2">Përmbajtja</tagname>
```

Shembull që tashmë e njohim pa e quajtur "atribut" — `<title>` te `<head>` nuk ka atribute, por `<img>` dhe `<a>` (shih më poshtë) mbështeten pikërisht tek atributet për të funksionuar fare.

> ⚠️ Atributet vendosen **vetëm** te etiketa hapëse, kurrë te etiketa mbyllëse (kur ka).

---

## 3. Imazhet — `<img>`

`<img>` shton një imazh në faqe. Është **void element** — nuk ka `</img>`.

```html
<img src="assets/kengetari.jpg" alt="Foto e këngëtarit" width="300" height="200">
```

- **`src`** (source) — rruga (path) tek fotoja; **i domosdoshëm**, pa të browser-i nuk e gjen imazhin.
- **`alt`** (alternative text) — tekst që shfaqet nëse fotoja nuk mund të ngarkohet, dhe që e lexojnë "screen reader"-at për persona me shikim të kufizuar. **Gjithmonë** vendos një `alt` kuptimplotë, jo bosh.
- **`width` / `height`** — dimensionet e imazhit (në pixel); ndihmojnë faqen të ngarkohet më "rrjedhshëm" (browser-i e di paraprakisht sa hapësirë të lërë).

> 💡 `alt` nuk është opsional "për zbukurim" — nëse fotoja nuk hapet (ose useri përdor screen reader), `alt`-i është e vetmja gjë që mbetet nga ai element.

---

## 4. Lidhjet / Linqet — `<a>`

`<a>` (anchor) krijon një **lidhje** (link) tek një faqe tjetër, një burim, ose një pjesë tjetër e së njëjtës faqe.

```html
<a href="https://www.jcoders.al">Vizito jCoders</a>
```

- **`href`** (hypertext reference) — ku të çon lidhja; **i domosdoshëm**.
- **`target="_blank"`** — hap lidhjen në një **tab të re** të browser-it (shumë e përdorshme për lidhje të jashtme, që useri të mos e humbë faqen jonë).

```html
<a href="https://www.jcoders.al" target="_blank">Vizito jCoders</a>
```

---

## 5. Lidhje relative vs absolute

- **Absolute** — adresa e plotë, me `https://...` (çon në një webfaqe tjetër, jashtë projektit tonë).
- **Relative** — adresa relative ndaj file-it aktual, brenda të njëjtit projekt (p.sh. `img/foto.jpg`, ose `rreth-nesh.html`).

```html
<!-- Absolute: shkon jashtë projektit -->
<a href="https://www.google.com">Google</a>

<!-- Relative: shkon tek një file tjetër brenda projektit tonë -->
<a href="rreth-nesh.html">Rreth nesh</a>

<!-- Relative: shkon tek një imazh brenda folderit "img" të projektit -->
<img src="img/logo.png" alt="Logo">
```

> ⚠️ Nëse lëviz projektin (ose e ngarkon online) dhe lidhjet relative "prishen", kontrollo së pari nëse struktura e folderave është ruajtur e njëjtë.

---

## Ushtrimi që bëmë në klasë

Tek projekti Lyrics Page (Ora 6–7), shtuam:

1. Një **imazh** të këngëtarit/es (me `src` dhe `alt` kuptimplotë).
2. Një **lidhje** që çon tek një faqe e jashtme me më shumë informacion për këngëtarin/en, e hapur në tab të re (`target="_blank"`).

---

## Përmbledhje e shpejtë

```
1. Void element = element pa etiketë mbyllëse (br, hr, img)
2. Atribut = emri="vlera", vendoset brenda etiketës hapëse
3. <img src="..." alt="..."> = imazh; src i domosdoshëm, alt kurrë bosh
4. <a href="...">...</a> = lidhje; target="_blank" hap në tab të re
5. Absolute = adresë e plotë (https://...); Relative = brenda të njëjtit projekt
```

---

## Fjalë të shkurtra

- **Void element** — element pa etiketë mbyllëse (p.sh. `<br>`, `<hr>`, `<img>`)
- **Atribut** — informacion shtesë brenda etiketës hapëse, në formën `emri="vlera"`
- **`src`** — rruga tek burimi (p.sh. një foto) që tregon një `<img>`
- **`alt`** — teksti alternativ i një imazhi, i rëndësishëm për qasshmëri (accessibility)
- **`href`** — destinacioni i një lidhjeje `<a>`
- **Link relativ / absolut** — adresë brenda projektit kundrejt adresës së plotë të jashtme

---

## 🎯 Sfida jote (pikë ekstra)

Krijo një faqe të vogël me **3 imazhe** dhe **3 lidhje**: të paktën një lidhje e jashtme me `target="_blank"`, dhe të paktën një lidhje relative tek një file tjetër brenda të njëjtit projekt. Sigurohu që çdo `<img>` ka një `alt` kuptimplotë.
