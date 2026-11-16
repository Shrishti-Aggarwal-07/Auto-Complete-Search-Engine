from flask import Flask, request, jsonify
from flask_cors import CORS
from trie import Trie
import os

app = Flask(__name__)

# Enable communication with React frontend
CORS(app)

# Initialize Trie
trie = Trie()

# Store original words for search results
word_list = []

# Load words from text file
def load_words():
    global word_list

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "words.txt"
    )

    if not os.path.exists(file_path):
        raise FileNotFoundError("words.txt file not found!")

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()

            if word:
                word_list.append(word)
                trie.insert(word)

    print(f"Successfully loaded {len(word_list)} words.")
    print("Trie has been constructed successfully.")


# API 1: Autocomplete suggestions
@app.route("/api/autocomplete", methods=["GET"])
def autocomplete():

    prefix = request.args.get("prefix", "").strip()

    if not prefix:
        return jsonify({
            "suggestions": []
        })

    suggestions = trie.autocomplete(prefix, limit=10)

    return jsonify({
        "suggestions": suggestions
    })


# API 2: Search (Trie-based prefix matches first, then other matches)
@app.route("/api/search", methods=["GET"])
def search():

    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify({
            "results": []
        })

    # If the query is an exact word in the Trie, count it as a popular search
    if trie.search(query):
        trie.increment_frequency(query)

    # 1) Prefix matches come from the Trie (fast, ranked)
    prefix_matches = trie.autocomplete(query, limit=50)

    # 2) Remaining "contains" matches (e.g. "script" -> "javascript")
    other_matches = [
        word for word in word_list
        if query in word.lower() and word.lower() not in prefix_matches
    ]

    results = prefix_matches + other_matches

    return jsonify({
        "results": results[:50]
    })


# API 3: Check backend status
@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({
        "status": "running",
        "message": "Auto Complete Search Engine backend is working!",
        "total_words": len(word_list)
    })


# Home route
@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Welcome to Auto Complete Search Engine API"
    })


# Load dataset and construct Trie
load_words()


# Run Flask server

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("FLASK_DEBUG", "0") == "1"
    )
