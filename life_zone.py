import math

def main():
    Lstar = float(input("Введите болометрический показатель звезды: "))
    Lsun = float(input("Введите болометрический показатель Солнца: "))

    radius = lambda Lstar, Lsun: math.sqrt(Lstar/Lsun)

    print(f"Средний радис обитаемой зоны вокруг земли: {radius(Lsun , Lstar)}")

if __name__ == "__main__":
    main()