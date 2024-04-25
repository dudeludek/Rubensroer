# Prosjekt Rubensrør
### Work in progress
Contributers:
Erik, Helene, Ulrik
### Todo
* Lage finere Readme.
* Drille luftehull til forsterker.
* Finne føtter og montere på forsterkeren.

## How to Rubensrør
### Sjekkliste
For en vellyket rubensrørøkt behøves følgende
- Ett stk rubensrør med skrutvinger. Denne står lagret oppunder taket på EL0.
- Rubensrør-prosjekteske. Denne står over Seksjon 4 på EL0 og inneholder:
    - Forsterker.
    - Høyttaler i festeanordning.
    - Gasslange.
    - Ekstra forsterker og høyttalerelement.
- Propan. Denne står lagret utenfor NTNUS gasslager. Ta kontakt med vakt og service for å få tilgang.
- Gassbrenner, lighter eller annen foretrukken kilde til antenning.
- Avspillingsmedium med musikk og/eller funskjonsgenerator.
- Minijack til RCA-kabel.
- Brannslukningsapparat.

Valgfritt:
- Aktiv høyttaler.
- Passiv DI-boks, ligger i #avkom-skuffen på CoE.
- XLR-kabel.

### Oppsett
Fest røret i et stødig bord med skrutvinger og koble til slangen med propan. Tre høyttaleren over røret på siden med membranet og koble til forsterkeren med bananplugger. Forsterkeren håndterer flere typer innganger, det anbefales å bruke RCA til minijack mellom forsterker og mediekilde.

 (Bilde)

 Lyden i høyttaleren vil være temmelig svak, slik at dersom det er et ønske å høre tydelig hva som skjer kan det kobles opp en aktiv høyttaler ved å plugge den ledige RCAen inn i en DI-boks og XLR videre til aktiv høyttaler. Merk at lydbølgene fra høyttaleren vil skape interferens med bølgene i røret dersom avstanden mellom disse er liten.

Åpne gassventilen forsiktig. Røret fylles ganske kjapt, slik at etter ca 10 sekunder er røret klar til antenning. Skru ventilen på propen flasken for å justere høyden på flammene til omtrent 2 cm. Merk at det kan være nødvendig å øke gassflyten senere da lyden har en tendens til å øke propanflyten ut av røret.

Sett i gang funksjonsgeneratoren/musikken og nyt.

 (Film)

### Viktig å merke seg
Rubensrøret krever helt vindstille forhold, derfor er det ikke anbefalt å sette opp utendørs. Mech har fungert fint til testing, bare påse at avtrekket står på. Det er en brannmelder i taket, men siden Mech er godkjent rom for varmearbeid skal det en del til for denne å reagere på varme, men utøv måtehold og pass på å ikke produsere røyk ved å sette fyr på klær eller hår.

## Motivasjon
Studentorganisasjonen Omega Verksted ønsket seg i vinter 2024 et rubensrør og godkjente i den anledning et støttemidler til prosjektet. Something flammer og lyd er gøy.. something Matte 4 oblig..

## Teori

## Test

## Konklusjon

## Forbedringer



**Forsterker**
* Finne noen finne knotter vi kan bruke som føtter.
* Luftehull?

**Rubensrøret**
* Finne og montere en flytregulator som ikke har for heftig innstrømming.
* Bytte rør til ett med mindre diameter og smalere hull
* Lage stødigere føtter til røret

![First_nodes](/Media/first_nodes.jpg)


## Litt teori
Med utgangspunkt i bølgelikningen

$$
\begin{equation}
\frac{1}{c^2}\frac{\delta u}{\delta t} = \frac{\delta^2u}{\delta x^2}
\end{equation}
$$

bla bla
Kan brukes:)

Ved $x=0$ betrakter vi røret som åpent siden membranet på denne siden er elastisk og tillater lydtrykk å fritt overføres mellom høyttalerelementet og røret. Ved $x=L$ vil det alltid være en node. Dette gir randkravene

$$
\begin{align}
\frac{\delta u(0,t)}{\delta x} &= 0 \\
u(L,x) &= 0
\end{align}
$$

Antar at løsningen kan skrives på formen

$$
\begin{equation}
u(x,t)=X(x)T(t),
\end{equation}
$$

så dette setter vi inn i bølgelikningen

$$
\begin{equation*}
\frac{1}{c^2} \frac{T''(t)}{T(t)} = \frac{X''(x)}{X(x)}.
\end{equation*}
$$

Her må hver side av likhetstegnet være lik en separasjonskonstant. Dette gir et system med to ordinære difflikninger

$$
\begin{align}
X''(x)+w^2X(x) &= 0     \\ 
T''(t)+c^2w^2T(t) &= 0   
\end{align}
$$

Bruker randbetingelsene (2) og (3)
$$
\begin{align*}
X(x) &= A\cos(wx)+B\sin(wx)     \\
X'(0) &= -wA\sin(0) +wB\cos(0) = 0 \\
wB &= 0.
\end{align*}
$$

Siden $w>0$ må $B=0$. Ved enden av røret har vi at

$$
\begin{align*}
X(L) &= A\cos(wL) = 0   \\
\cos(wL) &= 0     \\
w_nL &= \frac{(2n-1)\pi}{2}, \quad \text{for n heltall}
\end{align*}
$$

Som gir 
Høyden på flammene er proporsjonal med gassflyt ut hullet. Gassflyten er igjen proporsjonal med roten av differansen mellom trykket på innsiden og utsiden av røret. Dette er grunnen til at selv om trykket over tid på innsiden av røret er det samme gjennom røret, vil ikke alle flammene være like høye. Høyden på flammene har en ulinær sammenheng med trykket på innsiden av røret!


## Kildeliste
https://en.wikipedia.org/wiki/Rubens_tube


