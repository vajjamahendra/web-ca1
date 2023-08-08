from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"todo": "sample Todo", "done": Flase}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add()
    todo = request.form[todo]
    todos.append({"task": todo, "done": Flase})
    return redirect(Url_for("index"))


@app.route("/edit/<int:index>", method=["GET", "POST"])
def edit(index):
    todo = todo[index]
    if request.method == "POST":
        todo['task']= request.form["todo"]
        return redirect(url_for("index"))
@app.route("/check/<int:index>")    
    def check(index):
        todos[index]['done'] = not todos[index]['done']
        return redirect(url_for("index"))
    
@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    else:
        return render_templates("edit.html", todo=todo, index=index)