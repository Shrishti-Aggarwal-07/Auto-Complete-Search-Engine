
function Suggestions({ suggestions, onSelect, showSuggestions }) {
  if (!showSuggestions) {
    return null;
  }

  return (
    <div className="suggestions">
      {suggestions.length > 0 ? (
        suggestions.map((word, index) => (
          <div
            className="suggestion-item"
            key={index}
            onClick={() => onSelect(word)}
          >
            {word}
          </div>
        ))
      ) : (
        <div className="suggestion-item">
          No suggestions found
        </div>
      )}
    </div>
  );
}

export default Suggestions;
