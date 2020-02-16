import numpy as np
import pandas as pd
from surprise import Dataset, Reader, SVD, BaselineOnly
from surprise.model_selection import cross_validate

def init():
    #reader_anime = Reader(line_format='anime_id name genre type episodes rating members', sep=',',skip_lines=1)
    reader_rating = Reader(line_format='user item rating', sep=',',skip_lines=1)
    #anime = Dataset.load_from_file("anime.csv", reader=reader_anime)
    rating = Dataset.load_from_file("rating.csv", reader=reader_rating)
    return rating



if __name__ == "__main__":
    rating = init()
    cross_validate(BaselineOnly(), rating, verbose=True)
