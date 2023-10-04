import json

class MysqlDatabases:
    def __init__(self):
        with open('users.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.users = json.loads(text)
    
    def verify_login(self, email, password):
        for user in self.users:
            if email == user['email']: 
                if password == user['password']:
                    return True, "Login successful!"
                else:
                    return False, "Login failed! Invalid password!"
        return False, "Login failed! Invalid username!"
    
    def create_newuser(self, name, email, password):
        for user in self.users:
            if email == user['email']:
                return False, "User already exists. Please login instead."
        
        # Generate a unique student ID
        student_id = str(len(self.users) + 1).zfill(6)

        # Create a new user
        new_user = {
            "name": name,
            "email": email,
            "password": password,
            "student_id": student_id,
            "subjects": [],
            "role": "student"  # Assign the role of "student" by default
        }

        # Add the new user to the users list
        self.users.append(new_user)

        # Save the users list to the users.json file
        with open('users.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(self.users))

        return True, "Registration successful!"
    
db = MysqlDatabases()

if __name__ == '__main__':
   print(db.verify_login('sherlock.zhao@university.com', '123456'))