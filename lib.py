import numpy as np
import random

def random_chart(monthCount: int) -> np.ndarray:

    '''
    Funkcja generuje wykres akcji rynkowej
    '''

    stock: np.ndarray = [random.randint(300,600)]

    for i in range(monthCount):
        if random.randint(0,1) == 0:
            stock.append(stock[i] + random.randint(1,40))
        else:
            stock.append(stock[i] - random.randint(1,40))
    return stock


class aktywo_w_portfelu:
    def __init__(self, chart: np.ndarray):
        self.stockCount = 0
        self.chart = chart

    def update(self, n: float, month: int):

        # KUPNO
        if n > 0:
            self.stockCount = self.stockCount + n
            return -1*(self.chart[month]*n)
        
        # SPRZEDAŻ
        if n < 0:
            # Sprzedajemy wszystko co mamy, żeby nie zostawić ułamków
            k = self.stockCount
            self.stockCount = 0
            return self.chart[month]*k

        if n == 0:
            return 0

    def get_stockCount(self):
        return self.stockCount



def pick_random_percentage() -> float:
    list = [-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,0.8, 0.9, 1]
    return random.choice(list)


def h(A,B) -> np.ndarray:
    '''
    Funkcja składająca macierz
    '''
    return np.column_stack((A, B))


def create_random_solution(stockCharts):
    buf = 0

    for chart in stockCharts:
        stock = aktywo_w_portfelu(chart)
        temp_list = np.array([])

        for month in range(len(chart)):
            r = pick_random_percentage()
            stockInMoney = stock.update(r, month)
            temp_list = np.append(temp_list, stockInMoney)

        # Po co to jest? buf nie jest zmieniane w funkcji
        if type(buf) == int:
            buf = temp_list
        else:
            buf = h(buf, temp_list)

    return buf


def penalty_func(penaltyCount: int, fraction: int) -> float:
    return 1 - (fraction*penaltyCount)


def check_timeLimit(solution: np.ndarray, number: int) -> bool:
    '''
    Funkcja sprawdza, czy zostało spełnione ograniczenie czasowe
    '''
    
    m, n = np.shape(solution)

    for i in range(n):
        last = np.zeros(number)

        for j in range(m):
            recent = solution[j][i]

            if recent != 0 and last.any(0):
                return False
            else:
                last = np.append(last, recent)
                last = np.delete(last, 0)
    return True


def check_timeLimit2(solution: np.ndarray, monthBreak: int) -> int:
    '''
    Funkcja liczy, ile razy zostało niespełnione ograniczenie czasowe
    '''

    m, n = np.shape(solution)
    penaltyCount: int = 0
    elem_zero: int = 0
    elem_notZero: int = 0

    for i in range(n):
        for j in range(m):
            if solution[j][i] == 0 and elem_zero == monthBreak - 1 and elem_notZero == 1:
                'Dokładnie odpowiednia przerwa, kolejne zera z rzedu nie będą miały znaczenia'
                elem_notZero = 0
            
            elif solution[j][i] == 0 and elem_notZero == 0:
                'Albo do tej pory byly same zera, albo przerwa jest dluzsza niz minimalna'
                elem_zero += 1 

            elif solution[j][i] == 0 and elem_zero < monthBreak - 1 and elem_notZero == 1:
                'zero po jednym niezerowym elemencie (przerwa jeszcze nie osiagnela wymaganej dlugosci)'
                elem_zero += 1

            elif solution[j][i] != 0 and elem_notZero == 0:
                'pierwszy niezerowy element po przerwie lub po niespelnieniu warunku'
                elem_notZero += 1

            elif solution[j][i] != 0 and elem_notZero == 1:
                'warunek niespełniony'
                penaltyCount += 1
                elem_notZero = 0
    
    return penaltyCount


def check_if_selling_empty_stock2(A: np.ndarray) -> bool:
    '''
    Funkcja sprawdza, czy na początku nie sprzedajemy aktywa, którego nie mamy
    '''

    for stock in A.transpose():
        i = 0
        while((stock[i] == 0) and (i < np.size(stock) - 1)):
            i = i + 1

        if stock[i] > 0:
            return False
    else:
        return True


def check_if_selling_empty_stock(A: np.ndarray) -> bool:

    for stock in A.transpose():
        i: int = 0
        if stock[i] <= 0:
            return False
    return True
        

def spr(solutionMatrix: np.ndarray, initalBudget: float) -> bool:
    '''
    Funkcja sprawdza, czy nie zostało wydane więcej pieniędzy, niż było w budżecie
    True - budżet nie został przekroczony
    False - budżet został przekroczony
    '''

    currentBudget: float = initalBudget

    for month in solutionMatrix:
        currentBudget = currentBudget + sum(month)
        if currentBudget < 0:
            return False
    return True


def cost_function(solutionMatrix: np.ndarray, monthBreak: int, monthCount: int, initalBudget: int, fraction: int) -> float:

    suma: float = 0
    n, m = np.shape(solutionMatrix)

    for i in range(n):
        for j in range(m):
            suma += solutionMatrix[i][j]

    penaltyCount = check_timeLimit2(solutionMatrix, monthBreak)
    penaltyCoefficient = penalty_func(penaltyCount, fraction)

    if check_if_selling_empty_stock2(solutionMatrix) == False:
        #print('Sprzedaż aktywa, którego nie posiadamy')
        return 0
    
    if spr(solutionMatrix, initalBudget) == False:
        #print('Wydano więcej pieniędzy niż było w budżecie')
        return 0

    return suma*penaltyCoefficient

