class OwnError(Exception):
  def __init__(self, txt):
    self.txt = txt

list = []

while True:
  a = input('Enter num (or "stop" for stopping):')
  if a == 'stop':
    print(f'Done: {list}')
    break
  else:
    try: 
      if a.isdigit() == False:
        raise OwnError("Don`t enter a text!")
    except OwnError as err:
      print(err)
    else:
      list.append(a)