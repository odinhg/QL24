# &#128200; Del 7: Finn høyeste Q-verdi i en gitt posisjon

Vi skal nå lage en funksjon som gir oss den høyeste Q-verdien som er mulig for agenten å oppnå i en gitt posisjon $s\in\mathcal{S}$.

Lag en funksjon `get_maximum_q_value(agent_pos, q_table)` i `laby_ai.py` som tar in to parametere: 

- en tupel av heltall `agent_pos` på formen `(row, col)` som angir agentens posisjon i labyrinten og 
- en 2D-liste av oppslagsverk `q_table`. 

Funksjonen skal returnere den høyeste verdien i oppslagsverket `q_table[row][col]`, altså den høyeste Q-verdien som er mulig i posisjon `agent_pos` basert på Q-tabellen `q_table`.

For eksempel, hvis `q_table[row][col] = {"Left": 0.3, "Right": 0.1, "Up": 0.7, "Down": 0.3}` så skal funksjonen returnere `0.7` siden dette er den høyeste Q-verdien i posisjon `(row, col)`. 

<details>
  <summary><b>&#128161; Hint</b></summary>

 - For å hente ut en liste med alle verdiene i et oppslagsverk `my_dict` kan du kalle `my_dict.values()`.
 - For å finne den høyeste verdien i en liste `my_list` (med tall) kan du kalle `max(my_list)`.

For eksempel så vil følgende kodesnutt skrive ut den høyeste verdien i `my_dict` som her er `0.8`:

 ```python
my_dict = {"a": 0.3, "b": 0.8, "c": -1.2}
values = my_dict.values()
max_value = max(values)
print(max_value)
 ```

</details>


---

[<< Gå til del 6](./del_6.md) | [Gå til del 8 >>](./del_8.md)
