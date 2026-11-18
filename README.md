# Auto Complete Search Engine

A web-based autocomplete and search application that uses a **Trie (Prefix Tree) data structure** to generate word suggestions as users type.

The application supports prefix-based autocomplete, search functionality, and frequency-based ranking of suggestions.

## Live Demo

[Open Auto Complete Search Engine](https://auto-complete-search-engine.vercel.app)

## Features

- Real-time autocomplete suggestions.
- Trie-based prefix searching.
- Frequency-based ranking of suggestions.
- Alphabetical ordering when frequencies are equal.
- Case-insensitive searching.
- Substring search functionality.
- Flask REST API.
- React-based user interface.

## Tech Stack

### Backend
- Python
- Flask
- Flask-CORS
- Trie Data Structure

### Frontend
- React
- JavaScript
- Vite
- HTML
- CSS

### Tools and Deployment
- Git and GitHub
- VS Code
- Vercel (Frontend)
- Render (Backend)

## Project Structure

```text
Auto-Complete-Search-Engine/
│
├── Backend/
│   ├── app.py
│   ├── trie.py
│   ├── words.txt
│   ├── requirements.txt
│   └── test_trie.py
│
├── Frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── package-lock.json
│
├── .gitignore
└── README.md
```

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shrishti-Aggarwal-07/Auto-Complete-Search-Engine.git
```

### 2. Open the project folder

```bash
cd Auto-Complete-Search-Engine
```

### 3. Set up the backend

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r Backend/requirements.txt
```

Start the Flask backend:

```bash
cd Backend
python app.py
```

The backend runs at:

`http://127.0.0.1:5000`

### 4. Set up the frontend

Open a second terminal in the project root:

```bash
cd Frontend
npm install
npm run dev
```

The frontend runs at:

`http://localhost:5173`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Backend welcome message |
| GET | `/api/health` | Checks backend status |
| GET | `/api/autocomplete?prefix=comp` | Returns autocomplete suggestions |
| GET | `/api/search?q=computer` | Returns search results |

## Running Tests

From the project root:

```bash
python -m unittest discover -s Backend -p "test_*.py" -v
```

## Algorithm Used

The project uses a **Trie (Prefix Tree)** data structure for efficient prefix-based searching.

Each node represents a character, and words sharing common prefixes share the same initial path in the Trie.

The autocomplete process:
1. Traverses the Trie to find the node corresponding to the entered prefix.
2. Uses Depth First Search (DFS) to collect matching words.
3. Sorts suggestions by search frequency and alphabetically.
4. Returns the top suggestions.

## Database

The project uses a text file (`words.txt`) as its dataset. No database is required.

## Authentication

The application does not require user authentication or login credentials.

## Contributors

- **Shrishti Aggarwal** – Trie implementation, backend development, Flask APIs, and integration.
- **Shriyanshi** – Frontend development and user interface.

---

Developed as an Algorithm Design and Analysis (ADA) college project.