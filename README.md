# Project_3
 Recursion and basic GUI's

Design: My team and I decided to design a program that's a disc golf simulator. There are a few complex objects that we have come up with, such as course, disk, trees, wind, basket, person.

Object Design:

Disk:
    Disks can be either a putter, mid-range, or driver.
    Attributes:
        Turn: (Negative numbers to +1) disk tendency to turn right during initial part of flight
        Fade: (0-5) tendency to turn left during backhand throw and right during forehand throw
        Glide: (1-7) how well disk maintains lift and stays in air
        Speed: (1-14) how fast the disk needs to be thrown to maintain optimal flight

Trees: 
    Attributes:
        Size: Size of tree
        Location: Coordinates of the tree on the course

Wind: 
    Attributes: 
        Speed: How fast the wind is blowing
        Direction: Direction of the wind

Basket: 
    Attributes:
        Basket Number:(1-18) basket hole number on the course 
        Location: Coordinates of the basket on the course

Person:
    Attributes:
        Name:
        Throw Type: (Backhand or forehand) type of throw
        Throw Speed: How fast the disk is thrown
        Throw Direction: Direction the disk is thrown

Course:
    Course contains all the objects. 
    Attributes:
        Par Number: Used for scoring system
        Trees: Tree object(s)
        Basket: Basket object
        Wind: Wind object
        Person: Person object
        Disk: Disk object(s)

Object Relationships

    Course:
        Contains all objects
    
    Person:
        Interacts with disk object. Disk objects are thrown with different speed, direction and throw type

    Disk: 
        Interacts with person.
        Interacts with tree.Tree is an obstacle.
        Interacts with wind. Wind affects direction and speed of disk.
        Interacts with basket. Current course is complete when disk enters basket.
    
    Basket: 
        Interacts with disk.

    Wind: 
        Interacts with disk.

    Trees:
        Interacts with disk.
        

I was assigned the Person and Basket objects for this project.