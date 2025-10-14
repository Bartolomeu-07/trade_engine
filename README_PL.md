# 📘 Trade Engine

> 🇬🇧 **English version available here:** [README.md](README.md)

---

## 📈 Opis projektu

**Trade Engine** to aplikacja webowa napisana w **Django**, symulująca uproszczony system inwestycyjny.  
Umożliwia użytkownikom (inwestorom) **kupowanie i sprzedawanie aktywów** takich jak akcje, waluty czy surowce,  
natomiast administratorzy mogą **zarządzać rynkiem** – dodawać nowe aktywa, usuwać je oraz aktualizować ich ceny.

Projekt został zbudowany w architekturze **Model-View-Template (MVT)** z naciskiem na część backendową — logikę transakcji, relacje między modelami oraz zarządzanie danymi.

---

## 🚀 Główne funkcje backendu

### 🧩 Modele danych
Projekt opiera się na pięciu głównych modelach:

1. **AssetType** – określa typ aktywa (np. akcje, surowce, waluty).  
2. **Asset** – pojedyncze aktywo z nazwą, typem i aktualną ceną.  
3. **Investor** – użytkownik dziedziczący po `AbstractUser`, posiadający saldo oraz listę posiadanych aktywów.  
4. **Holding** – model pośredniczący między inwestorem a aktywem, przechowujący **ilość posiadanych jednostek**.  
5. **Order** – zlecenie kupna lub sprzedaży aktywów, zawierające dane o inwestorze, aktywie, ilości, wartości i dacie transakcji.

---

## ⚙️ Logika działania

- **Kupno i sprzedaż aktywów** – inwestor może kupować lub sprzedawać aktywa; wartość transakcji liczona jest dynamicznie (`cena × ilość`).  
- **Aktualizacja salda** – środki inwestora automatycznie zmieniają się po każdej transakcji.  
- **Zarządzanie stanem posiadania** – model `Holding` pozwala dokładnie śledzić ilość posiadanych aktywów.  
  Jeśli inwestor sprzeda wszystkie jednostki danego aktywa, odpowiedni rekord w `Holding` zostaje usunięty.  
- **Panel administracyjny** – administrator może tworzyć, edytować i usuwać aktywa oraz ich typy poprzez interfejs użytkownika lub panel Django Admin.

---

## 📊 Testy automatyczne

Projekt zawiera zestaw testów automatycznych obejmujących główne komponenty aplikacji.
Testy zostały przygotowane w oparciu o wbudowany framework testowy Django oraz pytest-django.

🔍 Zakres testów:

🧱 Modele – weryfikacja poprawności logiki biznesowej (np. automatyczne usuwanie obiektu Holding po wyzerowaniu ilości, poprawne obliczanie wartości Order itp.).

🌐 Widoki (Views) – testy endpointów i widoków klasowych (ListView, DetailView, CreateView, UpdateView, DeleteView) sprawdzające poprawność odpowiedzi HTTP, statusów i kontekstu.

📝 Formularze (Forms) – testy walidacji danych wejściowych, pól formularzy i zachowania w przypadkach brzegowych.

Testy umożliwiają automatyczne sprawdzenie integralności projektu i zapewniają stabilność po każdej zmianie w kodzie.

---

## 🖥️ Interfejs użytkownika

Warstwa frontendowa korzysta z motywu **Material Kit for Django**, dostosowanego do stylu projektu.  
Użytkownicy mogą:

- przeglądać aktywa i ich typy,  
- wyświetlać listę inwestorów oraz szczegóły kont,  
- wykonywać operacje **kupna**, **sprzedaży**, **aktualizacji** i **usuwania**,  
- edytować **saldo** oraz **hasło**.  

Każdy model posiada własne widoki `ListView` i `DetailView`, a wszystkie zmiany są automatycznie zapisywane w bazie danych.

---

## 🧠 Technologie

- **Python 3.13+**  
- **Django 5.x**  
- **SQLite** (domyślnie) lub dowolna baza zgodna z Django  
- **Bootstrap / Material Kit**  
- **HTML, CSS, JavaScript (szablony Django)**

---

## ⚙️ Jak uruchomić projekt

Wykonaj poniższe kroki, aby uruchomić aplikację lokalnie:

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/<twoje_repo>/trade_engine.git

# 2. Utwórz i aktywuj środowisko wirtualne
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS / Linux

# 3. Zainstaluj wymagane pakiety
pip install -r requirements.txt

# 4. Wykonaj migracje bazy danych
python manage.py migrate

# 5. Uruchom serwer deweloperski
python manage.py runserver
```
Następnie otwórz w przeglądarce adres:

http://127.0.0.1:8000/

## 👨‍💻 Autor i licencja

Bartosz Okrój

Projekt opracowany w celach edukacyjnych.
Może być dowolnie modyfikowany, rozwijany i wykorzystywany w dalszej nauce.