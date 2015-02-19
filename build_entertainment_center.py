"""This module imports Movie class, a json to build several Movie entities and
fresh_tomatoes module to build the html
"""
import json
import os

import fresh_tomatoes
from media import Movie


dir_path = os.path.dirname(os.path.realpath(__file__))
json_path = "{}/movies.json".format(dir_path)
with open(json_path) as file_obj:
    movies_json = json.load(file_obj)


movies = [Movie(**movie) for movie in movies_json]
fresh_tomatoes.open_movies_page(movies)
