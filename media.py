import webbrowser


class Video:
    """This class provides a way to store video related information shared by movies and tv shows."""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, production_company, box_art_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.production_company = production_company
        self.box_art_url = box_art_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)


class Movie(Video):
    """This class inherit from class Video and describes a movie."""

    def __init__(self, title, storyline, production_company, box_art_url, trailer_url, duration, box_office):
        Video.__init__(self, title, storyline, production_company, box_art_url, trailer_url)
        self.duration = duration
        self.box_office = box_office


class TvShow(Video):
    """This class inherit from class Video and describes a tv show."""

    def __init__(self, title, storyline, box_art_url, production_company, trailer_url,
                 episode_duration, number_of_seasons, number_of_episodes, is_ongoing):
        Video.__init__(self, title, storyline, production_company, box_art_url, trailer_url)
        self.episode_duration = episode_duration
        self.number_of_seasons = number_of_seasons
        self.number_of_episodes = number_of_episodes
        self.is_ongoing = is_ongoing # boolean
