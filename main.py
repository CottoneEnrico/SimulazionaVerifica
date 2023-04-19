from flask import Flask, render_template, request, Response
import pandas as pd

app = Flask(__name__)
df = pd.read_excel("https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true", sheet_name='customers')
groupby = df.groupby('state').count()['customer_id'].reset_index().sort_values(by = 'customer_id', ascending=False)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/nome", methods=["GET"])
def nome():
    return render_template("inputConNome.html")

@app.route('/risultatoNome', methods=['GET'])
def nomeRisultato():
    nome = request.args.get('box')
    cognome = request.args.get('box1')
    table = df[(df['first_name'] == nome) & (df['last_name'] == cognome)]
    return render_template('risultato.html', table = table.to_html())

@app.route("/citta", methods=["GET", "POST"])
def citta():
    cities = df['city'].tolist()
    return render_template("inputCitta.html", cities = list(set(cities)))

@app.route('/citta/<city>', methods=['GET', 'POST'])
def cittaRisultato(city):
    table = df[df['city'].str.contains(city)]
    return render_template('risultato.html', table = table.to_html())   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=32245, debug=True)