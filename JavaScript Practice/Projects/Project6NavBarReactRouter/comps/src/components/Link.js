import classNames from 'classnames';
import { Link as RouterLink, NavLink } from 'react-router-dom';

/* Old custom Link code (replaced by react-router-dom):
function Link({ to, children, className, activeClassName }) {
  // old custom navigation logic...
}
*/

// New version: delegate routing behavior to react-router-dom.
function Link({ to, children, className, activeClassName }) {
  if (activeClassName) {
    return (
      <NavLink
        className={({ isActive }) =>
          classNames('text-blue-500', className, isActive && activeClassName)
        }
        end={to === '/'}
        to={to}
      >
        {children}
      </NavLink>
    );
  }

  return (
    <RouterLink className={classNames('text-blue-500', className)} to={to}>
      {children}
    </RouterLink>
  );
}

export default Link;
