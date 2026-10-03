# Instrukcja dla Codexa

To archiwum projektu biżuterii Love Token / YOSE. Użytkownik chce kontynuować pracę w Codexie z zachowaniem historii projektu.

1. Przeczytaj `README.md`, `AKTUALNE.md`, `POCHODZENIE.md` i `meta/stan-aktualny.json`.
2. `main` jest ostatnim potwierdzonym stanem. Historyczne materiały są w commitach oznaczonych tagami `etap-*`. Nie są automatycznie aktualnymi decyzjami.
3. Zachowaj istniejące `.git`, wszystkie tagi i commity. Nie uruchamiaj ponownie `git init`, nie spłaszczaj historii ani nie zmieniaj starych commitów. Każdą nową pracę zapisuj jako nowy commit.
4. Najwyższa referencja geometrii to ręcznie poprawiona tablica z 21.09.2026 zaakceptowana przez użytkownika. Nie zamieniaj jej na późniejszy render opisany przez asystenta jako „final”.
5. Oddzielaj decyzję użytkownika, preferencję, propozycję asystenta, badanie i odrzucenie. Brak akceptacji oznacza brak potwierdzenia, a nie dowód odrzucenia.
6. Nie wprowadzaj do obecnej specyfikacji liczb z historycznych dokumentów, jeżeli nie są potwierdzone w aktualnym stanie. Nie traktuj makiet Instagrama jako rzeczywistych statystyk / opinii ani dossier jako dowodu działającej sprzedaży.
7. Osiem obecnych form odczytuj z tablicy. Nazwy i numery historycznych zestawów dziewięciu / dziesięciu koncepcji nie są obecnymi SKU.
8. Repozytorium nie zawiera gotowych modeli CAD. JPG nie potwierdza odlewalności, grubości ani geometrii produkcyjnej. Konkretne opracowania opraw i symulacji są badaniami w historii.
9. Projekt jest projektem biżuterii. Utworzenie aplikacji, nowego sklepu lub publikacja strony wymagają osobnego polecenia użytkownika. W ramach importu można przygotować podgląd i uporządkować środowisko.
10. Rozmawiaj po polsku. Używaj zwykłego łącznika `-`, bez znaku półpauzy.

Podgląd: `python3 scripts/przeglad.py`. Otwórz `podglad/index.html`. Skrypt używa tylko Pythona i Gita, nie wymaga internetu ani instalowania pakietów.
