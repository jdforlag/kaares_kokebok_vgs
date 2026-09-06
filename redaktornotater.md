# Redaktørnotater – løsninger til kapittel 7 og utover

Denne fila samler funn som dukket opp under arbeidet med løsningene til
oppgavene fra og med kapittel 7. Notatene er ment som et arbeidsdokument for
redaksjonen, ikke som en publisert feilliste. Det som bekreftes som trykkfeil,
kan flyttes over til `feilliste.md`.

**Status:** kapittel 7–16 er gjennomgått. Løsninger er laget til alle
A- og B-oppgaver. S-oppgavene er utelatt, slik `til_laereren.md` beskriver.

## Slik leser du notatene

Hvert punkt er merket med en kategori:

| Merke | Betydning |
| ----- | --------- |
| **FEIL** | Sannsynlig trykkfeil i boka. Bør rettes. |
| **UKLAR** | Oppgaveteksten eller kodebitene er tvetydige, og løsningen måtte tolke. |
| **VALG** | Løsningen avviker bevisst fra kodeskjelettet i boka, med begrunnelse. |
| **TEKNISK** | Fungerer, men avhenger av bibliotekversjon eller lignende. |

---

## Kapittel 7 – Funksjoner

### 7.12 — **FEIL** — fasit for `h(120)`

Fasitboksen viser:

```
h(120) = 1607400
```

Riktig verdi er **1670400**:

```
120**3 - 4*120**2 = 1 728 000 - 57 600 = 1 670 400
```

Ser ut som en sifferombytting (07 → 70). *Kandidat til feillista.*

### 7.7 — **FEIL** — funksjonsnavnet er inkonsistent

Kodebitene som skal settes sammen bruker to ulike navn på samme funksjon:

```python
def m(t):                      # ← definert som m
    return 1500 * 0.88**t

while maaker(aar) >= 10:       # ← kalt som maaker
```

Løsningen bruker `maaker` gjennomgående. Enten bør `def m(t)` bli
`def maaker(t)`, eller så bør while-linja bli `while m(aar) >= 10:`.

### 7.22 — **FEIL** — kodeskjelettet passer ikke med figuren

Skjelettet i oppgaveteksten er:

```python
kropp = (n+2) * (...) - 1
```

Figuren (`part1/tikz_funksjoner.pdf`, side 4) viser kropper med målene

| Figur | Kropp | Antall kvadrater i kroppen |
| ----- | ----- | -------------------------- |
| 1 | 3 × 2 | 3·2 − 1 = 5 |
| 2 | 5 × 3 | 5·3 − 1 = 14 |
| 3 | 7 × 4 | 7·4 − 1 = 27 |

Bredden følger altså `2n+1`, ikke `n+2`. `n+2` stemmer bare for figur 1.
Løsningen følger figuren:

```python
kropp = (2*n+1) * (n+1) - 1
```

Det gir 7, 20 og 39 kvadrater i figur 1–3, og **1 035 250** for de 100 første
figurene. Enten bør skjelettet i boka rettes til `(2*n+1)`, eller så bør
figuren endres.

### 7.14, 7.20 — **VALG** — sammenligner `f(x)` med `f(x+steg)`

Boka gir startkoden `while f(x) < f(x+steg):`. Løsningene bruker denne, men
merk at metoden stopper på det første punktet der funksjonen slutter å vokse.
Med `steg = 0.01` gir 7.14 toppunktet (2.50, 10.25), som er eksakt riktig.

### 7.16 — **VALG** — `dx` redusert til 0,0001

Oppgaven ber om at nullpunktet skal bli 1,4142 med fire desimaler. Startkoden
har `dx = 0.5`. Løsningen setter `dx = 0.0001`, som er det som skal til.
Løkka gjør da 40 000 iterasjoner, men kjører på under et sekund.

---

## Kapittel 8 – Logaritmer og likninger

### 8.9 — **FEIL** — steget i puslespillet er for grovt

Kodebitene gir denne sammensetningen:

```python
def N(p):
    return 300_000*(1+p)**25

prosent = 0
while N(prosent) < 2_250_000:
    prosent += 0.1
print(f"{prosent = }")
```

