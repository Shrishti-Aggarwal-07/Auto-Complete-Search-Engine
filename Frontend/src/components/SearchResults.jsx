
function SearchResults({ submittedSearch, results }) {
  if (!submittedSearch) {
    return null;
  }

  return (
    <div className="results-container">
      <h2>Search Results</h2>

      <p>Results for: {submittedSearch}</p>

      {results.length > 0 ? (
        results.map((word, index) => (
          <div className="result-item" key={index}>
            {word}
          </div>
        ))
      ) : (
        <p>No results found.</p>
      )}
    </div>
  );
}

export default SearchResults;
