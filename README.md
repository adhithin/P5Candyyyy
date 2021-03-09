# Arcade Smash 
The ultimate arcade for all your gaming purposes! 

## Goal 
A fast and easy way to play some great hit games. This will allow people to relax from a long day, and grab some coffee while having some fun. 

## Quick start guide

<a href="arcadesmash.tk"> Visit arcade smash here </a>

- Explore our multitide of games available for your leisure 

- Leave a rating and a review! 

## Key Technicals 

## CRUD 

we use the employment of CRUD, create, read, update, and delete. 

**EXTRA** 

Use of DB Browser for MySQLite
+ has all data 
+ can delete and update entries from here 
+ here is the <a href="https://sqlitebrowser.org/"> tool </a>

## Ratings and Reviews:

CREATE is used in our ratings and reviews. 

*when users add a review of the game. they include their name, a rating from 1-5, and a comment.* 

+ code for create is here <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L72"> from line 72 </a> of views.py

+ they can leave a rating and comment <a href="http://arcadesmash.tk/ratings"> here </a> on the site.


## SQL 


### Leaderboards: 

The leaderboards all capture the game score, and then queries it, along with the user's name, to the leaderboard, which is displayed afterward. 
+ sql table set up is here on <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L25"> line 25 </a> of views.py
+ users can enter leaderboard scores for the following games. code shows the form that queries information, runtime links show the site. 


code links | runtime links
------------ | -------------
<a href="https://github.com/adhithin/P5Candyyyy/blob/dc0d6f3ebbcc75716e3aac4ccc7ee05e0fa2fc5b/templates/game1-1.html#L177"> game1-1.html </a>| <a href="http://arcadesmash.tk/game1"> game 1 </a>
<a href="https://github.com/adhithin/P5Candyyyy/blob/be59a137e74922e5cf800dd6d3028ea90bb7048e/templates/game2.html#L167"> game2.html </a>| <a href="http://arcadesmash.tk/game2"> game 2 </a>
<a href="https://github.com/adhithin/P5Candyyyy/blob/be59a137e74922e5cf800dd6d3028ea90bb7048e/templates/game3.html#L577"> game3.html </a>| <a href="http://arcadesmash.tk/game3"> game 3 </a>
<a href="https://github.com/adhithin/P5Candyyyy/blob/3d12496aca3631c3f1677c7dc0697ceefeeebf5b/templates/game4.html#L228"> game4.html </a>| <a href="http://arcadesmash.tk/game4"> game 4 </a>
<a href="https://github.com/adhithin/P5Candyyyy/blob/3d12496aca3631c3f1677c7dc0697ceefeeebf5b/templates/game6.html#L226"> game6.html </a>| <a href="http://arcadesmash.tk/game6"> game 6 </a>

*note: there's no leaderboard for game 7 and game 8. we don't have a game 5. 

    

### Reviews and Ratings: 

Similar to the leaderboard, we set up a table for the reviews and ratings. Originally, this was just combined with the leaderboard, but since values and ideas were seperate, a new table was created <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L44"> here. </a>

## API 

We also use APIs in our game. In game1, the covid data tracking game, we use an API to import data regarding covid 19 statistics. 
+ game 1 <a href="https://github.com/adhithin/P5Candyyyy/blob/072e82e771ffbdd94cb5f88633ebd4dfeb007a82/templates/game1-1.html#L257"> api code </a>
+ game 1 <a href="http://arcadesmash.tk/game"> run time link </a>



