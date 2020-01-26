import json

from movie_model import MovieModel
from utils.response import response


def movie_list(event, context):
    # fetch all todos from the database
    results = MovieModel.scan()

    # create a response
    return response(200, {'items': [dict(result) for result in results]})
