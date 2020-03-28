string = '1 2 3 4 '
string = string[:-1]
print(len(string))
print(string)

colors = ['salmon', 'apricot', 'basic blue', 'perfect perriwinkle']
colors_string = ''
for item in colors:
	colors_string += item + "\n" 
colors_string = colors_string[:-1]

print(colors_string)

def list_maker(sequence):
	list = []
	for element in sequence:
		list.append(element) 
	return list

print(list_maker(range(5)))
