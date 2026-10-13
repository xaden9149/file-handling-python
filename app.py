

import streamlit as st

from backend import (
    list_files,
    create_file,
    read_file,
    overwrite_file,
    append_file,
    rename_file,
    delete_file
)

# Page setup
st.set_page_config(page_title="File Manager", page_icon="📁")

st.title("📁 File Management System")
st.write("Create, read, update, rename and delete files.")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Choose an operation",
    [
        "View Files",
        "Create File",
        "Read File",
        "Update File",
        "Rename File",
        "Delete File"
    ]
)

# 1. View files
if menu == "View Files":
    st.subheader("Your Files")

    files = list_files()

    if len(files) == 0:
        st.info("No files found.")
    else:
        for file in files:
            st.write("📄", file)

# 2. Create file
elif menu == "Create File":
    st.subheader("Create a File")

    name = st.text_input("Enter file name")
    content = st.text_area("Enter content")

    if st.button("Create File"):
        if name.strip() == "":
            st.warning("Please enter a file name.")
        else:
            message = create_file(name, content)
            st.write(message)

# 3. Read file
elif menu == "Read File":
    st.subheader("Read a File")

    files = list_files()

    if len(files) == 0:
        st.info("No files available.")
    else:
        name = st.selectbox("Choose a file", files)

        if st.button("Read File"):
            content = read_file(name)
            st.text_area("File Content", value=content, height=200)

# 4. Update file
elif menu == "Update File":
    st.subheader("Update a File")

    files = list_files()

    if len(files) == 0:
        st.info("No files available.")
    else:
        name = st.selectbox("Choose a file", files)

        action = st.radio(
            "Choose an action",
            ["Overwrite", "Append"]
        )

        content = st.text_area("Enter content")

        if st.button("Save Changes"):
            if action == "Overwrite":
                message = overwrite_file(name, content)
            else:
                message = append_file(name, content)

            st.write(message)

# 5. Rename file
elif menu == "Rename File":
    st.subheader("Rename a File")

    files = list_files()

    if len(files) == 0:
        st.info("No files available.")
    else:
        name = st.selectbox("Choose a file", files)
        new_name = st.text_input("Enter new file name")

        if st.button("Rename File"):
            if new_name.strip() == "":
                st.warning("Please enter a new name.")
            else:
                message = rename_file(name, new_name)
                st.write(message)

# 6. Delete file
elif menu == "Delete File":
    st.subheader("Delete a File")

    files = list_files()

    if len(files) == 0:
        st.info("No files available.")
    else:
        name = st.selectbox("Choose a file", files)

        confirm = st.checkbox("I confirm that I want to delete this file.")

        if st.button("Delete File"):
            if confirm:
                message = delete_file(name)
                st.write(message)
                st.rerun()
            else:
                st.warning("Please confirm before deleting.")
