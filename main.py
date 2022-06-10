from math import *

#** ** ** ** ** ** * basic practis
my_age = "44"
my_name = "tayyab"
no=12
my_str = "i am tayyab learning the python language my  age is " + my_age + " and name is" + my_name + " "
print(my_str.replace("language","zaban"))
print(floor(4.4))

#  *************  simple calculator

# fNo= input("Enter first no: ")
# sNo= input("enter second no ")
# result= int(fNo)+int(sNo)
# print(result)


#  *************  list


# no=[3,5,2,4,6,22,33,11]
# frnds=["tayyab", "zahid","zahid", "hamza", "shakoor"]
# frnds[1]="gujjr"
# frnds.append("rohin")
# frnds.insert(1,"momin")
# frnds.remove("rohin")
# frnds.clear()
# frnds.pop()  #remove last eliment
# frnds.sort()
# no.sort()
# frnds1=frnds.copy()
# print(frnds1)


# *************   tuple its simpilar to list


# once couple create it cannot change/not modififed
# coordinate=(4,5)
# print(coordinate)


#  *************  functions

def sayhi(name,age):
    print("helloe user "+ name +" and age is " + str(age))

sayhi("tayyab", 33)
def cube(num):
    return num*num*num
result=cube(4)
print(result)


#  *************   if elif  statements

is_male=False
is_tall=True
if is_male or is_tall:
    print("you are male")
elif is_male and not(is_tall):
    print("yoy are short male")
else:
    print("you are not male")


#*************  if elif and comparisons


def max_num(num1, num2 ,num3):
     if num1 >=num2 and num1>= num3:
         return num1
     elif num2 >= num1 and num2>= num3:
         return num2
     else:
         return num3

# print(max_num(30,2,33))


#  *************  adwance calculator


# num1 = float(input("enter first no: "))
# op = input("Enter operator")
# num2 = float(input("enter second no: "))

# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("invalid operator")


#  *************  dicitionaries and keys concept


monthconversion = { 1:"January",
                    "Feb": "Feburary",
                    "Mar": "March"}
# print(monthconversion.get(1, "not a valid key"))


#  *************  while loop


# i=1
# while i<=10:
#     print(i)
#     i +=1
# print("done with loop")


#  *************   guessing game

# secret_word = "tayyab"
# guess = ""
# out_of_guss=False
# count=0
# while guess != secret_word and not(out_of_guss) :
#     if count<3:
#         guess=input("Enter guess: ")
#         count +=1
#     else:
#         out_of_guss=True
# if out_of_guss:
#     print("you loss")
# else:
#     print("you win")



# *************   for looop



# namelist= ["tayab", "zahid", "hamza"]
    # for index in namelist:
    # for index in range(len(namelist)):
# for index in range(5):
#     if index==0:
#         print("first itration")
#     else:
#         print("not first")


#  *************   exponent function


def rais_to_power(baiseno, powerno):
     result=1
     for index in range(powerno):
         result=result*baiseno
     return result
#print(rais_to_power(2,5))


#  *************  2d list and nested loops

# number_grid=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# print(number_grid[1][2])
# for row in number_grid:
#     for col in row:
#         print(col)



#  *************  basic translator/ put G if it a latter exist in vovels


def translation(phrase):
     trans=""
     for latter in phrase:
         if latter.lower() in "aeiou":
             if latter.upper():
                 trans=trans+"G"
             else:
                 trans=trans+"g"
         else:
             trans=trans+latter
     return trans
#print(translation(input("enter phrase: ")))


#  **************try catch /error handling
try:
     value =10/0
     number = int(input("Enter integer no: "))
     print(number)
except ZeroDivisionError as err:
     print(err)
except ValueError:
     print("invalid input")


#**************reading from external files

employee_file = open("employee.txt","r")
print(employee_file.readlines())

for employee in employee_file.readlines():
        print(employee)

employee_file.close()

# *************  writing into file

employee_file = open("index.html","a+")
employee_file.write("\n <p> this is dummy web page</p>")

print(employee_file.readlines())

for employee in employee_file.readlines():
     print(employee)

employee_file.close()


#  *************   classes objects / object functions

from Student import Student

student1 = Student("Jim","Computer",3.4,False)
student2 = Student("Jon","Bussiness",3.6,False)

print(student1.gpa)
print(student2.onHonorRoll())


#  *************   mutiple choice paper



questions_prompt =[
     "what color of apple?\n a red\n b purple \n c orrange \n\n",
     "what color of bananas?\n a red\n b purple \n c orrange \n\n",
     "what color of strawberries?\n a red\n b purple \n c orrange \n\n"
 ]

from Question import Question

questions=[
     Question(questions_prompt[0],"a"),
     Question(questions_prompt[1],"b"),
     Question(questions_prompt[2],"c"),
 ]

def run_test(questions):
     score=0;
     for ques in questions:
         answer=input(ques.prompt)
         if answer == ques.answer:
             score +=1
     print("you got "+ str(score) + "/" + str(len(questions))+ " correct")

#run_test(questions)


from Chef import Chef
from ChinesChef import  ChinesChef

myChef=Chef()
myChef.makeChicken()
myChinesChef=ChinesChef()
myChinesChef.makeSpecialDish()


