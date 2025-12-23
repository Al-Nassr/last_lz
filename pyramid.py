import math 

def main():
  s_1 = float(input('Введите площадь верхнего основания '))
  s_2 = float(input('Введите площадь нижнего основания '))
  h = float(input('Введите длину вышей высоты '))

  v = lambda s_1, s_2, h: 1/3 * h *(s_1 + s_2 + (s_1 * s_2)**1/2 )
  
  print ("Ваш полученный объем = " , v(s_1, s_2, h))
if __name__ == "__main__":
    main()
