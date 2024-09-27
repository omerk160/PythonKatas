def get_movie_review(reviews, movie):
    """
    Returns a review on a given movie. If a movie review is not present, return 'Unknown movie.'.
    """

    # fixme
    return reviews['movie']


movie_reviews = {
    'Inception': 'Excellent movie with a mind-bending plot.',
    'Titanic': 'A classic love story with a tragic end.',
    'Avengers': 'Action-packed superhero movie with stunning visuals.'
}

result = get_movie_review(movie_reviews, 'Titanic')
print(result)  # A classic love story with a tragic end. expected

result = get_movie_review(movie_reviews, 'Avatar')
print(result)  # Unknown movie. expected

"""
To complete this exercise:
--------------------------
Fix the 'get_movie_review' function to return the review for the given movie from the 'reviews' dictionary.
If the movie is not present in the dictionary, return 'Unknown movie.' instead.


Exercise Breakdown:
-------------
In Python, you can use the `dict.get()` method to retrieve the value associated with a specified key from a dictionary. 
This method allows you to specify a default value to return if the key is not found.

value = dictionary.get(key, default_value)

Using `dict.get()` helps avoid `KeyError` and provides a default value if the key is not found.
"""
