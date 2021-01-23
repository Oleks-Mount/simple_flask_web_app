from flask import Flask, render_template, request ,redirect , url_for ,flash , session
import psycopg2
import jinja2


app = Flask(__name__)
app.config.from_object(__name__)

db = psycopg2.connect(dbname="#", user="#",password="#", host="#", port="5432")
con = db.cursor()

app.config.update(dict(
    DATABASE = db,
    DEBUG =True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = '111'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



@app.route('/')
def show_post():
    p_db =  con
    p_db.execute('select id ,title, text from post;')
    entries = con.fetchall()
    return render_template('main_page.html',entries=entries)



@app.route('/add_2')
def add_form():
    flash('You need to log in')
    return render_template('create_post.html')

# creating is possible only under the administrator
@app.route('/add', methods=['POST'])
def add_entry():
    p_db = con
    p_db.execute('insert into post (title, text) values(%s, %s)',
                     (request.form['title'], request.form['text']))
    db.commit()
    flash('New post was successfully posted')
    return redirect(url_for('add_form'))


@app.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] !=app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['Logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_post'))
    return render_template('login.html' , error = error)


@app.route('/logout')
def logout():
    session.clear()
    flash('You were logged out')
    return redirect(url_for('show_post'))


# removal is possible only under the administrator
@app.route('/delete', methods =['POST'])
def delete():
    p_db = con
    p_db.execute('delete from post where id = %s;',(request.form['id']))
    db.commit()
    flash('Was delete posted')
    return redirect(url_for('show_post'))



if __name__ == '__main__':
    app.run(debug=True)