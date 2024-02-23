from logger import input_data, print_data


def interface():
      print('Good day! You are in the bot mode \n 1 - enter data \n 2 - receive data')
      command = int(input('Enter number: '))
      
      while command != 1 and command != 2:
            print('Wrong input')
            command = int(input('Enter  number: '))
                 
      if command == 1:
            input_data()
      elif command == 2:
            print_data()


if  __name__ == '__main__':
      interface()

