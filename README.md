# 🇩🇪 Bot Telegram – Promemoria di tedesco

Un bot Telegram che ogni giorno ti invia una lezione di tedesco con: una **notizia** da leggere, una **canzone** da ascoltare, una **regola di grammatica** (difficoltà crescente dal giorno 1 al 15), un esercizio di **speaking** da fare con un'AI, **parole nuove** (solo tedesche / simili a IT-EN / falsi amici) e un **modo di dire**.

I contenuti sono **15 giorni già pronti** dentro `content.py`. Quando finiscono, il bot ricomincia da capo: per rinnovarli basta aggiungere altri giorni alla lista (vedi sotto).

---

## 1. Crea il bot su Telegram (2 minuti)

1. Apri Telegram e cerca **@BotFather**.
2. Scrivi `/newbot`, scegli un nome e uno username (deve finire in `bot`).
3. BotFather ti dà un **token** tipo `8123456789:AAH...`. Copialo: ti servirà come `TELEGRAM_TOKEN`.

### Trovare la tua chat id (consigliato)
Avvia il tuo bot e scrivigli `/start`: il bot ti risponderà mostrando la tua **chat id** (un numero). Tienila da parte per `TELEGRAM_CHAT_ID`. (In alternativa puoi usare il bot **@userinfobot**.)

---

## 2. Carica il progetto su GitHub

```bash
git init
git add .
git commit -m "Bot tedesco: 15 giorni pre-impostati"
git branch -M main
git remote add origin https://github.com/TUO-UTENTE/german-study-bot.git
git push -u origin main
```

> Il file `.gitignore` esclude già `.env` e `subscribers.json`: il token **non** finirà su GitHub.

---

## 3. Deploy su Railway

1. Vai su [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo** → scegli il repo.
2. Railway usa il file `railway.json` incluso: builder **Railpack** e comando di avvio `python bot.py` (già configurati, non devi toccare nulla).
3. Apri la scheda **Variables** e aggiungi:

| Variabile | Valore | Note |
|---|---|---|
| `TELEGRAM_TOKEN` | il token di BotFather | **obbligatoria** |
| `TELEGRAM_CHAT_ID` | la tua chat id | consigliata: ti garantisce la lezione anche dopo i riavvii |
| `START_DATE` | es. `2026-06-20` | il giorno "1" del percorso |
| `SEND_HOUR` | `8` | ora di invio (0–23) |
| `SEND_MINUTE` | `0` | minuto di invio |
| `TIMEZONE` | `Europe/Rome` | fuso orario |

4. Salva: Railway riavvia e il bot parte. Da quel momento riceverai la lezione ogni giorno all'orario scelto.

> **Nota su Railway:** il filesystem è effimero (gli iscritti salvati nel file possono azzerarsi a ogni nuovo deploy). Per questo c'è `TELEGRAM_CHAT_ID`: quell'id riceve **sempre** la lezione, a prescindere dai riavvii. Per uso personale è la soluzione più affidabile.

---

## 4. Comandi del bot

| Comando | Cosa fa |
|---|---|
| `/start` | Ti iscrive e mostra la tua chat id |
| `/oggi` | Invia subito la lezione di oggi (utile per provarlo) |
| `/giorno N` | Mostra la lezione del giorno N (1–15) |
| `/stop` | Disattiva il promemoria |
| `/help` | Guida rapida |

---

## 5. Come RINNOVARE i contenuti (dopo i 15 giorni)

Apri `content.py` e aggiungi nuovi dizionari alla lista `DAYS`, copiando la struttura di un giorno esistente. Il bot rileva da solo quanti giorni ci sono: se ne aggiungi fino a 30, il ciclo diventa di 30 giorni. Poi fai commit e push: Railway aggiorna in automatico.

```python
DAYS = [
    { ...giorno 1... },
    # ...
    { ...giorno 15... },
    { ...giorno 16 (nuovo)... },   # <-- aggiungi qui
]
```

Ogni giorno ha queste sezioni: `thema`, `reading`, `listening`, `grammar`, `speaking`, `vocab` (con `nur_deutsch`, `cognates`, `false_friends`) e `idiom`. Le commenti in cima al file spiegano ogni campo.

---

## 6. Provare in locale (facoltativo)

```bash
pip install -r requirements.txt
cp .env.example .env        # poi inserisci i tuoi valori
export $(grep -v '^#' .env | xargs)   # carica le variabili (Linux/Mac)
python bot.py
```
Poi scrivi `/oggi` al bot per vedere la lezione.

---

### Perché i link non "scadono"

Per le notizie e le canzoni il bot usa **link di ricerca** (Google News in tedesco e ricerca YouTube): puntano sempre a risultati reali e aggiornati, quindi non rischi mai un link rotto. Le fonti consigliate (Nachrichtenleicht, Deutsche Welle, tagesschau) sono siti stabili pensati per chi impara il tedesco.

Viel Erfolg! 🎓

---

## ⚠️ Risoluzione problemi di deploy

**"railpack process exited with an error" / build fallito**
- Causa più comune: un file `runtime.txt` con un formato che Railpack non gradisce (es. `python-3.12.7`). Questo progetto **non** lo include apposta: Railpack usa Python 3.13 di default, che va benissimo.
- Se vuoi comunque fissare la versione, NON usare `runtime.txt`: crea un file `.python-version` con dentro solo `3.12`.

**"No start command could be found"**
- Il file `railway.json` incluso imposta già `python bot.py`. In alternativa puoi impostarlo a mano in Railway → **Settings** → **Deploy** → **Custom Start Command**: `python bot.py`.

**Il bot non parte / si riavvia in loop**
- Controlla i **Deploy Logs** su Railway: quasi sempre è una variabile mancante (`TELEGRAM_TOKEN`).
- Essendo un bot in "polling" non espone una porta: è normale che Railway non mostri un dominio pubblico. Non serve.
