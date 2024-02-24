from data_create import name_data, surname_data, phone_data, address_data, record_number1, record_number2


def input_data():
      name = name_data()
      surname = surname_data()
      phone = phone_data()
      address = address_data()
      rec_num1 = record_number1()
      rec_num2 = record_number2()
      var = int(input(f"What format of data should be applied?\n\n"
      f"Option 1: \n"
      f"{name}\n{surname}\n{phone}\n{address}\n\n"
      f"Option 2: \n"
      f"{name};{surname};{phone};{address}\n"
      f"Choose option: "))

      while var != 1 and var != 2:
            print("Wrong input")
            var = int(input('Enter number: '))
      if var == 1:
            with open('data1.csv', 'a', encoding='utf-8') as f:
                  f.write(f"{name}\n{surname}\n{phone}\n{address}\n{rec_num1}\n\n")
            print(f'Your entry number: ',rec_num1)
      elif var == 2:
            with open('data2.csv', 'a', encoding='utf-8') as f:
                  f.write(f"{name};{surname};{phone};{address};{rec_num2}\n\n")
            print(f'Your entry number: ',rec_num2)
      

def print_data():
      var = int(input(f"What format of data were applied?\n"
      f"Option 1: \n"
      f"name\nsurname\nphone\naddress\nentry_number\n\n"
      f"Option 2: \n"
      f"name;surname;phone;address;entry_number\n"
      f"Choose option: "))
      while var != 1 and var != 2:
            print("Wrong input")
            var = int(input('Input number: '))
      if var == 1:
            with open('data1.csv', 'r', encoding='utf-8') as f:
                  data_1 = f.readlines()
            data_first = []
            var1 = int(input(f"Input your entry number: "))
            if var1*6 > len(data_1):
                  print("Wrong input")
            for i in range(1):
                  data_first.append(''.join(data_1[var1*6-6:var1*6-1]))
            print(''.join(data_first))

      elif var == 2:
            with open('data2.csv', 'r', encoding='utf-8') as f:
                  data_2 = f.readlines()
            var2 = int(input(f"Input your entry number: "))
            if var2*2-2 > len(data_2):
                  print("Wrong input")
            if var2 == 1:
                  print(data_2[0])
            for i in enumerate(data_2):                        
                  if i == var2*2-2:
                        break
                  pass
            print(data_2[var2*2-2])
            
    
def change_data():
      var_c = str(input(f'Enter \'Y\' to change your entry:\n'))
      while var_c != 'Y':
            print("Wrong input")
            var_c = int(input('Input number: '))
      if var_c == 'Y':
            var = int(input(f"What format of data were applied?\n"
            f"Option 1: \n"
            f"name\nsurname\nphone\naddress\nentry_number\n\n"
            f"Option 2: \n"
            f"name;surname;phone;address;entry_number\n"
            f"Choose option: "))
      name = name_data()
      surname = surname_data()
      phone = phone_data()
      address = address_data()
      rec_num1 = record_number1()
      rec_num2 = record_number2()     
      while var != 1 and var != 2:
            print("Wrong input")
            var = int(input('Input number: '))
      if var == 1:
            with open('data1.csv', 'r+', encoding='utf-8') as f:
                  data_1 = f.readlines()
            data_first = []
            var1 = int(input(f"Input your entry number: "))
            if var1*6 > len(data_1):
                  print("Wrong input")
            for i in range(1):
                  data_first.append(''.join(data_1[var1*6-6:var1*6-1]))

      elif var == 2:
            with open('data2.csv', 'r+', encoding='utf-8') as f:
                  data_2 = f.readlines()
            var2 = int(input(f"Input your entry number: "))
            if var2*2-2 > len(data_2):
                  print("Wrong input")
            if var2 == 1:
                  with open('data2.csv', 'r+', encoding='utf-8') as f:
                        f[0].write(f"{name};{surname};{phone};{address};{rec_num2}\n")
                  print(*f[0])
            with open('data2.csv', 'r+', encoding='utf-8') as f:
                  f[var2*2-2].write(f"{name};{surname};{phone};{address};{rec_num2}\n")
            print(*f[var2*2-2])


