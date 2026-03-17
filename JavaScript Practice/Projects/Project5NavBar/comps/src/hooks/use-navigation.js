import { useContext } from 'react';
import NavigationContext from '../context/navigation';

function useNavigation() {
  // Custom hook wrapper so components don't import/useContext(NavigationContext) directly.
  return useContext(NavigationContext);
}

export default useNavigation;
