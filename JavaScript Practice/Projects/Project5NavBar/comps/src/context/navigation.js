import { createContext, useEffect, useState } from 'react';

const NavigationContext = createContext();

function NavigationProvider({ children }) {
  const [currentPath, setCurrentPath] = useState(window.location.pathname);

  useEffect(() => {
    // Keep React state synchronized with browser back/forward navigation.
    const handler = () => {
      setCurrentPath(window.location.pathname);
    };
    window.addEventListener('popstate', handler);

    return () => {
      // Cleanup mirrors addEventListener to avoid leaked listeners.
      window.removeEventListener('popstate', handler);
    };
  }, []);

  // Equivalent to router navigation APIs (e.g., useNavigate):
  // pushState changes URL without full refresh, then we sync React state.
  const navigate = (to) => {
    window.history.pushState({}, '', to);
    setCurrentPath(to);
  };

  // Equivalent role to <BrowserRouter>: provide navigation state/functions app-wide.
  return (
    <NavigationContext.Provider value={{ currentPath, navigate }}>
      {children}
    </NavigationContext.Provider>
  );
}

export { NavigationProvider };
export default NavigationContext;
