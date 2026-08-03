from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My Website!</h1>
    <p>Hello, Praveen 👋</p>
    <p>This website is built using Python Flask.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
