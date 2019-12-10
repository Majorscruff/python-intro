def feet_to_inches(feet):
	return feet * 12

table_dimensions_feet = {
	"width": 5,
	"length": 6,
	"height": 3
}

table_length_inches = feet_to_inches(table_dimensions_feet["length"])
print(table_length_inches)

#second part of the homework Below this line

price =(20, 6, 9, 14, 5)
tax_percent = (13)
hst = (0.13)

def get_total (price, tax_percent):
	total = price * (tax_percent + 1)
	total_rounded = round(total, 2)
	return total_rounded

first_total = get_total(price[0], hst)
second_total = get_total(price[1], hst)

print ("The first two totals are $" + str (first_total) + " and $" + str (second_total) + " respectively.")
# The first two totals are $22.6 and $6.78 respectively.