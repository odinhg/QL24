# Del 5: Implementer belønningsfunksjonen

Vi skal nå implementere belønningsfunksjonen $R\colon\mathcal{S}\times\mathcal{A}\to\mathbb{R}$. Husk, belønningen er bestemt ut i fra agentens posisjon $s\in\mathcal{S}$, retningen $a\in\mathcal{A}$ og hva som skjer når agenten går i retning $a$ fra posisjon $s$.

I filen `laby_ai.py`, lag en ny funksjon `reward_function(app, direction)`. Importer funksjonen `get_neighbour` fra `laby_maze.py` og bruk denne til å finne posisjonen til ruten i retning `direction` fra `app.agent_pos`.

Funksjonen `reward_function` skal da returnere et flyttall som følger:

- **Agenten går ut av labyrinten:** Hvis ruten fra `get_neighbour` er utenfor labyrinten så returner `-1.0`.
- **Agenten går inn i veggen:** Hvis ruten fra `get_neighbour` er en veggrute (har verdi `1` i `app.maze`) så returner `-1.0`.
- **Agenten går i mål:** Hvis ruten fra `get_neighbour` er mål (har verdi `2` i `app.maze`), returner `1.0`.
- **Agenten går til en åpen rute:** Hvis ruten er en åpen rute (har verdi `0` i `app.maze`), returner `-0.1`.

---

[<< Gå til del 4](./del_4.md) | [Gå til del 6 >>](./del_6.md)
