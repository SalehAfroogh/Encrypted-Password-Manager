import os
from cryptography.fernet import Fernet
import password_managment  # Corrected to match the actual file name

def test_write_key():
    # Test key generation and writing to file
    test_key_path = "./test_key.key"
    key = Fernet.generate_key()
    with open(test_key_path, "wb") as f:
        f.write(key)
    
    assert os.path.exists(test_key_path), "Key file was not created."

    # Clean up
    os.remove(test_key_path)

def test_add_and_view_pass():
    # Test adding and viewing passwords
    test_key_path = "./test_key.key"
    test_file_path = "./test_passwords.txt"

    # Create a test key
    key = Fernet.generate_key()
    with open(test_key_path, "wb") as f:
        f.write(key)
    
    fernet = Fernet(key)

    # Replace paths in the main script (optional if paths are configurable)
    password_managment.key = key
    password_managment.fernet = fernet

    # Add a test password
    username = "test_user"
    password = "test_password"
    password_managment.add_pass(username, password)

    # Check if the password was written correctly (encrypted)
    with open(test_file_path, "r") as f:
        content = f.readlines()
    assert len(content) == 1, "Password file should contain one entry."
    stored_username, stored_encrypted_pass = content[0].strip().split("|")
    assert stored_username == username, "Username mismatch in stored data."
    decrypted_pass = fernet.decrypt(stored_encrypted_pass.encode()).decode()
    assert decrypted_pass == password, "Decrypted password does not match."

    # Test viewing passwords
    password_managment.view_pass()

    # Clean up
    os.remove(test_key_path)
    os.remove(test_file_path)

if __name__ == "__main__":
    test_write_key()
    test_add_and_view_pass()
    print("All tests passed!")
