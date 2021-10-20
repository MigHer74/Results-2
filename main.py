import os
import minis as ms
import dbaction as dba

connect_db = dba.connect_db()

cicle = True

while cicle:
    os.system("cls")

    print("N - Normal Game\nL - Long Game\nE - Enter Previous Data\nD - Delete All Data\nX - Exit\n")

    sel = input("Choose an option: ")

    if sel == "N":
        print("Normal Game")
    elif sel == "L":
        print("Long Game")
    elif sel == "E":
        print("Enter Previous Data")
    elif sel == "D":
        print("Delete All Data")
    elif sel == "X":
        print("Exit")
        break
    else:
        print("Try Again")