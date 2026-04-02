/*  If we had custom routing functions instead of react router
import { useContext } from "react";
import NavigationContext from "../context/navigation";

function useNavigation() {
//   If we were building our own router instead of using react-router-dom,
//   this hook would give components access to our custom navigation context.
  
//   Expected values from NavigationContext:
  - currentPath: the current URL path
  - navigate: a function that changes the path without a full page reload
  
//   Example navigate implementation inside a provider:
  window.history.pushState({}, "", to);
  setCurrentPath(to);
  
//   Then components could do:
  const { currentPath, navigate } = useNavigation();
  navigate("/buttons");
  return useContext(NavigationContext);
}

export default useNavigation;
*/
