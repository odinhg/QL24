# Tutorial: Løs labyrint med Q-læring

Dette er en tutorial lagd for studenter som tar INF100 (Innføring i programmering) våren 2024. Målet vårt er å lage et program der hvor en agent lærer seg å løse en labyrint ved hjelp av Q-læring, en form for forsterkende læring (reinforcement learning).

<!-- &#128210; [Trykk her for å gå til slides.](./slides/main.pdf) -->

For å visualisere agenten som handler i miljøet (labyrinten), bruker vi grafikkbiblioteket [`uib_inf100_graphics`](https://github.com/torsteins/uib_inf100_graphics).

Det ferdige prosjektet kan se noe slikt ut:

![Animert eksempel som viser det ferdige prosjektet.](./img/example_animated.gif)

Den oransje ruten er agenten vår som prøver å finne fram til den blå målruten. Når vi starter programmet så har agenten ingen kunnskap om labyrinten. Gjennom å utforske labyrinten, samler agenten gradvis erfaring og blir til slutt ekspert på å finne målet (eller målene). 

Kunnskapen agenten lærer lagres i en såkalt Q-tabell som representerer verdien av å utføre en spesifikk handling (gå venstre, høyre, opp eller ned) i en gitt tilstand (agentens posisjon).

Agenten mottar tilbakemelding på sine handlinger via en belønningsfunksjon. For eksempel, å gå inn i veggen gir en sterk negativ belønning. Å nå målruten gir en sterk positiv belønning. Å gå til en ny åpen rute gir en svak negativ belønning (siden vi vil at agenten skal lære seg å finne den raskeste veien til målet).

## Før du starter 

1. Installer grafikkbiblioteket `uib_inf100_graphics` hvis du ikke allerede har det installert. [Trykk her](https://github.com/torsteins/uib_inf100_graphics?tab=readme-ov-file#installation) for instruksjoner.
2. I en ny mappe, lag tre tomme Python-filer: `main.py`, `learning.py` og `maze.py`.

Filen `main.py` vil inneholde selve programmet, `learning.py` vil inneholde funksjoner relatert til Q-læring og `maze.py` vil inneholde funksjoner relatert til selve labyrinten (miljøet).

---

Tutorialen er delt opp i to deler. I den første delen skal vi lage funksjoner som har med labyrinten å gjøre. I den andre delen skal vi gjøre selve implementasjonen av Q-læringsalgoritmen.

[Trykk her for å komme til del 1.](./part_1.md)

[Trykk her for å komme til del 2.](./part_2.md)

Når du er ferdig med begge delene kan du ta en titt på listen nedenfor dersom du ønsker å forbedre programmet ditt.

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

---

## Wall of Fame

Skjermbilder av implementasjoner som utmerker seg kommer her etter innleveringsfristen.
