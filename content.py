# -*- coding: utf-8 -*-
"""
Contenuti di studio del tedesco: 15 giorni pre-impostati.

Per RINNOVARE i contenuti: aggiungi semplicemente altri dizionari alla lista
DAYS qui sotto, mantenendo la stessa struttura. Il bot rileva da solo quanti
giorni ci sono e li fa ciclare automaticamente.

Struttura di un giorno:
{
  "thema": "<tema del giorno in italiano>",
  "reading":   {"quelle": <nome fonte>, "url": <link fonte affidabile>,
                "news_query": <argomento per Google News in tedesco>,
                "tipp": <consiglio>},
  "listening": {"artist": <artista>, "titel": <titolo canzone>, "tipp": <consiglio>},
  "grammar":   {"titel": <titolo regola>, "erklaerung": <spiegazione IT>,
                "beispiele": [(<frase DE>, <traduzione IT>), ...]},
  "speaking":  {"prompt": <prompt da incollare in un'AI>, "saetze": [<frase di avvio>, ...]},
  "vocab":     {"nur_deutsch":   [(<parola DE>, <traduzione>), ...],
                "cognates":      [(<parola DE>, <parola simile EN/IT>), ...],
                "false_friends": [(<parola DE>, <significato + avviso>), ...]},
  "idiom":     {"phrase": <modo di dire/citazione>, "woertlich": <traduzione letterale>,
                "bedeutung": <significato>, "italienisch": <equivalente italiano>}
}
"""

from urllib.parse import quote_plus
from html import escape


