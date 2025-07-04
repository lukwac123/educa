# 🎓 Educa – Platforma e-learningowa w Django

Projekt Educa ilustruje, jak zbudować kompletną platformę e-learningową od podstaw, z uwzględnieniem:

- rejestracji i logowania użytkowników,
- zarządzania kursami przez nauczycieli,
- dynamicznego tworzenia treści kursów (tekst, wideo, quizy),
- zapisu użytkowników na kursy,
- interaktywnej pracy z AJAX-em i JavaScript,
- REST API (opcjonalnie),
- zabezpieczeń (autoryzacja i uprawnienia).

![Image](https://github.com/user-attachments/assets/e7c22a79-3a58-404b-840c-bb57d0aab49a)
<sub>Rys. 1. Strona główna projektu Educa.</sub>

---

## 📁 Struktura katalogów
| educa/                                  | Katalog projektu                                   |
|:----------------------------------------|:---------------------------------------------------|
| 📁 educa/                               | Katalog główny projektu Django                     |
| ├── 📁 courses/                         | Aplikacja kursów – modele, widoki, formularze      |
| ├── 📁 students/                        | Aplikacja dla użytkowników/kursantów               |
| ├── 📁 accounts/                        | Logowanie, rejestracja, zarządzanie kontem         |
| ├── 📁 templates/                       | Szablony HTML                                      |
| ├── 📁 static/                          | Pliki statyczne (CSS, JS, obrazy)                  |
| ├── 📁 media/                           | Pliki przesyłane przez użytkowników (video)        |
| ├── 📁 educa/                           | Główna konfiguracja Django (settings, urls, wsgi)  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📄 __init__.py                  | Plik inicjalizujący                                |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📄 asgi.py                      | Konfiguracja ASGI                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📄 settings.py                  | Ustawienia projektu                                |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── 📄 urls.py                      | Główne trasy URL                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 📄 wsgi.py                      | Konfiguracja WSGI                                  |
| ├── 📄 manage.py                        | Główne narzędzie CLI Django                        |
| ├── 📄 db.sqlite3                       | Baza danych SQLite                                 |
| ├── 📄 requirements.txt                 | Lista zależności Pythona                           |
| └── 📄 README.md                        | Dokumentacja projektu                              |

---
