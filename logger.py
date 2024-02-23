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
      f"'name'\n'surname'\n'phone''\n'address'\n'rec_num1'\n\n"
      f"Option 2: \n"
      f"name;surname;phone;address;rec_num2\n"
      f"Choose option: "))
      while var != 1 and var != 2:
            print("Wrong input")
            var = int(input('Input number: '))
      if var == 1:
            with open('data1.csv', 'r', encoding='utf-8') as f:
                  data_first = f.readlines()
                  data_first_list = []
            var1 = int(input(f"Input your entry number\n"))
            j = 0
            for i in range(len((data_first))):
                  if i > var1*6-6 and i < var1*6:
                        data_first_list.append(''.join(data_first[j:i+1]))
                        j=i
            print(''.join(data_first_list))
      elif var == 2:
            with open('data2.csv', 'r', encoding='utf-8') as f:
                  data_second = f.readlines()
                  var2 = int(input(f"Input your entry number\n"))
                  entry2 = ()
                  for i in range(data_second):
                        if i == var2*2:
                              entry2 = data_second[i]
                  print(*entry2)

