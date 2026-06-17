import os
import json
import logging
from datetime import time as dtime
from urllib.parse import quote_plus
from zoneinfo import ZoneInfo

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
STUDY_HOUR = int(os.environ.get("STUDY_HOUR", 8))
STUDY_MINUTE = int(os.environ.get("STUDY_MINUTE", 0))
TIMEZONE = os.environ.get("TIMEZONE", "Europe/Rome")

STATE_FILE = "state.json"
READING_URL = "https://www.nachrichtenleicht.de/"

# ── Contenuto: 14 giorni, grammatica a difficoltà crescente, niente ripetizioni ──

GRAMMAR = [
    {"topic": "Perfekt mit haben", "rule": "Per le azioni quotidiane il passato si forma con haben + Partizip II.",
     "example_de": "Ich habe gestern gekocht.", "example_it": "Ieri ho cucinato."},
    {"topic": "Perfekt mit sein", "rule": "Verbi di movimento o cambiamento di stato formano il Perfekt con sein.",
     "example_de": "Sie ist nach Berlin gefahren.", "example_it": "È andata a Berlino."},
    {"topic": "Modalverben", "rule": "Il verbo modale si conjuga, l'infinito va in fondo alla frase.",
     "example_de": "Ich muss heute früh aufstehen.", "example_it": "Oggi devo svegliarmi presto."},
    {"topic": "Nebensatz mit weil", "rule": "Dopo weil il verbo va in fondo alla frase secondaria.",
     "example_de": "Ich bleibe zu Hause, weil ich krank bin.", "example_it": "Resto a casa perché sono malato."},
    {"topic": "Nebensatz mit dass", "rule": "dass introduce una frase secondaria, verbo sempre in fondo.",
     "example_de": "Ich glaube, dass er Recht hat.", "example_it": "Credo che lui abbia ragione."},
    {"topic": "Komparativ und Superlativ", "rule": "Comparativo: aggettivo + er. Superlativo: am + aggettivo + sten.",
     "example_de": "Berlin ist groß, München ist größer, aber Berlin ist am größten.",
     "example_it": "Berlino è grande, Monaco è più grande, ma Berlino è la più grande."},
    {"topic": "Präpositionen mit Akkusativ", "rule": "für, durch, gegen, ohne, um richiedono sempre l'accusativo.",
     "example_de": "Das Geschenk ist für dich.", "example_it": "Il regalo è per te."},
    {"topic": "Präpositionen mit Dativ", "rule": "mit, nach, bei, von, zu, aus richiedono sempre il dativo.",
     "example_de": "Ich fahre mit dem Bus zur Arbeit.", "example_it": "Vado al lavoro con l'autobus."},
    {"topic": "Wechselpräpositionen", "rule": "in, an, auf usano l'accusativo se c'è movimento, il dativo se c'è stato.",
     "example_de": "Ich lege das Buch auf den Tisch. / Das Buch liegt auf dem Tisch.",
     "example_it": "Metto il libro sul tavolo. / Il libro è sul tavolo."},
    {"topic": "Relativsätze", "rule": "der/die/das come pronomi relativi si accordano con il genere del nome a cui si riferiscono.",
     "example_de": "Das ist die Frau, die nebenan wohnt.", "example_it": "Questa è la donna che abita di fianco."},
    {"topic": "Konjunktiv II (würde)", "rule": "würde + infinito si usa per richieste cortesi o ipotesi.",
     "example_de": "Ich würde gern mehr Deutsch sprechen.", "example_it": "Mi piacerebbe parlare più tedesco."},
    {"topic": "Passiv Präsens", "rule": "werden + Partizip II forma il passivo al presente.",
     "example_de": "Das Brot wird jeden Tag frisch gebacken.", "example_it": "Il pane viene cotto fresco ogni giorno."},
    {"topic": "Genitiv", "rule": "Il genitivo indica possesso; gli articoli diventano des/der + spesso -s al nome maschile/neutro.",
     "example_de": "Das ist das Auto meines Bruders.", "example_it": "Questa è la macchina di mio fratello."},
    {"topic": "Konjunktiv II (irreale)", "rule": "wäre/hätte + Partizip II per parlare di situazioni irreali o ipotesi nel passato.",
     "example_de": "Wenn ich Zeit gehabt hätte, wäre ich gekommen.", "example_it": "Se avessi avuto tempo, sarei venuto."},
]

