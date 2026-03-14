import NavLink from './NavLink';

function Navbar() {
  const links = [
    { label: 'Home', path: '/' },
    { label: 'Accordion', path: '/accordion' },
    { label: 'Dropdown', path: '/dropdown' },
    { label: 'Buttons', path: '/buttons' },
  ];

  const renderedLinks = links.map((link) => {
    return (
      <NavLink
        key={link.path}
        to={link.path}
        className='block rounded px-3 py-2 transition-colors hover:bg-neutral-200'
        activeClassName='bg-blue-100 text-blue-800 font-semibold'
      >
        {link.label}
      </NavLink>
    );
  });

  return (
    <aside className='sticky top-4 h-fit rounded border bg-neutral-100 p-2 shadow'>
      {/* Keeping this as a plain vertical list keeps the routing mechanics easy to trace while learning. */}
      <nav className='space-y-1'>{renderedLinks}</nav>
    </aside>
  );
}

export default Navbar;
