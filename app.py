from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_poem():
    poem = """
    Було колись — в Україні
    Ревіли гармати;
    Було колись — запорожці
    Вміли пановати.
    Пановали, добували
    І славу, і волю;
    Минулося — осталися
    Могили на полі.
    """
    return render_template('template.html', poem=poem)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
