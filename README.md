# RobotCDocs
![Preview Image](/Images/Preview_Image.png)

RobotCDocs is a tool developed for the purpose of attaching descriptions to user-defined functions in RobotC. 


# Table of contents

* [What it can do](#what-it-can-do)
* [How it works](#how-it-works)
* [How to use](#how-to-use)


## What it can do
### Scan / Parse Files
RobotCDocs recursively searches for any header (.h) or source (.c) files in a directory. Each individual header file will be scanned for comments detailing a declaration of a function or variable, like so:

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

### Custom Naming Schemes
By default, the documentation of a declaration will be listed under its file's name. This is seen in the above example, where Foo(parameter) is listed under the _Foo_ category. You can change the category of a declaration with the addition of `@`. In the code below, the addition of `@setup` means that the declaration will be listed under _Setup_, no matter what file it's in. As you can see, `setup` is automatically capitalized to `Setup`.
    
    FooLibrary / Foo.h - 

    /*
     * @setup
     *
     * Very important setup function.
    */
    void Init();


![Preview Image](/Images/Foo_Setup_Image.png)

## How it works
RobotC's function library descriptions are located in a file called `BuiltInVariables.txt` that get parsed at runtime. The contents of this file are the functions and variables you see in the function library of RobotC.

RobotCDocs allows you to add descriptions to any function or variable by writing the definition of it directly into `BuiltInVariables.txt`. The format of this function definition is similar to CSV. Here's a sample output of what RobotCDocs adds to `BuiltInVariables.txt`:

    Battery & Power Control,      Variables,          V2,            feat_NaturalLanguageInActive,           noFeatRest,                   F, A,   BackupBatteryLevel            //Returns the current voltage level of the VEX 


## How to use
### Configuring setup.txt
In `setup.txt`, you have to write your desired library name and a directory to be scanned:

    > Library Name
    [Desired Library Name]

    > Where to look for documentation files
    [Path to folder containing header files]
    
    > Where to output BuiltInVariables.txt
    [Path to RobotC folder containing BuiltInVariables.txt]


__Example__:

    > Library Name
    Diego's Custom Library

    > Where to look for documentation files
    C:\Users\user\Desktop\FooDocs

    > Where to output BuiltInVariables.txt
    C:\Program Files (x86)\Robomatter Inc\ROBOTC Development Environment 4.X\Includes


* __Library Name__ - The name of the custom library you want. All documentation will be inside it.
* __Where to look for files__ - A directory that contains header (.h) files. These files can be inside folders, if needed, and will be scanned for documentation.
* __Where to find BuiltInVariables.txt__ - The program folder of RobotC that contains `BuiltInVariables.txt`. This is needed to instantly write documentation down after RobotCDocs finishes.


### Running main.py
RobotCDocs has only been tested on Windows 10, and was written with python 3.7. To run in the console, simply type `python main.py` inside the root directory (assuming you installed python on your PATH).


### Format of Comments
RobotCDocs only parses multiline comments that precede a declaration of a function, and have an asterisk detailing the contents, such as below:

    /*
     * @Foo
     *
     * Here goes my description!
     * Here goes another sentence!
    */
    void NameOfFunction(); // Should be close to comment

Multiline comments that aren't preceding a declaration of a function or variable will be ignored, and a warning will be printed to the console. Same holds true for lines that don't have an asterisk, or don't have the correct number of spaces in them.

    /*
     * Foo.h
     *
     * This won't be parsed by RobotCDocs!
    */
    
    /*
     * This line will be parsed.
     This line won't be parsed.
       * This line won't be parsed.
    */
    task main();

Like previously mentioned, declarations with a custom category should have the name of the category right beside a `@`.

    /*
     * @setup
     *
     * Here goes my description!
    */
    void NameOfFunction(); // Should be close to comment

[Here](https://github.com/Desperationis/RobotCLibrary/blob/master/Helpers/Helpers.h) is a valid example listed inside RobotCLibrary.




