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
   '''bash
   git clone (https://github.com/radoslawbaranowski99/mecze-ics)
   cd mecze-ics
2.  Zainstaluj wymagane biblioteki:
    pip install requests beautifulsoup4 ics
3. Stwórz wirtualne środowisko:
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate # Linux/Mac
