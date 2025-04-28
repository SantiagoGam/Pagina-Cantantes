from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('PaginasRutas/PaginaPrincipal.html')

@app.route('/PAGINAHECTOR')
def PagHector():
    return render_template('PaginasRutas/PaginaPrincipalHector.html')

@app.route('/PAGINAEMINEM')
def PagEminem():
    return render_template('PaginasRutas/PaginaPrincipalEminem.html')

@app.route('/PAGINADONOMAR')
def PagDon():
    return render_template('PaginasRutas/PaginaPrincipalDonOmar.html')

if __name__=='__main__':
    app.run(debug=True)

    