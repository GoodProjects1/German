# 🇩🇪 German Study Bot

Bot Telegram personale per studiare tedesco. Ogni giorno invia un programma con:
reading, listening, una regola di grammatica (difficoltà crescente nel tempo),
spunti per il speaking, vocaboli nuovi (solo tedesco / uguali a IT-EN / false friends)
e una frase idiomatica del giorno.

Versione "semplice per i primi giorni": 14 giorni di contenuti curati a mano,
nessuna chiamata a servizi esterni a parte Telegram — niente API key da pagare,
niente da configurare oltre al bot stesso. Dal giorno 15 il ciclo riparte
(possiamo espanderlo con altri giorni, o collegarlo a un'AI per contenuti
sempre nuovi, quando vuoi passare al livello successivo).

---

## 🚀 Setup — GitHub + Railway (stesso schema di sempre)

### STEP 1 — Crea il bot Telegram (2 min)

1. Apri Telegram, cerca **@BotFather**
2. Invia `/newbot` → segui le istruzioni (nome + username che finisce in `_bot`)
3. BotFather ti manda il **TOKEN** (es. `1234567890:AAFxxx...`) → copialo

### STEP 2 — Trova il tuo Chat ID (1 min)

1. Cerca **@userinfobot** su Telegram
2. Invia `/start` → ti risponde con il tuo **ID numerico** (es. `123456789`) → copialo

### STEP 3 — Deploy su Railway (5 min)

1. Crea un repo su GitHub e carica questi file (bot.py, requirements.txt, railway.toml, .gitignore)
2. Vai su **railway.app** → **"New Project"** → **"Deploy from GitHub repo"** → seleziona il repo
3. In Railway, vai su **"Variables"** e aggiungi:
   ```
   TELEGRAM_TOKEN = il-tuo-token-da-BotFather
   CHAT_ID        = il-tuo-id-da-userinfobot
   ```
   Opzionali (hanno già un valore di default sensato):
   ```
   STUDY_HOUR   = 8        # ora di invio (0-23)
   STUDY_MINUTE = 0        # minuti
   TIMEZONE     = Europe/Rome
   ```
4. Railway fa il deploy automaticamente — aspetta 1-2 minuti

### STEP 4 — Avvia il bot (30 sec)

1. Vai su Telegram, trova il tuo bot
2. Invia `/start` → confermerà che è attivo
3. Invia `/oggi` per vedere subito il programma di oggi senza aspettare l'orario fissato

---

## Note

- Il contatore del giorno è salvato in un file locale (`state.json`) sul container Railway:
  se rifai il deploy da zero o cambi servizio, il contatore può ripartire da 0 — non è un problema,
  semplicemente ricomincia il ciclo dei 14 giorni.
- Il link "Reading" punta a **nachrichtenleicht.de**, un sito vero che pubblica ogni giorno
  notizie scritte in tedesco facile — quindi il contenuto è sempre fresco anche se il link è fisso.
- I link "Listening" sono ricerche YouTube già pronte (titolo + artista), così funzionano sempre
  anche se cambia il video esatto disponibile.
- Quando vuoi smettere con la versione "fissa" e passare a contenuti generati al volo (articolo
  diverso ogni giorno, vocaboli sempre nuovi, ecc.) possiamo aggiungere una chiamata all'API di
  Claude — te lo preparo quando sei pronto.
