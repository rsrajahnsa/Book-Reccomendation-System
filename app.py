from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

try:
    popular_df = pickle.load(open('popular.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
except Exception as e:
    print("Error loading pickled files:", e)
    popular_df = None
    pt = None
    books = None
    similarity_scores = None

@app.route('/')
def index():
    if popular_df is not None:
        return render_template('index.html',
                               book_name=list(popular_df['Book-Title'].values),
                               author=list(popular_df['Book-Author'].values),
                               image=list(popular_df['Image-URL-M'].values),
                               votes=list(popular_df['num_ratings'].values),
                               rating=list(popular_df['Avg_ratings'].values)
                               )
    else:
        return "Error: Failed to load data. Please check the pickled files."

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if pt is not None and similarity_scores is not None:
            index = np.where(pt.index == user_input)[0][0]
            similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

            data = []
            for i in similar_items:
                item = []
                temp_df = books[books['Book-Title'] == pt.index[i[0]]]
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

                data.append(item)

            print(data)
            return render_template('recommend.html', data=data)
        else:
            return "Error: Failed to load data. Please check the pickled files."

if __name__ == '__main__':
    app.run(debug=True)
