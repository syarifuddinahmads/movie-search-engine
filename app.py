from flask import Flask, render_template, request
from services import Home
from services.Home import Home

app = Flask(__name__)


@app.route('/')
def home():
    print('Request = ', str(request.args.get('genre')))

    discover = Home.get_random_data_discover(request.args.get('genre'))
    genre = Home.get_random_data_genre()
    return render_template('home.html', genre=genre, discover=discover)


@app.route('/search')
def search():
    data = Home.search_data(request.args.get('q'))
    genre = Home.get_random_data_genre()
    return render_template('home.html', genre=genre, discover=data)


if __name__ == '__main__':
    app.run(debug=True)