LISTENING = [
    ("Nena", "99 Luftballons", "Classico anni '80, pronuncia chiara, testo semplice e iconico."),
    ("Wir sind Helden", "Denkmal", "Pop-rock con testi diretti, buon esercizio d'ascolto per il livello B1."),
    ("Tokio Hotel", "Durch den Monsun", "Ritmo orecchiabile, frasi brevi e ripetitive, ottimo per principianti."),
    ("Cro", "Easy", "Rap leggero con frasi semplici e molte ripetizioni."),
    ("Mark Forster", "Chöre", "Pop moderno con dizione chiara, ritornello facile da imparare."),
    ("Silbermond", "Symphonie", "Ballata melodica, utile per il vocabolario dei sentimenti."),
    ("Element of Crime", "Delmenhorst", "Cantautorato con testo poetico ma cadenzato."),
    ("Herbert Grönemeyer", "Männer", "Classico tedesco, frasi brevi e dirette."),
    ("Peter Fox", "Haus am See", "Ritmo allegro, testo narrativo con vocabolario quotidiano."),
    ("AnnenMayKantereit", "Pocahontas", "Voce molto chiara, ottimo per esercitare l'ascolto."),
    ("Annett Louisan", "Das Spiel", "Ritmo lento, perfetto per seguire ogni parola."),
    ("Juli", "Perfekte Welle", "Pop-rock con ritornello molto orecchiabile."),
    ("Ich + Ich", "Vom selben Stern", "Ballata romantica con frasi semplici sui sentimenti."),
    ("Rosenstolz", "Ich bin ich (Wir sind wir)", "Inno motivazionale con frasi dirette e ripetitive."),
]

SPEAKING = [
    ["Stell dich vor: Wie heißt du, woher kommst du, was machst du beruflich?",
     "Beschreibe deine Wohnung in drei Sätzen.", "Was hast du heute Morgen gemacht?"],
    ["Erzähl von deiner Familie.", "Was isst du normalerweise zum Frühstück?",
     "Wie kommst du zur Arbeit oder zur Schule?"],
    ["Was machst du gern am Wochenende?", "Beschreibe deinen Lieblingsort in deiner Stadt.",
     "Was für ein Hobby möchtest du noch lernen?"],
    ["Erzähl von einem Gespräch, das dir wichtig war.", "Was bedeutet für dich Erfolg?",
     "Beschreibe einen typischen Tag bei dir."],
    ["Erzähl von einer Erfahrung, die dich verändert hat.", "Was brauchst du, um glücklich zu sein?",
     "Beschreibe das Verhältnis zu deinem besten Freund oder deiner besten Freundin."],
    ["Worüber freust du dich gerade?", "Erzähl von einer Gelegenheit, die du verpasst hast.",
     "Welche Mittel benutzt du, um Deutsch zu lernen?"],
    ["Was bedeutet für dich Pünktlichkeit?", "Erzähl von einem Vorbild in deinem Leben.",
     "Was machst du, wenn du dich verspätest?"],
    ["Beschreibe eine wichtige Beziehung in deinem Leben.", "Worüber denkst du oft nach?",
     "Glaubst du an das Schicksal? Warum?"],
    ["Wonach sehnst du dich gerade?", "Erzähl von einem Zufall, der dir passiert ist.",
     "Was hast du in letzter Zeit bemerkt?"],
    ["Wovor solltest du vorsichtig sein?", "Erzähl von etwas, das dir gelungen ist.",
     "Was ist dein größtes Bedürfnis im Moment?"],
    ["Erzähl von einer schwierigen Entscheidung.", "Was vermeidest du normalerweise?",
     "Welchen Eindruck möchtest du bei anderen hinterlassen?"],
    ["Wofür fühlst du dich verantwortlich?", "Worüber beschwerst du dich manchmal?",
     "Beschreibe deine Vorstellung von einem perfekten Tag."],
    ["Erzähl von einer Herausforderung, die du gerade hast.", "Wie verabschiedest du dich normalerweise von Freunden?",
     "Welche Gewohnheit möchtest du ändern?"],
    ["Erzähl von einer Überraschung, die du erlebt hast.", "An was erinnerst du dich aus deiner Kindheit gern?",
     "Wann brauchst du am meisten Geduld?"],
]

