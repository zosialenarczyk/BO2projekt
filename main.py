
#import tkinter as tk
import numpy as np
from numpy.lib.nanfunctions import nanmax
import lib
import random

def main():

    # Liczba miesięcy
    monthCount = 3

    # Wygenerowane wykresy akcji
    stock_charts = [lib.random_chart(monthCount),lib.random_chart(monthCount),lib.random_chart(monthCount)]

    monthBreak = 1
    num = 8 # liczba rozwiązań poczatkowych
    Nmax = 1000  # maksymalna liczba iteracji

    p = [] #najlepsze rozwiazania cząsteczek
    x = [] #rój pozycja
    v = [] #predkosc

    globalSolution = lib.create_random_solution(stock_charts) # najlepsze rozwiązanie globalne
    initialBudget = 100000

    for i in range(num):
        przy = lib.create_random_solution(stock_charts)

        while lib.spr(przy, initialBudget) == False or lib.check_timeLimit2(przy, monthBreak) != 0:
            przy = lib.create_random_solution(stock_charts)
        p.append(0)
        x.append(przy)
        p[i] = x[i]

        if lib.cost_function(p[i], monthBreak, monthCount, initialBudget) > lib.cost_function(globalSolution, monthBreak, monthCount, initialBudget):
            globalSolution = p[i]

        v.append(1) #inicjalizacja prędkości cząsteczki
        iter = 0

    print(f"ROZWIĄZANIE POCZĄTKOWE: \n{globalSolution}")

    while iter < Nmax:
        for i in range(num):

            r1 = random.randint(0 ,1)
            r2 = random.randint(0, 1)

            w = 1 #– współczynnik inercji ruchu cząstki,
            c1 = 1 #– stała dodatnia, tzw.wskaźnik samooceny,
            c2 = 1 #– stała dodatnia, wskaźnik społecznościowy(zaufanie położeniu sąsiadów)

            v[i] = w * v[i - 1] + c1 * r1 * (p[i - 1] - x[i - 1]) + c2 * r2 * (globalSolution - x[i - 1]) #aktualizacja prędkosci cząsteczek
            x[i] = x[i - 1] + v[i] #aktualizacja pozycji cząsteczek

            if lib.cost_function(x[i], monthBreak, monthCount, initialBudget) > lib.cost_function(p[i], monthBreak, monthCount, initialBudget):
                p[i] = x[i] #aktualizacja najlepszego rozwiązania cząsteczki

                if lib.cost_function(p[i],monthBreak, monthCount, initialBudget) > lib.cost_function(globalSolution, monthBreak, monthCount, initialBudget):
                    globalSolution = p[i] # aktualizacja najlepszego rozwiązania roju

                    #print(lib.cost_function(p[i], monthBreak, Nmax, initialBudget))
        iter += 1
        #print(iter)



    print(f"ROZWIĄZANIE KOŃCOWE: \n{globalSolution}")
    print(f'FUNKCJA CELU = {lib.cost_function(globalSolution, monthBreak, monthCount, initialBudget)}')
    print(f'CZY ZMIEŚCILIŚMY SIĘ W BUDŻECIE: {lib.spr(globalSolution, initialBudget)}')
    print(f'CZY NA POCZĄTKU SPRZEDALIŚMY AKTYWO, KTÓRE POSIADALIŚMY: {lib.check_if_selling_empty_stock2(globalSolution)}')
    print(f'ILE RAZY ZOSTAŁO NIESPEŁNIONE OGRANICZENIE CZASOWE: {lib.check_timeLimit2(globalSolution, monthBreak)}')


if __name__ == "__main__":
    main()