# --------------------------------------------------------------------------- #
#  I 15 GIORNI                                                                  #
# --------------------------------------------------------------------------- #
DAYS = [
    # ----------------------------- GIORNO 1 -------------------------------- #
    {
        "thema": "Saluti e persone",
        "reading": {
            "quelle": "Nachrichtenleicht (notizie in tedesco semplice)",
            "url": "https://www.nachrichtenleicht.de/",
            "news_query": "Deutschland aktuelle Nachrichten",
            "tipp": "Sito di notizie in tedesco FACILE: frasi corte e parole spiegate. Perfetto per iniziare.",
        },
        "listening": {
            "artist": "Tim Bendzko",
            "titel": "Nur noch kurz die Welt retten",
            "tipp": "Pronuncia chiarissima e ritmo lento: ideale per i primi ascolti. Leggi il testo mentre ascolti.",
        },
        "grammar": {
            "titel": "I pronomi personali + i verbi sein (essere) e haben (avere)",
            "erklaerung": "I due verbi più importanti del tedesco. Imparali a memoria. "
                          "SEIN: ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie/Sie sind. "
                          "HABEN: ich habe, du hast, er/sie/es hat, wir haben, ihr habt, sie/Sie haben.",
            "beispiele": [
                ("Ich bin müde.", "Sono stanco/a."),
                ("Du hast Zeit.", "Hai tempo."),
                ("Wir sind Freunde.", "Siamo amici."),
                ("Sie hat einen Bruder.", "Lei ha un fratello."),
            ],
        },
        "speaking": {
            "prompt": "Du bist mein geduldiger Deutschlehrer. Sprich mit mir auf sehr einfachem "
                      "Deutsch (Niveau A1) über das Thema 'sich vorstellen'. Stelle mir eine Frage "
                      "nach der anderen, korrigiere meine Fehler freundlich und erkläre sie kurz auf "
                      "Italienisch. Fangen wir an!",
            "saetze": [
                "Hallo, ich heiße ... und ich komme aus Italien.",
                "Ich lerne Deutsch seit ein paar Tagen.",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("der Mensch", "la persona / l'essere umano"),
                ("die Leute", "la gente"),
                ("kennenlernen", "fare conoscenza"),
                ("grüßen", "salutare"),
                ("die Freundschaft", "l'amicizia"),
            ],
            "cognates": [
                ("der Name", "name / nome"),
                ("die Familie", "family / famiglia"),
                ("die Person", "person / persona"),
                ("der Moment", "moment / momento"),
            ],
            "false_friends": [
                ("bekommen", "RICEVERE / ottenere — NON 'diventare'! (falso amico con l'inglese 'become')"),
                ("der Chef", "il CAPO / il direttore — NON il cuoco! (il cuoco è 'der Koch')"),
                ("sympathisch", "simpatico — qui invece coincide con l'italiano (utile saperlo)"),
            ],
        },
        "idiom": {
            "phrase": "Übung macht den Meister.",
            "woertlich": "L'esercizio fa il maestro.",
            "bedeutung": "Solo con la pratica costante si diventa bravi.",
            "italienisch": "La pratica rende perfetti / Sbagliando s'impara.",
        },
    },

    # ----------------------------- GIORNO 2 -------------------------------- #
    {
        "thema": "Famiglia e casa",
        "reading": {
            "quelle": "DW – Deutsch lernen (Deutsche Welle)",
            "url": "https://learngerman.dw.com/de/overview",
            "news_query": "Familie Alltag Deutschland",
            "tipp": "Corsi e articoli graduati per livello (A1–C). Cerca la sezione 'Nicos Weg' per i principianti.",
        },
        "listening": {
            "artist": "Namika",
            "titel": "Lieblingsmensch",
            "tipp": "Testo dolce e ripetitivo: ottimo per memorizzare vocaboli su persone ed emozioni.",
        },
        "grammar": {
            "titel": "Coniugazione dei verbi regolari al presente (Präsens)",
            "erklaerung": "Si prende la radice del verbo e si aggiungono le desinenze: "
                          "-e (ich), -st (du), -t (er/sie/es), -en (wir), -t (ihr), -en (sie/Sie). "
                          "Esempio con 'spielen' (giocare/suonare): ich spiele, du spielst, er spielt... "
                          "Se la radice finisce in -t o -d, si aggiunge una -e- (du arbeitest, er arbeitet).",
            "beispiele": [
                ("Ich spiele Fußball.", "Gioco a calcio."),
                ("Du wohnst in Italien.", "Tu abiti in Italia."),
                ("Er arbeitet viel.", "Lui lavora molto."),
                ("Wir lernen Deutsch.", "Noi impariamo il tedesco."),
            ],
        },
        "speaking": {
            "prompt": "Sprich mit mir auf einfachem Deutsch (A1) über meine Familie. Frag mich nach "
                      "meinen Eltern, Geschwistern und wo wir wohnen. Korrigiere meine Fehler und "
                      "erkläre sie auf Italienisch.",
            "saetze": [
                "Ich habe einen Bruder und eine Schwester.",
                "Meine Familie wohnt in einer kleinen Stadt.",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("der Schlüssel", "la chiave"),
                ("die Wohnung", "l'appartamento"),
                ("das Zimmer", "la stanza"),
                ("die Tür", "la porta"),
                ("aufräumen", "riordinare"),
            ],
            "cognates": [
                ("das Haus", "house / (casa)"),
                ("die Mutter", "mother / madre"),
                ("der Vater", "father / padre"),
                ("der Garten", "garden / (giardino)"),
            ],
            "false_friends": [
                ("die Firma", "la DITTA / l'azienda — NON la firma! (la firma è 'die Unterschrift')"),
                ("das Regal", "lo SCAFFALE — NON il regalo! (il regalo è 'das Geschenk')"),
                ("kalt", "FREDDO — attenzione: somiglia a 'caldo' ma è l'OPPOSTO!"),
            ],
        },
        "idiom": {
            "phrase": "Aller Anfang ist schwer.",
            "woertlich": "Ogni inizio è difficile.",
            "bedeutung": "È normale faticare all'inizio di qualcosa di nuovo.",
            "italienisch": "Il primo passo è sempre il più difficile.",
        },
    },

    # ----------------------------- GIORNO 3 -------------------------------- #
    {
        "thema": "Cibo e bevande",
        "reading": {
            "quelle": "Nachrichtenleicht",
            "url": "https://www.nachrichtenleicht.de/",
            "news_query": "Essen Ernährung Deutschland",
            "tipp": "Prova a riconoscere i verbi al presente che hai imparato ieri.",
        },
        "listening": {
            "artist": "Peter Fox",
            "titel": "Haus am See",
            "tipp": "Brano amatissimo in Germania. Ritmo piacevole e tante immagini quotidiane.",
        },
        "grammar": {
            "titel": "Articoli e genere (Nominativ): der / die / das",
            "erklaerung": "Ogni nome tedesco ha un genere: maschile (der), femminile (die), neutro (das); "
                          "al plurale l'articolo è sempre 'die'. L'articolo indeterminativo è 'ein' (m/n) "
                          "ed 'eine' (f). Consiglio: impara SEMPRE il nome insieme al suo articolo, "
                          "come fosse un'unica parola.",
            "beispiele": [
                ("der Mann", "l'uomo (m)"),
                ("die Frau", "la donna (f)"),
                ("das Kind", "il bambino (n)"),
                ("die Kinder", "i bambini (plurale)"),
            ],
        },
        "speaking": {
            "prompt": "Spiel die Rolle eines Kellners in einem deutschen Café. Sprich einfaches "
                      "Deutsch (A1). Frag mich, was ich essen und trinken möchte. Korrigiere meine "
                      "Fehler und erkläre sie auf Italienisch.",
            "saetze": [
                "Ich möchte einen Kaffee, bitte.",
                "Was empfehlen Sie?",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("das Brot", "il pane"),
                ("das Gemüse", "la verdura"),
                ("der Käse", "il formaggio"),
                ("lecker", "gustoso / buono"),
                ("das Frühstück", "la colazione"),
            ],
            "cognates": [
                ("der Kaffee", "coffee / caffè"),
                ("die Banane", "banana / banana"),
                ("die Pizza", "pizza / pizza"),
                ("das Wasser", "water / (acqua)"),
            ],
            "false_friends": [
                ("kalt", "FREDDO — di nuovo: NON 'caldo'! (caldo = 'warm' / 'heiß')"),
                ("das Kompott", "frutta cotta — non è esattamente la 'composta', ma ci va vicino"),
                ("die Marmelade", "marmellata/confettura — qui coincide con l'italiano, ottimo"),
            ],
        },
        "idiom": {
            "phrase": "Der Apfel fällt nicht weit vom Stamm.",
            "woertlich": "La mela non cade lontano dal tronco.",
            "bedeutung": "I figli somigliano ai genitori.",
            "italienisch": "Tale padre, tale figlio.",
        },
    },

    # ----------------------------- GIORNO 4 -------------------------------- #
    {
        "thema": "Città e trasporti",
        "reading": {
            "quelle": "DW – Top-Thema (notizie con audio e glossario)",
            "url": "https://learngerman.dw.com/de/deutsch-lernen/s-9528",
            "news_query": "Stadt Verkehr Deutschland",
            "tipp": "Ogni articolo ha l'audio + le parole difficili spiegate. Leggi e ascolta insieme.",
        },
        "listening": {
            "artist": "AnnenMayKantereit",
            "titel": "Barfuß am Klavier",
            "tipp": "Voce molto particolare e tedesco quotidiano. Buono per abituare l'orecchio.",
        },
        "grammar": {
            "titel": "Il caso accusativo (Akkusativ) — il complemento oggetto",
            "erklaerung": "Si usa per l'oggetto diretto (cosa/chi riceve l'azione). Cambia SOLO il "
                          "maschile: der → den, ein → einen. Femminile, neutro e plurale restano "
                          "uguali. Es.: 'Ich sehe DEN Mann' (vedo l'uomo), 'Ich habe EINEN Hund' "
                          "(ho un cane).",
            "beispiele": [
                ("Ich kaufe einen Apfel.", "Compro una mela."),
                ("Wir sehen den Bahnhof.", "Vediamo la stazione."),
                ("Sie liest ein Buch.", "Lei legge un libro."),
                ("Ich nehme die Straßenbahn.", "Prendo il tram."),
            ],
        },
        "speaking": {
            "prompt": "Ich bin ein Tourist in Berlin. Spiel einen Einheimischen und erkläre mir auf "
                      "einfachem Deutsch (A1–A2) den Weg zum Bahnhof. Stelle mir Fragen und korrigiere "
                      "meine Fehler auf Italienisch.",
            "saetze": [
                "Entschuldigung, wie komme ich zum Bahnhof?",
                "Ist es weit von hier?",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("die Straße", "la strada / via"),
                ("die Haltestelle", "la fermata"),
                ("die Fahrkarte", "il biglietto (dei mezzi)"),
                ("geradeaus", "dritto (direzione)"),
                ("abbiegen", "svoltare"),
            ],
            "cognates": [
                ("der Bus", "bus / autobus"),
                ("das Taxi", "taxi / taxi"),
                ("der Tunnel", "tunnel / tunnel"),
                ("die Position", "position / posizione"),
            ],
            "false_friends": [
                ("die Karte", "la mappa / la cartina (anche carta/tessera) — utile da ricordare"),
                ("die Mappe", "la CARTELLA / il raccoglitore — NON la mappa! (la mappa è 'die Karte')"),
                ("der Rock", "la GONNA — NON 'rock'! (la musica rock si dice comunque 'Rockmusik')"),
            ],
        },
        "idiom": {
            "phrase": "Ich verstehe nur Bahnhof.",
            "woertlich": "Capisco solo 'stazione'.",
            "bedeutung": "Non ci capisco niente.",
            "italienisch": "Per me è arabo / Non ci capisco un'acca.",
        },
    },

    # ----------------------------- GIORNO 5 -------------------------------- #
    {
        "thema": "Acquisti e negozi",
        "reading": {
            "quelle": "Nachrichtenleicht",
            "url": "https://www.nachrichtenleicht.de/",
            "news_query": "Einkaufen Preise Deutschland",
            "tipp": "Cerca gli accusativi nel testo: dove c'è 'den' o 'einen'?",
        },
        "listening": {
            "artist": "Mark Forster",
            "titel": "Chöre",
            "tipp": "Ritornello facile da cantare. Ottimo per la pronuncia delle vocali.",
        },
        "grammar": {
            "titel": "La negazione: 'nicht' contro 'kein'",
            "erklaerung": "'kein' nega un NOME (quando in italiano diresti 'nessun/non...un'): "
                          "Ich habe KEIN Auto = Non ho una macchina. "
                          "'nicht' nega tutto il resto (verbi, aggettivi, l'intera frase): "
                          "Das ist NICHT gut = Non è buono. Ich komme NICHT = Non vengo.",
            "beispiele": [
                ("Ich habe keine Zeit.", "Non ho tempo."),
                ("Das ist kein Problem.", "Non è un problema."),
                ("Ich verstehe das nicht.", "Non lo capisco."),
                ("Heute arbeite ich nicht.", "Oggi non lavoro."),
            ],
        },
        "speaking": {
            "prompt": "Spiel einen Verkäufer in einem Kleidungsgeschäft. Sprich einfaches Deutsch "
                      "(A2). Hilf mir, etwas zu kaufen, frag nach Größe und Farbe. Korrigiere meine "
                      "Fehler auf Italienisch.",
            "saetze": [
                "Ich suche eine Jacke in Größe M.",
                "Wie viel kostet das?",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("das Geschäft", "il negozio"),
                ("günstig", "conveniente / economico"),
                ("teuer", "caro"),
                ("die Kasse", "la cassa"),
                ("umtauschen", "cambiare (la merce)"),
            ],
            "cognates": [
                ("der Preis", "price / prezzo"),
                ("das Ticket", "ticket / biglietto"),
                ("der Test", "test / test"),
                ("die Garage", "garage / garage"),
            ],
            "false_friends": [
                ("das Geschenk", "il REGALO — da non confondere con 'Regal' (scaffale) di ieri!"),
                ("die Kaution", "la CAUZIONE / il deposito — NON 'caution' (= 'Vorsicht', cautela)"),
                ("kostbar", "prezioso / di valore — NON 'costoso' in senso negativo"),
            ],
        },
        "idiom": {
            "phrase": "Geiz ist geil.",
            "woertlich": "L'avarizia è fica.",
            "bedeutung": "Famoso slogan pubblicitario: risparmiare è bello/conveniente.",
            "italienisch": "Chi più spende meno spende (in chiave ironica).",
        },
    },

    # ----------------------------- GIORNO 6 -------------------------------- #
    {
        "thema": "Lavoro e studio",
        "reading": {
            "quelle": "DW – Deutsch im Job",
            "url": "https://learngerman.dw.com/de/deutsch-lernen/s-9528",
            "news_query": "Arbeit Beruf Deutschland",
            "tipp": "Da oggi le notizie sono un po' più complesse: non serve capire tutto, cogli il senso.",
        },
        "listening": {
            "artist": "Max Giesinger",
            "titel": "80 Millionen",
            "tipp": "Numeri, persone e quotidianità tedesca. Prova a trascrivere il ritornello a orecchio.",
        },
        "grammar": {
            "titel": "I verbi modali + la posizione del verbo a fine frase",
            "erklaerung": "Modali: können (potere/sapere), müssen (dovere), wollen (volere), "
                          "dürfen (avere il permesso), sollen (dovere morale), möchten (vorrei). "
                          "REGOLA CHIAVE: il verbo modale si coniuga in 2ª posizione, il secondo verbo "
                          "va ALL'INFINITO ALLA FINE della frase. Es.: 'Ich KANN gut Deutsch sprechen'.",
            "beispiele": [
                ("Ich kann gut schwimmen.", "So nuotare bene."),
                ("Wir müssen jetzt gehen.", "Dobbiamo andare adesso."),
                ("Möchtest du einen Kaffee trinken?", "Vorresti bere un caffè?"),
                ("Du sollst mehr lernen.", "Dovresti studiare di più."),
            ],
        },
        "speaking": {
            "prompt": "Führ ein einfaches Vorstellungsgespräch (Bewerbungsgespräch) mit mir auf "
                      "Deutsch (A2). Frag mich nach meinem Beruf, meinen Stärken und warum ich den Job "
                      "will. Korrigiere meine Fehler auf Italienisch.",
            "saetze": [
                "Ich arbeite als ... und ich kann gut im Team arbeiten.",
                "Ich möchte diesen Job, weil ...",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("die Arbeit", "il lavoro"),
                ("der Beruf", "la professione"),
                ("die Prüfung", "l'esame"),
                ("pünktlich", "puntuale"),
                ("erledigen", "sbrigare / portare a termine"),
            ],
            "cognates": [
                ("das Team", "team / squadra"),
                ("das Büro", "bureau / ufficio"),
                ("das Problem", "problem / problema"),
                ("die Pause", "pause / pausa"),
            ],
            "false_friends": [
                ("das Stipendium", "la BORSA DI STUDIO — NON lo stipendio! (lo stipendio è 'das Gehalt')"),
                ("die Note", "il VOTO scolastico (o nota musicale) — NON un appunto ('Notiz')"),
                ("das Gymnasium", "il LICEO — NON la palestra! (la palestra è 'das Fitnessstudio')"),
            ],
        },
        "idiom": {
            "phrase": "Das ist nicht mein Bier.",
            "woertlich": "Questa non è la mia birra.",
            "bedeutung": "Non è un problema mio / non mi riguarda.",
            "italienisch": "Non sono affari miei.",
        },
    },

    # ----------------------------- GIORNO 7 -------------------------------- #
    {
        "thema": "Tempo e routine quotidiana",
        "reading": {
            "quelle": "Nachrichtenleicht",
            "url": "https://www.nachrichtenleicht.de/",
            "news_query": "Alltag Deutschland Leben",
            "tipp": "Annota 3 parole nuove e prova a usarle in una frase tua.",
        },
        "listening": {
            "artist": "Clueso",
            "titel": "Gewinner",
            "tipp": "Dizione pulita e testo motivazionale. Ascoltalo due volte: la seconda capirai di più.",
        },
        "grammar": {
            "titel": "I verbi separabili (trennbare Verben)",
            "erklaerung": "Alcuni verbi hanno un prefisso che SI STACCA e va a fine frase. "
                          "Es.: aufstehen (alzarsi) → 'Ich STEHE um 7 Uhr AUF'. "
                          "einkaufen (fare la spesa) → 'Wir KAUFEN heute EIN'. "
                          "Prefissi comuni: auf-, an-, ab-, ein-, mit-, vor-, zu-, aus-.",
            "beispiele": [
                ("Ich stehe früh auf.", "Mi alzo presto."),
                ("Der Zug kommt um 8 Uhr an.", "Il treno arriva alle 8."),
                ("Rufst du mich an?", "Mi chiami (al telefono)?"),
                ("Wir kaufen am Samstag ein.", "Facciamo la spesa il sabato."),
            ],
        },
        "speaking": {
            "prompt": "Lass uns auf Deutsch (A2) über meinen Tagesablauf sprechen. Frag mich, wann ich "
                      "aufstehe, was ich morgens, mittags und abends mache. Achte besonders auf "
                      "trennbare Verben und korrigiere mich auf Italienisch.",
            "saetze": [
                "Ich stehe um sieben Uhr auf und frühstücke.",
                "Am Abend sehe ich fern oder lese ein Buch.",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("aufwachen", "svegliarsi"),
                ("der Feierabend", "fine della giornata lavorativa"),
                ("früh", "presto"),
                ("spät", "tardi"),
                ("die Woche", "la settimana"),
            ],
            "cognates": [
                ("die Minute", "minute / minuto"),
                ("die Stunde", "(hour) — vale come 'ora/lezione'"),
                ("der Kalender", "calendar / calendario"),
                ("das Ende", "end / (fine)"),
            ],
            "false_friends": [
                ("bald", "PRESTO (tempo) — NON 'bald' inglese (calvo = 'kahl')"),
                ("eventuell", "EVENTUALMENTE / forse — NON l'inglese 'eventually' (= 'schließlich')"),
                ("aktuell", "ATTUALE / corrente — NON l'inglese 'actually' (= 'eigentlich')"),
            ],
        },
        "idiom": {
            "phrase": "Morgenstund hat Gold im Mund.",
            "woertlich": "L'ora del mattino ha l'oro in bocca.",
            "bedeutung": "Chi si alza presto rende di più.",
            "italienisch": "Il mattino ha l'oro in bocca.",
        },
    },

    # ----------------------------- GIORNO 8 -------------------------------- #
    {
        "thema": "Corpo e salute",
        "reading": {
            "quelle": "DW – Top-Thema",
            "url": "https://learngerman.dw.com/de/deutsch-lernen/s-9528",
            "news_query": "Gesundheit Deutschland",
            "tipp": "Sottolinea i sostantivi e indovina il loro genere prima di controllarlo.",
        },
        "listening": {
            "artist": "Silbermond",
            "titel": "Symphonie",
            "tipp": "Ballata melodica e chiara. Concentrati sui suoni 'ö', 'ü', 'ä'.",
        },
        "grammar": {
            "titel": "Il caso dativo (Dativ) + le preposizioni che lo reggono",
            "erklaerung": "Il dativo indica il complemento di termine (a chi/a cui). Gli articoli "
                          "cambiano: der→dem, die→der, das→dem, die(pl)→den (+ -n al nome). "
                          "Reggono SEMPRE il dativo: mit, nach, aus, zu, von, bei, seit, gegenüber. "
                          "Es.: 'Ich fahre MIT DEM Bus' (vado in autobus).",
            "beispiele": [
                ("Ich gebe dem Kind einen Apfel.", "Do una mela al bambino."),
                ("Ich fahre mit dem Auto.", "Vado in macchina."),
                ("Sie kommt aus der Schweiz.", "Lei viene dalla Svizzera."),
                ("Wir wohnen bei den Eltern.", "Abitiamo dai genitori."),
            ],
        },
        "speaking": {
            "prompt": "Spiel einen Arzt. Ich bin der Patient und fühle mich nicht gut. Sprich Deutsch "
                      "(A2–B1), frag nach meinen Symptomen und gib mir Ratschläge. Korrigiere meine "
                      "Fehler auf Italienisch.",
            "saetze": [
                "Guten Tag, ich habe seit zwei Tagen Kopfschmerzen.",
                "Was soll ich machen?",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("der Kopf", "la testa"),
                ("das Auge", "l'occhio"),
                ("krank", "malato"),
                ("gesund", "sano / in salute"),
                ("wehtun", "far male"),
            ],
            "cognates": [
                ("die Medizin", "medicine / medicina"),
                ("der Doktor", "doctor / dottore"),
                ("der Arm", "arm / (braccio)"),
                ("die Hand", "hand / (mano)"),
            ],
            "false_friends": [
                ("sensibel", "SENSIBILE — coincide con l'italiano, ma NON con l'inglese 'sensible' (= 'vernünftig')"),
                ("die Kur", "il trattamento termale / la cura termale — non una 'cura' qualsiasi (= 'Behandlung')"),
                ("die Rente", "la PENSIONE — NON l'affitto inglese 'rent' (= 'die Miete')"),
            ],
        },
        "idiom": {
            "phrase": "Ich drücke dir die Daumen.",
            "woertlich": "Ti premo i pollici.",
            "bedeutung": "Ti auguro fortuna / faccio il tifo per te.",
            "italienisch": "Incrocio le dita per te.",
        },
    },

    # ----------------------------- GIORNO 9 -------------------------------- #
    {
        "thema": "Tempo atmosferico e natura",
        "reading": {
            "quelle": "Nachrichtenleicht",
            "url": "https://www.nachrichtenleicht.de/",
            "news_query": "Wetter Klima Deutschland",
            "tipp": "Prova a riassumere la notizia in UNA frase tua in tedesco.",
        },
        "listening": {
            "artist": "Revolverheld",
            "titel": "Ich lass für dich das Licht an",
            "tipp": "Testo pulito e ripetitivo. Ottimo per fissare il Perfekt che studi oggi.",
        },
        "grammar": {
            "titel": "Il passato prossimo (Perfekt): haben/sein + Partizip II",
            "erklaerung": "È il passato che si usa PARLANDO. Si forma con l'ausiliare (haben o sein) in "
                          "2ª posizione + il participio passato alla FINE. Participio regolare: ge-...-t "
                          "(machen→gemacht). Si usa 'sein' con verbi di MOVIMENTO o cambiamento di stato "
                          "(gehen→gegangen, fahren→gefahren, sein→gewesen).",
            "beispiele": [
                ("Ich habe Deutsch gelernt.", "Ho studiato il tedesco."),
                ("Wir sind nach Berlin gefahren.", "Siamo andati a Berlino."),
                ("Hast du das Buch gelesen?", "Hai letto il libro?"),
                ("Es hat geregnet.", "Ha piovuto."),
            ],
        },
        "speaking": {
            "prompt": "Lass uns auf Deutsch (A2–B1) über das Wetter und das letzte Wochenende sprechen. "
                      "Stell mir Fragen im Perfekt (Was hast du gemacht?) und korrigiere meine Fehler "
                      "auf Italienisch.",
            "saetze": [
                "Am Wochenende habe ich einen Spaziergang gemacht.",
                "Gestern hat es den ganzen Tag geregnet.",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("das Wetter", "il tempo (meteo)"),
                ("der Regen", "la pioggia"),
                ("die Wolke", "la nuvola"),
                ("der Baum", "l'albero"),
                ("der Himmel", "il cielo"),
            ],
            "cognates": [
                ("die Temperatur", "temperature / temperatura"),
                ("die Natur", "nature / natura"),
                ("der Wind", "wind / (vento)"),
                ("die Sonne", "sun / (sole)"),
            ],
            "false_friends": [
                ("der Nebel", "la NEBBIA — somiglia all'inglese 'nebula' ma vale 'nebbia'"),
                ("der Brand", "l'INCENDIO — NON 'brand'/marca inglese (= 'die Marke')"),
                ("der Mist", "il letame / 'accidenti!' — NON 'mist'/foschia inglese (= 'der Nebel')"),
            ],
        },
        "idiom": {
            "phrase": "Jetzt geht's um die Wurst.",
            "woertlich": "Adesso si tratta della salsiccia.",
            "bedeutung": "Ora è il momento decisivo, ci si gioca tutto.",
            "italienisch": "Adesso o mai più / È il momento della verità.",
        },
    },

    # ----------------------------- GIORNO 10 ------------------------------- #
    {
        "thema": "Viaggi e vacanze",
        "reading": {
            "quelle": "DW – Top-Thema",
            "url": "https://learngerman.dw.com/de/deutsch-lernen/s-9528",
            "news_query": "Reisen Urlaub Tourismus Deutschland",
            "tipp": "Metà percorso! Rileggi una notizia dei primi giorni: noterai i progressi.",
        },
        "listening": {
            "artist": "Andreas Bourani",
            "titel": "Auf uns",
            "tipp": "Inno alla vita, ottimo per il lessico delle emozioni e dei brindisi.",
        },
        "grammar": {
            "titel": "Le preposizioni di stato/moto (Wechselpräpositionen): Akkusativ o Dativ?",
            "erklaerung": "Queste 9 preposizioni reggono Akkusativ O Dativ a seconda del senso: "
                          "in, an, auf, über, unter, vor, hinter, neben, zwischen. "
                          "MOTO a luogo (Wohin? = dove vai?) → ACCUSATIVO. "
                          "STATO in luogo (Wo? = dove sei?) → DATIVO.",
            "beispiele": [
                ("Ich gehe in die Schule. (Wohin? → Akk)", "Vado a scuola."),
                ("Ich bin in der Schule. (Wo? → Dat)", "Sono a scuola."),
                ("Er legt das Buch auf den Tisch. (Akk)", "Mette il libro sul tavolo."),
                ("Das Buch liegt auf dem Tisch. (Dat)", "Il libro è sul tavolo."),
            ],
        },
        "speaking": {
            "prompt": "Spiel einen Mitarbeiter an der Hotelrezeption. Ich checke ein. Sprich Deutsch "
                      "(B1), frag nach meiner Reservierung und gib mir Infos. Korrigiere meine Fehler "
                      "auf Italienisch.",
            "saetze": [
                "Guten Abend, ich habe ein Zimmer reserviert.",
                "Um wie viel Uhr gibt es Frühstück?",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("die Reise", "il viaggio"),
                ("der Urlaub", "le ferie / la vacanza"),
                ("das Gepäck", "il bagaglio"),
                ("buchen", "prenotare"),
                ("das Ausland", "l'estero"),
            ],
            "cognates": [
                ("der Tourist", "tourist / turista"),
                ("das Hotel", "hotel / hotel"),
                ("das Visum", "visa / visto"),
                ("der Pass", "(passport) / passaporto"),
            ],
            "false_friends": [
                ("die Tournee/die Tour", "il giro turistico — attenzione al contesto, non sempre 'tour'"),
                ("der Smoking", "lo SMOKING / abito da sera — NON il fumare (= 'das Rauchen')"),
                ("der Oldtimer", "l'AUTO D'EPOCA — non una persona anziana!"),
            ],
        },
        "idiom": {
            "phrase": "Andere Länder, andere Sitten.",
            "woertlich": "Altri Paesi, altri costumi.",
            "bedeutung": "Ogni luogo ha le sue usanze, vanno rispettate.",
            "italienisch": "Paese che vai, usanza che trovi.",
        },
    },

    # ----------------------------- GIORNO 11 ------------------------------- #
    {
        "thema": "Sentimenti e carattere",
        "reading": {
            "quelle": "Nachrichtenleicht",
            "url": "https://www.nachrichtenleicht.de/",
            "news_query": "Gesellschaft Menschen Deutschland",
            "tipp": "Cerca gli aggettivi: ti serviranno per descrivere persone ed emozioni.",
        },
        "listening": {
            "artist": "Wincent Weiss",
            "titel": "Feuerwerk",
            "tipp": "Pop melodico e chiaro. Prova a cantarci sopra per la pronuncia.",
        },
        "grammar": {
            "titel": "Gli aggettivi possessivi e la loro declinazione",
            "erklaerung": "mein (mio), dein (tuo), sein (suo di lui), ihr (suo di lei), unser (nostro), "
                          "euer (vostro), ihr/Ihr (loro/Suo formale). Si declinano come 'ein/kein': "
                          "prendono le stesse desinenze a seconda del caso. "
                          "Es.: 'mein Bruder' (Nom) → 'meinen Bruder' (Akk) → 'meinem Bruder' (Dat).",
            "beispiele": [
                ("Das ist mein Bruder.", "Questo è mio fratello."),
                ("Ich liebe meinen Hund.", "Amo il mio cane. (Akk)"),
                ("Ich fahre mit meiner Schwester.", "Vado con mia sorella. (Dat)"),
                ("Wo ist euer Auto?", "Dov'è la vostra macchina?"),
            ],
        },
        "speaking": {
            "prompt": "Lass uns auf Deutsch (B1) über Persönlichkeit sprechen. Frag mich, wie ich bin, "
                      "was mich glücklich oder wütend macht. Benutze viele Adjektive und korrigiere "
                      "meine Fehler auf Italienisch.",
            "saetze": [
                "Ich bin meistens ruhig, aber manchmal ungeduldig.",
                "Ich werde glücklich, wenn ich Zeit mit Freunden verbringe.",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("die Angst", "la paura"),
                ("traurig", "triste"),
                ("glücklich", "felice"),
                ("schüchtern", "timido"),
                ("die Sehnsucht", "la nostalgia / lo struggimento"),
            ],
            "cognates": [
                ("nervös", "nervous / nervoso"),
                ("die Emotion", "emotion / emozione"),
                ("optimistisch", "optimistic / ottimista"),
                ("die Energie", "energy / energia"),
            ],
            "false_friends": [
                ("sympathisch", "SIMPATICO (di carattere) — l'inglese 'sympathetic' = comprensivo"),
                ("brav", "BUONO / ubbidiente (di bambino) — NON 'bravo'/capace! (= 'tüchtig')"),
                ("genial", "GENIALE / fantastico — non 'gentile/cordiale' (= 'freundlich')"),
            ],
        },
        "idiom": {
            "phrase": "Lügen haben kurze Beine.",
            "woertlich": "Le bugie hanno le gambe corte.",
            "bedeutung": "Le bugie vengono presto scoperte.",
            "italienisch": "Le bugie hanno le gambe corte.",
        },
    },

    # ----------------------------- GIORNO 12 ------------------------------- #
    {
        "thema": "Tecnologia e media",
        "reading": {
            "quelle": "DW – Top-Thema",
            "url": "https://learngerman.dw.com/de/deutsch-lernen/s-9528",
            "news_query": "Technologie Internet Deutschland",
            "tipp": "Prova a leggere senza dizionario: indovina le parole dal contesto.",
        },
        "listening": {
            "artist": "Cro",
            "titel": "Easy",
            "tipp": "Rap pop dalla dizione sorprendentemente chiara. Buono per il parlato veloce.",
        },
        "grammar": {
            "titel": "Comparativo e superlativo (Komparativ / Superlativ)",
            "erklaerung": "Comparativo: aggettivo + -er (+ 'als' per il paragone). "
                          "schnell → schneller (più veloce). 'Ich bin schneller ALS du'. "
                          "Superlativo: am + aggettivo + -sten (am schnellsten = il più veloce). "
                          "Irregolari da sapere: gut→besser→am besten; viel→mehr→am meisten; "
                          "gern→lieber→am liebsten; groß→größer→am größten.",
            "beispiele": [
                ("Mein Handy ist neuer als deins.", "Il mio cellulare è più nuovo del tuo."),
                ("Sie spricht besser Deutsch als ich.", "Lei parla tedesco meglio di me."),
                ("Das ist das schnellste Auto.", "Questa è la macchina più veloce."),
                ("Ich trinke am liebsten Kaffee.", "Bevo più volentieri il caffè."),
            ],
        },
        "speaking": {
            "prompt": "Lass uns auf Deutsch (B1) über Technologie und soziale Medien diskutieren. "
                      "Frag mich nach meiner Meinung und nutze Vergleiche (Komparativ/Superlativ). "
                      "Korrigiere meine Fehler auf Italienisch.",
            "saetze": [
                "Soziale Medien sind nützlicher, aber auch gefährlicher als früher.",
                "Meiner Meinung nach ist das Smartphone die wichtigste Erfindung.",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("die Nachricht", "il messaggio / la notizia"),
                ("herunterladen", "scaricare"),
                ("speichern", "salvare"),
                ("löschen", "cancellare"),
                ("der Bildschirm", "lo schermo"),
            ],
            "cognates": [
                ("das Internet", "internet / internet"),
                ("die Kamera", "camera / fotocamera"),
                ("das Tablet", "tablet / tablet"),
                ("die Batterie", "battery / batteria"),
            ],
            "false_friends": [
                ("das Handy", "il CELLULARE — NON l'inglese 'handy' (= pratico, 'praktisch')"),
                ("der Beamer", "il PROIETTORE — non ha a che fare con le BMW!"),
                ("die Werbung", "la PUBBLICITÀ — non un 'verbo' né un avvertimento"),
            ],
        },
        "idiom": {
            "phrase": "Den Nagel auf den Kopf treffen.",
            "woertlich": "Colpire il chiodo sulla testa.",
            "bedeutung": "Centrare esattamente il punto / cogliere nel segno.",
            "italienisch": "Centrare il punto / Colpire nel segno.",
        },
    },

    # ----------------------------- GIORNO 13 ------------------------------- #
    {
        "thema": "Soldi e burocrazia",
        "reading": {
            "quelle": "Nachrichtenleicht",
            "url": "https://www.nachrichtenleicht.de/",
            "news_query": "Geld Wirtschaft Deutschland",
            "tipp": "Lessico utile per la vita reale in Germania. Tieni questa lista a portata di mano.",
        },
        "listening": {
            "artist": "Apache 207",
            "titel": "Roller",
            "tipp": "Tormentone tedesco recente. Tedesco colloquiale e moderno.",
        },
        "grammar": {
            "titel": "Le frasi secondarie con 'weil' e 'dass' (Nebensätze)",
            "erklaerung": "Congiunzioni come weil (perché/poiché), dass (che), wenn (se/quando), "
                          "obwohl (sebbene) MANDANO IL VERBO CONIUGATO ALLA FINE della frase secondaria. "
                          "Davanti alla congiunzione va sempre la virgola. "
                          "Es.: 'Ich lerne Deutsch, WEIL ich in Deutschland ARBEITE'.",
            "beispiele": [
                ("Ich bleibe zu Hause, weil ich krank bin.", "Resto a casa perché sono malato."),
                ("Ich glaube, dass das wichtig ist.", "Penso che sia importante."),
                ("Wenn ich Zeit habe, lese ich.", "Quando ho tempo, leggo."),
                ("Er kommt, obwohl es regnet.", "Viene, sebbene piova."),
            ],
        },
        "speaking": {
            "prompt": "Spiel einen Mitarbeiter bei der Bank oder im Amt. Ich muss ein Konto eröffnen "
                      "oder ein Formular ausfüllen. Sprich Deutsch (B1), stell mir Fragen und nutze "
                      "Nebensätze. Korrigiere meine Fehler auf Italienisch.",
            "saetze": [
                "Ich möchte ein Konto eröffnen, weil ich hier arbeite.",
                "Welche Dokumente brauche ich dafür?",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("das Konto", "il conto (in banca)"),
                ("die Rechnung", "il conto / la fattura"),
                ("der Vertrag", "il contratto"),
                ("das Amt", "l'ufficio pubblico"),
                ("beantragen", "fare richiesta di"),
            ],
            "cognates": [
                ("die Bank", "bank / banca"),
                ("die Million", "million / milione"),
                ("die Steuer", "(non è 'steward') — vale 'tassa', ma 'Steuer' = anche volante"),
                ("der Euro", "euro / euro"),
            ],
            "false_friends": [
                ("die Firma", "la DITTA / l'azienda — la firma è 'die Unterschrift'"),
                ("die Provision", "la PROVVIGIONE / commissione — non 'provvista'"),
                ("die Kaution", "la CAUZIONE / deposito — NON 'cautela' (= 'Vorsicht')"),
            ],
        },
        "idiom": {
            "phrase": "Kleinvieh macht auch Mist.",
            "woertlich": "Anche il bestiame piccolo produce letame.",
            "bedeutung": "Anche le piccole somme/cose, sommate, contano.",
            "italienisch": "A quattrino a quattrino si fa il fiorino.",
        },
    },

    # ----------------------------- GIORNO 14 ------------------------------- #
    {
        "thema": "Tempo libero e hobby",
        "reading": {
            "quelle": "DW – Top-Thema",
            "url": "https://learngerman.dw.com/de/deutsch-lernen/s-9528",
            "news_query": "Freizeit Sport Hobby Deutschland",
            "tipp": "Scegli una notizia su un tema che ti piace: imparare diverte di più così.",
        },
        "listening": {
            "artist": "Sportfreunde Stiller",
            "titel": "Ein Kompliment",
            "tipp": "Classico indie tedesco, testo semplice e affettuoso.",
        },
        "grammar": {
            "titel": "Il Präteritum (passato semplice) dei verbi più comuni",
            "erklaerung": "È il passato della LINGUA SCRITTA (libri, racconti). MA per sein, haben e i "
                          "modali si usa anche parlando: war (ero), hatte (avevo), konnte (potevo), "
                          "wollte (volevo), musste (dovevo). Verbi regolari: radice + -te "
                          "(machen→machte). Irregolari frequenti: gehen→ging, kommen→kam, "
                          "sehen→sah, geben→gab.",
            "beispiele": [
                ("Ich war gestern müde.", "Ieri ero stanco."),
                ("Er hatte keine Zeit.", "Lui non aveva tempo."),
                ("Wir konnten nicht kommen.", "Non potevamo venire."),
                ("Sie ging nach Hause.", "Lei andò a casa."),
            ],
        },
        "speaking": {
            "prompt": "Lass uns auf Deutsch (B1) über Hobbys sprechen. Erzähl mir von einem Hobby und "
                      "frag mich nach meinem. Bitte mich, eine kleine Geschichte im Präteritum zu "
                      "erzählen, und korrigiere meine Fehler auf Italienisch.",
            "saetze": [
                "In meiner Freizeit wandere ich gern in den Bergen.",
                "Als Kind spielte ich jeden Tag Fußball.",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("die Freizeit", "il tempo libero"),
                ("wandern", "fare escursioni / camminare"),
                ("die Mannschaft", "la squadra"),
                ("gewinnen", "vincere"),
                ("sich treffen", "incontrarsi"),
            ],
            "cognates": [
                ("der Sport", "sport / sport"),
                ("das Konzert", "concert / concerto"),
                ("das Museum", "museum / museo"),
                ("der Film", "film / film"),
            ],
            "false_friends": [
                ("die Art", "il TIPO / la specie — NON 'arte'! (l'arte è 'die Kunst')"),
                ("der Roman", "il ROMANZO — NON 'romano' né 'romance'"),
                ("das Lokal", "il LOCALE / bar-ristorante — non un 'locale' qualsiasi"),
            ],
        },
        "idiom": {
            "phrase": "Wer A sagt, muss auch B sagen.",
            "woertlich": "Chi dice A, deve dire anche B.",
            "bedeutung": "Una volta iniziato, bisogna portare a termine.",
            "italienisch": "Chi ha detto A deve dire anche B / Chi inizia deve finire.",
        },
    },

    # ----------------------------- GIORNO 15 ------------------------------- #
    {
        "thema": "Idee e opinioni (ripasso + livello B1)",
        "reading": {
            "quelle": "tagesschau.de (notizie vere, livello avanzato)",
            "url": "https://www.tagesschau.de/",
            "news_query": "Deutschland Politik Gesellschaft",
            "tipp": "Notizie 'vere', non semplificate: una bella sfida finale. Leggi solo i titoli e i primi paragrafi.",
        },
        "listening": {
            "artist": "Herbert Grönemeyer",
            "titel": "Mensch",
            "tipp": "Una pietra miliare della musica tedesca. Testo profondo: cerca di coglierne il senso.",
        },
        "grammar": {
            "titel": "La declinazione dell'aggettivo (Adjektivdeklination) — la 'boss finale'",
            "erklaerung": "Quando un aggettivo sta DAVANTI a un nome, prende una desinenza che dipende "
                          "da articolo, genere e caso. È l'argomento più ostico: non serve padroneggiarlo "
                          "subito, ma riconoscerlo. Regola pratica al Nominativo: dopo articolo "
                          "determinativo → quasi sempre -e ('der gute Wein'); dopo articolo indeterminativo "
                          "l'aggettivo 'porta' il genere ('ein guter Wein', 'ein gutes Auto'); senza "
                          "articolo → desinenze 'forti' ('guter Wein', 'kaltes Wasser').",
            "beispiele": [
                ("der gute Mann / ein guter Mann", "il bravo uomo / un bravo uomo"),
                ("die schöne Stadt / eine schöne Stadt", "la bella città / una bella città"),
                ("das kleine Kind / ein kleines Kind", "il bambino piccolo / un bambino piccolo"),
                ("guter Wein, kaltes Bier", "buon vino, birra fredda (senza articolo)"),
            ],
        },
        "speaking": {
            "prompt": "Lass uns auf Deutsch (B1) eine kleine Debatte führen. Wähle ein Thema (z. B. "
                      "Homeoffice, Umwelt, Reisen), frag nach meiner Meinung und widersprich mir "
                      "höflich, damit ich argumentieren muss. Korrigiere meine Fehler auf Italienisch.",
            "saetze": [
                "Meiner Meinung nach ist das eine gute Idee, weil ...",
                "Einerseits stimme ich zu, andererseits denke ich, dass ...",
            ],
        },
        "vocab": {
            "nur_deutsch": [
                ("die Meinung", "l'opinione"),
                ("die Erfahrung", "l'esperienza"),
                ("die Entscheidung", "la decisione"),
                ("überzeugen", "convincere"),
                ("die Wahrheit", "la verità"),
            ],
            "cognates": [
                ("die Idee", "idea / idea"),
                ("die Diskussion", "discussion / discussione"),
                ("das Argument", "argument / argomento (di tesi)"),
                ("die Demokratie", "democracy / democrazia"),
            ],
            "false_friends": [
                ("konsequent", "COERENTE / conseguente nel comportamento — NON 'consequent' inglese"),
                ("eventuell", "EVENTUALMENTE / forse — NON l'inglese 'eventually'"),
                ("also", "QUINDI / dunque — NON l'inglese 'also' (= 'auch')"),
            ],
        },
        "idiom": {
            "phrase": "Es ist nicht genug zu wissen, man muss auch anwenden.",
            "woertlich": "Non basta sapere, bisogna anche applicare.",
            "bedeutung": "Citazione di Goethe: la conoscenza vale solo se messa in pratica.",
            "italienisch": "Sapere non basta: bisogna mettere in pratica. (J. W. von Goethe)",
        },
    },
]


