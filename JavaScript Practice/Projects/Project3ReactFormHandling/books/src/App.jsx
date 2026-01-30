import { useState, useEffect } from "react";
import axios from "axios";
import BookCreate from "./components/BookCreate.jsx";
import BookList from "./components/BookList.jsx";

function App() {
  const [books, setBooks] = useState([]);

  const fetchBooks = async () => {
    const response = await axios.get("http://localhost:3001/books");
    setBooks(response.data);
  };

  // useEffect common patterns:
  // 1) No deps array -> runs after every render (rare: logging/global tracking)
  // 2) [] -> runs once on mount (API calls, event listeners)
  // 3) [a, b] -> runs on mount + when a/b change (validation, syncing, filtered API calls)
  useEffect(() => {
    fetchBooks();
  }, []);

  const deleteBookById = async (id) => {
    await axios.delete(`http://localhost:3001/books/${id}`);
    fetchBooks();
  };

  const editBookById = async (id, newTitle) => {
    await axios.put(`http://localhost:3001/books/${id}`, {
      title: newTitle,
    });
    fetchBooks();
  };

  const createBook = async (title) => {
    await axios.post("http://localhost:3001/books", {
      title: title,
    });
    fetchBooks();
  };

  return (
    <div className="app">
      <h1>Reading List</h1>
      <BookList books={books} onDelete={deleteBookById} onEdit={editBookById} />
      <BookCreate onCreate={createBook} />
    </div>
  );
}

export default App;
