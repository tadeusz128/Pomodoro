# Love Token - archiwum do Codexa

Ta paczka zawiera repozytorium Git projektu biżuterii, podsumowania kolejnych stanów, obrazy, rendery, historię Instagrama, badania i historyczne źródła sklepu.

**Zacznij od `AKTUALNE.md`. Gałąź `main` zawiera ostatni potwierdzony stan i zaakceptowaną referencję ośmiu form. Starsze materiały są w historii Gita.**

## Import w Codexie

Rozpakuj całą paczkę, razem z `.git`. Polecenie do wklejenia znajduje się w `KOMENDA-DLA-CODEXA.txt`. Istniejącego repozytorium nie trzeba tworzyć ponownie.

## Podgląd historii

W folderze repozytorium uruchom:

```sh
python3 scripts/przeglad.py
```

Następnie otwórz `podglad/index.html`. Podgląd ma datowane etapy, podsumowania, galerie i wyszukiwanie obrazów. Działa bez internetu. Nie zmienia gałęzi, commitów ani tagów. Folder `podglad/` jest ignorowany przez Git.

## Dostęp przez Git

```sh
git log --oneline --decorate
git tag --list
git show etap-07-2026-09-07:STAN.md
git diff etap-11-2026-09-20 etap-12-2026-09-21-korekty -- STAN.md
```

Oglądanie dawnego designu bez przełączania bieżącej pracy:

```sh
git archive etap-13-2026-09-22 -o etap-13.zip
```

## Jak czytać to archiwum

Historia została odtworzona na podstawie odnalezionych materiałów. Daty etapów dotyczą źródeł, a commity powstały podczas rekonstrukcji. To podsumowanie stanów, nie pełny zapis wszystkich rozmów. `POCHODZENIE.md` wyjaśnia daty, statusy i granice odzyskania.

Rendery i makiety bez wyraźnej akceptacji pozostają propozycjami. Dossier i stare briefy nie zmieniają automatycznie obecnych decyzji. Nie odnaleziono prawdziwych modeli CAD; JPG są referencjami wizualnymi. Statystyki na makietach nie są wynikami działającego konta.

W repozytorium nie ustawiono zewnętrznego serwera Git. Lokalny Git z historią jest gotowy do pracy; publikację w zewnętrznym repozytorium można wykonać później na polecenie właściciela.
