import random
import pandas as pd


class Home():
    @classmethod
    def get_random_data_discover(self, request):
        dataframe = pd.read_csv('data_film.csv')
        # cek genre request
        if request is None:
            print('Masuk None')
            movies = dataframe
        elif request == "":
            print('Masuk String')
            movies = dataframe
        else:
            print('Masuk Found')
            movies = dataframe[dataframe['genre'] == str(request)]

        # variabel data temporary
        data = []
        # loop data movies from dataset by filter genre or without genre
        for index,row in movies.iterrows():
            title = row['title']
            description = row['description']
            genre = row['genre']
            year = row['year']
            url = row['url']
            thumbnail = row['thumbnail']
            movie = {'title': title, 'description': description, 'genre': genre, 'url': url, 'thumbnail': thumbnail,
                     'year': year}
            data.append(movie)
        # return data movies random
        return random.sample(data, 20)

    def get_random_data_genre(*self):
        genre = pd.read_csv('genre.csv')
        data = []
        for i in genre['genre']:
            data.append(i)
        return data
