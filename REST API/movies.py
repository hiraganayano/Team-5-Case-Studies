from flask import Flask, jsonify, request
app = Flask(__name__)

movies = [
    {
        "name" : "Squid Game",
        "casts" : ["Lee Kwon Yu", "Lee MonSuk", "Young Sheewon"],
        "genres" : ["Thriller", "Comedy"]
    },

    {
        "name" : "Little Women",
        "casts" : ["Rosemarie Chavez", "Heart Ebange", "Joana Miguel"],
        "genres" : ["Drama", "Suspense"]
    }
]
@app.route ('/movies', methods=['GET'])
def getMovies():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def addMovie():
    movie = request.get_json()
    movies.append(movie)
    return{'id': len(movies)},200

@app.route('/movies/<int:index>', methods=['DELETE'])
def deleteMovie(index):
    movies.pop(index)
    return 'Movie was successfully deleted', 200

if __name__ == '__main__':
    app.run()