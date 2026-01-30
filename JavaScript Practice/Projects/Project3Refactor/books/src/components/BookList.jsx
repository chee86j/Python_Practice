import BookShow from "./BookShow.jsx";
import BooksContext from "../context/books.jsx";
import { useContext } from "react";

function BookList() {
  const { books } = useContext(BooksContext);

  const renderedBooks = books.map((book) => {
    return (
      <BookShow key={book.id} book={book} />
    );
  });

  return (
    <div className="book-list">
      {renderedBooks}
    </div>
  );
}

export default BookList;
