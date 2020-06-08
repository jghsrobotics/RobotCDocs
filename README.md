# RobotCDocs
![Preview Image](/Images/Preview_Image.png)
RobotCDocs is a tool developed for the purpose of attaching descriptions to user-defined functions in RobotC. 


# Table of contents

* [What it can do](##what-it-can-do)
* [How it works](##how-it-works)
* [How to use](##how-to-use)


## What it can do
### Scan / Parse Files
RobotCDocs recursively searches for any header files in a directory. Each individual header file will be scanned for comments detailing a declaration of a function or variable, like so:

    FooLibrary / Foo.h - 

    /*
     * This function does some really cool stuff!
     * This sentence will be added to the ladder.
    */
    void Foo();

    /*
     * This function does some really cool stuff!
     * This sentence will be added to the ladder.
    */
    void Foo(int parameter);

    /*
     * A very cool variable!
    */
    bool testVariable;
   
![Preview Image](/Images/Foo_Image.png)

### Flag Setup Functions / Variables
Have setup functions or variables? By simply typing `[SETUP]` in any comment, the function or variable will be listed under `Setup`. 


    /*
     * [SETUP]
     *
     * Very important setup function.
    */
    void Init();


![Preview Image](/Images/Foo_Setup_Image.png)

## How it works
RobotC's function library descriptions are located in a file called `BuiltInVariables.txt` that get parsed at runtime. The contents of this file are the functions and variables you see in the function library of RobotC.

RobotCDocs allows you to add descriptions to any function or variable by writing the definition of it directly into `BuiltInVariables.txt`. The format of this function definition is similar to CSV. An example is included below. (You won't have to write at all in this dirty format, RobotCDocs does it for you)

    Battery & Power Control,      Variables,          V2,            feat_NaturalLanguageInActive,           noFeatRest,                   F, A,   BackupBatteryLevel            //Returns the current voltage level of the VEX 


## How to use
Using RobotCDocs is as easy as editing `setup.txt` and running `main.py`.

### Editing setup.txt
In `setup.txt`, you have to write your desired library name and a directory to be scanned:

    setup.txt - 
    > Library Name
    [Desired Library Name]

    > Where to look for files
    [Path to folder containing header files]
    
    > Where to find BuiltInVariables.txt
    [Path to RobotC folder containing BuiltInVariables.txt]


__Example__:

    setup.txt - 

    > Library Name
    Diego's Custom Library

    > Where to look for files
    C:\Users\user\Desktop\FooDocs

    > Where to find BuiltInVariables.txt
    C:\Program Files (x86)\Robomatter Inc\ROBOTC Development Environment 4.X\Includes


* __Library Name__ - The name of the custom library you want. All documentation will be inside it.
* __Where to look for files__ - A directory that contains header (.h) files. These files can be inside folders, if needed, and will be scanned for documentation.
* __Where to find BuiltInVariables.txt__ - The program folder of RobotC that contains `BuiltInVariables.txt`. This is needed to instantly write documentation down after RobotCDocs finishes.


### Running main.py
RobotCDocs has only been tested on Windows 10, and was written with python 3.7. To run in the console, simply type `python main.py` inside the root directory (assuming you installed python on your PATH). If unclear errors appear, be sure to report it in the issue tracker.


### Format of Comments

Each header file should have a multi-line comment detailing the contents of the file. This is __required__. The name of the file listed inside it will hold all the functions and declarations

    /*
     * Foo.h
     *
     * Here goes my description!
    */

As seen above, RobotCDocs only accepts multi-line comments that start each line with an asterisk with a space on each side. These comments should appear right above function or variable declarations.

    /*
     * Here goes my description!
    */
    void NameOfFunction(); // Should be close to comment

If the function should be listed under `Setup`, it should be formatted like so:

    /*
     * [SETUP]
     *
     * Here goes my description!
    */
    void NameOfFunction(); // Should be close to comment

[Here](https://github.com/Desperationis/RobotCLibrary/blob/master/Helpers/Helpers.h) is a valid example listed inside RobotCLibrary.




