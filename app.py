from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

class FoodRecommender:
    def __init__(self, data):
        self.data = data
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.data['features'] = self.data.apply(self._combine_features, axis=1)
        self.tfidf_matrix = self.tfidf.fit_transform(self.data['features'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        
    def _combine_features(self, row):
        return ' '.join([
            str(row['food_category']),
            str(row['sub_category']),
            str(row['flavour']),
            str(row['sub_menu'])
        ])
    
    def get_food_menu(self):
        """Return all foods with their IDs and names"""
        return self.data[['ProductId', 'food_name', 'food_category']].to_dict('records')
    
    def get_recommendations(self, food_id, n_recommendations=6):
        try:
            idx = self.data[self.data['ProductId'] == food_id].index[0]
            sim_scores = list(enumerate(self.cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:n_recommendations+1]
            food_indices = [i[0] for i in sim_scores]
            return self.data.iloc[food_indices][
                ['ProductId', 'food_name', 'food_category', 'sub_category', 
                 'flavour', 'price', 'sub_menu']
            ].to_dict('records')
        except Exception as e:
            print(f"Error getting recommendations: {str(e)}")
            return []
    
    def get_filtered_recommendations(self, category=None, sub_category=None, 
                                   flavour=None, max_price=None, n_recommendations=6):
        filtered_data = self.data.copy()
        
        if category:
            filtered_data = filtered_data[filtered_data['food_category'] == category]
        if sub_category:
            filtered_data = filtered_data[filtered_data['sub_category'] == sub_category]
        if flavour:
            filtered_data = filtered_data[filtered_data['flavour'] == flavour]
        if max_price:
            filtered_data = filtered_data[filtered_data['price'] <= float(max_price)]
            
        if len(filtered_data) == 0:
            return []
            
        return filtered_data.head(n_recommendations)[
            ['ProductId', 'food_name', 'food_category', 'sub_category', 
             'flavour', 'price', 'sub_menu']
        ].to_dict('records')

    def get_metadata(self):
        return {
            'categories': sorted(self.data['food_category'].unique().tolist()),
            'sub_categories': sorted(self.data['sub_category'].unique().tolist()),
            'flavours': sorted(self.data['flavour'].unique().tolist()),
            'price_range': {
                'min': float(self.data['price'].min()),
                'max': float(self.data['price'].max())
            }
        }

# Initialize
data = pd.read_csv('Food Dataset.csv')
recommender = FoodRecommender(data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/metadata')
def get_metadata():
    return jsonify(recommender.get_metadata())

@app.route('/api/food-menu')
def get_food_menu():
    # Add print statement for debugging
    menu = data[['ProductId', 'food_name', 'food_category']].to_dict('records')
    print("Sending food menu:", len(menu), "items")
    return jsonify(menu)

@app.route('/api/recommendations/<food_id>')
def get_recommendations(food_id):
    return jsonify(recommender.get_recommendations(food_id))

@app.route('/api/recommendations/filter')
def get_filtered_recommendations():
    params = {
        'category': request.args.get('category'),
        'sub_category': request.args.get('sub_category'),
        'flavour': request.args.get('flavour'),
        'max_price': request.args.get('max_price')
    }
    return jsonify(recommender.get_filtered_recommendations(**params))

if __name__ == '__main__':
    app.run(debug=True)