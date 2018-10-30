from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/welcome")
def welcome():
    return "my pleasure"
    
@app.route("/html_tag")
def html_tag():
    return "<h1>HEY BUDDY, I'VE BEEN WAITING YOU FOR A LONG TIME </h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1> multiple line</h1>
    <u1><li>1번</li>
    <li>2번</li></ul>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("file.html")
    
@app.route("/hello_name/<string:name>")
def hello_name(name):
    return render_template("hello.html", people_name = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    result = num**3
    return render_template("cube.html", num=num, cube_num=result)
    
    
    
@app.route("/donguni")
def donguni():
    return "<h1>보이냐 개씨발새끼야?!</h1>"