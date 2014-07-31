import sqlite3

conn = sqlite3.connect("newnum.db")

cursor = conn.cursor()

prompt = """
Select the operation that you want ot perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""


while True:
    choice = raw_input(prompt)
    if choice in set(["1", "2", "3", "4"]):
        operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int (choice)]
        cursor.execute("SELECT {}(num) from numbers".format(operation))
        get = cursor.fetchone()

        print operation + ": {}".format(get[0])

    elif choice == "5":
        print "Exit"
        break

