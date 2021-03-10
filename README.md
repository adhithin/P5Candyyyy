
# Arcade Smash 
The ultimate arcade for all your gaming purposes! 

## Key Terms 

- [x] **PYTHON**
- [x] **SQL**
- [x] **CRUD**
- [x] **CSS** 
- [x] **HTML**
- [x] **APIs**
- [x] **JAVA GAMES**
- [x] **JINJA**


## Goals 
A fast and easy way to play some great hit games. This will allow people to relax from a long day, and grab some coffee while having some fun. 

## Quick start guide

<a href="arcadesmash.tk"> Visit arcade smash here </a>

- **You'll land on the home page:**
 
<img width="500" alt="Screen Shot 2021-03-09 at 3 29 33 PM" src="https://user-images.githubusercontent.com/71796291/110552485-47ca2780-80ec-11eb-9cb2-e8f8e7afb245.png">

- **If you click GAMES at the top, you can find all of our games:**

<img width="500" alt="Screen Shot 2021-03-09 at 3 32 01 PM" src="https://user-images.githubusercontent.com/71796291/110552668-9b3c7580-80ec-11eb-9e37-fb26e8029482.png">

- **If you click ABOUT, it'll give you information, and the ratings for the game:**

<img width="500" alt="Screen Shot 2021-03-09 at 3 35 23 PM" src="https://user-images.githubusercontent.com/71796291/110552984-13a33680-80ed-11eb-89cf-bfa603223de5.png">

- **If you click BEGIN, the page will take you to tips. "Let's Start" will take you to the GAMES section. "Back to top" will take user to top. **

<img width="500" alt="Screen Shot 2021-03-09 at 3 36 07 PM" src="https://user-images.githubusercontent.com/71796291/110553029-2ddd1480-80ed-11eb-80ca-cb18815a7410.png">

# Key Technicals 

## CRUD 

we use the employment of CRUD, create, read, update, and delete. 

   **Tech Talk** February 3rd on <a href="http://nighthawkcoders.cf/pythondb/#FE-HTML"> CRUD models </a> on the nighthawk page. 

**EXTRA** 

Use of DB Browser for MySQLite
+ has all data 
+ can delete and update entries from here 
+ here is the <a href="https://sqlitebrowser.org/"> tool </a>

### Ratings and Reviews:

CREATE is used in our ratings and reviews. 

*when users add a review of the game. they include their name, a rating from 1-5, and a comment.* 

+ code for create in python is here <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L72"> from line 72 </a> of views.py

+ they can leave a rating and comment <a href="http://arcadesmash.tk/ratings"> here </a> on the site.

+ html form code for ratings is <a href="http://arcadesmash.tk/ratings"> here. </a> 

+ linked to the page and the table is printed with <a href="https://github.com/adhithin/P5Candyyyy/blob/5398498b014be5c8dc643293fb95ec014efca0ad/templates/ratings.html#L61">  **JINJA** </a> 


### Leaderboard:

CREATE is also used here. 

*once users play, they can log their score into the leaderboard* 

+ code for create in python is here <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L209"> from line 72 </a> of views.py

+ game 6 <a href="http://arcadesmash.tk/game6"> example </a> on the site.

+ <a href="https://github.com/adhithin/P5Candyyyy/blob/b63a9537f7164f4a7fd172c88edf0086116e7cbb/templates/game6.html#L226"> html form code </a> for game 6 

+ linked to the page and the table is printed with <a href="https://github.com/adhithin/P5Candyyyy/blob/5398498b014be5c8dc643293fb95ec014efca0ad/templates/game6.html#L248">  **JINJA** </a> 

## SQL 



### Leaderboards: 

   **Tech Talk** 
   February 17th Ms. Trish and assistance 

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

***notes:***
+ there's no leaderboard for game 7 and game 8
+ we don't have a game 5   

### Reviews and Ratings: 

Similar to the leaderboard, we set up a table for the reviews and ratings.
+ reviews and ratings table set up <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L44"> here. </a>
+ the live <a href="http://arcadesmash.tk/ratings">running site </a>

## API 

   **TECH TALK** 
   January 20th Flask/Python Review with <a href="http://nighthawkcoders.cf/restapi/"> API example </a> on nighthawk coding page. 

We also use APIs in our game. In game1, the covid data tracking game, we use an API to import data regarding covid 19 statistics. 
+ game 1 <a href="https://github.com/adhithin/P5Candyyyy/blob/072e82e771ffbdd94cb5f88633ebd4dfeb007a82/templates/game1-1.html#L257"> api code </a>
+ game 1 <a href="http://arcadesmash.tk/game"> run time link </a>

## CSS and HTML 

  **Tech Talk**
  Ms. Trish and assistance 

### Game 7 

+ uses and imports <a href="https://github.com/adhithin/P5Candyyyy/blob/main/static/css/gems.css"> gems.css </a> into html 
+ <a href="https://github.com/adhithin/P5Candyyyy/blob/f12b012ac85e7ec13e19ce6c090274cea7f5ad81/templates/game7.html#L9"> this line </a> imports the css into game 7 and the game's html code 

### Game 8 

+ uses and imports <a href="https://github.com/adhithin/P5Candyyyy/blob/main/static/css/dragon.css"> dragon.css </a> into html 
+ <a href="https://github.com/adhithin/P5Candyyyy/blob/f12b012ac85e7ec13e19ce6c090274cea7f5ad81/templates/game8.html#L6"> this line </a> imports the css into game 8 and the game's html code 


## JAVA GAMES

Some games in the arcade employ the use of Java. 

+ <a href="https://github.com/adhithin/P5Candyyyy/blob/5398498b014be5c8dc643293fb95ec014efca0ad/templates/game1-1.html#L2052"> Game 1 </a>

+ <a href="https://github.com/adhithin/P5Candyyyy/blob/5398498b014be5c8dc643293fb95ec014efca0ad/templates/game2.html#L196"> Game 2 </a>

+ <a href="https://github.com/adhithin/P5Candyyyy/blob/5398498b014be5c8dc643293fb95ec014efca0ad/templates/game4.html#L65"> Game 4 </a>

+ <a href="https://github.com/adhithin/P5Candyyyy/blob/5398498b014be5c8dc643293fb95ec014efca0ad/templates/game6.html#L62"> Game 6 </a>

+ <a href="https://github.com/adhithin/P5Candyyyy/blob/5398498b014be5c8dc643293fb95ec014efca0ad/templates/game7.html#L28"> Game 7 </a>

+ <a href="https://github.com/adhithin/P5Candyyyy/blob/f12b012ac85e7ec13e19ce6c090274cea7f5ad81/templates/game8.html#L22"> Game 8 </a>



  



