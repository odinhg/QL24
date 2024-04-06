# Del 2: Resett agenten

Vi skal nå endre hva som skjer dersom agenten havner på målruten. 

I stedet for å vise `You Won!` på skjermen slik vi gjorde i del 1 skal vi nå plassere agenten på en tilfeldig åpen rute (slik vi gjør dersom brukeren trykker `ESC`).

I funksjonen `timer_fired` i filen `laby_main.py`, sett agentens posisjon til en tilfeldig åpen rute dersom agenten havner på målruten. 

<details>
  <summary><b>&#128161; Hint</b></summary>

 - Du kan sjekke om agenten er i målruten ved å sjekke om `app.maze[row][col]` er lik `2` hvor `row, col = app.agent_pos`. 
 - Bruk funksjonen `move_agent_to_random_free_position` fra `laby_maze.py` for å flytte agenten til en tilfeldig rute.

</details>

---

[<< Gå til del 1](./del_1.md) | [Gå til del 3 >>](./del_3.md)
