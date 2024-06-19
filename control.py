import random
def numbers():  #Состовляем первое окно:
   first_field = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
   number = random.choice(first_field)
   return number

number = numbers()
print(number)

n = input("Ведите число: ")

def numbers2():  #Состовляем первое окно:
   second_field = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
   for i in range(second_field):
      i + 1
      for j in range(second_field):
         j = 1
         if i + j == (second_field)):
            print(i,j)
