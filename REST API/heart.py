from flask import Flask, jsonify, request
app = Flask(__name__)

heartinfo = [
    {
        "heart_id" : "1",
        "date" : "1/10/2022",
        "heart_rate" : "97"
    },
    {
        "heart_id" : "2",
        "date" : "1/10/2022",
        "heart_rate" : "101"
    },
    {
        "heart_id" : "23",
        "date" : "1/10/2022",
        "heart_rate" : "120"
    },
]
@app.route ('/', methods=['GET'])
def getHeartinfo():
    return jsonify(heartinfo)

@app.route('/', methods=['POST'])
def addHeartinfo():
    heartinfo = request.get_json()
    heartinfos.append(heartinfo)
    return{'heart_id': len(heartinfos)},200

if __name__ == '__main__':
    app.run()