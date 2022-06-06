class Equipment:
  def __init__(self, model, price, count):
    self.model = model
    self.price = price
    self.count = count


class Printer(Equipment):
  def __init__(self, model, price, count, speed):
    super().__init__(model, price, count)
    self.speed = speed
    self.list_eq = [model, price, count, speed]

class Scanner(Equipment):
  def __init__(self, model, price, count, format):
    super().__init__(model, price, count)
    self.format = format
    self.list_eq = [model, price, count, format]

class Copier(Equipment):
  def __init__(self, model, price, count, double):
    super().__init__(model, price, count)
    self.double = double
    self.list_eq = [model, price, count, double]

class Stock:
  def __init__(self, volume):
    self.volume = int(volume)
    self.eq = []
  
  def add_prt(self, model, price, count, speed):
    self.eq.append(Printer(model, price, count, speed))
    #total_count = total_count + self.count
    #print(self.count)
    
  def add_scn(self, model, price, count, format):
    self.eq.append(Scanner(model, price, count, format))
    
  def add_cpr(self, model, price, count, double):
    self.eq.append(Copier(model, price, count, double)) 
    
  def buy(self, buy_item):
    self.eq.pop(buy_item)
    
  def __str__(self):
    main_volume = []
    total_count = 0
    for el in self.eq:
      main_volume.append(el.list_eq)
      total_count = total_count + el.list_eq[2]
    print(f'На складе {total_count} единиц техники: ')
    c = self.volume - total_count
    try: 
      if c < 0:
        raise OwnError("Склад не может столько вместить")
        
    except OwnError as err:
      return err.txt
      
    else: 
      str_eq = ''
      for i in main_volume:
        for a in i:
          a = str(a)
          str_eq = str_eq + a + ' '
        str_eq = str_eq + '\n'  
      return str_eq

# Собственный класс исключение
class OwnError(Exception):
  def __init__(self, txt):
    self.txt = txt


# Создаем склад на 20 предметов
stock = Stock('20')
print(f'Создан склад на {stock.volume} единиц техники.\n')

# Пополняем склад конкретными моделями техники: Модель, Цена, Количество, Особенности
stock.add_prt('Canon', '150', 10, 45)
stock.add_prt('HP', '170', 3, 38)
stock.add_scn('Samsung', '100', 1, 'A4')
stock.add_scn('HP', '90', 1, 'A4')
stock.add_cpr('Xerox', '220', 3, True)
print(f'{stock}')

# Фирма покупает на складе конкретную модель
stock.buy(2)
print(f'Купленные модели отправлены со склада покупателю.\n')

# Остаток на складе
print(f'{stock}')