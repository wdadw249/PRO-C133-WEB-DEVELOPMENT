from flask import Flask, render_template

# creating instance of class Flask
app = Flask(__name__)


@app.route("/")
def home():

    name = "Muhammad Sayedi"
    age = "15"

    return render_template('index.html', name=name, age=age)


# define the route to father webpage
@app.route("/father")
def father_page():

    return render_template("father.html", name="Omar", age="40")


# define the route to mother webpage
@app.route("/mother")
def mother_page():

    return render_template("mother.html", name="Classified", age="40")


# define the route to friends webpage
@app.route("/friend")
def friend_page():

    return render_template("friend.html", name="Maiwand", age="15")


# run the file
if __name__ == '__main__':
    app.run(debug=True)
