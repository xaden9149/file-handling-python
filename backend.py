
from pathlib import Path

# Project folder
folder = Path(__file__).parent

def list_files():
    excluded = {".venv", "__pycache__", ".git"}

    items = [
        item for item in folder.rglob("*")
        if not any(part in excluded for part in item.parts)
        and item.is_file()
    ]

    return items


def create_file(name, content):
    p = folder / name

    if p.exists():
        return "File already exists!"

    try:
        p.parent.mkdir(parents=True, exist_ok=True)

        with open(p, "w") as f:
            f.write(content)

        return "File created successfully!"

    except Exception as err:
        return f"Error: {err}"


def read_file(name):
    p = folder / name

    if p.exists() and p.is_file():
        try:
            with open(p, "r") as f:
                return f.read()
        except Exception as err:
            return f"Error: {err}"

    return "File does not exist!"


def overwrite_file(name, content):
    p = folder / name

    if p.exists() and p.is_file():
        try:
            with open(p, "w") as f:
                f.write(content)

            return "File updated successfully!"

        except Exception as err:
            return f"Error: {err}"

    return "File does not exist!"


def append_file(name, content):
    p = folder / name

    if p.exists() and p.is_file():
        try:
            with open(p, "a") as f:
                f.write(content)

            return "Content appended successfully!"

        except Exception as err:
            return f"Error: {err}"

    return "File does not exist!"


def rename_file(name, new_name):
    p = folder / name
    p2 = folder / new_name

    if not p.exists() or not p.is_file():
        return "File does not exist!"

    if p2.exists():
        return "The new name already exists!"

    try:
        p.rename(p2)
        return "File renamed successfully!"

    except Exception as err:
        return f"Error: {err}"


def delete_file(name):
    p = folder / name

    if p.exists() and p.is_file():
        try:
            p.unlink()
            return "File deleted successfully!"

        except Exception as err:
            return f"Error: {err}"

    return "File does not exist!"
