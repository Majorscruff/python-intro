person1 = {
	"name": "Julia",
	"age": 21,
	"purchases": ["cider", "beer", "wine"]
}
person2 = {
	"name": "Jack",
	"age": 18,
	"purchases": ["beer", "beer", "more beer"]
}

def can_they_buy(person):
    name = person["name"]
    items = person["purchases"][0] + ", " + person["purchases"][1] + ", and " + person["purchases"][2]
    if person["age"] < 19:
        return name + " cannot buy " + items
    else:
        return name + " can buy " + items

print(can_they_buy(person1)) 
# "Julia can buy their cider, beer, and wine."

print(can_they_buy(person2)) 
# "Jack cannot buy their beer, beer, and more beer."