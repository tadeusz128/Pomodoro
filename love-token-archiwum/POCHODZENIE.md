# Pochodzenie i granice archiwum

Archiwum zrekonstruowano 3 października 2026 na podstawie odzyskanych podsumowań datowanych wiadomości użytkownika / asystenta oraz odnalezionych plików. Nie jest to pełny eksport rozmów ani oryginalna historia repozytorium. Użytkownik prosił o podsumowania stanów, a nie stenogram.

Najwcześniejsza odzyskana wiadomość dotycząca projektu ma datę 12 sierpnia 2026. Pierwsze odzyskane obrazy pochodzą z 13 sierpnia. Ostatnia wyraźna akceptacja geometrii w odzyskanym materiale pochodzi z 21 września; najnowsza paczka renderów z 22 września. Późniejsze dossier pochodzi z 1 października. Nie gwarantujemy odzyskania każdego załącznika lub każdej wypowiedzi ze wszystkich wątków.

Daty w manifestach plików oznaczają datę utworzenia zapisanej kopii źródłowej, a nie automatycznie datę decyzji. Daty wiadomości w podsumowaniach zapisano w UTC. W sierpniu i wrześniu czas we Wrocławiu / Warszawie był o 2 godziny późniejszy. W tagach podano zakres dat źródłowych. Commity powstały podczas rekonstrukcji i nie udają historycznych commitów z sierpnia.

## Statusy

| Status | Znaczenie |
| --- | --- |
| potwierdzone | Odzyskano datowaną decyzję / akceptację użytkownika |
| preferencja | Odzyskano preferencję użytkownika, bez pełnej specyfikacji wykonawczej |
| propozycja | Wariant asystenta, render, makieta lub roboczy opis bez odnalezionej akceptacji |
| badanie | Rozważany temat / porównanie, nie decyzja wdrożeniowa |
| odrzucone | Odzyskano wyraźne odrzucenie / polecenie powrotu przez użytkownika |
| brak danych | Nie odnaleziono źródła lub potwierdzenia |

## Obrazy i źródła

Raster przekonwertowano do JPG, maksymalnie 1000 px na dłuższym boku, jakość JPEG 63, tło przezroczyste złożone na białym. Nie wygenerowano nowych projektów. Usunięto wyłącznie identyczne kopie pikselowe oraz materiały rozpoznane jako niezwiązane z projektem. Kolejne podobne warianty pozostały osobnymi plikami.

Manifest w każdym etapie zapisuje nazwę źródła, datę, identyfikator źródłowego pliku i, dla paczek, ścieżkę wewnętrzną. Skróty SHA-256 dotyczą dostarczonego JPG / dokumentu, nie oryginalnego PNG. Nie dołączono oryginalnych pełnych PNG ani dużych źródłowych RAR / ZIP, ponieważ użytkownik prosił o kompresję. Ich odzyskana zawartość jest w historii.

Historyczne PDF i dokumenty zachowują treść źródłową. Ich stwierdzenia należy czytać wraz ze statusem etapu; nie każdy zapis PDF jest decyzją użytkownika. Tekstowe źródła sklepu zachowano, ale skompresowane rastry znajdują się osobno i wymagają dopasowania ścieżek przed uruchomieniem sklepu. Publicznych zależności, `node_modules`, kluczy dostępowych i zewnętrznych repozytoriów nie dołączono.

`meta/historia.json` jest indeksem tagów. Obecne pliki specyfikacji i obrazów opisują wyłącznie potwierdzony stan. Wywołanie podglądu eksportuje historię do ignorowanego folderu `podglad/`; nie zmienia `main` ani starej historii.
