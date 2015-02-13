import fresh_tomatoes
import media

movies = [
    {
    "title": "",
    "storyline": "",
    "image": "",
    "youtube_trailer": ""
    },
    {
    "title": "",
    "storyline": "",
    "image": "",
    "youtube_trailer": ""
    },
    {
    "title": "",
    "storyline": "",
    "image": "",
    "youtube_trailer": ""
    },
    {
    "title": "",
    "storyline": "",
    "image": "",
    "youtube_trailer": ""
    },
    {
    "title": "",
    "storyline": "",
    "image": "",
    "youtube_trailer": ""
    },
    {
    "title": "",
    "storyline": "",
    "image": "",
    "youtube_trailer": ""
    },
]

toy_story = media.Movie("Toy Story",
                        "A story",
                        "http://google.ro",
                        "https://www.youtube.com/watch?v=g2PMoUIQDCk")

fresh_tomatoes.open_movies_page([toy_story for i in range(5)])
