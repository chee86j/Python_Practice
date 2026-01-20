function BookShow({ book, onDelete }) {
  
  const handleClick = () => {
    onDelete(book.id);
  };

  return <div className="book-show">{book.title} 
  <div className="actions">
    <button className="delete" onClick={handleClick}>Delete</button></div>
    </div>;
  }


export default BookShow;
