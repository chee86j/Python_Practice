import { useState } from "react";

function BookEdit({ book, onEdit }) {
  const [title, setTitle] = useState(book.title);
  // starting value is the title of the book and alternatively you can use
  // placeholder value - placeholder="book.title" and leave the value empty
  // with this const [title, setTitle] = useState("");
  
  const handleChange = (event) => {
    setTitle(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onEdit(book.id, title);
  };

  return <form onSubmit={handleSubmit} className="book-edit">
    <label>Title</label>
    <input className="input" value={title} onChange={handleChange} />
    <button className="button is-primary">
      Save
    </button>
  </form>
}

export default BookEdit;
