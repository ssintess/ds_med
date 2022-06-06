class ComplexNum:
  def __init__(self, num):
    self.num = num

  def __add__(self, other):
    f1 = self.num.replace(' ', '')   #var 'x + yi' and 'x+yi' 
    list1 = f1.split('+')            #get 'x' and 'y'
    x1 = int(list1[0])
    y1 = ''
    for i in list1[1]:               #del 'i'
      if i.isdigit() == True:
        y1 = y1 + i
    y1 = int(y1)
    
    f2 = other.num.replace(' ', '')
    list2 = f2.split('+')
    x2 = int(list2[0])
    y2 = ''
    for i in list2[1]:
      if i.isdigit() == True:
        y2 = y2 + i
    y2 = int(y2)

    return f'{x1} + {y1} and {x2} + {y2}\n({self.num}) + ({other.num}) = {x1 + x2} + {y1 + y2}i'

  def __mul__(self, other):
    f1 = self.num.replace(' ', '')  
    list1 = f1.split('+')           
    x1 = int(list1[0])
    y1 = ''
    for i in list1[1]:              
      if i.isdigit() == True:
        y1 = y1 + i
    y1 = int(y1)
    
    f2 = other.num.replace(' ', '')
    list2 = f2.split('+')
    x2 = int(list2[0])
    y2 = ''
    for i in list2[1]:
      if i.isdigit() == True:
        y2 = y2 + i
    y2 = int(y2)
    
    return f'({self.num}) * ({other.num}) = {(x1 * x2) - (y1 * y2)} + {(y1 * x2) + (x1 * y2)}i'
    
cn1 = ComplexNum('1 + 2i')
cn2 = ComplexNum('20 + 4i')

print(cn1 + cn2)
print(cn1 * cn2)