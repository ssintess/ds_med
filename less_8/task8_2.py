class OwnError(Exception):
  def __init__(self, txt):
    self.txt = txt


a = int(input('Enter the first num:'))
b = int(input('Enter the second num:'))

try: 
  if b == 0:
    raise OwnError("You entered a zero!")
except OwnError as err:
  print(err)
else: 
  print(a / b)