Siden `p` er vekstfaktoren minus 1, tilsvarer `+= 0.1` et steg på **10
prosentpoeng**. Programmet svarer derfor `prosent = 0.1`, altså 10 %, mens
riktig svar er

```
(2 250 000 / 300 000)^(1/25) - 1 = 0,0839 = 8,39 %
```

Forslag: bytt kodebiten `+= 0.1` med `+= 0.001` (eller mindre). Løsningsfila
viser først puslespillet slik boka ber om, og deretter en gjentakelse med
steg 0,0001 som gir 8,40 %.

### 8.14 — **UKLAR** — hvilket heltall er «løsningen»?

Oppgaven ber om «en heltallig (tilnærmet) løsning» av `x·lg x = 150` mellom 10
og 100. Den vanlige while-løkka stopper på **x = 80**, men:

| x | x · lg x |
| -- | -------- |
| 79 | 149,91 |
| 80 | 152,25 |

Den eksakte løsningen er x ≈ 79,05, så **79** ligger nærmest. Løsningsfila
skriver ut begge og kommenterer hvilket som er nærmest. Vurder å presisere i
oppgaveteksten om det er «første heltall over 150» eller «nærmeste heltall»
som ønskes.

### 8.2 (og delkapittel 8.1–8.2) — **TEKNISK** — numpy 2 endrer utskriften

Fasitboksen i 8.2 viser:

```
lg(0.01) + lg(1000**4) = 10.0
```

Med numpy 2.x skriver `f"{... = }"` ut repr-formen i stedet:

```
lg(0.01) + lg(1000**4) = np.float64(10.0)
```

Dette gjelder også de eksisterende delkapittelfilene `0801_natlog.py` og
`0802_tierlog.py`. Løsningene er skrevet på bokas form for konsistens.
Mulige tiltak: pakk uttrykket i `float(...)`, eller ta med en merknad om
numpy-versjon i avsnittet om installering av bibliotek.

### 8.15 — **UKLAR** — «doblet seg» i forhold til hva?

«Utvid deretter programmet til å bestemme hvor lang tid vil det ta før verdien
av investeringen har doblet seg.» Løsningen tolker det som en dobling av
18-månedersverdien (36 000 kr → 72 000 kr), som nås etter **198 måneder**,
altså 180 måneder senere. Verdt å presisere i teksten.

### 8.18 — **VALG** — toleransen styrer nøyaktigheten

Algoritmen i oppgaven bruker `abs(f(m)) >= 0.01`. Det gir x ≈ 3,7314, mens det
eksakte nullpunktet er 2 + √3 ≈ 3,7321. Avviket kommer av at kravet stilles til
`f(m)`, ikke til `m`. Dette er greit for oppgaven, men kan være verdt en
merknad i teksten om hva toleransen faktisk måler.

---

## Kapittel 9 – Grafiske framstillinger

### 9.9 — **FEIL** — språkfeil i oppgaveteksten

> «En lokal blogg kalt Fornekteren mottar bare **et 12** forespørsler per sekund»

Skal antakelig være «bare 12 forespørsler per sekund».

### 9.9 — **UKLAR** — hva skal leses av?

Oppgaven ber om at eleven skal «bestemme ved å se på grafen omtrent når
Fornekteren passerer Sannheten». Løsningen tegner grafene som beskrevet, og
legger i tillegg til en løkke som regner ut det eksakte svaret: **674 sekunder**
(begge ligger da på ca. 9800 forespørsler per sekund). Det gjør det lett for
læreren å kontrollere elevenes avlesning.

### 9.6 — **TEKNISK** — plassering av forklaringsboksen

I figur 9.x i boka ligger forklaringsboksen (legend) nede til høyre. Med
`plt.legend()` uten argumenter velger matplotlib selv plassering, og lander
her øverst til venstre. Grafen er ellers identisk. Dersom figuren skal
gjenskapes helt likt, må `plt.legend(loc="lower right")` brukes. Løsningen
bruker den enkle varianten.

### 9.1 — **VALG** — beskrivelsen ligger som kommentar

