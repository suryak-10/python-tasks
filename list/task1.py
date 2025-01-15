# a=int(input("enter side a value:"))
# b=int(input("enter side b value:"))
# c=int(input("enter side c value:"))
# s=(a+b+c)/2
# print('the semi perimeter:',s)
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print("area of triangle sides",a,b,c,"is:",area)

# a=int(input("enter your first number:"))
# b=int(input("enter your second number:"))
# quotient=a//b    # (//) floor division
# remainder=a%b
# print("quotient value of ",a,"and",b, "is : ",quotient)
# print("remainder value of ",a,"and",b, "is : ",remainder)

# num=int(input("enter the number:"))
# if num<0:
#     print("please enter a positive number.")
# else:
#     val=0
#     while(num>0):
#         val=val+num
#         num=num-1
# print("the sum is:",val)

# num=int(input("Enter a number:"))
# factorial=1
# if num<0:
#   print("factorial cannot be found for negative numbers.")
# elif num==0:
#   print("The factorial of 0 is:",num)
# else:
#   for i in range(1,num+1):
#     factorial=factorial*i
#   print("The factorial of",num,"is: ",factorial)

# num = int(input("Enter the number of fibonacci series you want: "))
# n1,n2=0,1
# count=0
# if num<=0:
#   print("please enter the positive number to generate fibonacci series")
# elif num==1:
#   print("fibonacci series of ",num,"is:",n1)
# else:
#   print("the fibonacci series is:")
#   while count<num:
#     print(n1)
#     last=n1+n2
#     n1=n2
#     n2=last
#     count+=1

# number=   int(input("enter the numbers :"))
# value=0
# temp=number
# while(temp>0):
#   digit=temp%10
#   value=value+digit**3
#   temp=temp//10
# if number:
#    print("armstrong number.")
# else:
#   print("not an armstrong number.")

# year=int(input("enter the year"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(year,"is leap year")
#         else:
#             print(year,"not an leap year")
#     else:
#       print(year,"is an leap year")
# else:
#     print(year,"not an leap year")

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# if a>b:
#   smaller=b
# else:
#   smaller=a
# for i in range(1,smaller+1):
#   if ((a%i==0) and (b%i==0)):
#     hcf=i
# print("The HCF of",a,"and",b,"is",hcf)

# count = 0
# word = "happy"
# find = "p"
# for i in word:
#   if i == find:
#     count = count + 1
# print(count,"times occured")

# word = "happy"
# find = "p"
# print(word.count(find),"times occured")

# punc='''!()-[]{}:,/><.!@#$%^&*_~?'''   # punctuations
# string=input("enter the string:")
# no_punc=""   # "" <-- empty string
# for i in string:
#     if i not in punc:   # if condition
#         no_punc=no_punc+i
# print(no_punc)

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# if a>b:       # 64 > 48
#   smaller=b
# else:
#   smaller=a
# for i in range(1,smaller+1):
#   if ((a%i==0) and (b%i==0)):
#     hcf=i
# print("The HCF of",a,"and",b,"is",hcf)

# a=24
# b=36
# if a>b:
#   greater=a
# else:
#   greater=b
#   value=greater
# while(True):
#   if((greater%a==0)and(greater%b==0)):
#     lcm=greater
#     break
#   greater=greater + value
#   print(greater)
# print("LCM of",a,"and",b,"is",lcm)

# number=int(input("Enter a number: "))
# value=1
# print("the Factors of the given  numbers{0} are:".format(number))
# while(value<=number):
#   if (number%value==0):
#     print("{0}".format(value))
#   value = value+1

# punc='''!()-[]{}:,/><.!@#$%^&*_~?'''   # punctuations
# string=input("enter the string:")
# no_punc=""   # "" <-- empty string
# for i in string:
#     if i not in punc:
#         no_punc=no_punc+i
# print(no_punc)

# actualprice=float(input("Enter the actual price:"))
# sellingcost=float(input("Enter the selling price:"))
# if (actualprice>sellingcost):     # 10 > 12 false
#   amount=actualprice-sellingcost
#   print("Your Loss is:",amount)
# elif (sellingcost>actualprice):   # 10 > 12 true
#   amount=sellingcost-actualprice  # 12 - 10 = 2
#   print("Your Profit is:",amount)
# else:
#   print("NO PROFIT,NO LOSS!!!")

# p=float(input("enter your principle:"))
# n=float(input("enter your no.of years:"))
# r=float(input("enter your rate of intrest:"))
# si=(p*n*r)/100  # formula for SI
# amount=p+si
# print("your simple intrest (SI) is",si)
# print("net amount after",n,"years is:",amount)

# p=10000
# n=2
# r=10
# ci=p*((1+r/100)**n-1)
# print("the compound intrest is:",ci)

# import secrets
# l1 = ["anu","maxi","priya","ganesh",5,14,8,26,59,24,58,21,59]
# for i in range(7):
#   print("randomly selected :",secrets.choice(l1))

# from shutil import copyfile
# copyfile("D:/sample/file.txt", "D:/vicky/filenew.txt")

