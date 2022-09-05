from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return "Initial setup for News Article Sorting Application"


if __name__ == "__main__":
    app.run(debug=True)
