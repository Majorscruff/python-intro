def feet_to_inches(feet):
	return feet * 12

table_dimensions_feet = {
	"width": 5,
	"length": 6,
	"height": 3
}

table_length_inches = feet_to_inches(table_dimensions_feet["length"])
print(table_length_inches)