# Aktiviteti 3 — Figma (Vazhdim)
## Udhëzues

---

Në orën e kaluar mësuam bazat e Figma-s: Frame, forma dhe parametrat kryesorë (Fill, Corner radius). Tani vazhdojmë me parametra shtesë, tekstin, dhe si të organizojmë disa elemente së bashku në një grup.

Ky udhëzues shpjegon konceptet dhe hapat që i ndoqëm, në rendin e duhur.

---

## 1. Parametrat e elementeve (vazhdim) — Stroke

Nëse duam t'i shtojmë një kufizë (kontur) një forme, aktivizojmë opsionin **Stroke**:

- **Trashësia** — sa e trashë është kufiza
- **Inside / Outside / Center** — mënyra si shtohet kufiza: nga brenda, nga jashtë, apo nga mesi i formës

---

## 2. Effects — Drop Shadow

Për t'i shtuar hije (ose efekte të tjera) një elementi, aktivizojmë **Effects**. Krijohet një Drop Shadow me parametra:

- **X / Y** — pozita e hijes në boshtin horizontal/vertikal
- **Blur** — sasia e mjegullimit të hijes
- **Spread** — sa përhapet hija
- **Transparenca** (%) — sa e dukshme është hija

---

## 3. Text Tool

Shkurtorja **T** (ose në toolbar) aktivizon Text Tool-in. Dy mënyra për të shtuar tekst:

1. **Duke specifikuar gjerësinë/gjatësinë** — kur kemi një hapësirë të saktë që teksti nuk duhet ta kalojë.
2. **Vetëm duke specifikuar fillimin** — kur nuk kemi kërkesë specifike për gjerësinë e tekstit.

---

## 4. Parametrat e tekstit

- **Familja e fontit** (p.sh. Roboto, Mulish)
- **Trashësia** (Regular, Bold, Extra Bold, ...)
- **Madhësia** (në pixel)
- **Line height** — gjatësia/hapësira mes rreshtave
- **Letter spacing** — hapësira mes shkronjave
- **Alignment** — pozicionimi i tekstit brenda fushës së tij (majtas/qendër/djathtas)

Pjesa tjetër (fill, stroke, shadow) sillet njësoj si tek format (shapes).

---

## Ushtrimi që bëmë — Krijimi i butonit

1. Krijo një **Rectangle** 180 × 50 px.
2. Shto **corner radius** 10px.
3. Emërto layer-in **"Button-bg"**.
4. Ngjyra e rectangle-it: **#55ADFF**.
5. Shto mbi rectangle një **tekst** pa specifikuar gjerësi/gjatësi (mënyra 2).
6. Emërto layer-in e tekstit **"Button-text"**.
7. Përmbajtja e tekstit: **"Home"**.
8. Fonti: **Mulish**, trashësia **Bold**, madhësia **24px**.

> 💡 Mos harro: çdo projekt duhet të ketë të përzgjedhur një Frame fillimisht (p.sh. Desktop 1440×1024).

---

## 5. Groups / Grupet

Nëse duam të krijojmë disa butona identikë pa përsëritur çdo hap, i **grupojmë** elementet e një butoni ("Button-text" + "Button-bg").

**Si grupohen elementet:**

1. Në panelin e Layers, përzgjedh layers që dëshiron t'i gruposh (mbaj `CTRL` për të përzgjedhur më shumë se një).
2. Shkurtorja `CTRL + G` (ose klik i djathtë → Group Selection).
3. Krijohet një element i ri, "Group 1" — riemërtoje (p.sh. "Button").

> 💡 Mendoje një grup si një folder që përmban brenda tij disa elemente (në rastin tonë: Rectangle + Tekst).

**Pse na ndihmojnë grupet?** Nëse duhet edhe butona të tjerë të njëjtit stil, mjafton të **duplikojmë grupin**:

1. Përzgjedh grupin.
2. Mbaj `ALT` shtypur dhe lëviz me maus — shfaqet një kopje e butonit.
3. Mos e lësho `ALT`-in derisa të përcaktosh pozicionin e ri.

---

## Ushtrimi që bëmë — Krijimi i një card-i

1. Frame background color: **#E16373**
2. Card background: **white** + shto shadow (Effects)
3. Imazhi: nga randomuser.me (hulumto si vendoset një imazh në Figma)
4. Font: **Mulish**
5. Titulli i card-it: **#434343**, **30px**, **Extra Bold**
6. Teksti (Lorem ipsum): **#666666**, **16px**, **Light**
7. Button background: **#E16373**

---

## Përmbledhje e shpejtë

```
1. Stroke = kufiza e një forme (trashësia + inside/outside/center)
2. Effects (Drop Shadow) = X, Y, Blur, Spread, transparenca
3. Text Tool (T) -> dy mënyra: me gjerësi fikse, ose vetëm fillimi
4. Parametrat e tekstit: font, trashësia, madhësia, line height, letter spacing
5. CTRL+G = grupim; ALT + drag mbi grup = duplikim i shpejtë
```

---

## Fjalë të shkurtra

- **Stroke** — kufiza (kontur) e një elementi
- **Effect / Drop Shadow** — hije apo efekt shtesë mbi një element
- **Text Tool** — vegla për të shtuar tekst (shkurtore T)
- **Group** — disa layers të bashkuar në një element, që lëvizin/duplikohen së bashku

---

## 🎯 Sfida jote (pikë ekstra)

Pasi ke grupin e butonit "Home" të krijuar, duplikoje grupin (ALT + drag) dhe krijo edhe 2 butona të tjerë me tekst të ndryshëm (p.sh. "About", "Contact"), duke ruajtur të njëjtin stil (të njëjtën ngjyrë, madhësi, font). Kështu praktikon pikërisht arsyen pse na duhen grupet: konsistencë pa përsëritje pune.
