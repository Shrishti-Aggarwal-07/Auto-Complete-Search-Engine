
function SearchBar({ search, setSearch, onSearch }) {
  return (
    <div className="search-box">
      <input
        type="text"
        placeholder="Start typing something..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            onSearch();
          }
        }}
      />

      <button onClick={onSearch}>
        Search
      </button>
    </div>
  );
}

export default SearchBar;
