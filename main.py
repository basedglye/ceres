from flask import Flask
from card import Card

app = Flask(__name__)

def create_card(name):
	return Card(name, "cards/" + name + "/template.txt", "cards/" + name + "/data.json")

cards = {
	"example": create_card("example")
}



@app.route("/card/<string:name>")
def get_card(name):
	if name in cards:
		return cards[name].get_data()
	return "ERROR"

@app.route("/raw/<path:loc>")
def get_raw(loc):
	with open("raw/" + loc, 'r') as filereader:
		return filereader.read()

@app.route("/<path:loc>")
def get_root(loc):
	return get_raw(loc)

if __name__ == "__main__":
	app.run(host="needs.money", port=9010)
