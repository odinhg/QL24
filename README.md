# Tutorial: Løs labyrint med Q-læring

---
## TODO

- [ ] Endre fra (col, row) til (row, col) i slides, part 2 og testkoder.
- [ ] Skrive om part 2 basert på ny part 1
- [ ] Følge tutorialen

---

Dette er en tutorial lagd for studenter som tar INF100 (Innføring i programmering) våren 2024. Målet vårt er å lage et program der hvor en agent lærer seg å løse en labyrint ved hjelp av Q-læring, en form for forsterkende læring (reinforcement learning).

&#128210; [Trykk her for å gå til slides om Q-læring.](./slides/main.pdf)

For å visualisere agenten som handler i miljøet (labyrinten), bruker vi grafikkbiblioteket [`uib_inf100_graphics`](https://github.com/torsteins/uib_inf100_graphics).

Det ferdige prosjektet kan se noe slikt ut:

![Animert eksempel som viser det ferdige prosjektet.](./img/example_animated.gif)

Den oransje ruten er agenten vår som prøver å finne fram til den blå målruten. Når vi starter programmet så har agenten ingen kunnskap om labyrinten. Gjennom å utforske labyrinten, samler agenten gradvis erfaring og blir til slutt ekspert på å finne målet (eller målene). 

Kunnskapen agenten lærer lagres i en såkalt Q-tabell som representerer verdien av å utføre en spesifikk handling (gå venstre, høyre, opp eller ned) i en gitt tilstand (agentens posisjon).

Agenten mottar tilbakemelding på sine handlinger via en belønningsfunksjon. For eksempel, å gå inn i veggen gir en sterk negativ belønning. Å nå målruten gir en sterk positiv belønning. Å gå til en ny åpen rute gir en svak negativ belønning (siden vi vil at agenten skal lære seg å finne den raskeste veien til målet).

## Før du starter 

For å fullføre denne tutorialen må du først ha gjort del 1 ([Link til del 1](https://inf100.ii.uib.no/lab/8/#tutorial-5-april-labyrint)) hvor du implementerer selve labyrinten og agentens evne til å gå i labyrinten.

Du skal med andre ord ha en mappe med følgende filer:

```
laby_main.py
laby_maze.py
laby_view.py
laby_ai.py
level1.lev
level2.lev
```

Når du kjører `laby_main.py` skal labyrinten leses fra en av filene `level*.lev` og du skal kunne flytte agenten rundt med piltastene. Når man trykker `ESC` (escape) så skal agenten flyttes til en tilfeldig åpen rute (rute med verdien `0`).

[Trykk her for å komme til selve tutorialen](./part_2.md)

Når du er ferdig, kan du ta en titt på listen nedenfor dersom du ønsker å forbedre programmet ditt.

---

## Utvidelser 

Her er en liste over forslag til mulige forbedringer og eksperimenter du kan velge å implementere:

- Prøv forskjellige verdier av læringsparametrene $\alpha$, $\gamma$ og $\epsilon$.
- Automatisk resett agenten dersom den bruker for mange steg uten å nå en målrute.
- La agenten gå diagonalt (utvid $\mathcal{A}$ med fire nye retninger).
- Prøv å ha flere enn bare én målrute i labyrinten.
- Lag fin grafikk.
- Lag en labyrintgenerator som automatisk lager en løsbar labyrint...
- ...eller lag et eget program for å tegne labyrinter.
- Lag nye rutetyper. For eksempel, lag en bomberute som gir stor negativ belønning og resetter agenten.
- Tegn en pil i de åpne rutene som peker i den retningen som har høyest Q-verdi (se hvordan pilene endrer seg under trening).
- Start med en tom Q-tabell og legg til tilstander ved behov. Med andre ord, start med en Q-tabell som kun inneholder en rad for startposisjonen `agent_pos` og utvid Q-tabellen når agenten utforsker en nye ruter.
- Utforsk dyp Q-læring (Deep Q-learning) hvor vi erstatter Q-tabellen med et nevralt nettverk. Se for eksempel [her (link)](https://www.youtube.com/watch?v=AhyznRSDjw8) og [her (link)](https://huggingface.co/learn/deep-rl-course/unit3/introduction).

**Eksempel/inspirasjon:**

![Animert eksempel som viser en forbedret versjon.](./img/improved_example_animated.gif)

