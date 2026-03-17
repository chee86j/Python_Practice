import { Route as ReactRouterRoute } from 'react-router-dom';

/* Old custom Route code (replaced by react-router-dom):
function Route({ path, children }) {
  // old custom path-matching logic...
}
*/

// New version: re-export Route from react-router-dom.
export default ReactRouterRoute;
