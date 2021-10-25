import os
import minis as ms

cicle = True

while cicle:
    os.system("cls")

    print("N - Normal Game\nL - Long Game\nE - Enter Previous Data\nV - View Data\nD - Delete All Data\nX - Exit\n")
    
    sel = input("Choose an option: ")

    if sel == "N":
        ms.enter_data("N")
    elif sel == "L":
        ms.enter_data("L")
    elif sel == "E":
        ms.add_data()
    elif sel == "V":
        ms.show_data()        
    elif sel == "D":
        ms.delete_data()
    elif sel == "X":
        print("Exit")
        break
    else:
        print("Try Again")