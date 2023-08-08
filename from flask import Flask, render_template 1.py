from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"task": "sample Todo", "done": False}]  # Corrected 'Flase' to 'False' and changed 'todo' to 'task'

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():  # Added a missing colon
    todo = request.form["todo"]  # Corrected 'todo' to "todo" in request.form[]
    todos.append({"task": todo, "done": False})  # Corrected 'Flase' to 'False' and changed 'todo' to 'task'
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])  # Corrected 'method' to 'methods'
def edit(index):
    todo = todos[index]  # Corrected 'todo' to 'todos[index]'
    if request.method == "POST":
        todo['task'] = request.form["todo"]  # Corrected 'todo' to 'todos'
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)  # Corrected 'render_templates' to 'render_template'

@app.route("/check/<int:index>", methods=["GET", "POST"])  # Added 'methods' to specify allowed methods
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))  # Removed 'else' as it was unnecessary

if __name__ == "__main__":
    app.run(debug=True)
