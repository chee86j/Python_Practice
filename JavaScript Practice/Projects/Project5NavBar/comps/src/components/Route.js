import { useContext } from 'react';
import NavigationContext from '../context/NavigationContext';

function Route({ path, children }) {
  const { currentPath } = useContext(NavigationContext);

  // Render children only when this route path matches the current browser path.
  if (currentPath !== path) {
    return null;
  }

  return children;
}

export default Route;
