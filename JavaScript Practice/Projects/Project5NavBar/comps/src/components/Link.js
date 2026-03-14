import useNavigate from '../hooks/useNavigate';

function Link({ to, children, className, ...rest }) {
  const navigate = useNavigate();

  const handleClick = (event) => {
    /* If the user is opening in a new tab/window (cmd/ctrl click or middle click),
    let the browser do its normal behavior and do not hijack it. */
    if (
      event.metaKey ||
      event.ctrlKey ||
      event.shiftKey ||
      event.altKey ||
      event.button !== 0
    ) {
      return;
    }

    event.preventDefault();
    navigate(to);
  };

  return (
    <a {...rest} href={to} onClick={handleClick} className={className}>
      {children}
    </a>
  );
}

export default Link;
