import numpy as np
import random


class aktywo_w_portfelu:
    def __init__(self, wykres):
        self.ilosc=0
        self.wykres=wykres
    def aktualizacja(self,n,miesiac):
        if n>0:
            self.ilosc=self.ilosc+n

            return self.wykres[miesiac]*n
        if n<0:
            k=self.ilosc
            self.ilosc=0
            return -1*(self.wykres[miesiac]*k)
        if n==0:
            return 0
    def c(self):
        return self.ilosc
    def check(self,n):
        if self.ilosc>n:
            return True
        else:
            return False


def losuj():
    list = [-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,0.8, 0.9, 1]
    return random.choice(list)


def h(A,B):
    return np.column_stack((A, B))


def create_random_solution(list):
    buf=0
    for aktywo in list:
        i=0
        Aktywo = aktywo_w_portfelu(aktywo)
        lista = np.array([])
        for miesiac in range(len(aktywo)):
            r = losuj()
            akt=Aktywo.aktualizacja(r, miesiac)
            lista=np.append(lista,akt)


        if type(buf)==int:
            buf=lista
        else:
            buf=h(buf,lista)
    return buf


"Funkcja sprawdza czy został spełniony warunek nr1"
def check_time(solution,number):
    m,n=np.shape(solution)
    for i in range(n):
        last=np.zeros(number)
        for j in range(m):
            recent=solution[j][i]
            if recent!=0 and last.any(0):
                return False
            else:
                last=np.append(last,recent)
                last=np.delete(last, 0)
    return True


"Funckja sprawdza czy na począku nie sprzedajemy aktywa którego nie mamy"
def czy_na_poczatku_sprzedajemy(A):
    for aktywo in A:
        i=0
        while((aktywo[i]==0) and (i<np.size(aktywo)-1)):
            i=i+1

        if aktywo[i]<0:
            return False
    else:
        return True


def spr(A,war):
    A=np.transpose(A)
    portfel=war
    for miesiac in A:
        for aktywo in miesiac:
            portfel=portfel-aktywo
        if portfel<0:
            return False
    return True


def funkcja_celu(A,liczba_mie,kar1,kar2,portf):
    suma = 0
    n,m=np.shape(A)
    for i in range(n):
        for j in range(m):
            suma += A[i][j]
    "liczymy karę dla funkcji"
    kara=1
    #if spr(A,portf)==False:
    #    return 0
    if check_time(A,liczba_mie)==False:
        return 0
    if czy_na_poczatku_sprzedajemy(A)==False:
        return 0
    return suma*kara

def random_chart(miesiace):
    stock=[random.randint(300,600)]
    for i in range(miesiace):
        if random.randint(0,1) == 0:
            stock.append(stock[i] + random.randint(1,40))
        else:
            stock.append(stock[i] - random.randint(1,40))
    return stock

