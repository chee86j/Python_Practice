import { useState } from "react";
import BookEdit from "./BookEdit.jsx";

function BookShow({ book, onDelete, onEdit }) {
  const [showEdit, setShowEdit] = useState(false);

  const handleDeleteClick = () => {
    onDelete(book.id);
  };

  const handleEditClick = () => {
    setShowEdit(!showEdit);
  };

  let content = <h3>{book.title}</h3>;
  if (showEdit) {
    content = <BookEdit book={book} onEdit={onEdit}/>;
  }

  return <div className="book-show">{book.title} 
  <div>{content}</div>
  <div className="actions">
    <button className="edit" onClick={handleEditClick}>Edit</button>
    <button className="delete" onClick={handleDeleteClick}>Delete</button></div>
    </div>;
  }

export default BookShow;
