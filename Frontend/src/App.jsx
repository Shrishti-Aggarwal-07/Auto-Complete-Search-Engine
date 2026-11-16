import { useState, useEffect } from "react";
import "./App.css";

import SearchBar from "./components/SearchBar";
import Suggestions from "./components/Suggestions";
import SearchResults from "./components/SearchResults";

function App() {
  const [search, setSearch] = useState("");
  const [showSuggestions, setShowSuggestions] = useState(true);

  const [suggestions, setSuggestions] = useState([]);
  const [results, setResults] = useState([]);
  const [submittedSearch, setSubmittedSearch] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Flask backend URL
  const API_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:5000";

  // Fetch autocomplete suggestions from Flask
  useEffect(() => {
    const prefix = search.trim();

    if (!prefix || !showSuggestions) {
      setSuggestions([]);
      return;
    }

    const controller = new AbortController();

    // Small delay to avoid sending a request for every keystroke immediately
    const timer = setTimeout(async () => {
      try {
        const response = await fetch(
          `${API_URL}/api/autocomplete?prefix=${encodeURIComponent(prefix)}`,
          { signal: controller.signal }
        );

        if (!response.ok) {
          throw new Error("Failed to fetch suggestions");
        }

        const data = await response.json();

        setSuggestions(data.suggestions || []);
        setError("");
      } catch (err) {
        if (err.name !== "AbortError") {
          setError("Unable to connect to the backend.");
          setSuggestions([]);
        }
      }
    }, 200);

    return () => {
      clearTimeout(timer);
      controller.abort();
    };
  }, [search, showSuggestions]);

  // Search using Flask API
  const handleSearch = async () => {
    const query = search.trim();

    if (!query) return;

    setLoading(true);
    setError("");
    setShowSuggestions(false);
    setSubmittedSearch(query);

    try {
      const response = await fetch(
        `${API_URL}/api/search?q=${encodeURIComponent(query)}`
      );

      if (!response.ok) {
        throw new Error("Search request failed");
      }

      const data = await response.json();

      setResults(data.results || []);
    } catch (err) {
      setResults([]);
      setError("Unable to connect to the backend.");
    } finally {
      setLoading(false);
    }
  };

  // Select an autocomplete suggestion
  const handleSelect = (word) => {
    setSearch(word);
    setShowSuggestions(false);
  };

  return (
    <div className="app">
      <h1>Auto-Complete Search Engine</h1>
      <p>Find what you're looking for, faster.</p>

      <div className="search-container">
        <SearchBar
          search={search}
          setSearch={(value) => {
            setSearch(value);
            setShowSuggestions(true);
            setSubmittedSearch("");
            setResults([]);
            setError("");
          }}
          onSearch={handleSearch}
        />

        {search.trim() !== "" && (
          <Suggestions
            suggestions={suggestions}
            onSelect={handleSelect}
            showSuggestions={showSuggestions}
          />
        )}
      </div>

      {loading && <p>Searching...</p>}

      {error && <p>{error}</p>}

      <SearchResults
        submittedSearch={submittedSearch}
        results={results}
      />
    </div>
  );
}

export default App;