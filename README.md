# La Conquista delle Province d'ITAGLIA

Un piccolo sito che fa vedere, giorno per giorno, come cambia la mappa nel gioco
della **conquista delle province italiane** nato su [r/ITAGLIA](https://www.reddit.com/r/ITAGLIA/).

La regola è semplice: ogni giorno due (o più) province vicine si sfidano ai voti, e chi vince
si prende quella che perde. Un'immagine alla volta la mappa dell'Italia cambia, finché resterà
una sola provincia che tiene tutto il Paese.

**Sito online:** https://USERNAME.github.io/conquista-itaglia/
(sostituisci `USERNAME` con il tuo utente GitHub dopo aver acceso le Pages)

## Cosa puoi fare

- Far partire l'animazione della mappa con play, pausa, avanti, indietro, ricomincia e ripeti.
- Vedere per ogni giorno lo scontro del momento e il risultato del giorno prima, con i voti.
- Guardare i dati, ricostruiti dai risultati:
  - quante province restano in gioco,
  - la classifica degli "imperi", cioè chi ha conquistato più province,
  - quante province tiene in mano ogni regione,
  - il registro di tutte le battaglie.

## Come leggere le mappe

L'immagine di ogni giorno prende il nome dallo scontro che si vota quel giorno, ma fa vedere
la mappa com'era prima del voto. Il risultato di quello scontro si vede quindi sull'immagine del
giorno dopo. Il sito tiene già conto di questa cosa in tutti i dati.

## Crediti

Mappe e dati vengono dalla serie di
[u/DateAffectionate3719](https://www.reddit.com/user/DateAffectionate3719/) su
[r/ITAGLIA](https://www.reddit.com/r/ITAGLIA/). Questo è un sito fatto da un fan, non ufficiale.
Le mappe sono sue.

---

<details>
<summary>Note tecniche (per chi scarica il repository)</summary>

Il sito è statico, non serve nessun server.

- `index.html`: il sito che si vede.
- `data.json`: tutti gli scontri. Gli imperi e le statistiche vengono ricalcolati nel browser.
- `images/`: le mappe di ogni giorno (`NN-Provincia1-Provincia2.webp`).
- `admin.html`: strumento per chi cura il sito, per aggiungere un nuovo giorno (prepara l'immagine
  e aggiorna `data.json`).

Per vederlo in locale: `index.html` legge `data.json`, e aprendo il file con doppio clic il
browser blocca la lettura. Avvia un piccolo server nella cartella:

```
python3 -m http.server 8080
```

e apri `http://localhost:8080`. Online (per esempio su GitHub Pages) funziona senza fare niente.

</details>
