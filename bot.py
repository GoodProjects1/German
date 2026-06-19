# -*- coding: utf-8 -*-
"""
Bot Telegram per lo studio quotidiano del tedesco.

Invia ogni giorno, all'orario impostato, una lezione (lettura, ascolto,
grammatica, speaking, vocaboli, modo di dire) pescando dai 15 giorni
pre-impostati in content.py. Quando i giorni finiscono, ricomincia da capo.

Variabili d'ambiente (da impostare su Railway):
  TELEGRAM_TOKEN     (obbligatoria)  -> token del bot, da @BotFather
  TELEGRAM_CHAT_ID   (consigliata)   -> la tua chat id; riceve sempre la lezione
  START_DATE         (consigliata)   -> 'AAAA-MM-GG', il giorno 1 del percorso
  SEND_HOUR          (default 8)      -> ora di invio
  SEND_MINUTE        (default 0)      -> minuto di invio
  TIMEZONE           (default Europe/Rome)
"""

import os
import json
import logging
from datetime import date, datetime, time
from zoneinfo import ZoneInfo

from telegram import Update
from telegram.constants import ParseMode
from telegram.error import TelegramError
from telegram.ext import Application, CommandHandler, ContextTypes

from content import build_lesson_messages, total_days

# --------------------------------------------------------------------------- #
#  Configurazione                                                              #
# --------------------------------------------------------------------------- #
logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("german-bot")

TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise SystemExit("ERRORE: manca la variabile d'ambiente TELEGRAM_TOKEN.")

ENV_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
TIMEZONE = os.environ.get("TIMEZONE", "Europe/Rome")
SEND_HOUR = int(os.environ.get("SEND_HOUR", "8"))
SEND_MINUTE = int(os.environ.get("SEND_MINUTE", "0"))
START_DATE = os.environ.get("START_DATE", "").strip()  # 'AAAA-MM-GG'

TZ = ZoneInfo(TIMEZONE)
SUBSCRIBERS_FILE = "subscribers.json"


# --------------------------------------------------------------------------- #
#  Gestione iscritti (file locale + chat id da variabile d'ambiente)           #
# --------------------------------------------------------------------------- #
def load_subscribers() -> set:
    ids = set()
    if ENV_CHAT_ID:
        ids.add(int(ENV_CHAT_ID))
    try:
        with open(SUBSCRIBERS_FILE, "r", encoding="utf-8") as f:
            ids.update(int(x) for x in json.load(f))
    except (FileNotFoundError, ValueError, json.JSONDecodeError):
        pass
    return ids


def save_subscribers(ids: set) -> None:
    # non salviamo l'id che arriva dalla variabile d'ambiente: è sempre incluso
    to_save = [i for i in ids if str(i) != ENV_CHAT_ID]
    try:
        with open(SUBSCRIBERS_FILE, "w", encoding="utf-8") as f:
            json.dump(to_save, f)
    except OSError as e:
        logger.warning("Impossibile salvare gli iscritti: %s", e)


# --------------------------------------------------------------------------- #
#  Calcolo della lezione del giorno (deterministico dalla data)                #
# --------------------------------------------------------------------------- #
def get_lesson_for_today() -> tuple[int, int]:
    """
    Ritorna (day_index, lesson_number).
    Il numero di lezione si basa sui giorni trascorsi da START_DATE, così
    resta coerente anche dopo un riavvio o un nuovo deploy su Railway.
    """
    total = total_days()
    if START_DATE:
        try:
            anchor = datetime.strptime(START_DATE, "%Y-%m-%d").date()
        except ValueError:
            logger.warning("START_DATE non valida ('%s'), uso oggi.", START_DATE)
            anchor = date.today()
    else:
        anchor = date.today()

    days_passed = (date.today() - anchor).days
    if days_passed < 0:
        days_passed = 0
    lesson_number = days_passed + 1
    day_index = days_passed % total
    return day_index, lesson_number


# --------------------------------------------------------------------------- #
#  Invio                                                                        #
# --------------------------------------------------------------------------- #
async def send_lesson(context: ContextTypes.DEFAULT_TYPE, chat_ids, day_index, lesson_number):
    blocks = build_lesson_messages(day_index, lesson_number)
    for chat_id in chat_ids:
        for block in blocks:
            try:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=block,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except TelegramError as e:
                logger.warning("Invio fallito a %s: %s", chat_id, e)
                break  # se la prima parte fallisce, salta questo utente


