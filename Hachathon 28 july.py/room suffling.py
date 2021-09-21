import random
name =["neha","priti","dev","kirti","shivani","meena","chinu","dehati","pihu","dolly"]
room =[[],[],[],[],[]]
i=0
while i<len(room):
    for g in name: 
        a=random.choice(name)
        if a not in room[i]:
            room[i].append(a)
            name.remove(a)    
    i+=1
room_no=[101,102,103,104,105]
no=1
for new in room:
    number=0 
    for n in new:
        print(n,"your room no is",room_no[number],"your bed is",no)
        no+=1
        number+=1




# a=5.2
# b=3.7
# print(a+b)

# =5.8
# b=3
# print(a+b)a




