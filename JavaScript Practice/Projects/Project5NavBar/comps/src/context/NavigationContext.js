import { createContext, useEffect, useState } from 'react';

const NavigationContext = createContext();

function NavigationProvider({ children }) {
  const [currentPath, setCurrentPath] = useState(window.location.pathname);

  useEffect(() => {
    /* This listener keeps our React state in sync with browser navigation
    like back/forward button clicks from the user. */
    const handler = () => {
      setCurrentPath(window.location.pathname);
    };

    window.addEventListener('popstate', handler);

    return () => {
      // Cleanup: remove listener on unmount so we do not leak handlers.
      window.removeEventListener('popstate', handler);
    };
  }, []);

  const navigate = (to) => {
    // pushState changes the URL without triggering a full page refresh.
    window.history.pushState({}, '', to);
    setCurrentPath(to);
  };

  return (
    <NavigationContext.Provider value={{ currentPath, navigate }}>
      {children}
    </NavigationContext.Provider>
  );
}

export { NavigationProvider };
export default NavigationContext;
