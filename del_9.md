# &#127913; Del 9: $\epsilon$-grådig strategi

### Del A

Modifiser funksjonen `get_direction(app)` i filen `laby_ai.py` som følger:

- Med sannsynlighet $\epsilon$ (som vi har lagret i variabelen `app.epsilon`), bruk `random.choice` til å velge en tilfeldig retning og returner denne.
- Med sannsynlighet $1-\epsilon$, bruk retningen returnert av funksjonen `get_policy_direction`.

<details>
  <summary><b>&#128161; Hint</b></summary>

Vi kan bruke funksjonen `random` fra `random` for å få et tilfeldig flyttall mellom `0` og `1`. Se kodesnutten under for å se hvordan vi kan kjøre kode med sannsynlighet $\epsilon\in[0,1]$. 

```python
import random

epsilon = 0.8

if random.random() < epsilon:
    # Runs with probability epsilon (0.8)
    print("Hello")
else:
    # Runs with probability 1 - epsilon (0.2)
    print("World")
```

Her skriver vi ut `Hello` med sannsynlighet `0.8` og vi skriver ut `World` med sannsynlighet `0.2`.

</details>

### Del B

I funksjonen `timer_fired` i filen `laby_main.py`, sett `app.epsilon` til `0.8` ganger den nåværende verdien av `app.epsilon` hver gang agenten havner i målruten. Her kan du bruke samme `if`-setning som du bruker for å resette agenten.

På denne måten minker vi verdien av $\epsilon$ for hver fullførte episode (agenten finner mål). Verdien av $\epsilon$ blir da $0.5\cdot0.8^{n_e}$ hvor $n_e$ er antall ganger agenten har funnet mål.

---

[<< Gå til del 8](./del_8.md) | [Gå til del 10 >>](./del_10.md)
