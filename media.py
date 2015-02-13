import webbrowser

class Movie():
    def __init__(self, title, storyline, image, youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
