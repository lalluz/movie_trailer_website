import webbrowser


class Movie:
    """ This class provides a way to store movie related information.

    Attributes:
        title (str): the movie title
        storyline (str): a short description of the movie
        box_art_url (str): a url to a poster image
        trailer_url (str): a url to a youtube trailer video
        production_company (str): the production company name
        director (str): the director full name
        duration (str): the duration in minutes
        box_office (str): the amount of money raised by ticket sales in dollars
        year (str): the release year

    """

    def __init__(self, title, storyline, box_art_url, trailer_url,
                 production_company, director, duration, box_office, year):
        """ Init Movie class """
        self.title = title
        self.storyline = storyline
        self.box_art_url = box_art_url
        self.trailer_url = trailer_url
        self.production_company = production_company
        self.director = director
        self.duration = duration
        self.box_office = box_office
        self.year = year

    def show_trailer(self):
        """ Open the browser at the youtube trailer url. """
        webbrowser.open(self.trailer_url)
