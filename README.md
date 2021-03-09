# Arcade Smash 
The ultimate arcade for all your gaming purposes! 

## Goal 
A fast and easy way to play some great hit games. This will allow people to relax from a long day, and grab some coffee while having some fun. 

## Quick start guide

<a href="arcadesmash.tk"> Get onto arcade smash here </a>

- Explore our multitide of games available for your leisure 

- Leave a rating and a review! 

## Key Technicals 

### CRUD 

we use the employment of CRUD as a DATABASE. 

### Ratings and Reviews:

CREATE is used in our ratings and reviews. 

*when users add a review of the game. they include their name, a rating from 1-5, and a comment.* 

+ code for create is here <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L72"> from line 72 </a> of views.py

+ they can leave a rating and comment <a href="http://arcadesmash.tk/ratings"> here </a> on the site.


### SQL 

We use SQL databases to capture data. In our arcade, we use the employment of two tables: one for the game leaderboards, as well as one for the reviews and ratings. 

#### Leaderboards: 

The leaderboards all capture the game score, and then queries it, along with the user's name, to the leaderboard, which is displayed afterward. 
<a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L25"> link to code - this sets up the Scores table </a>

#### Reviews and Ratings: 

Similar to the leaderboard, we set up a table for the reviews and ratings. Originally, this was just coombined with the leaderboard, but since values and ideas were seperate, a new table was created <a href="https://github.com/adhithin/P5Candyyyy/blob/2cd317c8a0bb2203be14b4b2d60d673801f3fff6/views.py#L44"> here. </a>

### API 

We also use APIs in our game. In game1, the covid data tracking game, we use an API to import data regarding covid 19 statistics. 


