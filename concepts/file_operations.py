import os
import shutil

def check_if_exists(path):
    """Check if a file or directory exists."""
    return os.path.exists(path)

def create_folder(folder_path):
    """Create a new folder if it doesn't already exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

def delete_file(file_path):
    """Delete a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    else:
        print(f"File does not exist: {file_path}")

def delete_folder(folder_path):
    """Delete a folder and its contents."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder deleted: {folder_path}")
    else:
        print(f"Folder does not exist: {folder_path}")

def copy_file(source, destination):
    """Copy a file from source to destination."""
    if os.path.exists(source):
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    else:
        print(f"Source file does not exist: {source}")

def move_file(source, destination):
    """Move a file from source to destination."""
    if os.path.exists(source):
        shutil.move(source, destination)
        print(f"File moved from {source} to {destination}")
    else:
        print(f"Source file does not exist: {source}")

def list_contents(folder_path):
    """List all files and folders in a directory."""
    if os.path.exists(folder_path):
        contents = os.listdir(folder_path)
        print(f"Contents of {folder_path}: {contents}")
        return contents
    else:
        print(f"Folder does not exist: {folder_path}")
        return []

# Examples of usage
if __name__ == "__main__":
    # Define file and folder paths
    folder = "example_folder"
    file_name = "example_file.txt"
    file_path = os.path.join(folder, file_name)
    copy_path = "example_file_copy.txt"
    moved_file_path = os.path.join(folder, "moved_file.txt")

    # Example 1: Create folder
    create_folder(folder)

    # Example 2: Create a file inside the folder
    if not check_if_exists(file_path):
        with open(file_path, "w") as file:
            file.write("This is an example file.")
        print(f"File created: {file_path}")

    # Example 3: List folder contents
    list_contents(folder)

    # Example 4: Copy the file
    copy_file(file_path, copy_path)

    # Example 5: Move the file
    move_file(file_path, moved_file_path)

    # Example 6: Check if the moved file exists
    if check_if_exists(moved_file_path):
        print(f"The moved file exists at: {moved_file_path}")

    # Example 7: Write additional content to the moved file
    with open(moved_file_path, "a") as file:
        file.write("\nAdding more content to the moved file.")
        print(f"Additional content written to: {moved_file_path}")

    # Example 8: Read the contents of the moved file
    with open(moved_file_path, "r") as file:
        content = file.read()
        print(f"Contents of {moved_file_path}:\n{content}")

    # Example 9: Delete the copied file
    delete_file(copy_path)

    # Example 10: Delete the folder
    delete_folder(folder)
