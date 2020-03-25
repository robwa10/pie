# 10: The Execution Context - Creation and Hoisting

The Execution Context is created in two phases.  

**The Creation Phase**  
In this phase as the parses runs through the code it recognizes where you have setup variables and functions. This step sets up memory space for variables and functions. This is confusionly called "Hoisting".  

This doesn't move code to the top of the page. The JS Engine sets aside memory space for the variables and functions you have written in your code. They exist in memory so when your code is executed line by line it can access them.  

__Function__  
The function in its entirety is placed into memory. It's name and the code inside the function.  

__Variables__  
In this example:  

```js
console.log(a)
const a = 'Hello World!'
```  

Assigments are set in the __Execution Phase__. In the Creation phase if a variable is referenced before it has been declared the value `undefined` is set to that variable. **All variables in JavaScript are initially set to undefined and functions are in memory in their entirety**.


# 11: Javascript and 'undefined'

`undefined` is a special value which means the value on the variable hasn't been set.

The Creation Phase of the Execution Context sets all variables to `undefined` when setting up the memory space.


# 13: Single Threaded, Synchronous Execution

> single threaded: one command at a time

> synchronous: one at a time and in order


# 14: Function Invocation and the Execution Stack

When you invoke a function an execution context is created and placed on the exection stack.


# 15: Functions, Context, and Variable Environments

> variable environment - where the variable lives and how they relate to each other in memory

Every Exectuion Context has it's own variable environment. This is better known as scope.


# 16: The Scope Chain
