from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load data and model
df_eng = pd.read_csv("nafdac_data.csv")
embeddings = np.load("drug_embeddings.npy")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Flask app
app = Flask(__name__)

def get_recommendations(query, embeddings, model, data, top_n=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    top_indices = similarities[0].argsort()[-top_n:][::-1]
    return data.iloc[top_indices]

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    nrn_result = None
    query = ""
    nrn_query = ""
    top_n = 5

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        nrn_query = request.form.get('nrn', '').strip().upper()
        try:
            top_n = int(request.form.get('top_n', 5))
        except ValueError:
            top_n = 5

        if nrn_query:
            # Search for NRN
            result = df_eng[df_eng['NRN'].str.upper() == nrn_query]
            if not result.empty:
                nrn_result = result.iloc[0]  # Just one product
        elif query:
            # Use recommendation system
            recommendations = get_recommendations(query, embeddings, model, df_eng, top_n=top_n)

    return render_template(
        'front8.html',
        recommendations=recommendations,
        nrn_result=nrn_result,
        query=query,
        nrn_query=nrn_query,
        top_n=top_n
    )

if __name__ == '__main__':
    app.run(debug=True)
