from media import Movie
import fresh_tomatoes


''' Create instances of Movie class '''

avatar = Movie('Avatar',
    'A marine on an alien planet',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=5PSNL1qE6VY',
    'Lightstorm Entertainment',
    'James Cameron',
    '161',
    '2.788 billion',
    '2009')

toy_story = Movie('Toy Story',
    'A story of a boy and his toys that come to life',
    'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',  # NOQA
    'https://www.youtube.com/watch?v=KYz2wyBy3kc',
    'Pixar',
    'John Lasseter',
    '81',
    '373.7 million',
    '1995')

frankenstein = Movie('Young Frankenstein',
    'The creation of a monster',
    'https://upload.wikimedia.org/wikipedia/en/b/b5/Young_Frankenstein_movie_poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=mOPTriLG5cU',
    '20th Century Fox',
    'Mel Brooks',
    '105',
    '86.2 million',
    '1974')

life_of_brian = Movie('Life of Brian',
    'A guy mistaken for Jesus',
    'https://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg',  # NOQA
    'https://www.youtube.com/watch?v=HxIlg4m5fns',
    'HandMade Films',
    'Monty Python',
    '93',
    '20 million',
    '1979')

zoolander = Movie('Zoolander',
    'An idiot male model saves the world',
    'https://upload.wikimedia.org/wikipedia/en/7/7c/Movie_poster_zoolander.jpg',  # NOQA
    'https://www.youtube.com/watch?v=YtQq0T3ExLs&t=1s',
    'Village Roadshow Pictures',
    'Ben Stiller',
    '89',
    '60 million',
    '2001')

spirited_away = Movie('Spirited Away',
    'A girl in the world of spirits',
    'https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG',  # NOQA
    'https://www.youtube.com/watch?v=ByXuk9QqQkk',
    'Studio Ghibli',
    'Hayao Miyazaki',
    '125',
    '289 million',
    '2001')

# Create a list of Movie objects
movies = [
    spirited_away,
    frankenstein,
    life_of_brian,
    zoolander,
    toy_story,
    avatar]

# Pass it to open_movies_page method  in fresh_tomatoes module
# Generate the html code and open the browser
# with the page populated with movies
fresh_tomatoes.open_movies_page(movies)
