file = open("input1","r")
i = int(input('Digit the number of the line that you want to change: '))-1
text = input('Write the text you want to append: ')
list_of_lines = []
for line in file:
    counter = 1
    element = str(counter)+'. '+  line.strip('\n')
    counter+=1
    list_of_lines.append(element)
list_of_lines[i]= text
print(list_of_lines)

file.close()

""" file = open("input1","w")

readfile.writelines(readfile)

file.close() """