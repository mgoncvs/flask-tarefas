from flask import flask,redirect,render_template,request,session

app = flask(__name__)
app.secret_key = "senha secreta"

@app.router('/')
def index():
    if 'lista' not in session:
        session['lista'] = []
    return render_template('tela.html',lista=session['lista'])

if __name__ == "__main__":
   app.run(debug=True)