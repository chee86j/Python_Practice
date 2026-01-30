import { useEffect, useContext } from "react";
import BookCreate from "./components/BookCreate.jsx";
import BookList from "./components/BookList.jsx";
import BooksContext from "./context/books.jsx";

function App() {
  const { fetchBooks } = useContext(BooksContext);

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <div className="app">
      <h1>Reading List</h1>
      <BookList />
      <BookCreate />
    </div>
  );
}

export default App;