# --------------------------------------------------------------------------- #
#  COSTRUZIONE LINK (link di RICERCA: non scadono mai, niente link "morti")    #
# --------------------------------------------------------------------------- #
def _youtube_link(artist, titel):
    q = quote_plus(f"{artist} {titel}")
    return f"https://www.youtube.com/results?search_query={q}"


def _google_news_link(query):
    q = quote_plus(query)
    return f"https://news.google.com/search?q={q}&hl=de&gl=DE&ceid=DE:de"


def _a(url, text):
    """Crea un link HTML per Telegram (con & correttamente escapato)."""
    safe_url = url.replace("&", "&amp;")
    return f'<a href="{safe_url}">{escape(text)}</a>'


def _e(text):
    return escape(str(text))


# --------------------------------------------------------------------------- #
#  FORMATTAZIONE DEL MESSAGGIO                                                  #
# --------------------------------------------------------------------------- #
def build_lesson_messages(day_index, lesson_number):
    """
    Restituisce una LISTA di stringhe (HTML) da inviare in sequenza su Telegram.
    day_index   = indice nella lista DAYS (0..len-1)
    lesson_number = numero progressivo della lezione mostrato all'utente (1, 2, 3, ...)
    """
    d = DAYS[day_index]
    total = len(DAYS)
    ciclo = (lesson_number - 1) // total + 1

    messages = []

    # ---- Messaggio 1: intestazione + Reading + Listening -----------------
    header = (
        f"📚 <b>Lezione di tedesco #{lesson_number}</b>  "
        f"(giorno {day_index + 1}/{total}, ciclo {ciclo})\n"
        f"🎯 <i>Tema di oggi: {_e(d['thema'])}</i>\n"
        f"{'─' * 20}"
    )

    r = d["reading"]
    reading = (
        "📰 <b>READING — leggere</b>\n"
        f"Fonte consigliata: <b>{_e(r['quelle'])}</b>\n"
        f"• {_a(r['url'], 'Apri la fonte')}\n"
        f"• {_a(_google_news_link(r['news_query']), 'Notizie di oggi su: ' + r['news_query'])}\n"
        f"💡 {_e(r['tipp'])}"
    )

    li = d["listening"]
    listening = (
        "🎧 <b>LISTENING — ascoltare</b>\n"
        f"Canzone: <b>{_e(li['titel'])}</b> — {_e(li['artist'])}\n"
        f"• {_a(_youtube_link(li['artist'], li['titel']), 'Ascolta su YouTube')}\n"
        f"💡 {_e(li['tipp'])}"
    )

    messages.append(f"{header}\n\n{reading}\n\n{listening}")

    # ---- Messaggio 2: Grammatica + Speaking ------------------------------
    g = d["grammar"]
    beispiele = "\n".join(
        f"   • <i>{_e(de)}</i> → {_e(it)}" for de, it in g["beispiele"]
    )
    grammar = (
        "🔧 <b>GRAMMAR — grammatica</b>\n"
        f"<b>{_e(g['titel'])}</b>\n"
        f"{_e(g['erklaerung'])}\n\n"
        f"<b>Esempi:</b>\n{beispiele}"
    )

    sp = d["speaking"]
    saetze = "\n".join(f"   • <i>{_e(s)}</i>" for s in sp["saetze"])
    speaking = (
        "🗣️ <b>SPEAKING — parlare</b>\n"
        "Incolla questo prompt in un'AI (es. Claude o ChatGPT) e fatti rispondere in tedesco:\n"
        f"<blockquote>{_e(sp['prompt'])}</blockquote>\n"
        f"Frasi per iniziare:\n{saetze}"
    )

    messages.append(f"{grammar}\n\n{speaking}")

    # ---- Messaggio 3: Vocaboli + Modo di dire ----------------------------
    v = d["vocab"]
    nur = "\n".join(f"   • <b>{_e(w)}</b> — {_e(t)}" for w, t in v["nur_deutsch"])
    cog = "\n".join(f"   • <b>{_e(w)}</b> — {_e(t)}" for w, t in v["cognates"])
    ff = "\n".join(f"   • <b>{_e(w)}</b> — {_e(t)}" for w, t in v["false_friends"])
    vocab = (
        "🆕 <b>VOKABELN — parole nuove di oggi</b>\n\n"
        f"🇩🇪 <u>Solo tedesche</u> (da memorizzare):\n{nur}\n\n"
        f"🔁 <u>Simili a inglese/italiano</u> (facili!):\n{cog}\n\n"
        f"⚠️ <u>Falsi amici</u> (attenzione, ti ingannano!):\n{ff}"
    )

    idi = d["idiom"]
    idiom = (
        "💬 <b>REDEWENDUNG — frase da imparare</b>\n"
        f"« <b>{_e(idi['phrase'])}</b> »\n"
        f"🔤 Letterale: <i>{_e(idi['woertlich'])}</i>\n"
        f"✅ Significato: {_e(idi['bedeutung'])}\n"
        f"🇮🇹 In italiano: {_e(idi['italienisch'])}\n\n"
        f"{'─' * 20}\n"
        "✨ <i>Viel Erfolg beim Lernen! A domani.</i>"
    )

    messages.append(f"{vocab}\n\n{idiom}")

    return messages


def total_days():
    return len(DAYS)
