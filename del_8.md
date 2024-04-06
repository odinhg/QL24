# Del 8: Finn retning med høyeste Q-verdi

Vi skal nå gjøre *nesten* det samme som i forrige del. Men i stedet for å returnere den høyeste Q-verdien, så skal vi returnere den retningen som gir høyest Q-verdi.

Med andre ord, vi skal implementere $\pi^\*\colon\mathcal{S}\to\mathcal{A}$ fra forelesningen som vi definerte ved $\pi^\*(s)=\arg\max_{a\in\mathcal{A}}Q(s,a)$.

Lag en funksjon `get_policy_direction(agent_pos, q_table)` i `laby_ai.py` som tar in to parametere: 

- en tupel av heltall `agent_pos` på formen `(row, col)` som angir agentens posisjon i labyrinten og 
- en 2D-liste av oppslagsverk `q_table`. 

Funksjonen skal returnere den retningen/nøkkelen som har høyest verdi i `q_table[row][col]`. Altså, en av følgende strenger: `"Left"`, `"Right"`, `"Up"` eller `"Down"`.

For eksempel, hvis `q_table[row][col] = {"Left": 0.3, "Right": 0.4, "Up": 0.2, "Down": 0.3}` så skal funksjonen returnere `"Right"` siden dette er retningen har høyest verdi.

<details>
  <summary><b>&#128161; Hint</b></summary>

En elegant måte å finne nøkkelen med høyest verdi i et oppslagsverk er å bruke `max` sammen med parameteren `key` og metoden `dict.get`.

For eksempel så vil følgende kodesnutt skrive ut nøkkelen med høyeste verdi i `my_dict` som her er `"b"`:

```python
my_dict = {"a": 0.2, "b": 0.6, "c": -0.1}
max_value_key = max(my_dict, key=my_dict.get)
print(max_value_key)
```

</details>


---

[<< Gå til del 7](./del_7.md) | [Gå til del 9 >>](./del_9.md)
