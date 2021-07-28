import os.path
file = input('Enter a file name: ')
if os.path.isfile(file):
    print('This file already exists...\nDo you want to:(type the #) \n 1.Read the file \n 2.Write the file \n 3.Append the file \n 4.Replace a single line of the file')
    answer = int(input(''))
    if answer == 1:
        #read the file
        print(' ')
        readFile = open(file,"r")
        theWholeFile = readFile.read()
        print(theWholeFile)
        readFile.close()
    elif answer == 2:
        #write the file
        writeFile = open(file,"w")
        fileInfo = []
        while True:
            i = 1
            if i == 1:
                print('Enter the info that you want to write on it:')
                fileInformation = input('Take a note: ')
                fileInfo.append(fileInformation)
                print('Do you want to take more notes?(type the #) \n1.Yes \n2.No')
                i = input('')
            else:
                print('You stopped taking notes.')
        for data in fileInfo:
            writeFile.write(data + '\n')
        writeFile.close()
    elif answer==3:
        #append the file
        appendFile = open(file,"a")
        print('Do you want to add more notes?(type the #) \n1.Yes \n2.No')
        newInformation = []
        while True:
            i = int(input(''))
            if i == 1:
                print('Type the new info that you want to add:')
                info = input('')
                newInformation.append(info)
                print('Do you want to add more info?(type the #) \n1.Yes \n2.No')
            else:
                print('You stopped adding notes.')
                break

        
        for data in newInformation:
            appendFile.write(data + '\n')
            
        appendFile.close()
    else:
        #REPLACE LINE
        replaceFile = open(file,"r")
        lines = []

        #THIS IS TO INTERACT WITH THE USER EASIER
        counter = 1
        for line in replaceFile:
            element = str(counter)+'. '+ line.strip('\n')
            counter+=1
            print(element)
            lines.append(line.strip('\n'))

        i = int(input('Digit the number of the line that you want to change: ')) - 1
        text = input('Write the text you want to append: ')

        lines[i]= text
        for element in lines:
            print(element.strip('\n'))
            
        replaceFile.close()
        
        writeFile = open(file, 'w')
        for data in lines:
            writeFile.write(data + '\n')
        writeFile.close()

else: 
    print('File does not exists \n Do you want to take notes?(type the #) \n1.Yes \n2.No')
    writeFile = open(file, 'w')
    fileInfo = []
    
    while True:
        i = int(input(''))
        if i == 1:
            print('Enter the info that you want to write on it:')
            info = input('')
            fileInfo.append(info)
            print('Do you want to take more notes?(type the #) \n1.Yes \n2.No')
        else:
            print('You stopped taking notes.')
            break

    
    for data in fileInfo:
        writeFile.write(data + '\n')
    
    writeFile.close()