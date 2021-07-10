import random

import pandas as pd

class Home():
    @classmethod

    def get_random_data_discover(*self):
        movies = pd.read_csv('data_film.csv')
        data= []
        for i in range(0,len(movies)):
            title = movies['title'][i]
            description = movies['description'][i]
            genre =  movies['genre'][i]
            url =  movies['url'][i]
            thumbnail =  movies['thumbnail'][i]
            movie = {'title':title,'description':description,'genre':genre,'url':url,'thumbnail':thumbnail}
            print('Movie Item =',movie)
            data.append(movie)

        return []

    def get_random_data_genre(*self):
        genre = pd.read_csv('genre.csv')
        data = []
        for i in genre['genre']:
            data.append(i)
        return data