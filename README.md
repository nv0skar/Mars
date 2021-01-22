# Mars
#### Save and load variables magically 🪄

### What can this do?
- Save and load variables from a file 🗄
- Save files in JSON 🪐

## Quick Guide
```
import mars # Import Mars
conf = mars.object("fileName.json") # Set the path to the save file
var1 = mars.mars("var1", True, conf) # Define the var
var1.set("Hello!") # Change the value
var1.get() # Get the value
```
If you run the following code you're going to nottice that the value Is saved, under the key name:

```
import mars # Import Mars
conf = mars.object("fileName.json") # Set the path to the save file
var1 = mars.mars("var1", True, conf) # Define the var
var1.get() # Get the value
```
You're going to get `"Hello!"`

## Explanation
1. `mars.object("path")` -> Here you have to define the path of the file to save and load the variables.
2. `mars.mars("key", "default_value", object)`
- In the first argument you have to define the key name. The key name Is the identification of the variable inside of the save file
- In the second argument you have to define the default value of the variable.
- In the third argument you have to return `mars.object()` to specify the path.
3. `mars.mars.get()` -> This Is going to return the value of the variable.
4. `mars.mars.set("value")` -> This Is going to set the value of the variable.

## Installation
That's a good question...
1. Firstly you have to copy `mars` and import it.\
#### And you're done! 😂