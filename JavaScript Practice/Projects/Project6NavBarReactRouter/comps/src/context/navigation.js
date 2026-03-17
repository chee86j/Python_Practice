import { createContext } from 'react';

/* Old custom navigation context/provider (replaced by BrowserRouter):
function NavigationProvider({ children }) {
  // old custom popstate + pushState sync logic...
}
*/

// New approach:
// BrowserRouter from react-router-dom now owns navigation state,
// so this custom context is no longer needed.
const NavigationContext = createContext(null);

function NavigationProvider({ children }) {
  return children;
}

export { NavigationProvider };
export default NavigationContext;