VOCAB = [
    {"german_only": [("die Wohnung", "appartamento"), ("der Kühlschrank", "frigorifero"), ("aufstehen", "alzarsi/svegliarsi")],
     "cognates": [("das Hotel", "hotel"), ("die Information", "informazione")],
     "false_friends": [("das Büro", "burro", "ufficio"), ("bekommen", "l'inglese become", "ricevere/ottenere")]},
    {"german_only": [("die Rechnung", "fattura/conto"), ("das Fenster", "finestra"), ("gehören", "appartenere")],
     "cognates": [("das Restaurant", "ristorante"), ("der Moment", "momento")],
     "false_friends": [("der Chef", "chef/cuoco", "capo, responsabile"), ("fast", "l'inglese fast (veloce)", "quasi")]},
    {"german_only": [("die Ausbildung", "formazione professionale"), ("der Termin", "appuntamento"), ("versuchen", "provare/tentare")],
     "cognates": [("das Problem", "problema"), ("die Universität", "università")],
     "false_friends": [("der Konkurs", "concorso", "bancarotta, fallimento"), ("das Handy", "l'inglese handy (comodo)", "telefono cellulare")]},
    {"german_only": [("die Umgebung", "dintorni/ambiente"), ("erreichen", "raggiungere"), ("das Gespräch", "conversazione")],
     "cognates": [("das Theater", "teatro"), ("die Adresse", "indirizzo")],
     "false_friends": [("das Gift", "regalo/gift", "veleno"), ("der Mist", "una nebbiolina", "letame, robaccia (esclamazione di disappunto)")]},
    {"german_only": [("die Erfahrung", "esperienza"), ("brauchen", "avere bisogno di"), ("das Verhältnis", "rapporto/relazione")],
     "cognates": [("der Computer", "computer"), ("das Foto", "foto")],
     "false_friends": [("der Brand", "marca/brand", "incendio"), ("das Glas", "glassa dolce", "vetro, bicchiere")]},
    {"german_only": [("die Gelegenheit", "occasione"), ("sich freuen", "essere felice/contento"), ("das Mittel", "mezzo/strumento")],
     "cognates": [("die Musik", "musica"), ("das Telefon", "telefono")],
     "false_friends": [("die Rente", "rendita", "pensione"), ("die Hochzeit", "alta epoca", "matrimonio")]},
    {"german_only": [("die Verspätung", "ritardo"), ("bedeuten", "significare"), ("das Vorbild", "modello/esempio")],
     "cognates": [("der Sport", "sport"), ("das Taxi", "taxi")],
     "false_friends": [("der Hut", "l'inglese hut (capanna)", "cappello"), ("das Bad", "l'inglese bad (cattivo)", "bagno (stanza)")]},
    {"german_only": [("die Beziehung", "relazione"), ("nachdenken", "riflettere"), ("das Schicksal", "destino")],
     "cognates": [("die Bank", "banca"), ("der Tourist", "turista")],
     "false_friends": [("der Konzern", "Konzert/concerto", "gruppo aziendale, multinazionale"), ("die Note", "nota musicale", "voto scolastico")]},
    {"german_only": [("die Sehnsucht", "nostalgia, desiderio profondo"), ("bemerken", "notare/accorgersi"), ("der Zufall", "caso/coincidenza")],
     "cognates": [("die Pizza", "pizza"), ("das Auto", "auto")],
     "false_friends": [("das Pony", "l'animale pony", "frangetta di capelli"), ("der Schal", "scialle", "sciarpa")]},
    {"german_only": [("die Vorsicht", "cautela"), ("gelingen", "riuscire"), ("das Bedürfnis", "bisogno/esigenza")],
     "cognates": [("der Doktor", "dottore"), ("die Idee", "idea")],
     "false_friends": [("die Tante", "tante (italiano)", "zia"), ("kalt", "caldo (italiano)", "freddo")]},
    {"german_only": [("die Entscheidung", "decisione"), ("vermeiden", "evitare"), ("der Eindruck", "impressione")],
     "cognates": [("das Radio", "radio"), ("die Garage", "garage")],
     "false_friends": [("der Stock", "l'inglese stock (scorta)", "piano di un edificio, bastone"), ("brav", "bravo (italiano)", "ubbidiente, ben educato")]},
    {"german_only": [("die Verantwortung", "responsabilità"), ("sich beschweren", "lamentarsi/reclamare"), ("die Vorstellung", "idea/rappresentazione")],
     "cognates": [("die Limonade", "limonata"), ("der Tee", "tè")],
     "false_friends": [("also", "l'inglese also (anche)", "quindi, dunque"), ("billig", "niente in particolare", "economico, scadente")]},
    {"german_only": [("die Herausforderung", "sfida"), ("sich verabschieden", "salutarsi/congedarsi"), ("die Gewohnheit", "abitudine")],
     "cognates": [("der Elefant", "elefante"), ("die Banane", "banana")],
     "false_friends": [("das Gymnasium", "l'inglese gymnasium (palestra)", "liceo"), ("die Hose", "l'inglese hose (tubo flessibile)", "pantaloni")]},
    {"german_only": [("die Überraschung", "sorpresa"), ("sich erinnern", "ricordarsi"), ("die Geduld", "pazienza")],
     "cognates": [("das Internet", "internet"), ("die Politik", "politica")],
     "false_friends": [("der Rat", "l'inglese rat (ratto)", "consiglio, parere"), ("die Mappe", "mappa", "cartella, raccoglitore di documenti")]},
]

