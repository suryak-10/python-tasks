import os
import shutil

# Set up sample files and directories for demonstration
def setup_sample_files():
    os.makedirs("sample_dir/sub_dir", exist_ok=True)
    with open("sample_dir/sample_file.txt", "w") as f:
        f.write("This is a sample file.")
    print("Sample files and directories set up.")

# Rename a file or folder
def rename_item(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'")
    else:
        print(f"'{old_name}' does not exist.")

# Copy a file or folder
def copy_item(source, destination):
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print(f"Copied file '{source}' to '{destination}'")
    elif os.path.isdir(source):
        shutil.copytree(source, destination)
        print(f"Copied directory '{source}' to '{destination}'")
    else:
        print(f"'{source}' does not exist.")

# Move a file or folder
def move_item(source, destination):
    if os.path.exists(source):
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}'")
    else:
        print(f"'{source}' does not exist.")

# Check if a file or folder exists
def check_existence(path):
    if os.path.exists(path):
        print(f"'{path}' exists.")
    else:
        print(f"'{path}' does not exist.")

# Delete a file
def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted file '{file_path}'")
    else:
        print(f"'{file_path}' is not a valid file.")

# Delete a folder
def delete_folder(folder_path):
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted folder '{folder_path}'")
    else:
        print(f"'{folder_path}' is not a valid folder.")

# Main script to demonstrate operations
if __name__ == "__main__":
    setup_sample_files()

    # Rename a file
    rename_item("sample_dir/sample_file.txt", "sample_dir/renamed_file.txt")

    # Copy a file
    copy_item("sample_dir/renamed_file.txt", "sample_dir/copied_file.txt")

    # Move a file
    move_item("sample_dir/copied_file.txt", "sample_dir/sub_dir/copied_file.txt")

    # Check existence
    check_existence("sample_dir/renamed_file.txt")
    check_existence("sample_dir/non_existent_file.txt")

    # Delete a file
    delete_file("sample_dir/renamed_file.txt")

    # Delete a folder
    delete_folder("sample_dir/sub_dir")

    # Final check
    check_existence("sample_dir/sub_dir")
