# list1 =  [1,4.3,9,"Section B",10]
# print(list1)
# print(list1[2])
# print(list1[-3])
# print(list1[1:5])
# print(list1[:4])
# print(list1[2:])
# print(list1[-1:-5:-2])
# list1.append("SE")
# print(list1)
# list1.insert(3,"5th Sem")
# print(list1)
# list1[1] = 11
# print(list1)
# list1.pop()
# print(list1)
# list1.remove("5th Sem")
# print(list1)
# list1.reverse()
# print(list1)
# list1.clear()
# print(list1)
# del list1
# list2 = [9,1,4,2,7,3,5,0]
# list2.sort()
# print(list2)
# list3 = ["AC","AB","C"]
# list3.sort()
# print(list3)

# list1 =  [1,4.3,9,"Section B",10,[3,1,4]]
# print(list1[-1][2])


# tuples = (1,2,"SE","Section B")
# print(tuples)
# print(tuples[1])
# print(tuples[1:])
# list1 = list(tuples)
# list1.append("5th sem")
# list1.insert(0,6)
# list1.remove(1)
# tuples = tuple(list1)
# print(tuples)


# set1 = {True,1,3,0,False,"se",2,1,1.2,4}
# set2 = {2,9,1,4}
# print(set1)
# # set1[-1]
# set1.add("5th sem")
# print(set1)
# # set1.append(10)
# # print(set1)
# # set1.pop()
# # print(set1)
# set1.remove(0)
# print(set1)
# set1.update({10,11,12})
# print(set1)
# set1.union(set2)
# print("unoin is ", set1)
# set3 = set1.intersection(set2)
# print("intersection", set3)


# class 3

# dic  = {
#     'name':'arham',
#     "Section":'A',
#     'semster':"5th sem",
#     'id':4422,
#     'subject':["SE","CS","DS","AI"]
# }
# dic2 = {
#     "uni":"cecos",
#     "address":"peshawar"
# }
# dic3 = dic.update(dic2)
# print(dic)
# dic3  =dic+dic2
# print(dic3)
# for i, keys in dic.items():
#     print(i, keys)
# print(dic['name'])
# print(dic['subject'][2])
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# dic['Section']="B"
# print(dic)
# dic["CGPA"]= 3.2
# print(dic)

# dic.pop("name")
# print(dic)
# dic.clear()
# print(dic)
# del dic['name']
# print(dic)

# if(A>b){}

# a = 5
# b = 7
# print(a>b)

# if a > b:
#     print(a)
# else:
#     print(b)
# print(a)


# is_loggin = False
# username = input()
# password = input()

# if username.lower() == "arham" and password == "123":
#     is_loggin= True
#     if is_loggin:
#         print("directed to dashboard")
# else:
#     print("invalid")

# a = 5
# b = 2
# print(a) if a < b else print(b)

# marks = int(input("enter marks "))

# if marks >100:
#     print("invalid")
# elif marks >= 90 and marks <=100:
#     print("A")
# elif marks >= 80 and marks <=89:
#     print("B")
# elif marks >= 70 and marks <=79:
#     print("C")
# else:
#     print("fail")

# sales
#  >1000 10%
#  >700 7%
#  >500 2%

# sales = int(input("sales "))
# basic_salary = 10000
# if sales>=1000:
#     total_salary = basic_salary + (basic_salary*0.10)
#     print(total_salary)
# elif sales < 1000 and sales >=700:
#      total_salary = basic_salary + (basic_salary*0.07)
#      print(total_salary)
# elif sales <700 and sales >=500:
#      total_salary = basic_salary + (basic_salary*0.02)
#      print(total_salary)
# else:
#     print("no comission ")



# class 4

# range(start , condition, step)
# range(condition)
# range(2,10)
# i<11
# for i in range(11):
#     print(i)

# for i in range(2,11):
#     print(i)
 

# for i in range(1,11,2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# list1  =[1,4,5,1,9,"Section B"]
# # print(list1)
# # length = len(list1)
# # for i in range(length):
# #     if list1[i]%2!=0:
# #         print(list1[i])

# for i in list1:
#     print(i)

# name = "Arham"
# # print(name[2:])
# for i in name:
#     print(i)

# set1 = {1,3,5,2}
# length  = len(set1)
# for i in set1:
#     print(i)

