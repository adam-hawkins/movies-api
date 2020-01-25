# Movie Service
A repo for movie details

## Get all movies
### Definition
```
GET /movies
```
### Response

`200 OK` on success

```json
[
    {
        "id": "b92fdae2-3a8c-11ea-9f6d-38f9d36e1234",
        "title": "Star Wars Episode IV: A New Hope",
        "format": "VHS",
        "length": 121,
        "release_year": 1977,
        "rating": 5
    },
    {
        "id": "b92fdae2-3a8c-11ea-9f6d-38f9d36e1235",
        "title": "Star Wars Episod V: Empire Strikes Back",
        "format": "VHS",
        "length": 124,
        "release_year": 1980,
        "rating": 5
    }
    {
        "id": "b92fdae2-3a8c-11ea-9f6d-38f9d36e1236",
        "title": "Star Wars Episod VI: Return of the Jedi",
        "format": "VHS",
        "length": 132,
        "release_year": 1983,
        "rating": 5
    }
]
```

## Add new movie
### Definition
```
POST /movies
```
If a movie with the same title already exists, the existing movie will be overwritten

### Response
`201 Created` on success

## Look up a single movie
```
GET /movie/<id>
```
### Response
`404 Not Found` if the movie does not exist

`200 OK` on success
```json
{
    "id": "b92fdae2-3a8c-11ea-9f6d-38f9d36e1231",
    "title": "Iron Man",
    "format": "DVD",
    "length": 125,
    "release_year": 2008,
    "rating": 5
}
```

## Delete a movie
### Definition
```
DELETE /movie/<id>
```

### Response
`404 Not Found` if the movie does not exist

`204 No Content` on success