PHRASES = [
    ("Da steppt der Bär.", "Lì si scatena la festa.", "Si usa per dire che un posto o un evento è molto divertente e animato."),
    ("Ich glaub, ich spinne.", "Non riesco a crederci.", "Esprime sorpresa o incredulità, in modo informale."),
    ("Das ist mir Wurst.", "Per me è indifferente.", "Si usa quando qualcosa non importa affatto."),
    ("Die Katze im Sack kaufen.", "Comprare alla cieca.", "Corrisponde all'italiano «comprare a scatola chiusa»."),
    ("Tomaten auf den Augen haben.", "Non vedere l'ovvio.", "Si dice quando qualcuno non si accorge di una cosa evidente."),
    ("Jemandem die Daumen drücken.", "Tenere le dita incrociate per qualcuno.", "Equivalente del nostro «in bocca al lupo» come gesto di augurio."),
    ("Schwein haben.", "Avere fortuna.", "Si usa quando capita un colpo di fortuna inaspettato."),
    ("Den Nagel auf den Kopf treffen.", "Colpire nel segno.", "Corrisponde all'italiano «centrare il punto»."),
    ("Hals- und Beinbruch!", "Buona fortuna!", "Augurio scherzoso usato prima di un evento importante."),
    ("Um den heißen Brei reden.", "Girare attorno al problema.", "Si usa quando si evita di dire le cose chiaramente."),
    ("Da liegt der Hund begraben.", "Qui sta il problema.", "Indica la vera causa di una difficoltà."),
    ("Eine Extrawurst bekommen.", "Ricevere un trattamento speciale.", "Si usa quando qualcuno ottiene un favore particolare."),
    ("Ins Gras beißen.", "Tirare le cuoia.", "Modo informale e un po' nero per dire «morire», usalo con cautela."),
    ("Alles hat ein Ende, nur die Wurst hat zwei.", "Tutto finisce.", "Modo scherzoso per dire che ogni cosa arriva alla fine."),
]

