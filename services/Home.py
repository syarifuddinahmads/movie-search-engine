import random
import pandas as pd
from operator import itemgetter
from math import log
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
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
        for index, row in movies.iterrows():
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

    def search_data(request):
        word = request
        stop_words = stopwords.words('english')
        stemmer = PorterStemmer()
        i = 1
        data = pd.read_csv('data_film.csv', sep=',')  # data real sebelum di prosesing
        # data_after = pd.read_csv('post_processing_data_film_cleaned.csv',sep="|")
        data_after = pd.read_csv('post_processing_data_film_stemmed.csv', sep="|")

        data_word = word.split(" ")

        # query
        query_word = []
        for dw in data_word:
            token = word_tokenize(dw)
            dw_cleaned_token = ""
            for word_token in token:
                if word_token not in stop_words:
                    dw_cleaned_token += word_token + " "

            token_stemming = word_tokenize(dw_cleaned_token)
            for ws in token_stemming:
                query_word.append(stemmer.stem(ws))

        # TF - DF
        termFreq = []
        docsFreq = []
        for i, term in enumerate(query_word):  # untuk looping kata-kata inputan dari user
            docsCounter = []
            docsFreqCounter = 0
            for doc in data_after['word']:  # looping untuk document per baris
                # doc 1
                # doc 2
                # doc 3
                counter = 0
                for word in doc.split(' '):  # looping kata-kata dari dokumen perbaris
                    if word == term:  # ini untuk cek apakah kata-kata sama atau relevan
                        counter += 1
                docsCounter.append(counter)

                if counter > 0:
                    docsFreqCounter += 1
            termFreq.append(docsCounter)
            docsFreq.append(docsFreqCounter)

        # IDF + 1
        idf_one = []
        docsTotal = len(data)
        for i in docsFreq:
            idf_one.append(log(docsTotal) / (i + 1))

        # TFIDF
        docs_weight = termFreq[:]  # ['word','cutting']
        for i in range(len(docs_weight)):
            for j in range(len(docs_weight[i])):
                docs_weight[i][j] = termFreq[i][j] * idf_one[i]

        total_weight = []
        for i in range(len(docs_weight[0])):
            total_weight.append([i, 0])

        for i in range(len(docs_weight)):
            for j in range(len(docs_weight[i])):
                total_weight[j][1] += docs_weight[i][j]

        # sort document relevan
        total_weight = sorted(total_weight, key=itemgetter(1), reverse=True)

        # show top 32 document relevan
        data_movie = []
        for i in range(0, 32):
            title = data['title'][total_weight[i][0]]
            description = data['description'][total_weight[i][0]]
            genre = data['genre'][total_weight[i][0]]
            year = data['year'][total_weight[i][0]]
            url = data['url'][total_weight[i][0]]
            thumbnail = data['thumbnail'][total_weight[i][0]]
            movie = {'title': title, 'description': description, 'genre': genre, 'url': url, 'thumbnail': thumbnail,
                     'year': year}
            print('Item Movies = ',movie)
            data_movie.append(movie)

        return data_movie