# dic = {
#     'name':'arham',
#     'id':1,
#     'section':'B'
# }
# for i,j in dic.items():
#     print(i,j)


# i = 10
# while i>=1:
#     print(i)
#     i-=1


# while True:
#     login = "1 login"
#     signup  = "2 signup"
#     logout = "3 logout"
#     print(login)
#     print(signup)
#     print(logout)
#     user_value = int(input("select any value"))
#     if user_value==1:
#         print("login")
#     elif user_value==2:
#         print("signup")
#     elif user_value==3:
#         print("logout")
#         break


# local and global 
# a=20
# b=30

# def fucntionname(a):
#     for i in a:
#         if i%2==0:
#             print("even ",i)
# fucntionname([2,3,4,7,8,10])
# # recursion

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(3))

# class 7

# class student:
#     name  = "hammad"
#     id = 123
#     print(name, id)
# # student st1
# st1 = student()
# st2 = student()

# class student:
#     def __init__(self):
#         self.name  = "hammad"
#         self.id  =  123
#         print(self.name, self.id)

# st1 =student()
# st2 = student()
# st3 = student()

# class cecosuni:
#     def __init__(self,name, id, email, contact):
#         self.name  = name
#         self.id  = id
#         self.email=  email
#         self.contact = contact
#     def setdata(abc):
#         abc.name  =input("name ")
#         abc.id = int(input("ID "))
#         abc.email = input("EMail ")
#         abc.contact  =int(input("Contact "))
#     def getdata(self):
#         print(f"name {self.name} ID {self.id} email {self.email} contact {self.contact}")
#         print("name ", self.name, "ID", self.id)
# student = cecosuni("hammad", 123, "ham12", 123) 
# student.setdata()
# student.getdata()


# class cecosuni:
#     def __init__(self):
#         self.name = "hdam"
#         self.id = 12
#         self.email ="sd"
#         self.contact = 123
#         self.__salary  = 456
#     def __setdata(abc):
#         abc.name  =input("name ")
#         abc.id = int(input("ID "))
#         abc.email = input("EMail ")
#         abc.contact  =int(input("Contact "))
#         abc.__salary = int(input("Salary "))
#     def getdata(self):
#         self.__setdata()
#         print(f"name {self.name} ID {self.id} email {self.email} contact {self.contact} Salary {self.__salary}")
#         # print("name ", self.name, "ID", self.id)
# student = cecosuni() 
# # student.setdata()
# student.getdata()

# print(student.name)
# print(student.__salary)


# class cecosuni:
#     def __init__(self):
#         self.name = "abc"
#         self.id = 123
#         self.address = "abc"
#         self.CNIC = 123
#         self.contact = 345
#     def setdata(self):
#         self.name = input("Name ")
#         self.id = int(input("ID "))
#         self.address = input("Address ")
#         self.CNIC = int(input("CNIC "))
#         self.contact = int(input("Con num "))

# class student(cecosuni):
#     def __init__(self):
#         self.department  = "SE"
#         self.section  = "A"
#     def setstudent_data(self):
#         self.setdata()
#         self.department  = input("department ")
#         self.section  = input("section ")
#     def display(self):
#         print(f"ID {self.id} Name {self.name} Address {self.address} CNIC {self.CNIC} Contact Number {self.contact} Department {self.department} Section {self.section}")

# class faculty:
#     def __init__(self):
#         self.designation = "lecturer"
#     def fac(self):
#         # self.setstudent_data()
#         self.designation  = input(" Designation ")
#     def display1(self):
#         print(f"ID {self.id} Name {self.name} Address {self.address} CNIC {self.CNIC} Contact Number {self.contact} Department {self.department} Section {self.section} designation {self.designation}")


# class admin(cecosuni, faculty):
#     def setadmin(self):
#         self.setdata()
#         self.fac()
#     def display2(self):
#         print(self.designation)
# # st1  =student()
# # st1.setstudent_data()
# # st1.display()
# # fac1  =faculty()
# # fac1.fac()
# # fac1.display1()
# ad  =admin()
# ad.setadmin()
# ad.display2()

list1  =[1,2,3]
naem ="arham"

print(len(list1))
print(len(naem))

class student:
    def marks(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2
        print(self.sub1 + self.sub2)
        print("Hello world")

st1 =student()
st1.marks(12,45)
st1.marks(10.5, 23.2)