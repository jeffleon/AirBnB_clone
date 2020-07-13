# Project: AirBnB clone - The console

Console for the AirBnB clone.
This repository contains the files for AirBnB clone - the console project.


# Description

The console project is the first step towards building the full web application project: The AirBnB clone.
The objective of this project is to make our console program. The program is limited to a specific use-case, having the following functionalities:

    Create a new object (objects: BaseModel, User, Amenity, City, Place, Review, State)
    Retrieve an object from a file, a json file, file.json is used
    Do operations on objects (count, show, destroy, all, update)
    Update attributes of an object
    Destroy an object


# How to start it

To start the console execute the 'console.py' file, use:

   ./console.py


# How to use it

To use the console you have to execute it first (check previous tip: how to start it) then in the console (check for the '(hbnb)' prompt) use the following commands:

    create  -	Creates a new instance of a class
    show    -	Print the string representation of an instance based on the class name
    destroy -	Deletes an instance based on the class name and id
    all     -	Print all string representation of all instances based or not on the class name
    update  -	Updates an instance based on the class name and id by adding or updating attribute
    help    -	Shows the help entry
    quit    -	Exit the console


# Examples

create <class_name>:

    (hbnb) create User

show <class_name>:

    (hbnb) show City

destroy <class_name> <object_id>:

    (hbnb) destroy Amenity 1234-1234-1234-1234-1234

all <class_name> or all:

    (hbnb) all Review
    or
    (hbnb) all

update <class_name> <object_id> <attribute_name> "<attribute_value>":

    (hbnb) update State 1234-1234-1234-1234-1234 name "Florida"


# By

* jeffleon
* SneyderHOL