Oppgaven ber om at det visuelle resultatet skal beskrives med ord. I
løsningsfila står beskrivelsen som en kommentar nederst: linja går opp, skrått
ned og opp igjen, slik at figuren ligner bokstaven **N**.

---

## Kapittel 10 – Grenseverdier og funksjoner

### 10.4 — **FEIL** — koden fra 10.1 gir divisjon med null

Oppgaven ber eleven bruke koden fra oppgave 10.1 til å undersøke

$$\lim_{x\to 0^+} \frac{3-x}{x^2-1}$$

Koden fra 10.1 starter på `a = 4.0` og halverer: 4,0 → 2,0 → **1,0** → 0,5 → …
Ved `a = 1.0` blir nevneren `x**2 - 1 = 0`, og programmet krasjer med
`ZeroDivisionError`. Alle elever som følger oppgaveteksten ordrett vil treffe
dette.

Forslag: legg til en merknad om at `f` ikke er definert for `x = 1`, og be
eleven starte på for eksempel `a = 0.5`. Løsningsfila starter på 0,5 og
forklarer hvorfor. Grenseverdien er **−3**.

### 10.15 — **FEIL** — manglende parentes i tipsboksen

Tipsboksen viser:

```python
while abs(h(x1) > 0.001:
```

Det mangler en parentes etter `h(x1)`, og `abs` er satt utenpå sammenligningen
i stedet for utenpå funksjonsverdien. Riktig linje er:

```python
while abs(h(x1)) > 0.001:
```

### 10.16 — **UKLAR** — stoppkriteriet bør bruke absoluttverdi

> «Du skal stoppe repetisjonene når $f(x_1) < 10^{-7}$»

Uten absoluttverdi er kriteriet oppfylt så snart `f(x1)` er negativ, uansett
hvor langt unna nullpunktet vi er. Løsningen bruker `abs(f(x1)) > 10**(-7)`,
i tråd med hvordan Newtons metode er presentert i delkapittel 10.9. Bør
presiseres i oppgaveteksten.

### 10.9 — **UKLAR** — siste gren nås aldri i praksis

Skjelettet legger opp til `if fd(varer) > 0: ... elif fd(varer) < 0: ...`.
Toppunktet ligger i x = 250, men den numeriske deriverte med foroverdifferanse
gir `fd(250) = -0.0002`, altså aldri nøyaktig 0. Løsningsfila kommenterer
dette. Verdt en merknad i teksten om at numerisk derivasjon gir en tilnærming.

### 10.14 — **TEKNISK** — avrundingsfeil for store `n`

Oppgaven ber om differansen $e - \left(1+\tfrac{1}{n}\right)^n$. Differansen
krymper fint til rundt `n = 10**8`, men fra `n = 10**9` begynner den å hoppe
og blir negativ, fordi datamaskinen ikke lenger klarer å skille `1 + 1/n` fra
`1`. Løsningen bruker 9 runder i løkka og kommenterer fenomenet. Dette kan
være et fint poeng å nevne i teksten, men det bør ikke overraske eleven.

### 10.11 — **VALG** — også øvre grense tatt med

Oppgaven spør hvor mange enheter som må produseres for at overskuddet
overstiger 15 000 kr. Siden `f` er en andregradsfunksjon med toppunkt, synker
overskuddet igjen. Løsningen oppgir hele intervallet: **236–764 enheter**.

---

## Kapittel 11 – Sannsynlighet

### 11.12, 11.14, 11.16 — **FEIL** — `hypergeometric` mangler antall trekninger

Alle tre oppgavene kaller `hypergeometric` med bare to tall pluss `size`:

```python
forsokene = hypergeometric(hjerter, ikke_hjerter, size=antall_forsok)   # 11.12
hypergeometric(3, 47, size=1000)                                        # 11.14 (tipsboks)
svarte_trukket = hypergeometric(svarte, hvite, size=1500)               # 11.16
```

Signaturen i numpy er `hypergeometric(ngood, nbad, nsample, size=None)`.
Uten det tredje tallet får eleven

```
TypeError: hypergeometric() missing required argument 'nsample'
```

Riktige kall:

