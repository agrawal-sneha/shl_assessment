from flask import Flask, request, jsonify, render_template
from rag_recommender.modules.rag_pipeline import search_assessments
import re

app = Flask(__name__)

def generate_url(course_name: str) -> str:
    base_url = "https://www.shl.com/solutions/products/product-catalog/view/"
    cleaned = re.sub(r'[^\w\s-]', '', course_name)
    cleaned = cleaned.lower()
    slug = re.sub(r'\s+', '-', cleaned.strip())
    return base_url + slug + "/"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    try:
        results = search_assessments(query)

        # Add URLs to each result
        for r in results:
            if "title" in r:
                r["url"] = generate_url(r["title"])  # Ensure r has a 'title' key
        
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

