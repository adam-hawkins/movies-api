from pynamodb.exceptions import DoesNotExist, DeleteError
from movie_model import MovieModel
from utils.response import response


def delete(event, context):
    print(event)
    try:
        found_movie = MovieModel.get(hash_key=event['path']['id'])
    except DoesNotExist:
        return response(404, {'error_message': 'Movie was not found'})
    try:
        found_movie.delete()
    except DeleteError:
        return response(400, {'error_message': 'Unable to delete the movie'})

    # create a response
    return response(204)
