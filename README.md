0x00. AirBnB clone - The console

The Weight of this project is: 5

This Project to be done in teams of 2 people Lynda Ndidiamaka, ASAKWONYE COLLINS ONYEKACHI

This project started Feb 5, 2024 6:00 AM, must end by Feb 12, 2024 6:00 AM

The Checker for this project will be released at Feb 10, 2024 12:00 PM

This project is the first step towards building your first full web application the AirBnB clone

Develop a command-line interface for the Airbnb project's console, allowing users, such as the application's administrators, to modify or delete database entries. This functionality empowers administrators to manipulate various objects and data within the Airbnb clone application. The objects include:

Users

Places

States

Cities

Amenities

Reviews

Source Files

1. HBNHCommand: console.py

2. Amenity: models/amenity.py

3. BaseModel: models/base_model.py

4. City: models/city.py

5. models.init : models/init.py

6. Place: models/place.py

7. Review: models/review.py

8. State: models/state.py

9. User: models/user.py

10. FileStorage: models/engine/file_storage.py

11. engine.init: models/engine/init.py

Setting up the system

To use this console, it is necessary to possess:

1. Linux ubuntu 14.04.3 LTS or higger

2. Python 3.7 or higger

Executing the command interpreter can be achieved by following these steps:

1. $ ./console.py

Illustrative instances

Interactive mode:

$ ./console.py

(hbnb) help

Commands with documented information (enter help <topic>):

EOF  help  quit

(hbnb)

(hbnb)

(hbnb) quit

$

Non-interactive mode:

$ echo "help" | ./console.py

(hbnb)

Commands with documented information (enter help <topic>):
========================================

EOF  help  quit
(hbnb) 

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF  help  quit

(hbnb)

$

Necessary conditions or prerequisites

Python Scripts

Allowed editors: vi, vim, emacs

All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

A README.md file, at the root of the folder of the project, is mandatory

Your code should use the PEP 8 style (version 1.7 or more)

All your files must be executable

The length of your files will be tested using wc

All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__
("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

This AirBnB_clone Project was done by Asakwonye Collins Onyekachi and Lynda Ndidiamaka
