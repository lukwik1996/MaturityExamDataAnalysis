# MaturityExamDataAnalysis

Skrypt służący do analizy zdawalności egzaminów maturalnych w Polsce w latach 2010 - 2018

Istnieje pięć różnych komend dostępnych do użycia. Aby wykonać funkcję należy podać jej nazwę jako argument wywołując skrypt z linii komend.
Skrypt pozwala na korzystanie zarówno z polskich jak i angielskich nazw funkcji i dodatkowych argumentów. Pełna lista dostępnych funkcji znajduje się poniżej.

**1) ŚredniaLiczbaOsób *rok* *płeć***
ta funkcja zwraca średnią liczbę osób, które przystąpiły do egzaminu dla danego województwa w danym roku 

**2) Zdawalność *województwo* *płeć***
ta funkcja zwraca procentową zdawalność dla danego województwa na przestrzeni lat 

**3) NajlepszeWojewództwo *rok* *płeć***
ta funkcja zwraca województwo o najlepszej zdawalności w konkretnym roku

**4) Regresja *płeć***
ta funkcja zwraca województwa, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku)

**5) PorównajDwa *województwo1* *województwo2* *płeć***
a funkcja porównuje dwa województwa i dla każdego kolejnego roku wypisuje to, które osiągnęło wtedy lepszą zdawalność

Argument *płeć* nie jest wymagany, może on przyjąć jedną z wartości: *mężczyźni* lub *kobiety*.