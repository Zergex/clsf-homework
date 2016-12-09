from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from stop_words import get_stop_words


rubrics = ['Россия', 'Мир', 'Бывший СССР', 'Финансы', 'Бизнес',
           'Силовые структуры', 'Наука и техника', 'Культура', 'Спорт',
           'Интернет и СМИ', 'Ценности', 'Путешествия', 'Из жизни']

filenames = ['russia.txt', 'world.txt', 'ussr.txt', 'economics.txt', 'business.txt',
           'forces.txt', 'science.txt', 'culture.txt', 'sport.txt', 'media.txt', 'style.txt', 'travel.txt', 'life.txt']

content = []
for i in range(len(rubrics)):
    news_file = open(filenames[i], 'r', encoding="utf-8")
    content.append(news_file.read())
    news_file.close()

vectorizer = TfidfVectorizer(max_features=20000, stop_words=get_stop_words('ru'))
data = vectorizer.fit_transform(content)
joblib.dump(vectorizer, 'vectorizer.clf')

classifier = MultinomialNB().fit(data, rubrics)
joblib.dump(classifier, 'classifier.clf')
