from pathlib import Path
import os 

def readfielandfolder():
    path = Path('.')

    excluded = {'.venv', '__pycache__', '.git'}

    items = [
        item for item in path.rglob('*')
        if not any(part in excluded for part in item.parts)
    ]

    for i, item in enumerate(items, start=1):
        print(f"{i}: {item}")

def createfile():
    try:
        readfielandfolder()
        name = input("please tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in this file :- ")
                fs.write(data)
            
            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exist")
        
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfielandfolder()
        name = input("which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            
            print("Readed successfully ")
        else:
            print("the file doesnot exist")
    except Exception as err:
        print(f"An error occured as {err}")


def updatefile():
    try:
            
        readfielandfolder()
        name = input("tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file ")
            print("press 3 for appending some content in your file ")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input("tell  your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write this is overwrite the data :- ")
                    fs.write(data)
        
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" "+data)

    except Exception as err:
        print("an error occured as {err}")


def deletefile():
    try:

        readfielandfolder()
        name = input("whuich file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
        
            print("file removes suiccessfully ")
    
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")



while True:
    print("\n========== FILE MANAGEMENT SYSTEM ==========")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Exit")

    check = input("Please enter your choice: ")

    if check == "1":
        createfile()

    elif check == "2":
        readfile()

    elif check == "3":
        updatefile()

    elif check == "4":
        deletefile()

    elif check == "5":
        print("\nThank you for using the File Management System!")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 5.")