async def daily_job(context: ContextTypes.DEFAULT_TYPE):
    """Eseguito automaticamente ogni giorno all'orario impostato."""
    subscribers = load_subscribers()
    if not subscribers:
        logger.info("Nessun iscritto: lezione non inviata.")
        return
    day_index, lesson_number = get_lesson_for_today()
    logger.info("Invio lezione #%s a %d iscritti.", lesson_number, len(subscribers))
    await send_lesson(context, subscribers, day_index, lesson_number)


# --------------------------------------------------------------------------- #
#  Comandi                                                                      #
# --------------------------------------------------------------------------- #
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    subs = load_subscribers()
    subs.add(chat_id)
    save_subscribers(subs)
    await update.message.reply_text(
        "🇩🇪 <b>Willkommen!</b> Sei iscritto al promemoria quotidiano di tedesco.\n\n"
        f"Riceverai una lezione ogni giorno alle "
        f"<b>{SEND_HOUR:02d}:{SEND_MINUTE:02d}</b> ({TIMEZONE}).\n\n"
        f"La tua chat id è <code>{chat_id}</code> — utile da mettere nella variabile "
        "<code>TELEGRAM_CHAT_ID</code> su Railway, così ricevi la lezione anche dopo i riavvii.\n\n"
        "Comandi:\n"
        "• /oggi — la lezione di oggi\n"
        "• /giorno N — vedi la lezione del giorno N (1–{n})\n"
        "• /stop — disattiva il promemoria\n"
        "• /help — guida".format(n=total_days()),
        parse_mode=ParseMode.HTML,
    )


async def cmd_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    subs = load_subscribers()
    subs.discard(chat_id)
    save_subscribers(subs)
    await update.message.reply_text(
        "Promemoria disattivato. Scrivi /start quando vuoi riprendere. Tschüss! 👋"
    )


async def cmd_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_index, lesson_number = get_lesson_for_today()
    await send_lesson(context, [update.effective_chat.id], day_index, lesson_number)


async def cmd_day(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total = total_days()
    if not context.args:
        await update.message.reply_text(f"Uso: /giorno N  (N da 1 a {total})")
        return
    try:
        n = int(context.args[0])
    except ValueError:
        await update.message.reply_text("Devi indicare un numero. Es.: /giorno 3")
        return
    if not (1 <= n <= total):
        await update.message.reply_text(f"Scegli un numero tra 1 e {total}.")
        return
    await send_lesson(context, [update.effective_chat.id], n - 1, n)


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 <b>Bot di tedesco</b>\n\n"
        "Ogni giorno ricevi: una notizia da leggere, una canzone da ascoltare, "
        "una regola di grammatica (difficoltà crescente), un esercizio di speaking "
        "da fare con un'AI, parole nuove (solo tedesche / simili / falsi amici) e un "
        "modo di dire.\n\n"
        "Comandi:\n"
        "• /start — iscriviti\n"
        "• /oggi — lezione di oggi\n"
        f"• /giorno N — lezione del giorno N (1–{total_days()})\n"
        "• /stop — disattiva\n"
        "• /help — questa guida",
        parse_mode=ParseMode.HTML,
    )


# --------------------------------------------------------------------------- #
#  Avvio                                                                        #
# --------------------------------------------------------------------------- #
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("stop", cmd_stop))
    app.add_handler(CommandHandler("oggi", cmd_today))
    app.add_handler(CommandHandler("today", cmd_today))
    app.add_handler(CommandHandler("giorno", cmd_day))
    app.add_handler(CommandHandler("day", cmd_day))
    app.add_handler(CommandHandler("help", cmd_help))

    # Pianifica l'invio giornaliero
    app.job_queue.run_daily(
        daily_job,
        time=time(hour=SEND_HOUR, minute=SEND_MINUTE, tzinfo=TZ),
        name="lezione_quotidiana",
    )

    logger.info(
        "Bot avviato. Invio giornaliero alle %02d:%02d (%s). Giorni disponibili: %d.",
        SEND_HOUR, SEND_MINUTE, TIMEZONE, total_days(),
    )
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
