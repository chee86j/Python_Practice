import BookShow from "./BookShow.jsx";
import useBooksContext from "../hooks/use-books-context.jsx";

function BookList() {
  const { books } = useBooksContext();

  const renderedBooks = books.map((book) => {
    return (
      <BookShow key={book.id} book={book} />
    );
  });

  return (
    <div className="book-list">
      {count} <button onClick={incrementCount}>Click</button>
      {renderedBooks}
    </div>
  );
}

export default BookList;
