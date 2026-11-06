"""
Created on Oct 30 2026
@author Elizabeth Jasmi George

"""

import pandas as pd


def get_movie_rating(data, movie_title, column_name):
    """
    A function to get the rating for the movie availalble from the given column_name
    and return the description

    parameters
    ---------
    data: dataframe
    pandas data frame which contains the details of the movie

    movie_title:str
    Name of the movie

    columb_name: str
    the name of the column which has the ratings for movies

    returns
    -------
    rating_description: str
    The string with the rating code and explanation of that code

    raises
    ------
    Type error: if data argument is not of type dateframe

    example
    -------
    get_movie_rating(Disney_total_gross_grouped_by_year,"Aladdin", "MPAA_rating")
    >>> "G- General Audience"
    """

    # checks if the passed data is of type dataframe
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    assert column_name in data.columns, "column is not present in the data frame"
    assert isinstance(movie_title, str), "movie title is not of type string"
    assert movie_title != "", "title cannot be empty"

    # get the rating from the dataframe for the given movie
    row = data[data["movie_title"] == movie_title]
    if row.empty:
        return "Movie not found"
    else:
        rating = row[column_name].iloc[0]

    # remove any leading and trailing spaces from the rating
    rating = rating.strip()

    if rating == "":
        return "No Rating available"
    elif rating == "G":
        return "G- General Audience"
    elif rating == "PG":
        return "PG- parental guidance"
    elif rating == "PG-13":
        return "PG-13- Parents Strongly Cautioned"
    elif rating == "R":
        return "R- Restricted"
    else:
        return rating

    return rating


def get_number_of_movies_with_a_rating(
    movie_dataframe, rating_column, rating_to_find="G"
):
    """
    A function to return the number of movies in the data frame with a rating 'rating_to_find'

    input
    -----
    movie_dataframe: dataframe
    The dataframe from which to obtain the count

    rating_column: str
    The column name which has ratings

    rating_to_find: str, optional, default value is "G"
    The particular rating for which we want the count of movies with that rating

    returns
    -------
    movie_count: int
    The number of movies in the dataframe with a 'rating_to_find' rating

    raises
    ------
    Type Error: if movie_dataframe argument is not of type dateframe

    examples
    -------
    number_of_movies_with_a_rating(data,"MPAA_rating","PG-13")
    >>>145

    >>>number_of_movies_with_a_rating(data,"MPAA_rating","G")
    >>>86

    """
    if not isinstance(movie_dataframe, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    assert (
        rating_column in movie_dataframe.columns
    ), "column is not present in the data frame"
    assert isinstance(
        rating_to_find, str
    ), "rating given as parameter is not of type string"

    # read the data frame and group by the rating column
    grouped_result = movie_dataframe.groupby(rating_column).agg("count")
    movie_count = int(
        grouped_result.loc[grouped_result.index.str.strip() == rating_to_find].iloc[
            0, 0
        ]
    )
    return movie_count
