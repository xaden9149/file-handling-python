
import streamlit as st

from notesbackend import view_notes, add_note, edit_note, delete_note

st.set_page_config(page_title="Notes App", page_icon="📝")

st.title("📝 My Notes App")
st.write("Save your thoughts, one note at a time.")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Choose an operation",
    ["View Notes", "Add Note", "Edit Note", "Delete Note"]
)

# 1. View notes
if menu == "View Notes":
    st.subheader("Your Notes")

    notes = view_notes()

    if len(notes) == 0:
        st.info("You have no notes yet.")
    else:
        for i, note in enumerate(notes, start=1):
            st.write(f"**{i}.** {note}")

# 2. Add a note
elif menu == "Add Note":
    st.subheader("Add a New Note")

    note = st.text_area("Write your note")

    if st.button("Save Note"):
        message = add_note(note)
        st.write(message)

        if message == "Note saved successfully!":
            st.rerun()

# 3. Edit a note
elif menu == "Edit Note":
    st.subheader("Edit a Note")

    notes = view_notes()

    if len(notes) == 0:
        st.info("No notes available to edit.")
    else:
        # Show notes with their numbers
        for i, note in enumerate(notes, start=1):
            st.write(f"**{i}.** {note}")

        number = st.number_input(
            "Enter note number",
            min_value=1,
            max_value=len(notes),
            step=1
        )

        new_note = st.text_area("Enter updated note")

        if st.button("Update Note"):
            message = edit_note(number, new_note)
            st.write(message)

            if message == "Note updated successfully!":
                st.rerun()

# 4. Delete a note
elif menu == "Delete Note":
    st.subheader("Delete a Note")

    notes = view_notes()

    if len(notes) == 0:
        st.info("No notes available to delete.")
    else:
        for i, note in enumerate(notes, start=1):
            st.write(f"**{i}.** {note}")

        number = st.number_input(
            "Enter note number to delete",
            min_value=1,
            max_value=len(notes),
            step=1
        )

        confirm = st.checkbox("I want to delete this note.")

        if st.button("Delete Note"):
            if confirm:
                message = delete_note(number)
                st.write(message)
                st.rerun()
            else:
                st.warning("Please confirm before deleting.")
