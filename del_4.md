# &#128220; Del 4: Lag en tom Q-tabell

Vi skal nå opprette **Q-tabellen** som representerer Q-funksjonen $Q\colon\mathcal{S}\times\mathcal{A}\to\mathbb{R}$. Q-tabellen skal være en 2D-liste av oppslagsverk hvor hvert oppslagsverk har nøkler `"Left"`, `"Right"`, `"Up"` og `"Down"` og aller tilhørende verdier er `0.0`.

I funksjonen `init` i filen `laby_ai.py` (ikke i `laby_maze.py`!), lag en ny variabel `app.q_table` som er en 2D-liste av samme størrelse som `app.maze`, men i stedet for heltall, skal `app.q_table` være en 2D-liste av oppslagsverk `{"Left": 0.0, "Right": 0.0, "Up": 0.0, "Down": 0.0}`.

For eksempel, Q-verdien for paret $((1, 2), \text{venstre})$, altså $Q((1, 2), \text{venstre})$, kan vi nå finne ved å skrive `app.q_table[1][2]["Left"]` For å få tak i Q-verdien for å gå ned når agenten er i posisjon $(1,0)$, leser vi verdien til `q_table[1][0]["Down"]`.

<details>
  <summary><b>&#128161; Hint</b></summary>

- Du kan starte med å lage en tom liste `app.q_table`.
- Bruk to nøstede for-løkker for å lage 2D-listen av oppslagsverk.
- Hvis du vil, kan du ta utgangspunkt i koden under og finne ut hva som skal erstatte `...`:

```python
new_q_table = []
for row in range(n_rows):
    q_row = []
    for col in range(n_cols):
        q_row.append(...)
    new_q_table.append(q_row)

app.q_table = new_q_table
```

</details>

---

[<< Gå til del 3](./del_3.md) | [Gå til del 5 >>](./del_5.md)
