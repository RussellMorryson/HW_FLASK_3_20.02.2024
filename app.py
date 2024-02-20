from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from model import db, User
from form import Registration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)
app.config['SECRET_KEY'] = 'd4d3b21880bb754fcc7442e9eca026ff8c59048d35d0f2356f456742a7466249'

csrf = CSRFProtect(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()

@app.route('/registration/', methods=['GET', 'POST'])
def login():
    form = Registration()
    if request.method == 'POST' and form.validate():
        user = User(
            name = form.name.data,
            surname = form.surname.data,
            email = form.email.data,
            password = form.password.data
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        context = {
            'name': form.name.data,
            'surname': form.surname.data,
            'email': form.email.data
        }
        return render_template('complete.html', **context)
    return render_template('registration.html', form = form)

if __name__ == '__main__':
    #init_db()
    app.run(debug=True)