| Oppgave | Riktig kall | Kommentar |
| ------- | ----------- | --------- |
| 11.12 | `hypergeometric(13, 39, 5, size=1500)` | 5 kort trekkes |
| 11.14 | `hypergeometric(3, 47, 1, size=1000)` | 1 vinnerlodd trekkes |
| 11.16 | `hypergeometric(svarte, hvite, 2, size=1500)` | 2 kuler trekkes |

Dette er nok den viktigste rettelsen i kapitlet — slik det står nå stopper
programmet med en feilmelding for alle tre oppgavene.

### 11.4 — **FEIL** — skjelettkoden gir en evig løkke

Puslespillet er satt opp slik:

```python
kast1 = randint(1, 7)
kast2 = randint(1, 7)
kast_nr ...

while kast1 + kast2 < 12:
    kast_nr ...
print(...)
```

Løkkekroppen har bare plass til `kast_nr += 1`. Terningene kastes aldri på
nytt, så med mindre det aller første kastet gir 12, kjører programmet i det
uendelige. Løsningen kaster begge terningene på nytt inni løkka.

Forslag: la skjelettet vise tre linjer i løkkekroppen, eller legg inn
kodebitene `kast1 = randint(1, 7)` og `kast2 = randint(1, 7)` blant dem som
skal plasseres.

### 11.5 — **FEIL** — manglende parentes i kodebiten

Kodebiten er

```python
print(f"{mulige = }"
```

Den mangler avsluttende parentes: `print(f"{mulige = }")`.

### 11.15 — **INFO** — fasit til b-oppgaven

Den minste terningen som gir $P(X>60) > 0{,}5$ er **n = 17**
(146/289 = 0,5052; for n = 16 er det 119/256 = 0,4648). Med 20 000
simuleringer per verdi treffer programmet dette stabilt. Løsningsfila regner
også ut de eksakte verdiene som kontroll, siden simulering alene ligger nær
grensa for n = 16 og 17.

### 11.16 — **INFO** — fasit

Det må være minst **6 svarte kuler** i krukka. Ved regning:
$P(\text{2 svarte}) = \tfrac{s}{s+2}\cdot\tfrac{s-1}{s+1}$, som gir 0,476 for
s = 5 og 0,536 for s = 6.

### 11.9, 11.10 — **VALG** — forklaringene ligger som kommentar

Begge eksamensoppgavene ber om en forklaring i tillegg til kode. I
løsningsfilene står forklaringen som kommentar øverst, og koden under.
Fasit: 11.9 a) $P(\text{sum} \ge 8) = 15/36 = 0{,}4167$, b) 42/216 = 0,1944.
11.10 b) $P(\text{sum} = 9) = 4/36 = 1/9 = 0{,}1111$.

---

## Kapittel 12 – Reelle data

### 12.15 — **FEIL** — kolonnenavnet i `vareeksport.csv` stemmer ikke med boka

Filvisningen i oppgaveteksten viser:

```
år,verdi
1980,91.7
```

Fila i repoet (`reelle_data_S1/vareeksport.csv` og kopien under `losninger/`)
har derimot overskriften

```
år,verdi (i milliarder kroner)
```

En elev som skriver `data["verdi"]` etter mønster fra boka, får `KeyError`.
Forslag: forkort overskriften i fila til `verdi`, eller oppdater filvisningen
i boka. Løsningen bruker det navnet fila faktisk har.

### 12.1 — **UKLAR** — puslespillet mangler en `print`

Oppgaven ber om at programmet skal «bestemme det største antallet jordskjelv
på ett år, og skrive dette ut», men det er ingen `print`-kodebit blant de
seks som listes opp. En av kodebitene står tom. Antakelig skulle den ha
inneholdt `print(maks_skjelv)`.

### 12.14 — **UKLAR** — algoritmen regner utenfor datamaterialet

Modellen blir $O(x) = -0{,}1x^2 + 200x - 40000$, og algoritmen gir intervallet
**[330, 1671]**. Datafila stopper imidlertid på 1200 enheter, så den øvre
grensa 1671 kommer fra ekstrapolasjon. Løsningen kommenterer dette. Verdt en
merknad i teksten om at en modell ikke uten videre gjelder utenfor det
området vi har data for.

