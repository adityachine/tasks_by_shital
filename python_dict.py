from email import header
from os import name


students = {
    "Alice": "AASPL067",
    "Bob": "AASPL068",
    "Charlie": "AASPL069",
    "David": "AASPL070",
    "Eva": "AASPL071",
    "Frank": "AASPL072",
    "Grace": "AASPL073",
    "Hannah": "AASPL074",
    "Ian": "AASPL075",
    "Jack": "AASPL076",
    "Kira": "AASPL077",
    "Liam": "AASPL078",
    "Maya": "AASPL079",
    "Noah": "AASPL080",
    "Olivia": "AASPL081",
    "Paul": "AASPL082",
    "Quinn": "AASPL083",
    "Riya": "AASPL084",
    "Sam": "AASPL085",
    "Tina": "AASPL086"
}
print(students)

x = students["Riya"]
print(x)
print(len(students))
print(type(students))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(type(thisdict))

for x in thisdict:
    print(x)
    
for y in students.values():
  print(y)

for y in students.keys():
    print(y)
    
for x,y in students.items():
    print(x,":-",y)
    
x= students.clear()
print(x)

