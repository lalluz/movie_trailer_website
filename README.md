# Movie Trailer Website
A [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) project.  
A little server-side Python application to show movie related information.

### What it Does
This application generates a web page showing a number of movies, each one with poster, 
link to YouTube trailer and other related information.

### Project Contents

This project contains the following files:
* media.py - it defines the class Movie that stores movie information.
* entertainment_center.py - it creates instances of the Movie object and 
pass them as a list to the HTML generator function defined in the module fresh_tomatoes.py.
* fresh_tomatoes.py - starter code provided by Udacity. It contains the HTML 
code that actually creates the structure of the web page along with the function 
that populates the page with Movie objects defined in entertainent_center.py.

### Requirements
 This project is in Python 3.5, but it's quite simple and it will work 
 also with Python 2.7 and Python 3.6.
 
### How to Run it
Download the project zip file and unzip it. 
Or clone this repository:
` https://github.com/lalluz/movie_trailer_website.git `
In your terminal navigate to the project directory and type:
` python entertainment_center.py `

Your default browser should open the Movie Trailer Website.

Hit ` CTRL+C ` to exit the process.

### Licence
No license for this project, feel free to use it.