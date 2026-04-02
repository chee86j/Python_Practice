/*  If we had custom routing functions instead of react router
import { createContext, useEffect, useState } from "react";

const NavigationContext = createContext();

function NavigationProvider({ children }) {
  // Store the browser's current path in React state so components can react
  // to navigation changes.
  const [currentPath, setCurrentPath] = useState(window.location.pathname);

  useEffect(() => {
    // When the user clicks the browser's back or forward buttons,
    // update currentPath so the UI stays in sync with the URL.
    const handler = () => {
      setCurrentPath(window.location.pathname);
    };

    window.addEventListener("popstate", handler);

    return () => {
      window.removeEventListener("popstate", handler);
    };
  }, []);

  // This custom navigate function changes the URL without a full page reload,
  // then updates React state so matching Route components can re-render.
  const navigate = (to) => {
    window.history.pushState({}, "", to);
    setCurrentPath(to);
  };

  // Provide both the current path and the navigate function to the rest
  // of the app through context.
  return (
    <NavigationContext.Provider value={{ currentPath, navigate }}>
      {children}
    </NavigationContext.Provider>
  );
}

export { NavigationProvider };
export default NavigationContext;
*/
