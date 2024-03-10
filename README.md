# HBNB - The Console

Welcome to HBNB, a student project aiming to build a clone of the AirBnB website. In this initial stage, we've implemented a backend interface, known as the console, allowing users to manage program data. The console supports commands for creating, updating, and destroying objects, as well as managing file storage through JSON serialization/deserialization, ensuring persistent data between sessions.

## Project Structure

The repository is organized based on different tasks related to the project. Each task is associated with specific files, providing a structured approach to the development process.

### Project Tasks and Files
1. **Authors/README File**
    - **AUTHORS**: Lists project authors
2. **Pep8**
    - All code is PEP8 compliant.
3. **Unit Testing**
    - **/tests**: Contains unit tests for all class-defining modules.
4. **Make BaseModel**
    - **/models/base_model.py**: Defines a parent class to be inherited by all model classes.
5. **Update BaseModel w/ kwargs**
    - **/models/base_model.py**: Adds functionality to recreate an instance from a dictionary representation.
6. **Create FileStorage class**
    - **/models/engine/file_storage.py, /models/__init__.py, /models/base_model.py**: Defines a class to manage persistent file storage.
7. **Console 0.0.1**
    - **console.py**: Adds basic functionality to the console program, allowing it to quit, handle empty lines, and ^D.
8. **Console 0.1**
    - **console.py**: Updates the console with methods allowing the user to create, destroy, show, and update stored data.
9. **Create User class**
    - **console.py, /models/engine/file_storage.py, /models/user.py**: Dynamically implements a user class.
10. **More Classes**
    - **/models/user.py, /models/place.py, /models/city.py, /models/amenity.py, /models/state.py, /models/review.py**: Dynamically implements more classes.
11. **Console 1.0**
    - **console.py, /models/engine/file_storage.py**: Updates the console and file storage system to work dynamically with all classes.

## General Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/Amineafilal/AirBnB_clone.git
    ```

2. Navigate to the "console.py" file and run it:

    ```bash
    ./console.py
    ```

    This command will open the HBNB console, indicated by the prompt `(hbnb)`.

## Console Commands

The HBNB console supports various commands for managing objects and file storage. Here are some key commands:

- **create**: Creates an instance based on a given class.
- **destroy**: Destroys an object based on class and UUID.
- **show**: Shows an object based on class and UUID.
- **all**: Shows all objects the program has access to, or all objects of a given class.
- **update**: Updates existing attributes of an object based on class name and UUID.
- **quit**: Exits the program (EOF will as well).

### Alternative Syntax

Users can issue commands using an alternative syntax:

- **Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])**

Advanced syntax is implemented for specific commands:

- **all**: Shows all objects the program has access to, or all objects of a given class.
- **count**: Returns the number of object instances by class.
- **show**: Shows an object based on class and UUID.
- **destroy**: Destroys an object based on class and UUID.
- **update**: Updates existing attributes of an object based on class name and UUID.

## Examples

### Primary Command Syntax

#### Example 1: Create an Object
```bash
(hbnb) create BaseModel
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
```

#### Example 2: Show an Object
```bash
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
```

#### Example 3: Destroy an Object
```bash
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)
```

#### Example 4: Update an Object
```bash
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```

### Alternative Syntax

#### Example 1: Show all User Objects
```bash
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}",
"[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 2:

 Destroy a User
```bash
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
[]
```

#### Example 3: Update User (by attribute)
```bash
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 4: Update User (by dictionary)
```bash
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

Feel free to explore more commands and features within the HBNB console!

## Contributors
- List of project authors can be found in the [AUTHORS](AUTHORS) file.

## Acknowledgments
- Thanks to the AirBnB website for providing inspiration for this project.
