class Data:
  def __init__(self, day, month, year):
    self.day = day
    self.month = month
    self.year = year
  
  @staticmethod
  def get_data(obj):
    try:
      if obj.day > 30 or obj.month > 12 or obj.year < 1970:
        return 'incorrect date'
      else:  
        return f'D {obj.day}; M {obj.month}; Y {obj.year}'
    except AttributeError:
      return 'incorrect date (no int in date))'

  @classmethod
  def set_data(cls, data):
    da = data
    list = da.split('-')
    for i in list:
      try:
        i = int(i)
      except ValueError:
        return 'errr'
    d = int(list[0])
    m = int(list[1])
    y = int(list[2])
    return cls(d, m, y)

    
data = "05-05-2022"
d = Data.set_data(data)
print(Data.get_data(d))