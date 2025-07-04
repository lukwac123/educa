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

## 📘 Etapy projektu
| Etap | Temat                                             | Opis                                                               |
|:------------|:---------------------------------------------------|:-------------------------------------------------------------------------------------|
| 1          | Inicjalizacja projektu                            | Tworzenie projektu `educa`, aplikacji `courses`, konfiguracja środowiska Django    |
| 2          | Modele i relacje                                  | Projektowanie modeli kursów i treści, relacje 1-wiele, wiele-wiele, GenericForeignKey |
| 3          | Admin i zarządzanie treściami                     | Personalizacja Django Admin, obsługa zagnieżdżonych modeli i dynamicznych struktur |
| 4          | Widoki klasowe (CBV)                              | Implementacja `ListView`, `DetailView`, `FormView`, renderowanie danych w widokach |
| 5          | System kont użytkowników                          | Rejestracja, logowanie, dashboard, `UserCreationForm`, `LoginRequiredMixin`        |
| 6          | Autoryzacja dostępu                               | Kontrola dostępu do kursów i lekcji, sprawdzanie właściciela, `@login_required`    |
| 7          | Dynamiczne zarządzanie treścią                    | `formsets`, AJAX, przeciąganie treści (`jQuery UI`), interaktywny panel edycji     |
| 8          | Zapisy na kursy                                   | Formularze zapisu, dostęp tylko dla zapisanych kursantów, relacje M2M              |
| 9          | Obsługa mediów                                    | Przesyłanie i wyświetlanie filmów, dokumentów, zdjęć – `MEDIA_URL`, `MEDIA_ROOT`   |
| 10         | Panel nauczyciela (CMS)                           | Zarządzanie własnymi kursami – CRUD, dynamiczne widoki, filtrowanie danych         |
| 11         | Deployment (opcjonalny)                           | Przygotowanie do wdrożenia, `gunicorn`, `collectstatic`, plik `Procfile`, hosting  |

---

## 📚 Źródło
Książka: _Django 4 by Example_  
Autor: Antonio Melé  
Wydawnictwo: Packt / Helion (PL)  
