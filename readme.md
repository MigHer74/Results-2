# Results v2.0

This program is the second version of my first program in Python; the main idea is to obtain how many times a number is repeating in a list of 36 and 108 numbers.

I based the idea in the results of a local lottery who play every week, so each list is the result of the winner combination.

After enter the data of each week, the program gives the numbers who has 2, 3, 4 and 5 or more repetitions separately in the shorter version of the game (36 numbers version) and in the long version of the game with 108 numbers the program gives the numbers who has 3, 4, 5 and 6 or more repetitions.

The file named "main.py" is the launcher program, the file named "minis.py" contains the functions of the main program and the file named "dbaction.py" contains the functions for the database actions.

Instead of using 2 txt files storing the results of the last 6 weeks, I use a database named "results2.db" with a table named "games" contains all de numbers of the 2 types of games. This database has created in SQLite.

I'm using lists, tuples and statements if, elif and for.

The program is still growing, so I'm going to still update the progress.
  

## Project Files
- readme.md   | Readme file.
- main.py     | Main Program.
- minis.py    | General program functions.
- dbaction.py | Functions that interact with the database
- results2.db | Database file.


## Project Directories
There are no directories at this moment.
  
  
> **If you think education is expensive, try ignorance. - Derek Bok**