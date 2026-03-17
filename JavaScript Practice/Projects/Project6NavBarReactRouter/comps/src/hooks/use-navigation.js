import { useNavigate } from 'react-router-dom';

/* Old custom hook (replaced by react-router-dom hooks):
function useNavigation() {
  // old useContext(NavigationContext) logic...
}
*/

function useNavigation() {
  // New hook maps to react-router-dom programmatic navigation.
  return { navigate: useNavigate() };
}

export default useNavigation;
