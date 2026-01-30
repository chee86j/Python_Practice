import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { Provider } from "./context/books.jsx";

const el = document.getElementById("root");
const root = ReactDOM.createRoot(el);

root.render(
  <Provider>
    <App />
  </Provider>
);

// Alternatively if we only want Context we can do:
// root.render(
//   <BooksContext.Provider value={{ count: 5, incrementCount: () => { setCount(count + 1); } }}>
//     <App />
//   </BooksContext.Provider>
// );
