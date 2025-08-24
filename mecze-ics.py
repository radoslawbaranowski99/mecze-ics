
#import calendar library
from ics import Calendar, Event
from datetime import datetime, date, timedelta
import os

#Dropbox folder path
DROPBOX_FOLDER = r"C:\Users\rados\Dropbox"
ICS_FILENAME = "matches.ics"
ICS_PATH = os.path.join(DROPBOX_FOLDER, "matches.ics")


#List of matches
matches = [
    {"team": "Anwil Włocławek", "opponent": "KB Bashkimi Prizen", "date": "2025-10-01"},
    {"team": "Anwil Włocławek", "opponent": "Tauron GTK Gliwice", "date": "2025-10-06"},
    {"team": "Anwil Włocławek", "opponent": "AMW Arka Gdynia", "date": "2025-10-10"},
    {"team": "Anwil Włocławek", "opponent": "MKS Dąbrowa Górnicza", "date": "2025-10-18"},
    {"team": "Anwil Włocławek", "opponent": "King Szczecin", "date": "2025-10-23"},
    {"team": "Anwil Włocławek", "opponent": "PGE Start Lublin", "date": "2025-11-8"},
    {"team": "Anwil Włocławek", "opponent": "Energa Icon Sea Czarni Słupsk", "date": "2025-11-21"},
    {"team": "Anwil Włocławek", "opponent": "Miasto Szkła Krosno", "date": "2025-12-11"},
    {"team": "Anwil Włocławek", "opponent": "Dziki Warszawa", "date": "2026-1-03"},
    {"team": "Anwil Włocławek", "opponent": "Górnik Zamek Książ Wałbrzych", "date": "2026-1-06"},
    {"team": "Anwil Włocławek", "opponent": "Legia Warszawa", "date": "2026-03-07"},
    {"team": "Anwil Włocławek", "opponent": "Arriva Polski Cukier Toruń", "date": "2026-03-23"},
    {"team": "Anwil Włocławek", "opponent": "Tasomix Rosiek Stal Ostrów Wielkopolski", "date": "2026-04-6"},
    {"team": "Anwil Włocławek", "opponent": "Orlen Zastal Zielona Góra", "date": "2026-04-19"},
    {"team": "Anwil Włocławek", "opponent": "WKS Śląsk Wrocław", "date": "2026-04-25"},
    {"team": "Anwil Włocławek", "opponent": "Trefl Sopot", "date": "2026-05-06"},
    {"team": "Orlen Wisła Płock", "opponent": "KS Iskra Kielce", "date": "2025-08-30"},
    {"team": "Orlen Wisła Płock", "opponent": "RK Zagrzeb", "date": "2025-09-17"},
    {"team": "Orlen Wisła Płock", "opponent": "Eurofarm Palister", "date": "2025-10-08"},
    {"team": "Orlen Wisła Płock", "opponent": "PSG", "date": "2025-10-15"},
    {"team": "Orlen Wisła Płock", "opponent": "Barcelona", "date": "2025-10-23"},
    {"team": "Orlen Wisła Płock", "opponent": "GOG", "date": "2025-12-4"},
    {"team": "Orlen Wisła Płock", "opponent": "SC Magdeburg", "date": "2026-02-25"},
    {"team": "Orlen Wisła Płock", "opponent": "Szeged", "date": "2026-03-11"},
    {"team": "Wisła Płock", "opponent": "Zagłębie Lubin", "date": "2025-08-25"},
    {"team": "Wisła Płock", "opponent": "Cracovia", "date": "2025-09-13"},
    {"team": "Wisła Płock", "opponent": "GKS Katowice", "date": "2025-09-27"},
    {"team": "Wisła Płock", "opponent": "Nieciecza", "date": "2025-10-18"},
    {"team": "Wisła Płock", "opponent": "Pogoń Szczecin", "date": "2025-11-01"},
    {"team": "Wisła Płock", "opponent": "Lech Poznań", "date": "2025-11-29"},
    {"team": "Wisła Płock", "opponent": "Raków", "date": "2026-01-31"},
    {"team": "Wisła Płock", "opponent": "Widzew Łódź", "date": "2026-02-14"},
    {"team": "Wisła Płock", "opponent": "Arka Gdynia", "date": "2026-03-07"},
    {"team": "Wisła Płock", "opponent": "Jagiellonia", "date": "2026-03-21"},
    {"team": "Wisła Płock", "opponent": "Lechia Gdańsk", "date": "2026-04-11"},
    {"team": "Wisła Płock", "opponent": "Radomiak", "date": "2026-04-25"},
    {"team": "Wisła Płock", "opponent": "Motor Lublin", "date": "2026-05-09"},
    {"team": "Wisła Płock", "opponent": "Górnik Zabrze", "date": "2026-05-16"},
]

#Ticket links
tickets = {
    "Wisła Płock": "https://bilety.wisla-plock.pl",
    "Anwil Włocławek": "https://kkwloclawek.abilet.pl",
    "Orlen Wisła Płock": "https://sprwislaplock.abilet.pl/"
    }

calendar = Calendar()
today = date.today()

for m in matches:
    match_date = datetime.strptime(m["date"], "%Y-%m-%d").date()
    event = Event()
    event.name = f"{m['team']} vs {m['opponent']}"
    event.begin = match_date

    days_to_match = (match_date - today).days
    ticket_link = tickets.get(m["team"])

    #Add description with ticket info
    if days_to_match <= 14 and ticket_link:
        event.description = f"Sprawdź dostępność biletu: {ticket_link}"
    elif days_to_match <= 14:
        event.description = "Sprawdź, czy dostępne są bilety"
    else:
        event.description = "ticket not available yet"

    calendar.events.add(event)

    #Console output
    print(f"{m['team']} vs {m['opponent']} ({m['date']}): {event.description}")

# Saving ics file in local folder
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
local_path = os.path.join(script_dir, "matches.ics")

with open(local_path, "w", encoding="utf-8") as f:
    f.writelines(calendar.serialize_iter())
print(f"✅ File saved in local folder: {local_path}")
