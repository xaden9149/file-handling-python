
from pathlib import Path

# Location of notes.txt
file_path = Path(__file__).parent / "notes.txt"


def view_notes():
    # Create notes.txt if it does not exist
    if not file_path.exists():
        file_path.touch()

    with open(file_path, "r") as file:
        notes = file.readlines()

    # Remove the newline from each note
    notes = [note.strip() for note in notes]

    return notes


def add_note(note):
    if note.strip() == "":
        return "Note cannot be empty!"

    with open(file_path, "a") as file:
        file.write(note.strip() + "\n")

    return "Note saved successfully!"


def edit_note(number, new_note):
    notes = view_notes()

    if number < 1 or number > len(notes):
        return "Invalid note number!"

    if new_note.strip() == "":
        return "Note cannot be empty!"

    # Update the selected note
    notes[number - 1] = new_note.strip()

    with open(file_path, "w") as file:
        for note in notes:
            file.write(note + "\n")

    return "Note updated successfully!"


def delete_note(number):
    notes = view_notes()

    if number < 1 or number > len(notes):
        return "Invalid note number!"

    # Remove the selected note
    removed_note = notes.pop(number - 1)

    with open(file_path, "w") as file:
        for note in notes:
            file.write(note + "\n")

    return f"Deleted note: {removed_note}"
