from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
#"term frequency times inverse document frequency"
#отражает то, насколько важным является слово для документа в их коллекции
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

vectorizer = TfidfVectorizer(max_features=20000, stop_words=get_stop_words('ru')) #в словарь войдут первые max_features слов с наиболее высокой частотой, игнорируя stop-words
data = vectorizer.fit_transform(content)  #учит словарь, возвращает матрицу "document-term"
joblib.dump(vectorizer, 'vectorizer.clf')   #сохраняет объект vectorizer в виде файла для дальнейшего использования

classifier = MultinomialNB().fit(data, rubrics)  #для подсчета слов подходит полиномиальный байес
joblib.dump(classifier, 'classifier.clf')