# day=int(input("Enter the day:"))
# month=int(input("Enter the month:"))
# year=int(input("Enter the year:"))
#   Total number of words in this  string =
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#   max_days=31
# elif month==4 or month==6 or month==9 or month==11:
#   max_days=30
# elif year%4==0 and year%100!=0 or year%400==0:
#   max_days=29
# else:
#   max_days=28
#
# if month<=1 and month>=12:
#   print("not a valid month")
# elif day<1 or day>max_days:
#   print("entered day is invalid.")
# # elif year<2000 or year>2025:
# #   print("entered year is invalid.")
# else:
#   print("Valid Date....")

# from shutil import copyfile
# copyfile("D:/sample/New File.txt", "D:/sample1/filenew.py")


# str1 = input("please enter your own string:")
# str1 = "  Total number of words in this  string ="
# total=1

# for char in str1:   #0-13
#   print(char, ord(char))
#   if(char == ' ' or str1 == "\n"): # (happy learning) counting number of space
#     total=total+1

# print("Total number of words in this  string = ",total)

# from shutil import copyfileobj
# copyfileobj("D:/sample/New File.txt", "D:/sample1/objnotepad.txt")

# from shutil import copy2
# copy2("D:/sample/New File.txt", "D:/sample1/copy2file.txt")

# from shutil import copy2
# copy2("D:/sample/New File.txt", "D:/sample1/wordfile.doc")

# day=int(input("Enter the day:"))
# month=int(input("Enter the month:"))
# year=int(input("Enter the year:"))
#
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#   max_days=31
# elif month==4 or month==6 or month==9 or month==11:
#   max_days=30
# elif year%4==0 and year%100!=0 or year%400==0:
#   max_days=29
# else:
#   max_days=28
# # if month<=1 or month>=12:
# if month < 1 or month > 12:          # lesser than 1 and greater than 12
#   print("not a valid month")
# elif day<1 or day>max_days:
#   print("entered day is invalid.")
# else:
#   print("Valid Date....")

# day=int(input("Enter the day:"))
# month=int(input("Enter the month:"))
# year=int(input("Enter the year:"))
#
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#   max_days=31
# elif month==4 or month==6 or month==9 or month==11:
#   max_days=30
# elif year%4==0 and year%100!=0 or year%400==0:
#   max_days=29
# else:
#   max_days=28
#
# if month<=1 and month>=12:
#   print("not a valid month")
# elif day<1 or day>max_days:
#   print("entered day is invalid.")
# elif year<2000 or year>2025:
#   print("entered year is invalid.")
# else:
#   print("Valid Date....")

# import random
# l1 = [5,14,8,26,59,24,58,21,59]
# print("randomly selected number is:",random.choice(l1))

# p=10000
# n=3
# r=3
# ci=p*((1+r/100)**n-1)
# print("the compound intrest is:",ci)

# p=float(input("enter your principle:"))
# n=float(input("enter your no.of years:"))
# r=float(input("enter your rate of intrest:"))
# si=(p*n*r)/100  # formula for SI
# amount=p+si
# print("your simple intrest (SI) is",si)
# print("net amount after",n,"years is:",amount)

# name1={1:"maxi",2:"john",3:"priya",4:"bee",5:"max"}
# name={1:"maxi",2:"johnwilson",3:"priyavarma",4:"bee",5:"maxwell"}
# print(name1|name)
# print(name1)

# dt={"a":"how","b":"are","c":"you"}
#
# for key in dt.keys():
#     print(key)
#
# for value in dt.values():
#     print(value)

# dict_1={"a":"how","b":"are","c":"you"}
#
# for key , value in dict_1.items():
#     print(key , value)

# dict_1={"a":"how","b":"are","c":"you"}
#
# for key in dict_1:                    # no method used
#     print(key , dict_1[key])
# print(dict_1["a"])
# print(dict_1["b"])
# print(dict_1["c"])

# index=[1,2,3,1]
# name=("maxi","john","priya","riya")
#
# dictionary = dict(zip(index,name))   # eg: to combine 4 to 5 files we use "zip" file
# print(dictionary)

# index=[1,2,3,1]
# name=("maxi","john","priya","riya")  # "dictionary" will not accept repeated keys , so we converted into "list"
#
# dictionary = list(zip(index,name))   # eg: to combine 4 to 5 files we use "zip" file
# print(dictionary)

# dict_1={"a":"how","b":"are","c":"you"}
#
# for i in dict_1.keys():         # it will just access the keys
#     print(i)
#
# for j in dict_1.values():       # it will just access the values
#     print(j)

# dict_1={"a":"how","b":"are","c":"you"}
#
# for key in dict_1:                    # no method used
#     print(key , dict_1[key])
# print(dict_1['a'])

# dict_1={"a":"how","b":"are","c":"you"}
#
# for key in dict_1:                    # no method used
#     print(key , dict_1[key])

# dict_1={1:"hay",2:"buddy"}
# dict_2={3:"happy",4:"learning"}
# print({**dict_1,**dict_2})      #
# # { **1:"hay",2:"buddy", **3:"happy",4:"learning" }

# def name(name,age):
#   print(name, age)
#
# name(age=22, name="surya")
# name(name="surya", age=22)

# def name(**name):
#   print(name, name1, name3)
#
# name("suray", "John", '121')

# def name(*names):
#   for name in names:
#     print(name)
#   # print(names)
#
# name("surya", "John", '121', 21, 3, 2,3,342)