# RobotCDocs
RobotCDocs is a tool developed for the purpose of attaching descriptions to user-defined functions in RobotC. 
![Preview Image](/Images/Preview_Image.png)

## What it can do
RobotCDocs recursively searches for any header files in a root directory. Each individual header file will be scanned for comments detailing an instantiation of a function or variable, like so:

```
FooLibrary / Foo.h - 

/*
 * This function does some really cool stuff!
 * This sentence will be added to the ladder.
*/
void Foo();

/*
 * A very cool variable!
*/
bool testVariable;
```
Here's how it would look like in the RobotC function library after running RobotCDocs:
![Preview Image](/Images/Foo_Image.png)
Cool Right?
