# 🏟️ Mecze ICS
Skrypt w Pythonie, który pobiera terminarze drużyn sportowych i zapisuje je do pliku `.ics` (kalendarz).  
Dodatkowo, jeśli do meczu został tydzień, przypomina o sprawdzeniu dostępności biletów.  
Dzięki temu mecze mogą być automatycznie dodawane do Twojego kalendarza (Apple, Google, Outlook).

---

## ⚙️ Funkcje
- Pobieranie terminarzy z wybranych stron klubów.
- Eksport do pliku `.ics` zgodnego z kalendarzem Apple/Google.
- Automatyczne dodanie przypomnienia: „Sprawdź bilety”.
- Możliwość dostosowania linków do zakupu biletów w zależności od drużyny.

---

## 🚀 Instalacja
1. Pobierz repozytorium:
   git clone (https://github.com/radoslawbaranowski99/mecze-ics)
2.  Zainstaluj wymagane biblioteki:
    pip install requests beautifulsoup4 ics
    
---

## ️▶️Użycie
Uruchom skrypt:
python mecze.py
W folderze projektu pojawi się plik:
matches.ics
Otwórz matches.ics:
na iPhonie → otworzy się w aplikacji Kalendarz, kliknij „Dodaj”.
w Google Calendar → importuj przez „Ustawienia → Importuj”.
w Outlooku → przeciągnij plik do kalendarza.

## 📂 Struktura projektu
mecze-ics
│-- mecze-ics.py        # główny skrypt
│-- matches.ics     # wygenerowany plik kalendarza
│-- README.md       # opis projektu

## 💡 Przykład działania

Jeśli do meczu pozostały dwa tygodnie → w kalendarzu pojawia się przypomnienie:
„Sprawdź czy dostępne są bilety (link: ... )”

## 🛠️ Technologie

Python 3
ics – obsługa plików kalendarza

## 📌 Autor
Projekt stworzony w ramach nauki Pythona po kursie podstawowym.
Możesz używać i rozwijać dalej 🚀
