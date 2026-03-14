import { createContext, useEffect, useState } from 'react';

const NavigationContext = createContext();

function NavigationProvider({ children }) {
  const [currentPath, setCurrentPath] = useState(window.location.pathname);

  useEffect(() => {
    /* This listener keeps our React state in sync with browser navigation like back/forward button 
    clicks from the user. */
    /* whenever popstate is triggered, we cleanup with the handler function to update our currentPath 
    state to match the URL. */
    const handler = () => {
      setCurrentPath(window.location.pathname);
    };
    window.addEventListener('popstate', handler);

    return () => {
      // Cleanup: remove listener on unmount so we do not leak handlers.
      window.removeEventListener('popstate', handler);
    };
  }, []);

  // this function will be used by our custom Link component to update URL & currentPath state when link is clicked.
  // pushState changes the URL without triggering a full page refresh. It is the equivalent of React Router's Link.
  const navigate = (to) => {
    window.history.pushState({}, '', to);
    setCurrentPath(to);
  };

  /* This navigation context provider is the equivalent of React Router's BrowserRouter component. 
  It provides the current path and navigate function to all child components that consume this context. */
  return (
    <NavigationContext.Provider value={{ currentPath, navigate }}>
      {children}
    </NavigationContext.Provider>
  );
}

export { NavigationProvider };
export default NavigationContext;
