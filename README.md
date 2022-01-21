# Mars 🚀
#### Save and load values magically 🪄
Mars is a lightweight config parser that aims to be simple and understandable

### What can this do?
- Save and load data from a file 🗄
- Save files in Plist 🍎
- Save files in JSON 🪐

## Quick Guide
```python
import mars # Import Mars
conf = mars.generate("fileName.json", mars.types.json) # Set the path of the save file and the save file type
var1 = mars.element("var1", True, conf) # Define the var
var1.set("Hello!") # Change the value
var1.get() # Get the value
```

If you run the following code you're going to notice that the value Is saved, under the key name `var1`:
```python
import mars # Import Mars
conf = mars.generate("fileName.json", mars.types.json) # Set the path of the save file
var1 = mars.element("var1", True, conf) # Define the var
var1.get() # Get the value
```
You should get `"Hello!"`

## Usage
1. `mars.generate("path", mars.types.SOME_TYPE)`
2. `mars.element("key", "default_value", genData)`
3. `mars.element.get()` -> Return the value of the variable.
You could also call the class to get the value.
4. `mars.element.set("value")` -> Set the value of the variable.

### Types
There are the following types
1. `mars.types.json`
2. `mars.types.plist` **(NoneType is not suported by plistlib)**

## Installation
That's a good question...
1. Simply, copy `mars` to your projects directory and import it.

Or maybe you could...
1. Generate a wheel and install it.

**And it's done! 🎉**
