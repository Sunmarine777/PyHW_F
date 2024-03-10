def name_data():
      name = input('Enter your name: ').title()
      return name

def surname_data():
      surname = input('Enter your surname: ').title()
      return surname

def phone_data():
      phone = input('Enter your phone number: ')
      return phone

def address_data():
      address = input('Enter your address: ').title()
      return address

def record_number1():
      with open('data1.csv', 'r', encoding='utf-8') as f:   
            data_1 = f.read()
            data1 = data_1.rstrip().split()
            entry1 = data1[-1].rstrip().split()
            entry_1 = int(entry1[-1])   
      return(entry_1+1)    

def record_number2():
      with open('data2.csv', 'r', encoding='utf-8') as f:   
            data_2 = f.read()
            data2 = data_2.rstrip().split()
            entry2 = data2[-1].rstrip().split(';')
            entry_2 = int(entry2[-1])   
      return(entry_2+1)
