import math 

qwe = lambda L1, L2: math.sqrt(L1 / L2)

def main():
    L1 = float(input('показатель звезды (L1): '))
    L2 = 3.86*10**33
    result = qwe (L1, L2)
    print('Средний радиус:', format(result*149597870700, '.10f'))

if __name__ == "__main__":
    main()
