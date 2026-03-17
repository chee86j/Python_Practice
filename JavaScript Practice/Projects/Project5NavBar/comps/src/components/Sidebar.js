import Link from './Link';

function Sidebar() {
  const links = [
    { label: 'Dropdown', path: '/' },
    { label: 'Accordion', path: '/accordion' },
    { label: 'Buttons', path: '/buttons' },
  ];
  const activeLinkClasses = 'font-bold border-l-4 border-blue-500 pl-2';

  const renderedLinks = links.map((link) => {
    return (
      <Link
        key={link.label}
        to={link.path}
        className="mb-3"
        // Similar to NavLink's active styling.
        activeClassName={activeLinkClasses}
      >
        {link.label}
      </Link>
    );
  });

  return (
    <div className="sticky top-0 flex max-h-screen flex-col items-start overflow-y-auto">
      {renderedLinks}
    </div>
  );
}

export default Sidebar;
