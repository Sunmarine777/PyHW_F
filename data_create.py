def name_data():
      name = input('Enter your name: ')
      return name

def surname_data():
      surname = input('Enter your surname: ')
      return surname

def phone_data():
      phone = input('Enter your phone number: ')
      return phone

def address_data():
      address = input('Enter your address: ')
      return address

def record_number1():
      with open('data1.csv', 'r', encoding='utf-8') as f:   
            count = int()    
            for i in enumerate(f):
                  if i != '\n':
                        count += 1
                  pass
      countf = count//6                
      return (countf+1)        

def record_number2():
      with open('data2.csv', 'r', encoding='utf-8') as f:   
            count = int()    
            for i in enumerate(f):
                  if i != '\n':
                        count += 1
                  pass
      countf = count//2                
      return (countf+1)

