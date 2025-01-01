
key = Fernet.generate_key()
fernet = Fernet(key)

def add_pass(username, password):
    with open("./passwords.txt", "a") as f:
        #string => byte (encode)
        encrypted_pass = fernet.encrypt(password.encode()).decode() 
        f.write(f"{username}|{encrypted_pass}\n")
    print("ADDED!")
    
def view_pass():
    with open(f"./passwords.txt", "r") as f:
            for item in f:
                item = item.rstrip()
                username, encrypted_password = item.split("|")
                password = fernet.decrypt(encrypted_password).decode()
                print(f"USERNAME: {username} | PASSWORD: {password}")
            
    

while True:
    user_input = input("Enter the mood (v: view, a: add, q:quiet): ")
    
    if user_input == "v":
        print("Your passwords are as follows:")
        view_pass()
            
    
    elif user_input == "a":
        print("Let's add a new password.")
        
        username = input ("Enter your username: ")
        password = input ("Enter your password: ")
        
        add_pass (username, password)
        
    
    elif user_input == "q":
        break
    else:
        print("Wrong mode")    
        