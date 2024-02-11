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
            records = f.readlines()
      last_record = records[-2]
      rec_num = last_record.split('\n')[-1]
      return rec_num        

def record_number2():
      with open('data2.csv', 'r', encoding='utf-8') as f:
            records = f.readlines()     
      last_record = records[-2]
      rec_num = last_record.split(';')[-1]
      return rec_num


