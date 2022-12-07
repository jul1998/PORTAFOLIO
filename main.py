from flask import Flask, render_template, send_from_directory, redirect
from forms import MyForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Any key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Projects(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    repo = db.Column(db.String(50), nullable=False, unique=True)
    img = db.Column(db.String(250), nullable=False)
    group = db.Column(db.String(50), nullable=False)

#db.create_all()


@app.route("/")
def home():
    projects = Projects.query.all()
    for project in projects:
        print(project.repo)
    return render_template("index.html", projects=projects)

@app.route("/add_project", methods=["POST", "GET"])
def add_new_project():
    form = MyForm()
    if form.validate_on_submit():
        repo = form.repo.data
        img = form.img.data
        group = form.group.data
        new_project = Projects(repo=repo, img=img, group=group)
        db.session.add(new_project)
        db.session.commit()
        return redirect('/')
    return render_template("add_project.html", form=form)

@app.route("/download_cv")
def download():
    return send_from_directory(
        directory="static", path="files/Julian_CV.pdf"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