### 12.13 — **INFO** — avviket blir tilnærmet null

Tallene i `populasjon.csv` følger en eksponentialmodell nesten helt nøyaktig
(modellen blir $f(x) = 297{,}83 \cdot 1{,}07^x$). Avviket etter 50 måneder er
under én innbygger. Oppgaven ber eleven «beregne avviket», og svaret blir
altså ~0. Det er kanskje litt antiklimaks — data med litt støy ville gjort
poenget tydeligere. Løsningen skriver avviket med to desimaler så det ikke
ser ut som en feil.

### 12.13, 12.15 — **TEKNISK** — krever scipy

Begge oppgavene bruker `scipy.optimize.curve_fit`. Det er i tråd med
delkapitlene 12.7 og 12.8, men scipy må installeres separat. Verdt å nevne i
oppgavene, slik det gjøres i merkeboksene ellers i boka.

### 12.5 — **INFO** — fortegnet i utskriften

Fasitboksen viser `f(x) = 2.6x - 0.5`. For å få minustegnet må man skrive
`{abs(b):.1f}` og selv sette inn minus, siden `b` er negativ. Løsningen gjør
dette og kommenterer det. En mer generell løsning ville trengt en
`if`-setning på fortegnet til `b`.

---

## Kapittel 13 – Tallfølger og rekker

### 13.19 — **FEIL** — summeformelen i skjelettkoden mangler faktoren *n*

Skjelettkoden er:

```python
def S(d, a1=100, n=10):  # Gir S10 der d varierer
    return (a1 + a1+d*(n-1)) / 2
```

Summeformelen for en aritmetisk rekke er

$$S_n = n\cdot\frac{a_1+a_n}{2}$$

Faktoren `n` mangler. Slik koden står, regner `S(d)` ut gjennomsnittet av
første og siste ledd, ikke summen. Konsekvensen er at programmet svarer at
Ida må øke sparebeløpet med **400 kr** i uka, mens riktig svar er **20 kr**.

Riktig linje:

```python
    return n * (a1 + a1+d*(n-1)) / 2
```

Løsningsfila bruker den rettede formelen og gir 20 kr (som gir nøyaktig
1900 kr på 10 uker).

### 13.21 — **FEIL** — summeformelen i tipsboksen

Tipsboksen viser:

$$S_n = a_1 \cdot \frac{k^n-1}{k-n}$$

Nevneren skal være $k-1$, ikke $k-n$:

$$S_n = a_1 \cdot \frac{k^n-1}{k-1}$$

Fasit: mengden virkestoff nærmer seg $7/(1-0{,}9) = 70$ mg og kommer aldri
over 100 mg, så legen har rett.

### 13.10 — **INFO** — fasit

Eleven regner ut summen av den aritmetiske rekka $3+7+11+\ldots$
Med N = 10 blir svaret 210. Med N = 100 blir svaret
$S_{100} = 50\cdot(6+99\cdot4) = 20100$.

### 13.2 — **INFO** — antall runder i løkka

Utskriften har 17 tall (7 til 55 med differanse 3). Siden det siste tallet
skrives ut etter løkka, skal løkka kjøre 16 ganger: `for i in range(16):`.

### 13.20, 13.26 — **INFO** — fasit

13.20: Tilbud B gir mer enn tilbud A fra og med **uke 28** (A: 370 kr,
B: 373,35 kr).
13.26: Det trengs **27 ledd** (til og med 121 393). Summen blir da 317 810.

### 13.25 — **TEKNISK** — flyttall når summen når 1

Delsummene når nøyaktig `1.0` etter 16 ledd i Python, fordi flyttall har
begrenset presisjon. Det er akkurat poenget oppgaven ønsker å illustrere,
men det kan være verdt å nevne at «=1» her er en avrunding i maskinen, mens
likheten $0{,}999\ldots = 1$ er eksakt matematisk.

---

## Kapittel 14 – Integrasjon

### 14.6 — **FEIL** — x-verdiene starter i 0 i stedet for i x1

Skjelettkoden er:

```python
x1 = 1
x2 = 3
n = 20
bredde = ...
rekt_sum = 0
for i in range(n):
    x_verdi = bredde*i        # ← her
    hoyde = ...
```

