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
      f"Choose format: "))

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
      f"Choose format: "))
      while var != 1 and var != 2:
            print("Wrong input")
            var = int(input('Input number: '))
      if var == 1:
            with open('data1.csv', 'r', encoding='utf-8') as f:   
                  data_1 = f.read()
            data_first = data_1.rstrip().split('\n\n')
            var1 = input(f"Input your entry number: ")
            for entry1 in data_first:
                  entry_1 = entry1.split()
                  if var1 in entry_1[4]:
                        print(entry1)
                  pass

      elif var == 2:
            with open('data2.csv', 'r', encoding='utf-8') as f:
                  data_2 = f.read()
            data_second = data_2.rstrip().split('\n\n')
            var2 = input(f"Input your entry number: ")
            for entry2 in data_second:
                  entry_2 = entry2.split(';')
                  if var2 in entry_2[4]:
                        print(entry2)
                  pass
            
    
def change_data():

      var = int(input(f"What format of data were applied?\n"
      f"Option 1: \n"
      f"name\nsurname\nphone\naddress\nentry_number\n\n"
      f"Option 2: \n"
      f"name;surname;phone;address;entry_number\n"
      f"Choose format: "))
      name = name_data()
      surname = surname_data()
      phone = phone_data()
      address = address_data()
     
      while var != 1 and var != 2:
            print("Wrong input")
            var = int(input('Input number: '))
      if var == 1:
            with open('data1.csv', 'r+', encoding='utf-8') as f:
                  data_1 = f.read()
            data_first = data_1.rstrip().split('\n\n')
            var1 = input(f"Input your entry number: ")
            for entry1 in data_first:
                  entry_1 = entry1.split()
                  if var1 in entry_1[4]:
                        entry_c1 = entry1
                  pass

            with open('data1.csv', 'w+', encoding='utf-8') as f:
                  for i in data_first:
                        if i != entry_c1:
                              f.write(f"{i}\n\n")
                              pass
                        elif i == entry_c1:
                              f.write(f"{name}\n{surname}\n{phone}\n{address}\n{var1}\n\n")
                              pass
                        pass
                  print('Entry updated')

      elif var == 2:
            with open('data2.csv', 'r+', encoding='utf-8') as f:
                  data_2 = f.read()
            data_second = data_2.rstrip().split('\n\n')
            var2 = input(f"Input your entry number: ")
            for entry2 in data_second:
                  entry_2 = entry2.split(';')
                  if var2 in entry_2[4]:
                        entry_c2 = entry2
                  pass

            with open('data2.csv', 'w+', encoding='utf-8') as f:
                  for i in data_second:
                        if i != entry_c2:
                              f.write(f"{i}\n\n")
                              pass
                        elif i == entry_c2:
                              f.write(f"{name};{surname};{phone};{address};{var2}\n\n")
                              pass
                        pass
                  print('Entry updated')



def delete_data():
      var_c = str(input(f'Enter \'Y\' if you want to cancel your entry:\n'))
      if var_c != 'Y':
            print("Terminated")
            exit()
      elif var_c == 'Y':
            var = int(input(f"What format of data were applied?\n"
            f"Option 1: \n"
            f"name\nsurname\nphone\naddress\nentry_number\n\n"
            f"Option 2: \n"
            f"name;surname;phone;address;entry_number\n"
            f"Choose format: "))

      while var != 1 and var != 2:
            print("Wrong input")
            var = int(input('Input number: '))
      if var == 1:
            with open('data1.csv', 'r+', encoding='utf-8') as f:
                  data_1 = f.read()
            data_first = data_1.rstrip().split('\n\n')
            var1 = input(f"Input your entry number: ")
            for entry1 in data_first:
                  entry_1 = entry1.split()
                  if var1 in entry_1[4]:
                        entry_d1 = entry1
                  pass
            print(entry_d1)
            with open('data1.csv', 'w+', encoding='utf-8') as f:
                  for i in data_first:
                        if i != entry_d1:
                              f.write(f"{i}\n\n")
                              pass
                        pass
            print('Deleted')

      elif var == 2:
            with open('data2.csv', 'r+', encoding='utf-8') as f:
                  data_2 = f.read()
            data_second = data_2.rstrip().split('\n\n')
            var2 = input(f"Input your entry number: ")
            for entry2 in data_second:
                  entry_2 = entry2.split(';')
                  if var2 in entry_2[4]:
                        entry_d2 = entry2 
                  pass
            print(entry_d2)
            with open('data2.csv', 'w+', encoding='utf-8') as f:
                  for i in data_second:
                        if i != entry_d2:
                              f.write(f"{i}\n\n")
                              pass
                        pass
            print('Deleted')
           
