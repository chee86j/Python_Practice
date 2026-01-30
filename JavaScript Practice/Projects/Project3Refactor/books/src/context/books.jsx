import { useState, createContext } from "react";
import axios from "axios";

const BooksContext = createContext();

// Custom Provider Component
function Provider({ children }) {
  const [books, setBooks] = useState([]);

  const fetchBooks = async () => {
    const response = await axios.get("http://localhost:3001/books");
    setBooks(response.data);
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

  const deleteBookById = async (id) => {
    await axios.delete(`http://localhost:3001/books/${id}`);
    fetchBooks();
  };

  const valueToShare = {
    books,
    deleteBookById,
    editBookById,
    createBook,
    fetchBooks
  };

  return (
    <BooksContext.Provider value={valueToShare}>
      {children} {/* This is the children prop which we will explain later*/}
    </BooksContext.Provider>
  );
}

export { Provider };
export default BooksContext;

// import BooksContext, { Provider } from "./books"; when we want the Provider component to wrap our app
// if we only the BooksContext we use 'import BooksContext from "./books";'
