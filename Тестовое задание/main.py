import os
import commands
import keyboard

while True:
    choice = int(input("\nВыберите команду: \n1)Открыть заметку \n2)Создать заметку \n3)Удалить заметку \n4)Выйти\n\n"))
    
    #открыть заметку
    if choice == 1:
        
        print("\nВыберите заметку, которую хотите открыть:\n")
        filesArray = os.listdir('Notes/')
        
        for i in range(0, len(filesArray)):
            print(str(i+1) + ')' + filesArray[i])
            
        
        print("\n0)Назад")
            
        choiceFile = int(input())
        
        if choiceFile == 0:
            pass        
        else:
            
            file = filesArray[choiceFile-1]
            fileName = str(file.split('.')[0])
            fileFormat = str(file.split('.')[1])
        
        
            print('\nТекст заметки под названием: ' + fileName + '\n\n')
            commands.openFile(fileName, fileFormat)

            choice = int(input("\nВыберите команду: \n1)Изменить заметку \n0)Назад\n\n"))
            #изменить заметку
            if choice == 1:
                if fileFormat == 'docx':
                    choiceDocx = int(input('1)Изменить текст \n2)Добавить картинку\n'))
                if (choice == 1 and fileFormat == 'txt') or (choice == 1 and choiceDocx == 1):
                    print("\n/exit - для выхода\nВведите текст, который хотите добавить в заметку: \n\n")
                    line = input()
                    if line != '/exit':
                        commands.changeFile(fileName, fileFormat, line)
                    while True:
                        if keyboard.read_key() == 'enter':
                            line = input()
                            if line != '/exit':
                                commands.changeFile(fileName, fileFormat, '\n' + line)
                        if line == '/exit':
                            break
                else:
                    print("\n0)Назад\nВыберите картинку: \n")
                    picArray = os.listdir('Img/')
                    for i in range(0, len(picArray)):
                        print(str(i+1) + ')' + picArray[i])
                    
                    choicePic = int(input())
                    if choicePic == 0:
                        pass
                    else:
                    
                        picture = picArray[choicePic-1]
                        commands.addPicture(fileName, picture)
                    
                
        #вернуться назад в меню
    elif choice == 0:
            pass
        
    #создать заметку    
    elif choice == 2:
        fileName = input('\nВведите название заметки: \n\n')
        fileFormat = input('\nНапишите формат файла\n\n')
        commands.createFile(fileName, fileFormat)
     
    #удалить заметку    
    elif choice == 3:
        
        print("\nВыберите заметку, которую хотите удалить:\n")
        filesArray = os.listdir('Notes/')
        
        for i in range(0, len(filesArray)):
            print(str(i+1) + ')' + filesArray[i])
            
        choiceFile = int(input())
        
        file = filesArray[choiceFile-1]    
        
        
        os.remove('Notes\{}'.format(file))
        
    #закрыть программу    
    elif choice == 4:
        break
    