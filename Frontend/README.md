# Auto-Complete Search Engine – Frontend

## Project Overview
This is the React frontend of our Auto-Complete Search Engine project, developed using Vite.

The application allows users to:
- Enter a search prefix.
- View autocomplete suggestions.
- Select a suggestion.
- Search and display matching results.

Currently, temporary hardcoded sample data is used for testing.

## Technologies Used
- React.js
- JavaScript
- CSS
- Vite

## Project Structure
```text
src/
├── components/
│   ├── SearchBar.jsx
│   ├── Suggestions.jsx
│   └── SearchResults.jsx
├── App.jsx
├── App.css
├── index.css
└── main.jsx
```

## How to Run

1. Install Node.js.
2. Open the project folder in the terminal.
3. Run:

```bash
npm install
npm run dev
```

4. Open the local URL displayed in the terminal.

## Backend Integration

The frontend will be connected to the Python Flask backend.

Expected API:

**Endpoint:** `GET /api/autocomplete`

**Example request:**
```text
/api/autocomplete?prefix=comp
```

**Expected JSON response:**
```json
{
  "suggestions": [
    "computer",
    "computer science",
    "compiler"
  ]
}
```

The backend will use a Trie data structure and a text-file dataset to generate suggestions.

The frontend will fetch suggestions from this API instead of using temporary hardcoded data.

## Team Responsibilities

**Frontend:** React UI, search input, suggestions dropdown and search results.

**Backend:** Python, Flask, Trie implementation and text-file dataset.

**Integration:** Connect the React frontend with the Flask API.
