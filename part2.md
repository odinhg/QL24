## Finn retning med høyeste Q-verdi

Lag en funksjon `get_policy_direction(agent_pos, q_table)` i `laby_ai.py` som tar in to parametere: en tuple av heltall `agent_pos` på formen `(row, col)` som angir agentens posisjon i labyrinten og en 2D-liste av oppslagsverk `q_table`. Returner den retningen/nøkkelen som har høyest verdi i `q_table[row][col]`.

For eksempel, hvis `q_table[row][col] = {"Left": 0.3, "Right": 0.4, "Up": 0.2, "Down": 0.3}` så skal funksjonen returnere `"Right"` siden dette er retningen har høyest verdi.

## $\epsilon$-grådig strategi

### Del A

Modifiser funksjonen `get_direction(app)` i filen `laby_ai.py` som følger:

- Med sannsynlighet $\epsilon$ (`app.epsilon`), bruk `random.choice` til å velge en tilfeldig retning og returner denne.
- Med sannsynlighet $1-\epsilon$, bruk retningen returnert av funksjonen `get_policy_direction`.

### Del B

1. I funksjonen `init` i filen `laby_ai.py`, opprett opprett variabelen `app.episodes_trained` med verdi `0`.
2. I funksjonen `timer_fired` i filen `laby_main.py`, øk `app.episodes_trained` med `1` dersom agenten havner i målruten. Oppdater også verdien av `app.epsilon` til `1 / 2 ** (1 + app.epsiodes_trained / 10)`.

Dette gjør at verdien av $\epsilon$ (`app.epsilon`) gradvis minker for hver gang agenten kommer i mål.

## Implementer Q-læringsalgoritmen

I funksjonen `timer_fired` i filen `laby_main.py` flyttes nå agenten i en tilfeldig retning dersom `app.auto_mode` er `True`. Vi skal nå bruke Q-læring for å gjøre agenten smartere.

I funksjonen `timer_fired` dersom `app.auto_mode` er `True`, skal vi, i stedet for å flytte agenten tilfeldig, gjøre følgende steg:

1. Bruk $\epsilon$-grådig strategi til å velge en retning $a_t$ ved å kalle funksjonen `direction = get_direction(...)` fra `laby_ai.py`.
2. Beregn belønningen $R(s_t, a_t)$ ved å kalle `reward_function` fra `laby_ai.py`.
3. Lagre `app.agent_pos` i en ny variabel `prev_pos`. Tenk på `prev_pos` som $s_t$.
4. Flytt agenten i retning `direction` ved å kalle `move_agent_in_direction` fra `laby_maze.py`. Nå er `app.agent_pos` lik $s_{t+1}$.
5. Finn den nåværende Q-verdien $Q(s_t, a_t)$ i `app.q_table` ved å bruke `prev_pos` og `direction`.
6. Finn estimert fremtidig belønning $\max_{a\in\mathcal{A}}Q(s_{t+1}, a)$ ved å kalle `get_maximum_q_value` med `app.agent_pos` og `app.q_table`.
7. Regn ut den nye Q-verdien med formelen $(1-\alpha)Q(s_t, a_t) + \alpha\left(R(s_t, a_t) + \gamma\max_{a\in\mathcal{A}}Q(s_{t+1}, a)\right)$.
8. Oppdater $Q(s_t, a_t)$ til å være den nye Q-verdien fra forrige steg.