Med `x_verdi = bredde*i` blir den første x-verdien 0, ikke 1. Siden
$h(x)=e^x/x$ ikke er definert i 0, stopper programmet med
`ZeroDivisionError` allerede i første runde. Linja må være

```python
    x_verdi = x1 + bredde*i
```

Løsningen bruker den rettede linja og kommenterer hvorfor. Svaret blir
omtrent **7,844**.

### 14.11 — **UKLAR** — summegrensa passer ikke med x-verdiene

Oppgaven ber om

$$\sum_{i=0}^{8} f(x_i)\cdot dx \quad\text{der}\quad \{x_i\}=\{1, 3, 5, \ldots, 15\}$$

Mengden $\{1, 3, 5, \ldots, 15\}$ har åtte elementer ($x_0$ til $x_7$), mens
summen går til $i=8$ og altså krever ni ledd (opp til $x_8 = 17$). Løsningen
følger den oppgitte mengden, altså x fra 1 til 15, og gir summen **1376**.
Forslag: endre øvre grense til $i=7$, eller utvid mengden til 17.

### 14.4 — **UKLAR** — én av «feilene» er en tallverdi, ikke en skrivefeil

I feilsøkingsoppgaven må eleven både rette variabelnavnet (`delta_x` brukes
som `dx`) og endre verdien fra 0,5 til 1, siden intervallet $[0,2]$ deles i
to. Det siste er ikke en skrivefeil, men følger av oppgaveteksten under
koden. Kanskje verdt å nevne eksplisitt at også tallverdier kan være feil.

### 14.17 — **INFO** — nøyaktighet med 300 rektangler

Eksakt løsning er $b = 27/7 \approx 3{,}857$. Med 300 venstreorienterte
rektangler og steg 0,001 gir programmet **b ≈ 3,862**. Avviket kommer av
rektangelmetoden, ikke av søket. Verdt å nevne dersom fasit skal oppgis med
tre desimaler.

### 14.20 — **INFO** — fasit

Trapesmetoden kommer innenfor 0,01 av 18 allerede ved **22 rektangler**
(17,9907), mens rektangelmetoden fortsatt ligger på 18,6043 der.
Trapesmetoden vinner altså klart.

### 14.8, 14.12, 14.13 — **INFO** — fasitverdier

| Oppgave | Tilnærming | Eksakt |
| ------- | ---------- | ------ |
| 14.8 (Thea) | 20,0020 med 6000 rektangler | 20 |
| 14.12 (kvartsirkel) | 4 · 0,7875 = 3,1500 | $\pi$ = 3,1416 |
| 14.13 (eksamen S2) | 6,666 | 20/3 = 6,667 |

---

## Kapittel 15 – Diskrete sannsynlighetsfordelinger

### 15.14 — **FEIL** — importlinja mangler `as plt`

Skjelettkoden begynner slik:

```python
import matplotlib.pyplot
import numpy as np
```

Resten av programmet må bruke `plt.plot(...)`, men `plt` er aldri definert.
Eleven får `NameError: name 'plt' is not defined`. Linja skal være

```python
import matplotlib.pyplot as plt
```

### 15.5 — **FEIL** — kodebitene refererer til en variabel som ikke finnes

Skjelettet har linjene

```python
resultater = ...
treff = ...
print(...)
```

mens kodebitene som skal settes inn er `sum(resultater)`, `100`,
`np.random.binomial(n, p, size=N)` og `"Antall bom:", bom`. Variabelen `bom`
blir aldri regnet ut noe sted, og oppgaveteksten ber bare om antall **treff**.

Forslag: bytt kodebiten til `"Antall treff:", treff`, eller legg til en linje
`bom = N*n - treff` i skjelettet. Løsningen regner ut begge deler.

### 15.8 — **UKLAR** — 50 eller 70 simuleringer?

Skjelettkoden setter `N = 50`, men oppgaveteksten sier «Gjennomfør 70
simuleringer av antall dødsfall». Løsningen bruker 70, i tråd med teksten og
figurteksten. Bør samkjøres.

### 15.3 — **INFO** — fasit

