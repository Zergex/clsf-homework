from flask import Flask
from flask import request
from flask import render_template
from sklearn.externals import joblib

app = Flask(__name__)

vectorizer = joblib.load('vectorizer.clf')
classifier = joblib.load('classifier.clf')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        text = request.form.get('newstext')
        tfed_text = vectorizer.transform([text])
        rubrics = classifier.predict(tfed_text)
        return render_template('result.html', rubrics=rubrics)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()