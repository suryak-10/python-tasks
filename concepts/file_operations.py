import os
import shutil

def setup_sample_environment():
    """Set up a sample environment for file and folder operations."""
    os.makedirs("sample_dir/sub_dir", exist_ok=True)
    with open("sample_dir/sample_file.txt", "w") as f:
        f.write("This is a sample file.")
    print("Sample environment set up.\n")


# File operations
def create_file(file_path, content=""):
    """Create a file with optional content."""
    with open(file_path, "w") as f:
        f.write(content)
    print(f"File '{file_path}' created.")


def read_file(file_path):
    """Read and print the content of a file."""
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        print(f"Content of '{file_path}':\n{content}")
    else:
        print(f"'{file_path}' does not exist.")


def append_to_file(file_path, content):
    """Append content to a file."""
    if os.path.isfile(file_path):
        with open(file_path, "a") as f:
            f.write(content)
        print(f"Appended content to '{file_path}'.")
    else:
        print(f"'{file_path}' does not exist.")


def rename_file(old_name, new_name):
    """Rename a file."""
    if os.path.isfile(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print(f"'{old_name}' does not exist.")


def copy_file(source, destination):
    """Copy a file."""
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print(f"File copied from '{source}' to '{destination}'.")
    else:
        print(f"'{source}' does not exist.")


def delete_file(file_path):
    """Delete a file."""
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    else:
        print(f"'{file_path}' is not a valid file.")


# Folder operations
def create_folder(folder_path):
    """Create a folder."""
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder '{folder_path}' created.")


def rename_folder(old_name, new_name):
    """Rename a folder."""
    if os.path.isdir(old_name):
        os.rename(old_name, new_name)
        print(f"Folder renamed from '{old_name}' to '{new_name}'.")
    else:
        print(f"'{old_name}' does not exist.")


def copy_folder(source, destination):
    """Copy a folder."""
    if os.path.isdir(source):
        shutil.copytree(source, destination)
        print(f"Folder copied from '{source}' to '{destination}'.")
    else:
        print(f"'{source}' does not exist.")


def move_folder(source, destination):
    """Move a folder."""
    if os.path.isdir(source):
        shutil.move(source, destination)
        print(f"Folder moved from '{source}' to '{destination}'.")
    else:
        print(f"'{source}' does not exist.")


def delete_folder(folder_path):
    """Delete a folder."""
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' deleted.")
    else:
        print(f"'{folder_path}' is not a valid folder.")


def list_folder_contents(folder_path):
    """List the contents of a folder."""
    if os.path.isdir(folder_path):
        contents = os.listdir(folder_path)
        print(f"Contents of '{folder_path}': {contents}")
    else:
        print(f"'{folder_path}' is not a valid folder.")


# Check existence
def check_existence(path):
    """Check if a file or folder exists."""
    if os.path.exists(path):
        print(f"'{path}' exists.")
    else:
        print(f"'{path}' does not exist.")


# Main script demonstrating operations
if __name__ == "__main__":
    setup_sample_environment()

    # File operations
    create_file("sample_dir/new_file.txt", "Hello, World!")
    read_file("sample_dir/new_file.txt")
    append_to_file("sample_dir/new_file.txt", "\nAppended text.")
    read_file("sample_dir/new_file.txt")
    rename_file("sample_dir/new_file.txt", "sample_dir/renamed_file.txt")
    copy_file("sample_dir/renamed_file.txt", "sample_dir/copied_file.txt")
    delete_file("sample_dir/copied_file.txt")

    # Folder operations
    create_folder("sample_dir/new_folder")
    rename_folder("sample_dir/new_folder", "sample_dir/renamed_folder")
    copy_folder("sample_dir/renamed_folder", "sample_dir/copied_folder")
    move_folder("sample_dir/copied_folder", "sample_dir/moved_folder")
    delete_folder("sample_dir/moved_folder")

    # List contents and check existence
    list_folder_contents("sample_dir")
    check_existence("sample_dir/renamed_file.txt")
    check_existence("sample_dir/non_existent.txt")

    # Clean up
    delete_folder("sample_dir")
    check_existence("sample_dir")