Med $\mu = 4{,}7$ blir $\mathrm{Var}(X) = 5{,}610$ og $\mathrm{SD}(X) = 2{,}369$.

### 15.13 — **INFO** — fasit

$P(\text{sum}\ge 10) = 6/36$ og $P(\text{sum}=3 \text{ eller } 5) = 6/36$, så

$$E(X) = 300\cdot\tfrac16 + 200\cdot\tfrac16 = 83{,}33 \text{ kr}$$

Nettogevinsten per runde blir $83{,}33 - 100 = -16{,}67$ kr. Simuleringen med
4000 forsøk gir typisk rundt −16 til −17 kr.

### 15.6, 15.16 — **INFO** — fasit

15.6: $P(X \ge 3) = 12852/27405 = 0{,}469$.
15.16: $P(X > 30) = 0{,}5645$ (og $P(X = 30) = 0{,}0888$).

### 15.16 — **TEKNISK** — krever scipy

Som i kapittel 12 forutsetter oppgaven at scipy er installert.

---

## Kapittel 16 – Normalfordelingen og hypotesetesting

### 16.15 — **FEIL** — ulikheten i algoritmen peker feil vei

Algoritmen i oppgaven er:

```
La t få verdien mu - 4*sigma
Gjenta for alltid:
    Regn ut P(X<=t)
    Regn ut P(X>t)
    Hvis P(X>t) >= 0.758:
        Bryt løkka
    Øk t med 0,1
Skriv ut t
```

Søket starter i $t = \mu - 4\sigma = 300$, der $P(X>t)$ er tilnærmet 1.
Betingelsen `P(X>t) >= 0.758` er da oppfylt med en gang, og løkka brytes i
første runde. Programmet skriver ut 300.

Siden $P(X>t)$ **synker** når t øker, må betingelsen være

```
    Hvis P(X>t) <= 0.758:
        Bryt løkka
```

Da blir svaret **t ≈ 465,1 timer**, som stemmer med at $z = -0{,}7$.

### 16.2 — **FEIL** — kodebiten bruker et engelsk variabelnavn

Kodebitene som skal settes sammen inneholder

```python
for hoyde in hoyder:
print(f"{height:.2f}")
```

Løkkevariabelen heter `hoyde`, men utskriften bruker `height`. Eleven får
`NameError: name 'height' is not defined`. Kodebiten bør være
`print(f"{hoyde:.2f}")`.

### 16.6 — **FEIL** — arealet regnes ut med feil faktor

Skjelettkoden er:

```python
x_verdier = np.arange(10, 15, 0.01)
arealer = x_verdier * f(...)
sum_areal = ...
```

Arealet av hvert lille rektangel er **bredden** ganger høyden, altså
`0.01 * f(x_verdier)` — ikke `x_verdier * f(...)`. Slik linja står nå,
multipliseres høyden med x-verdien i stedet for med steglengden, og svaret
blir helt feil.

Forslag til rettelse:

```python
dx = 0.01
x_verdier = np.arange(10, 15, dx)
arealer = dx * f(x_verdier)
sum_areal = sum(arealer)
```

Fasit: $P(10<X<15) = 14{,}5\ \%$ (eksakt $e^{-1}-e^{-1{,}5} = 0{,}1448$).

### Datafiler — **VALG** — CSV-filene er kopiert inn i kapittelmappa

`losninger/kap16_normalfordelingen_og_hypotesetesting/` inneholdt ingen
datafiler, men både de eksisterende delkapittelløsningene (`1609_hyptestdata.py`,
`1610_tosidig.py`) og oppgavene 16.19 og 16.20 leser CSV-filer. Uten filene
stopper programmene med `FileNotFoundError`.

Vi har derfor kopiert fire filer fra `reelle_data_S2/` inn i kapittelmappa,
etter samme mønster som `kap12_reelle_data`:

- `oppholdstider.csv`
- `stemmer_rv.csv`
- `inntekter.csv`
- `heste_hindre.csv`

Slett dem gjerne igjen dersom dere heller vil at elevene skal laste dem ned
selv — men da bør det stå i oppgaveteksten hvor filene skal ligge.

