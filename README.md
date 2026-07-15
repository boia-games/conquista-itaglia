# La Conquista delle Province d'ITAGLIA — visualizzatore

Sito statico che mostra, giorno per giorno, la conquista delle province italiane
del gioco su [r/ITAGLIA](https://www.reddit.com/r/ITAGLIA/) (di u/DateAffectionate3719).

- **`index.html`** — visualizzatore pubblico (player, timeline, filtri, statistiche). Sola lettura.
- **`data.json`** — tutti gli scontri. Il sito ricostruisce imperi e statistiche al volo.
- **`images/`** — le mappe di ogni giorno (`NN-Provincia1-Provincia2.webp`).
- **`admin.html`** — strumento **tuo**, locale, per aggiungere un nuovo giorno.

## Come funziona la logica dei giorni (importante)

L'immagine `N` è intitolata allo scontro che si vota **quel** giorno, ma mostra la mappa
**prima** che quello scontro si risolva. Quindi l'immagine `N` riflette gli esiti dei giorni `1…N-1`.
L'esito dello scontro `N` diventa visibile solo sull'immagine `N+1`.
Il visualizzatore e l'admin gestiscono già questo sfasamento.

## Pubblicare online (GitHub Pages, gratis)

1. Crea un repository su GitHub (es. `conquista-itaglia`).
2. Carica **tutto** il contenuto di questa cartella nella radice del repo
   (da terminale, dentro la cartella):
   ```bash
   git init
   git add .
   git commit -m "Sito conquista ITAGLIA"
   git branch -M main
   git remote add origin https://github.com/TUO-UTENTE/conquista-itaglia.git
   git push -u origin main
   ```
3. Su GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   branch `main`, cartella `/ (root)`, **Save**.
4. Dopo qualche minuto il sito è online su
   `https://TUO-UTENTE.github.io/conquista-itaglia/`.

Il pubblico può **vedere e filtrare** tutto, ma **non può modificare** nulla:
per aggiungere uno scontro serve fare `push` sul repo, e solo tu hai quell'accesso.
Questo è il "backend": il controllo in scrittura è quello del repository Git.

## Aggiungere un nuovo giorno

1. Apri `admin.html`. Per farlo funzionare in locale con la lettura automatica di `data.json`,
   avvia un mini-server nella cartella del sito e vai su `http://localhost:8080/admin.html`:
   ```bash
   python3 -m http.server 8080
   ```
   (In alternativa apri `admin.html` con doppio-clic e carica `data.json` a mano.)
2. **Punto 2** — inserisci l'esito dello scontro in sospeso (vincitore + voti).
3. **Punto 3** — numero del nuovo giorno, tipo (duello/bonus), province in sfida
   (la regione si autocompila se già nota) e carica la **nuova immagine** della mappa
   (viene ottimizzata automaticamente a WebP 840px).
4. **Punto 4** — scarica **l'immagine ottimizzata** e il **`data.json` aggiornato**.
5. Metti l'immagine in `images/`, sostituisci `data.json`, poi:
   ```bash
   git add images/ data.json
   git commit -m "Giorno 27"
   git push
   ```
   Il sito online si aggiorna da solo.

> `admin.html` è solo un generatore locale: non scrive nulla sul server.
> Se preferisci non pubblicarlo affatto, puoi tenerlo fuori dal repo e usarlo solo sul tuo computer.

## Anteprima locale

`index.html` legge `data.json` via `fetch`, che i browser bloccano se apri il file con
doppio-clic (`file://`). Per l'anteprima locale avvia un server nella cartella:

```bash
python3 -m http.server 8080
# poi apri http://localhost:8080
```

Su GitHub Pages non serve fare nulla: funziona già servito via HTTP.

## Crediti

Mappe e dati provengono dalla serie su r/ITAGLIA di u/DateAffectionate3719.
Questo è un visualizzatore non ufficiale creato a scopo di fan-project.
