# TabuSearchTSP
Implementacja algorytmu metaheurystycznego Tabu Search dla problemu TSP (znalezienie minimalnego cyklu Hamiltona w pełnym grafie ważonym)<br>
W pliku **alg.py** znajduje się zaimplementowany algorytm, a w pliku tsp.txt znajduje się przykładowa instancja problemu

## Opis Algorytmu
- Funkcja get_data odczytuje z pliku tekstowego instancję problemu i tworzy macierz odległości między miastami.
- Funkcja calculate_distance oblicza odległość (koszt) trasy, sumując wagi krawędzi między kolejnymi wierzchołkami (miastami) na ścieżce. Ostatni krok dodaje również odległość z ostatniego wierzchołka do punktu początkowego.
- Funkcja get_neighborhood generuje sąsiedztwo aktualnej ścieżki. Iteruje po indeksach ścieżki, zamienia kolejność miast między tymi indeksami i dodaje nowe sąsiednie ścieżki do listy sąsiadów. Jeśli dana sąsiednia ścieżka nie znajduje się na liście tabu, jest dodawana do listy sąsiadów wraz z obliczoną odległością.
- Funkcja tabu_search wykonuje właściwe przeszukiwanie z wykorzystaniem algorytmu Tabu Search. Na początku losowo inicjalizuje najlepszą ścieżkę (best_path) jako permutację indeksów od 0 do n-1, gdzie n to liczba miast w grafie. Następnie oblicza jej odległość (best_distance) za pomocą funkcji calculate_distance. Tworzy również pustą listę tabu (tabu_list).
- W głównej pętli algorytmu (iterującej od 0 do max_iterations) generuje sąsiedztwo najlepszej ścieżki za pomocą funkcji get_neighborhood. Jeśli sąsiedztwo jest puste, przerywa pętlę, ponieważ nie ma więcej możliwości poprawy.
- Sortuje sąsiadów według ich odległości, aby wybrać najbliższego sąsiada. Pierwszy sąsiad na liście będzie miał najkrótszą odległość.
- Następna ścieżka (next_path) i jej odległość (next_distance) są dodawane do listy tabu. Jeśli lista tabu osiągnie maksymalny rozmiar (tabu_size), usuwa najstarszy element z listy
- Jeśli nowa odległość jest lepsza od obecnej najlepszej odległości (next_distance < best_distance), aktualizuje najlepszą ścieżkę i najlepszą odległość.
- Algorytm powtarza powyższe kroki, iterując przez określoną liczbę iteracji (max_iterations) lub do momentu, gdy nie ma możliwości poprawy trasy.
- Na koniec zwracana jest najlepsza odnaleziona odległość.

## Przykład działania:
Stan początkowy:<br>![image](https://github.com/MateuszSztefek/TabuSearchTSP/assets/88203590/12a4450a-4b63-4b44-9a8f-ea57eebbde8a)<br>
Krok 1:<br>![image](https://github.com/MateuszSztefek/TabuSearchTSP/assets/88203590/c4fcebbf-205b-444d-990d-b405d8d607ce)<br>
Krok 2:<br>![image](https://github.com/MateuszSztefek/TabuSearchTSP/assets/88203590/c8ddf71c-4dd6-4249-96e0-631a44b79088)<br>
Długość trasy: 30.22



