# 1)კომენტარების სახით ახსენით რას აკეთებს type ფუნქცია

# type ფუნქცია ამოწმებს ცვლადში შენახული მნიშვნელობა რა ტიპის მონაცემია.

# 2)მომხმარებელს შემოატანინეთ ასეკი და გადაამოწმე რომელ მონაცეთა ტიპს მიეკუთვნება ეს მნიშვნელობა

age =  input("enter your age")
print(type(age))

# 3)მომხმარებელს შემოატანინეთ სამჯერ მნიშვნელობა და თითოეულს მიანიჭეთ სხვადასხვა
#  მონაცემთა ტიპი და საბოლოოდ გადაამოწმეთ type ფუნქციით

number =  int(input("enter your number"))
name = input("enter your name")
age = float(input("enter your age"))
print(type(number))
print(type(name))
print(type(age))

# 4)შექმენით ოთხი ცვლადი, პირველს მიანიჭეთ თქვენი სახელი,მეორეს
#  თქვენი გვარი,მესამეს თქვენი ასაკი და მეოთხეს თქვენი სიმაღლე.
# საბოლოოდ გადაამოწმეთ რომელი მონაცემთა ტიპი არის შენახული თითოეულ ცვლადში

name = "George"
Last_name = "Chakvetadze"
age = 12
Height = 152
print(type(name))
print(type(Last_name))
print(type(age))
print(type(Height))