TOTAL_DAYS = len(GRAMMAR)


def load_day() -> int:
    try:
        with open(STATE_FILE) as f:
            return json.load(f).get("day", 0)
    except FileNotFoundError:
        return 0


def save_day(day: int) -> None:
    with open(STATE_FILE, "w") as f:
        json.dump({"day": day}, f)


def yt_search(artist: str, song: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(f"{artist} {song}")


def build_messages(day: int) -> list:
    i = day % TOTAL_DAYS
    g = GRAMMAR[i]
    artist, song, why_listen = LISTENING[i]
    vocab = VOCAB[i]
    phrase_de, phrase_it, phrase_ctx = PHRASES[i]

    out = [f"📚 <b>Tedesco — Giorno {day + 1}</b>\nEcco il programma di oggi 👇"]

    out.append(
        "📰 <b>Reading</b>\n"
        f"<a href=\"{READING_URL}\">Nachrichtenleicht — notizie in tedesco semplice</a>\n"
        "Ogni giorno nuove notizie scritte apposta in un tedesco facile da leggere."
    )

    out.append(
        "🎧 <b>Listening</b>\n"
        f"<a href=\"{yt_search(artist, song)}\">{song} — {artist}</a>\n"
        f"{why_listen}"
    )

    out.append(
        f"🧩 <b>Grammar — {g['topic']}</b>\n"
        f"{g['rule']}\n\n"
        f"DE: {g['example_de']}\n"
        f"IT: {g['example_it']}"
    )

    sp = "\n".join(f"• {p}" for p in SPEAKING[i])
    out.append("🗣️ <b>Speaking</b>\nProva queste frasi con un assistente AI vocale:\n" + sp)

    vocab_text = "📝 <b>Vocabolario nuovo</b>\n\n<b>Solo tedesco</b>\n"
    vocab_text += "\n".join(f"• {de} — {it}" for de, it in vocab["german_only"])
    vocab_text += "\n\n<b>Uguali in tedesco/inglese/italiano</b>\n"
    vocab_text += "\n".join(f"• {de} — {it}" for de, it in vocab["cognates"])
    vocab_text += "\n\n<b>⚠️ False friends</b>\n"
    vocab_text += "\n".join(f"• {de} (sembra: {like}) → {real}" for de, like, real in vocab["false_friends"])
    out.append(vocab_text)

    out.append(
        "💬 <b>Frase del giorno</b>\n"
        f"<i>{phrase_de}</i>\n"
        f"{phrase_it}\n\n"
        f"{phrase_ctx}"
    )

    return out


async def send_today(chat, day: int) -> None:
    for msg in build_messages(day):
        await chat.send_message(msg, parse_mode="HTML", disable_web_page_preview=False)


async def daily_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    day = load_day()
    await send_today(context.bot, day)
    save_day(day + 1)
    logger.info(f"Inviato programma giorno {day + 1}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Ciao! 🇩🇪 Il tuo bot di tedesco è attivo.\n"
        f"Ogni giorno alle {STUDY_HOUR:02d}:{STUDY_MINUTE:02d} ({TIMEZONE}) ricevi il programma di studio.\n"
        "Usa /oggi per vedere subito il programma di oggi."
    )


async def oggi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    day = load_day()
    await send_today(update.message, day)
    save_day(day + 1)


def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("oggi", oggi))
    app.job_queue.run_daily(
        daily_job,
        time=dtime(hour=STUDY_HOUR, minute=STUDY_MINUTE, tzinfo=ZoneInfo(TIMEZONE)),
    )
    logger.info("Bot avviato ✅")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
