from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.debug = True
debug = DebugToolbarExtension(app)

@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/goodbye')
def say_bye():
    return "GOOD BYE"

@app.route('/lucky')
def lucky_number():
    num = randint(1,10)
    return render_template("lucky.html", lucky_num=num, msg="You are so lucky!")

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route("/form-2")
def show_form_2():
    return render_template("form_2.html")

COMPLIMENTS = ["cool", "nice", "kind", "clever", "tenacious", "awesome", "pythonic"]

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)

@app.route('/greet-2')
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS,3)
    return render_template("greet_2.html", username = username, wants_compliments=wants, compliments=nice_things)
    

@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word)

@app.route('/ryan')
def say_ryan():
    html = """
    <html>
        <body>
            <h1>Hello, Ryan!</h1>
            <p>This is the hello Ryan page</>
        </body>
    </html>
    """
    return html

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Hello Person!</h1>
            <p>This is the home page</>
            <a href='/hello'>Go to Hello Page</a>
        </body>
    </html>
    """
    return html


@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by {sort}</p>"



@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment= request.form["comment"]
    username= request.form["username"]
    return f"""
        <h1>SAVED YOUR COMMENT</h1>
        <ul>
            <li>Username: {username}</li>
            <li>Comment: {comment}</li>

        </ul> 
    """


# @app.route('/r/<subreddit>')
# def show_subreddit(subreddit):
#     return "THIS IS A SUBREDDIT"


# @app.route('/r/<subreddit>')
# def show_subreddit(subreddit):
#     return f"<h1>You are now browsing the {subreddit} subreddit!!</h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f"<p>{post}</p>"


@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_subreddit(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} subreddit!!</h1>"