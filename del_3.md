# &#128644; Del 3: Styr hastigheten

Vi skal nå la brukeren endre hastigheten til agenten når automodus er på.

1. I funksjonen `app_started` i filen `laby_main.py`, lag en variabel `app.timer_delay` med verdi `50`. Denne variabelen bestemmer hvor ofte funksjonen `timer_fired` kalles.
2. Hvis `r` ("raskere") trykkes, mink `app.timer_delay` med `1` dersom `app.timer_delay > 1`.
3. Hvis `s` ("saktere") trykkes, øk `app.timer_delay` med `1` dersom `app.timer_delay < 500`.

---

[<< Gå til del 2](./del_2.md) | [Gå til del 4 >>](./del_4.md)
