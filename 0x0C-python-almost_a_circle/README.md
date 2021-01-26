# Models

## Base class:
- Manages id attribute for subclasses
- Manages json serialization/deserialization for subclasses
- Manages CSV serialization/deserialization for subclasses
- Manages storing instances to and loading from json or CSV files
- Create method allows instance creation from a dictionary

## Rectangle class:
- Inherits from base class
- Initializes rectangle instances
- Getters and setters for private attributes
- Area calculation method
- Display method prints rectangle instance to stdout using #s
- __str__ method for pretty printing
- Update method with either no-keyword arguments and key-worded arguments
- To_dictionary method returns a dictionary representation of a rectangle

## Square class:
- Inherits from rectangle class
- Initializes square instances
- Getter and setter for size attribute (sets width and height of rectangle to the same value)
- __str__ method for pretty printing
- Update method similar to rectangle class
- To_dictionary method similar to rectangle class

# Tests

## Test_models:
- Unittests for each model
- Tests validation and/or output for each method in each model

# A project to review and learn some Python concepts:
- Import
- Exceptions
- Class
- Private attribute
- Getter and Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read and Write file
- `args` and `kwargs`
- Serialization and Deserialization
- JSON
