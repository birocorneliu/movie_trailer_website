"""This module incorporates Movie class"""
import webbrowser

class Movie(object):
    """Class Movie that creates movies entities.i

    Attributes:
        title (str): movie title
        storyline (str): movie storyline
        poster_image_url (str): url image of the movie
        trailer_youtube_url (str): url of youtube trailer
    """

    def __init__(self, title, storyline, image, youtube_trailer):
        """Movie constructor

        Args:
            title (str): movie title
            storyline (str): movie storyline
            image (str): url image of the movie
            youtube_trailer (str): url of youtube trailer
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        """Method that opens a webbrowser and youtube url"""
        webbrowser.open(self.trailer_youtube_url)