### 16.17 — **INFO** — resultatet ligger tett på signifikansnivået

Marte får 8 av 10 riktige. p-verdien blir

$$P(X\ge 8) = \frac{45+10+1}{1024} = 0{,}0547$$

Det er **så vidt over** 5 %, så nullhypotesen beholdes. Dette er et fint
diskusjonspunkt i klasserommet, men verdt å være klar over dersom noen
forventer motsatt konklusjon.

### 16.19, 16.20 — **INFO** — fasitverdier

| Oppgave | Resultat |
| ------- | -------- |
| 16.19 (spisested) | Gjennomsnitt 14 969,75 kr, p-verdi **0,00344** → H₀ forkastes |
| 16.20 (Maria) | 1441 av 2000 hindre (0,721), p-verdi **0,0235** → H₀ forkastes |

p-verdien i 16.19 stemmer med kommentaren i kildefila
(`%p-verdi: 0.0034402995511286782`).

### 16.13, 16.14 — **INFO** — fasitverdier

16.13 (tre skoler): $P(\text{snitt} > 4) \approx 0{,}21$.
16.14 (jenter og gutter): $P(\text{høyde} > 175) \approx 0{,}42$.

---

## Oppsummering

### Feil som bør rettes før neste opplag

Disse gjør at elevens program **stopper med feilmelding eller gir feil svar**
om oppgaveteksten følges ordrett:

| Oppgave | Kort beskrivelse |
| ------- | ---------------- |
| 7.12 | Fasit `h(120) = 1607400` skal være 1670400 |
| 7.22 | `kropp = (n+2)*(...)` passer ikke med figuren; skal være `(2n+1)` |
| 8.9 | Steget `+= 0.1` er 10 prosentpoeng; svaret blir 10 % i stedet for 8,39 % |
| 10.4 | Koden fra 10.1 treffer x = 1, der nevneren er 0 |
| 10.15 | `while abs(h(x1) > 0.001:` — feilplassert parentes |
| 11.4 | Løkkekroppen kaster ikke terningene på nytt → evig løkke |
| 11.5 | `print(f"{mulige = }"` mangler parentes |
| 11.12, 11.14, 11.16 | `hypergeometric` mangler antall trekninger → `TypeError` |
| 12.15 | Kolonnenavnet i `vareeksport.csv` stemmer ikke med filvisningen |
| 13.19 | Summeformelen mangler faktoren `n`; svaret blir 400 i stedet for 20 |
| 13.21 | Tipsboksens formel har $k-n$ i nevneren; skal være $k-1$ |
| 14.6 | `x_verdi = bredde*i` gir x = 0 → divisjon med null |
| 15.5 | Kodebiten bruker variabelen `bom`, som aldri regnes ut |
| 15.14 | `import matplotlib.pyplot` mangler `as plt` → `NameError` |
| 16.2 | Kodebiten bruker `height` i stedet for `hoyde` → `NameError` |
| 16.6 | `arealer = x_verdier * f(...)`; skal være `dx * f(x_verdier)` |
| 16.15 | Ulikheten i algoritmen peker feil vei; løkka brytes i første runde |

### Punkter som bør presiseres

7.7 (funksjonsnavn `m` vs. `maaker`) · 8.14 (hvilket heltall er svaret?) ·
8.15 (doblet i forhold til hva?) · 9.9 (språkfeil «et 12») · 10.9 (siste gren
nås aldri) · 10.16 (bør bruke absoluttverdi) · 12.1 (manglende `print`) ·
12.14 (modellen brukes utenfor datagrunnlaget) · 14.11 (summegrense passer
ikke med x-verdiene) · 15.8 (50 eller 70 simuleringer?) · 16-mappa (manglende
datafiler)

### Om bibliotekversjoner

- **numpy 2:** `f"{uttrykk = }"` med numpy-verdier skriver `np.float64(10.0)`
  i stedet for `10.0`. Dette påvirker fasitboksene i kapittel 8 og de
  eksisterende delkapittelfilene der.
- **scipy:** kreves i oppgavene 12.13, 12.15, 15.16 og i store deler av
  kapittel 16. Merkeboks om installering kunne vært gjentatt der.
