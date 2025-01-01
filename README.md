# Password Manager

A simple and secure Python-based password manager that encrypts passwords using the `cryptography` library. This project allows users to add and view encrypted passwords stored in a file.

## Features
- **Password Encryption**: Ensures passwords are stored securely using `Fernet` encryption.
- **Key Management**: Generates and securely stores an encryption key.
- **User-Friendly Interface**: Easy-to-use terminal-based interface.

## Requirements
- Python 3.8+
- `cryptography` library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/password-manager.git
   cd password-manager
Install dependencies:

bash
Copy code
pip install cryptography
Generate an encryption key (run this once):

python
Copy code
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("mykey.key", "wb") as key_file:
    key_file.write(key)
Usage
Run the script:

bash
Copy code
python password_manager.py
Choose from the following options:

### Add Password: Save a new username-password pair.
### View Passwords: View all stored passwords (decrypted).
### Quit: Exit the program.

# Test
Run the test script to ensure everything works as expected:

bash
Copy code
python test_password_manager.py
File Structure
bash
Copy code

<img width="497" alt="Screenshot 2025-01-01 at 10 56 06 AM" src="https://github.com/user-attachments/assets/15871e64-a55f-4c1e-b335-aa59cb0e9118" />

# Security Notes
The encryption key (mykey.key) is critical to decrypt passwords. Keep it secure and do not share it.
If the key is lost, all stored passwords will be irretrievable.
Ensure passwords.txt is stored in a secure location with restricted access.
Future Enhancements
Add a GUI for a better user experience.
Implement password validation and strength checks.
Add support for password generation.

# License
MIT License

