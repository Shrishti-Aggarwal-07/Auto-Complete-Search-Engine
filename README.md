# Auto Complete Search Engine (Trie)

Prefix-based search suggestions using a Trie, with a Flask backend and React frontend.

## Run the backend
```
cd Backend
pip install -r requirements.txt
python app.py
```
Runs at http://127.0.0.1:5000

## Run the frontend
```
cd Frontend
npm install
npm run dev
```

## Run tests
```
cd Backend
python test_trie.py
```

## API
- `GET /api/autocomplete?prefix=comp` – top 10 suggestions (Trie)
- `GET /api/search?q=python` – search results
- `GET /api/health` – status