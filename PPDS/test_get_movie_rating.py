"""
Created on Oct 30 2026
@author Elizabeth Jasmi George

"""

from get_movie_rating import get_movie_rating, get_number_of_movies_with_a_rating
import pandas as pd


def test_get_movie_rating():

    # create a dictionary to populate the dummy data frame
    raw_data = {
        "movie_title": ["Bambi", "Dumbo", "Aristocats", "Pinocchio", "Mulan", "Frozen"],
        "rating": ["G", "", "PG", "PG-13  ", "R", "G"],
        "genre": ["adventure", "comedy", "Comedy", "Drama", "drama", "Drama"],
        "year": [1992, 1887, 1989, 1990, 2000, 2012],
    }
    # create a dummy dataframe from the dictionary named raw_data
    test_data_frame = pd.DataFrame.from_dict(raw_data)

    assert get_movie_rating(test_data_frame, "Bambi", "rating") == "G- General Audience"
    assert get_movie_rating(test_data_frame, "Moana", "rating") == "Movie not found"
    assert get_movie_rating(test_data_frame, "Dumbo", "rating") == "No Rating available"
    return


def test_get_number_of_movies_with_a_rating():

    # create a dictionary to populate the dummy data frame
    raw_data = {
        "movie_title": ["Bambi", "Dumbo", "Aristocats", "Pinocchio", "Mulan", "Frozen"],
        "rating": ["G", "", "PG", "PG-13  ", "R", "G"],
        "genre": ["adventure", "comedy", "Comedy", "Drama", "drama", "Drama"],
        "year": [1992, 1887, 1989, 1990, 2000, 2012],
    }
    # create a dummy dataframe from the dictionary named raw_data
    test_data_frame = pd.DataFrame.from_dict(raw_data)

    #
    assert get_number_of_movies_with_a_rating(test_data_frame, "rating") == 2
    assert get_number_of_movies_with_a_rating(test_data_frame, "rating", "G") == 2
    assert get_number_of_movies_with_a_rating(test_data_frame, "rating", "PG-13") == 1
    assert get_number_of_movies_with_a_rating(test_data_frame, "rating", "R") == 1

    return
