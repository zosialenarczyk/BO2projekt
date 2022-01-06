
#import tkinter as tk
import numpy as np
import lib
import random

# Liczba miesięcy
monthCount = 3

# Wygenerowane wykresy akcji
stock_charts = [lib.random_chart(monthCount),lib.random_chart(monthCount),lib.random_chart(monthCount)]

#jeszcze kara maks jesli kupimy cos za wiecej niz mamy
kar1=1 #kara 1
kar2=1 # kara 2

num = 8 # liczba rozwiązań poczatkowych
Nmax = 10000  # maksymalna liczba iteracji

p = [] #najlepsze rozwiazania cząsteczek
x = [] #rój pozycja
v = [] #predkosc

globalSolution = lib.create_random_solution(stock_charts) # najlepsze rozwiązanie globalne
initialBudget = 100000

for i in range(num):
    przy = lib.create_random_solution(stock_charts)

    while lib.spr(przy, initialBudget) == False or lib.check_timeLimit(przy,monthCount) == False:
        przy = lib.create_random_solution(stock_charts)
    p.append(0)
    x.append(przy)
    p[i] = x[i]

    if lib.cost_function(p[i], monthCount, kar1, kar2, initialBudget) > lib.cost_function(globalSolution, monthCount, kar1, kar2, initialBudget):
        globalSolution = p[i]

    v.append(1) #inicjalizacja prędkości cząsteczki
    iter = 0

print(globalSolution)

while iter < Nmax:
    for i in range(num):

        r1 = random.randint(0,1)
        r2 = random.randint(0,1)

        w = 1 #– współczynnik inercji ruchu cząstki,
        c1 = 1 #– stała dodatnia, tzw.wskaźnik samooceny,
        c2 = 1 #– stała dodatnia, wskaźnik społecznościowy(zaufanie położeniu sąsiadów)

        v[i] = w * v[i - 1] + c1 * r1 * (p[i - 1] - x[i - 1]) + c2 * r2 * (globalSolution - x[i - 1]) #aktualizacja prędkosci cząsteczek
        x[i] = x[i - 1] + v[i] #aktualizacja pozycji cząsteczek

        if lib.cost_function(x[i], monthCount, kar1, kar2, initialBudget) > lib.cost_function(p[i], monthCount, kar1, kar2, initialBudget):
            p[i] = x[i] #aktualizacja najlepszego rozwiązania cząsteczki

            if lib.cost_function(p[i],monthCount,kar1,kar2, initialBudget) > lib.cost_function(globalSolution, monthCount, kar1, kar2, initialBudget):
                globalSolution = p[i] # aktualizacja najlepszego rozwiązania roju

                print(lib.cost_function(p[i], monthCount, kar1, kar2, initialBudget))
    iter += 1
    #print(iter)



print(globalSolution)
print(lib.cost_function(globalSolution, monthCount, kar1, kar2, initialBudget))
print(lib.spr(globalSolution, initialBudget))
print(lib.check_if_selling_empty_stock(globalSolution))
print(lib.check_timeLimit(globalSolution, monthCount))