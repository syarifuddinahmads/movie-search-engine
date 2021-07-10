from flask import Flask, render_template
from services import Home
from services.Home import Home

app = Flask(__name__)


@app.route('/')
def home():
    discover = Home.get_random_data_discover()
    genre = Home.get_random_data_genre()
    return render_template('home.html',genre=genre,discover=discover)


if __name__ == '__main__':
    app.run(debug=True)
