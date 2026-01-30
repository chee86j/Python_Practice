import { useState, createContext } from "react";

// When 'count' state is updated, this component will re-render, along with all its children
const BooksContext = createContext();

// Custom Provider Component
function Provider({ children }) {
  const [count, setCount] = useState(5);

  // Object we want to share with all our components
  const valueToShare = {
    count: count,
    incrementCount: () => {
      setCount(count + 1);
    },
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
