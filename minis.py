import dbaction as dba
import tabulate as tba

def main_labels(stype,sgame,sweek):
    nlist = []

    if sgame == "T1":
        label = " GROUP #1 \n----------"
    elif sgame == "T2":
        label = " GROUP #2 \n----------"
    else:
        label = " GROUP #3 \n----------"

    print(label)

    n1 = int(input("\tEnter the 1st number: "))
    n2 = int(input("\tEnter the 2nd number: "))
    n3 = int(input("\tEnter the 3th number: "))
    n4 = int(input("\tEnter the 4th number: "))
    n5 = int(input("\tEnter the 5th number: "))
    n6 = int(input("\tEnter the 6th number: "))

    nlist = [stype,sgame,sweek,n1,n2,n3,n4,n5,n6]

    return nlist


def add_data():
    print("Select the game you want to enter de data:\n\nN - Normal Game\nL - Long Game\n")

    gsel = input("Choose an option: ")

    if gsel == "N":
        for i in range(1,7):
            print(" WEEK #" + str(i),"\n----------")
            data = main_labels(1,"T1","W" + str(i))
            data = check_data(data)
            dba.add_db(data)
    else:
        for i in range(1,7):
            for ii in range(1,4):
                print(" WEEK #" + str(i),"\n----------")
                data = main_labels(2,"T" + str(ii),"W" + str(i))
                data = check_data(data)
                dba.add_db(data)


def check_data(data):
    cicle = True

    while cicle:
        print()
        P1 = data[:3]
        P2 = data[3:]
        conf = input(f"\tIs the list {P2} correct (Y/N) ? ")
        print()

        if conf == "N":
            for num in P2:
                print("\t->",num)

            selo = int(input("\tSelect the number to change: "))
            selc = int(input("\tEnter the new value........: "))
            
            P2[P2.index(selo)] = selc

            data = P1 + P2
        else:
            break

    return data


def show_data():
    print("Select the data you want to view:\n\nN - Normal Game\nL - Long Game\nA - All Data\n")

    vsel = input("Choose an option: ")
    data = dba.view_db(vsel)
    headers = ["ID", "GAME TYPE", "WEEK", "N1","N2","N3","N4","N5","N6"]
    table = tba.tabulate(data, headers, tablefmt = "fancy_grid")

    print(table)
    input("\nPress any key to continue...")


def delete_data():
    print("Select the game you want to delete de data:\n\nN - Normal Game\nL - Long Game\nA - All Data\n")

    gsel = input("Choose an option: ")
    csel = input("Are you sure to delete the data (Y/N) ? ")

    if csel == "Y":
        dba.delete_db(gsel)