import dbaction as dba
import tabulate as tba

def main_labels(stype,sgame,sweek):
    nlist = []

    if sgame == "T1":
        label = "\n GROUP #1 \n----------"
    elif sgame == "T2":
        label = "\n GROUP #2 \n----------"
    else:
        label = "\n GROUP #3 \n----------"

    print(label)

    n1 = int(input("\tEnter the 1st number: "))
    n2 = int(input("\tEnter the 2nd number: "))
    n3 = int(input("\tEnter the 3th number: "))
    n4 = int(input("\tEnter the 4th number: "))
    n5 = int(input("\tEnter the 5th number: "))
    n6 = int(input("\tEnter the 6th number: "))

    nlist = [stype,sgame,sweek,n1,n2,n3,n4,n5,n6]

    return nlist


def select_game(typeg):
    datal = []

    print("S - Short Game\nL - Long Game\n")

    gsel = input("Choose an option: ")

    if typeg == "E":
        if gsel == "S":
            enter_data("S")
            data = dba.view_db("S")
        else:
            enter_data("L")
            data = dba.view_db("L")
    else:
        if gsel == "S":
            data = dba.view_db("S")
        else:
            data = dba.view_db("L")


    for d in data:
        dlist = list(d)
        dlist = dlist[3:]
        
        for dd in dlist:
            datal.append(dd)
    
    engine_game(datal, gsel)


def enter_data(selg):
    if selg == "S":
        dba.change_db(selg)
        data = main_labels("A","T1","W1")
        data = check_data(data)
        dba.enter_db(data)
    else:
        dba.change_db(selg)
        for i in range(1,4):
            data = main_labels("B","T" + str(i),"W1")
            data = check_data(data)
            dba.add_db(data)


def add_data():
    print("Select the game you want to enter de data:\n\nS - Short Game\nL - Long Game\n")

    gsel = input("Choose an option: ")

    if gsel == "S":
        for i in range(1,7):
            print("\n WEEK #" + str(i),"\n----------")
            data = main_labels("A","T1","W" + str(i))
            data = check_data(data)
            dba.add_db(data)
    else:
        for i in range(1,7):
            for ii in range(1,4):
                print("\n WEEK #" + str(i),"\n----------")
                data = main_labels("B","T" + str(ii),"W" + str(i))
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
    print("Select the data you want to view:\n\nS - Short Game\nL - Long Game\nA - All Data\n")

    vsel = input("Choose an option: ")
    data = dba.view_db(vsel)
    headers = ["ID", "GAME TYPE", "WEEK", "N1","N2","N3","N4","N5","N6"]
    table = tba.tabulate(data, headers, tablefmt = "fancy_grid")

    print(table)
    input("\nPress any key to continue...")


def delete_data():
    print("Select the game you want to delete de data:\n\nS - Short Game\nL - Long Game\nA - All Data\nC - Cancel\n")

    gsel = input("Choose an option: ")
    csel = input("\nAre you sure to delete the data (Y/N) ? ")

    if csel == "Y":
        dba.delete_db(gsel)


def engine_game(mlist,gsel):
    n2 = []
    n3 = []
    n4 = []
    n5 = []
    n6 = []
    
    mlist.sort()

    # 39 - Short
    # 56 - Long

    if gsel == "S":
        for n in range(1,40):
            count = mlist.count(n)

            if count == 2:
                n2.append(n)
            elif count == 3:
                n3.append(n)
            elif count == 4:
                n4.append(n)
            elif count >= 5:
                n5.append(n)
    else:
        for n in range(1,57):
            count = mlist.count(n)

            if count == 3:
                n2.append(n)
            elif count == 4:
                n3.append(n)
            elif count == 5:
                n4.append(n)
            elif count >= 6:
                n5.append(n)
    
    print("\n Results\n---------")

    if gsel == "S":    
        print("\tNumbers with 2 repetitions........:", n2)

    print("\tNumbers with 3 repetitions........:", n3)
    print("\tNumbers with 4 repetitions........:", n4)

    if gsel == "S":
        print("\tNumbers with 5 or more repetitions:", n5)
    else:
        print("\tNumbers with 5 repetitions........:", n5)

    if gsel == "L":
        print("\tNumbers with 6 or more repetitions:", n6)
    
    input("\n\tPress any key to continue...")
