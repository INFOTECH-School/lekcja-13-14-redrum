# 🎮 **Fortnite Tournament App (Django)**  

## 📝 **Opis projektu**

Aplikacja **Django** umożliwia:  
- 🧑‍💻 **Rejestrację i logowanie użytkowników**  
- 🕹️ **Zapisy na turniej Fortnite**  
- 🧭 **Zarządzanie zgłoszeniami przez administratora**

Projekt składa się z dwóch aplikacji:  
- **`login`** – obsługa użytkowników (rejestracja, logowanie)  
- **`turniej`** – zapisy i zarządzanie turniejem  

---

## ⚙️ **Funkcje**

- 🔐 **Rejestracja i logowanie użytkowników**  
- 📋 **Formularz zgłoszeniowy na turniej** (nick, platforma, kontakt)  
- 👤 **Panel użytkownika** z informacją o statusie zgłoszenia  
- 🧩 **Panel administratora** do akceptowania lub odrzucania uczestników  

---

## 💻 **Wymagania**

- 🐍 **Python 3.10+**  
- 🌐 **Django 5.0+**  
- 💾 **SQLite** (domyślna baza danych)  
- 📦 **pip**, **virtualenv**

---

## 🚀 **Uruchomienie projektu**

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/twoj-repozytorium/fortnite-tournament.git
   cd fortnite-tournament
   ```

2. **Utwórz i aktywuj wirtualne środowisko:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate       # Windows
   ```

3. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Uruchom migracje i serwer:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Otwórz aplikację w przeglądarce:**  
   👉 [http://localhost:8000](http://localhost:8000)

---

## 🧠 **Autorzy**
📧 *mlodysigma_pet@nga.cambodia*

📧 *2mlodysigma_pet@nga.cambodia*
