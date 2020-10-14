import os
import sqlite3
import time

running = True


def printtable(tablename):
    database = "DataLabellingAPI.db"
    os.system('clear')
    db = sqlite3.connect(database)
    rv = db.execute('SELECT * FROM ' + tablename)
    data = [_ for _ in rv][::-1]
    for i in range(0, len(data), 20):
        temp = data[i:i + 20]
        [print(i + o, data) for o, data in enumerate(temp)]
        if i + 20 < len(data):
            a = input("Press any key for next page/ press 'q' to end...")
            if a == 'q':
                break
            os.system('clear')
    db.close()
    input("Press any key to go back...")


# select count(*), slide_set from Pool_Table where slide = 's12015a' group by slide_set
while running:
    os.system('clear')
    print("1. Show User Table")
    print("2. Show Pool Table")
    print("3. Show Flag Table")
    print("4. Show slide Table")
    print("5. Show Image Table")
    print("6. Show Assigned Table")
    print("7. Run Query")
    print("8. total / slied")
    print("9. Labelled / slide")
    print("10. images/pool")
    print("11. Show labbeled info")
    print("0. Exit")
    try:
        choice = int(input("Input?:"))
    except:
        choice = -1

    if choice == 1:
        printtable("User_Table")
    elif choice == 2:
        printtable("Pool_Table")
    elif choice == 3:
        printtable("Flag_Table")
    elif choice == 4:
        printtable("Slide_Table")
    elif choice == 5:
        printtable("Image_Table")
    elif choice == 6:
        printtable("Assigned_Table")
    elif choice == 7:
        try:
            query = input("Enter query:")
            database = "DataLabellingAPI.db"
            db = sqlite3.connect(database)
            rv = db.execute(query)
            [print(_) for _ in rv]
            db.commit()
            db.close()
        except Exception as e:
            print("error occured!\n", e)
        input("Press any key to go back...")
    elif choice == 8:
        try:
            database = "DataLabellingAPI.db"
            db = sqlite3.connect(database)
            rv = db.execute(
                "SELECT username, count(*), slide, slide_set, discarded FROM Image_Table group by username, slide, slide_set")
            [print(_) for _ in rv]
            db.commit()
            db.close()
        except Exception as e:
            print("error occured!\n", e)
        input("Press any key to go back...")
    elif choice == 9:
        try:
            database = "DataLabellingAPI.db"
            db = sqlite3.connect(database)
            choice_9 = int(input("Detailed? [0/1]:"))
            if choice_9 == 1:
                rv = db.execute(
                    "SELECT username, count(*), slide, slide_set, discarded FROM Image_Table WHERE label is not null group by username, slide, slide_set")
            else:
                rv = db.execute(
                    "SELECT username, count(*), slide, slide_set, discarded FROM Image_Table WHERE label is not null group by username")
            [print(_) for _ in rv]
            db.commit()
            db.close()
        except Exception as e:
            print("error occured!\n", e)
        input("Press any key to go back...")
    elif choice == 10:
        try:
            database = "DataLabellingAPI.db"
            db = sqlite3.connect(database)
            rv = db.execute("SELECT count(*), slide, slide_set FROM Pool_Table group by slide, slide_set")
            [print(_) for _ in rv]
            db.commit()
            db.close()
        except Exception as e:
            print("error occured!\n", e)
        input("Press any key to go back...")
    elif choice == 11:
        try:
            query = input("Enter query:")
            database = "DataLabellingAPI.db"
            db = sqlite3.connect(database)
            rv = db.execute("select * from Image_Table where imname = '" + query + "'")
            [print(_) for _ in rv]
            db.commit()
            db.close()
        except Exception as e:
            print("error occured!\n", e)
        input("Press any key to go back...")
    elif choice == 0:
        running = False
    else:
        print("Wrong choice!")
        time.sleep(1)
