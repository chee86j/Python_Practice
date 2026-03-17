import classNames from 'classnames';
import useNavigation from '../hooks/use-navigation';

/* Equivalent to React Router's <Link>:
it renders a real <a> for semantics/accessibility, then intercepts normal left-click navigation. */
function Link({ to, children, className, activeClassName }) {
  const { navigate, currentPath } = useNavigation();

  const classes = classNames(
    'text-blue-500',
    className,
    currentPath === to && activeClassName
  );

  const handleClick = (event) => {
    // Match router-like behavior: do not hijack modified clicks or non-left-clicks.
    if (
      event.metaKey ||
      event.ctrlKey ||
      event.shiftKey ||
      event.altKey ||
      event.button !== 0
    ) {
      return;
    }

    // Prevent full page reload, then do client-side URL/state update.
    event.preventDefault();
    navigate(to);
  };

  return (
    <a className={classes} href={to} onClick={handleClick}>
      {children}
    </a>
  );
}

export default Link;
