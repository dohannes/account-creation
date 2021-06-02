users = {"User": [], "Password": [], "user-count": 0} #creation of dictionary 
class create_account:
	def append(self):
		users["User"].append(self.username)
		users["Password"].append(self.password)
		users["user-count"] += 1

	def __init__(self, username, password):
		self.username = username
		self.password = password
		create_account.append(self)
while True:
	x = input("Create | Show | Exit\n").lower()
	if x.isalpha():
		if x == "create":
			print("--Create Account--")
			u = input("Create Username: ")
			while u in users["User"]: #this while loop checks if the username has already been taken
				for i in users["User"]:
					if i == u:
						print("Username already taken!")
						u = input("Create Username: ")
			p = input("Create Password: ")
			account = create_account(u, p)
			print(f"--Account Creation Successful--\nUnder Username: {u}")
		elif x == "show":
			if users["user-count"] == 0:
				print("There are no accounts given...")
			else:
				u = input("Find User: ")
				for i in users["User"]: #this loop finds the password attached to the username given in var u
					if i == u:
						print(f'Password: {str(users["Password"][users["User"].index(i)])}') #checks password for user in index i(u)
		elif x == "exit":
			print("Cya next time!")
			break
		else:
			print("Command doesn't exist!")
	elif x.isdigit():
		print("Please try again!")
	else:
		print("Command doesn't exist!")