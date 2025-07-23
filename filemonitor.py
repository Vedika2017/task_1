import hashlib
import os

file_path = input("Enter the path of the file to monitor: ")


def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):  
                sha1.update(chunk)
        return sha1.hexdigest()
    except FileNotFoundError:
        print("File not found!")
        return None


current_hash = calculate_sha1(file_path)


hash_file = "hash_record.txt"
previous_hash = None

if os.path.exists(hash_file):
    with open(hash_file, 'r') as f:
        previous_hash = f.read().strip()


if current_hash:
    if previous_hash is None:
        print("No previous record found. Saving current hash.")
    elif previous_hash == current_hash:
        print("✅ The file has NOT changed.")
    else:
        print("⚠️ The file HAS CHANGED!")


    with open(hash_file, 'w') as f:
        f.write(current_hash)
