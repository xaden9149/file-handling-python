
def add_note():
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write( note + "\n")

    print("Note saved successfully!")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print("\n--- Your Notes ---")
            print(file.read())

    except Exception as err:
           print(f"An error occured as {err}")


def edit_note():
    with open("notes.txt", "r") as file:
        notes = file.readlines()

    if len(notes) == 0:
        print("No notes available to edit.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")

    number = int(input("Which note do you want to edit? "))

    if number < 1 or number > len(notes):
        print("Invalid note number.")
        return

    new_note = input("Enter the updated note: ")
    notes[number - 1] = new_note + "\n"

    with open("notes.txt", "w") as file:
        file.writelines(notes)

    print("Note updated successfully!")


def delete_note():
    with open("notes.txt", "r") as file:
        notes = file.readlines()

    if len(notes) == 0:
        print("No notes available to delete.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")

    number = int(input("Which note do you want to delete? "))

    if number < 1 or number > len(notes):
        print("Invalid note number.")
        return

    removed_note = notes.pop(number - 1)

    with open("notes.txt", "w") as file:
        file.writelines(notes)

    print(f"Deleted note: {removed_note.strip()}")

   


while True:
    print("\n1. Add a note")
    print("2. View notes")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")