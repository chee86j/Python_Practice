import useNavigation from "../hooks/use-navigation";

function Route({ path, children }) {
  const { currentPath } = useNavigation();

  // Equivalent to a very small <Route>: render only when URL path matches.
  if (currentPath === path) {
    return children;
  }

  // Returning null means "render nothing" for non-matching paths.
  return null;
}

export default Route;
