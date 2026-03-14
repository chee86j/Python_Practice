import classNames from 'classnames';
import { useContext } from 'react';
import NavigationContext from '../context/navigation';
import Link from './Link';

function NavLink({ to, children, className, activeClassName, ...rest }) {
  const { currentPath } = useContext(NavigationContext);

  const finalClassName = classNames(
    className,
    // We add activeClassName only when this link matches the current URL path.
    currentPath === to && activeClassName
  );

  return (
    <Link {...rest} to={to} className={finalClassName}>
      {children}
    </Link>
  );
}

export default NavLink;
