name=["Harry", "Saad", "Madelyn"]
print(name)#comment
print(f"Hello, {name}")
name.append("Draco") #adds draco to name
name.sort() #with order
#the set is used when we want unique values
s=set()
s.add(1)
s.add(2)
s.add(3)
print(s)
print(f"This set has {len(s)} elements.")
s.add(3)# will do nothing
s.remove(2)
print(s)
print(f"This set has {len(s)} elements.")
if len(s)<=2:
    print("Great!")
else:
    print("Not so great")    


for i in [1,2,3,4]:#for i in range(4): 
    print(i)

def square(x):
    return x*x

for name in name:
    print(name)        