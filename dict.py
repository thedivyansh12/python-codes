a = {"key" : "value",
     "divyansh" : 100,
     "goat" : "ME",
     "list" : [1, 4, 7]
     }


#print(a.keys())

#print(a.items())

a.update({"goat" : "WITH THE SOLE EXCEPTION OF ME OFCOURSE"})
print(a)
print(a.get("goat"))


