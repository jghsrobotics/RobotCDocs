# RobotCDocs
RobotCDocs is a tool developed for the purpose of attaching descriptions to user-defined functions in RobotC. 
![Preview Image](/Images/Preview_Image.png)

## What it can do
RobotCDocs recursively searches for any header files in a root directory. Each individual header file will be scanned for comments detailing an instantiation of a function or variable, like so:

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

![Preview Image](/Images/Foo_Image.png)

Have setup functions or variables? By simply typing ```[SETUP]``` in any comment, the function or variable will be listed under ```Setup```. 


    /*
     * [SETUP]
     *
     * Very important setup function.
    */
    void Init();


![Preview Image](/Images/Foo_Setup_Image.png)

## How to use

Using RobotCDocs is as easy as editing ```setup.txt``` and running ```main.py```.

In ```setup.txt```, you have to write your desired library name and a directory to be scanned:

    setup.txt - 
    > Library Name
    [Desired Library Name]

    > Where to look for files
    [Path to folder containing header files]


__Example__:

    setup.txt - 

    > Library Name
    Diego's Custom Library

    > Where to look for files
    [Path to folder containing header files] C:\Users\user\Desktop\FooDocs










