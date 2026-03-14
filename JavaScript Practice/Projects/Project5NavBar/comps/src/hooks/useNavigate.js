import { useContext } from 'react';
import NavigationContext from '../context/NavigationContext';

function useNavigate() {
  const { navigate } = useContext(NavigationContext);
  return navigate;
}

export default useNavigate;
