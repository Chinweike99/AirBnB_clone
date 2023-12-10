This is a team project on were we build a clone of the AirBnB website,
using the concept of OOP and cmd module


AirBnB Clone Project
This project aims to build a functional clone of the popular vacation rental platform AirBnB. The project is designed to be modular and extensible, allowing for easy integration of new features and functionalities.

Command Interpreter
The project utilizes a command interpreter for managing various aspects of the platform. This interface allows users to:

Create and manage user accounts
List and manage properties
Search for available rentals
Make booking requests
Manage bookings
Getting Started

1. Starting the Command Interpreter:

Open a terminal window and navigate to the project root directory.
Run the command python3 console.py.
Or ./console.py

2. Using the Command Interpreter:

Create a user	User.create()
Print user instance count	User.count()
Print all users	User.all()
Print user with a specific id	User.show("user-id")
Update user record	User.update("user-id", "attribute", "value")
Update user record using a dictionary	User.update("user-id", {"attribute": "value"})
Delete a user by id	User.destroy("user-here")

Examples
$ ./console.py
(hbnb) create User
d4db9f83-73b4-41d6-9784-870dfd06b083
(hbnb)
(hbnb) User.create()
22833fda-7c79-4521-bfd1-a69b585c16a3
(hbnb) User.count()
2
(hbnb) User.show(22833fda-7c79-4521-bfd1-a69b585c16a3)
[User] (22833fda-7c79-4521-bfd1-a69b585c16a3) {'id': '22833fda-7c79-4521-bfd1-a69b585c16a3', 'created_at': datetime.datetime(2022, 10, 29, 11, 0, 31, 710814), 'updated_at': datetime.datetime(2022, 10, 29, 11, 0, 31, 711088)}
(hbnb) User.destroy(22833fda-7c79-4521-bfd1-a69b585c16a3)
(hbnb) User.count()
1
