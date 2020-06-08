# RobotCDocs
RobotCDocs is a tool developed for the purpose of attaching descriptions to user-defined functions in RobotC. 
![Preview Image](/Images/Preview_Image.png)

## How it works
RobotCDocs automatically searches for any header files in a root directory. Each individual header file will be scanned for comments detailing an instantiation of a function or variable, like so:

```
FooLibrary / Foo.h - 


/*
 * Foo.h
 * 
 * This file comment description is needed for the parser to work properly. All 
 * function and variable docs will be listed below the header's name.
*/

/*
 * This function does some really cool stuff!
 * This sentence be added to the ladder.
*/
void Foo();

/*
 * A very cool variable!
*/
bool testVariable;
```

![Preview Image](/Images/Foo_Image.png)
