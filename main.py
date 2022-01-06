
#import tkinter as tk
import numpy as np
import lib
import random


k=3
wykres=[lib.random_chart(k),lib.random_chart(k),lib.random_chart(k)]
#jeszcze kara maks jesli kupimy cos za wiecej niz mamy
liczba_mie=1 # liczba miesiecy
kar1=1 #kara 1
kar2=1 # kara 2
num=8 # liczba rozwiązań poczatkowych
Nmax = 10000  # maksymalna liczba iteracji
p=[]#najlepsze rozwiazania cząsteczek
g=lib.create_random_solution(wykres) # najlepsze rozwiązanie globalne
x=[] #rój
v=[]
portf=100000
for i in range(num):
    przy=lib.create_random_solution(wykres)
    while lib.spr(przy, portf) == False or lib.check_time(przy,liczba_mie)==False:
        przy = lib.create_random_solution(wykres)
    p.append(0)
    x.append(przy)
    p[i] = x[i]
    if lib.funkcja_celu(p[i],liczba_mie,kar1,kar2,portf) > lib.funkcja_celu(g,liczba_mie,kar1,kar2,portf):
        g = p[i]
    v.append(1) #inicjalizacja prędkości cząsteczki
    iter=0
print(g)
while iter<Nmax:
    for i in range(num):
        r1=random.randint(0,1)
        r2=random.randint(0,1)
        w=1 #– współczynnik inercji ruchu cząstki,
        c1=1 #– stała dodatnia, tzw.wskaźnik samooceny,
        c2=1 #– stała dodatnia, wskaźnik społecznościowy(zaufanie położeniu sąsiadów),
        v[i] = w * v[i - 1] + c1 * r1 * (p[i - 1] - x[i - 1]) + c2 * r2 * (g - x[i - 1]) #aktualizacja prędkosci cząsteczek
        x[i]=x[i-1]+v[i] #aktualizacja pozycji cząsteczek
        if lib.funkcja_celu(x[i], liczba_mie, kar1, kar2,portf) > lib.funkcja_celu(p[i], liczba_mie, kar1, kar2,portf):
            p[i]=x[i] #aktualizacja najlepszego rozwiązania cząsteczki

            if lib.funkcja_celu(p[i],liczba_mie,kar1,kar2,portf) > lib.funkcja_celu(g,liczba_mie,kar1,kar2,portf):
                g=p[i]# aktualizacja najlepszego rozwiązania roju
                print(lib.funkcja_celu(p[i], liczba_mie, kar1, kar2, portf))
    iter=iter+1
    #print(iter)

print(g)
print(lib.funkcja_celu(g, liczba_mie, kar1, kar2,portf))
print(lib.spr(g,portf))
print(lib.czy_na_poczatku_sprzedajemy(g))
print(lib.check_time(g, liczba_mie))