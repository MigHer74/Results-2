import dbaction as dba

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
            dba.add_db(data)
    else:
        for i in range(1,7):
            for ii in range(1,4):
                print(" WEEK #" + str(i),"\n----------")
                data = main_labels(2,"T" + str(ii),"W" + str(i))
                dba.add_db(data)


def delete_data():
    print("Select the game you want to delete de data:\n\nN - Normal Game\nL - Long Game\nA - All Data\n")

    gsel = input("Choose an option: ")
    csel = input("Are you sure to delete the data (Y/N) ? ")

    if csel == "Y":
        dba.delete_db(gsel)