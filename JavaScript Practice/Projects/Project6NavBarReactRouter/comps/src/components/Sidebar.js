import classNames from "classnames";
import { Link, NavLink, useNavigate } from "react-router-dom";

function Sidebar() {
  const navigate = useNavigate();

  const links = [
    { label: "Dropdown", path: "/" },
    { label: "Accordion", path: "/accordion" },
    { label: "Buttons", path: "/buttons" },
    { label: "Modal", path: "/modal" },
    { label: "Table", path: "/table" },
    { label: "Counter", path: "/counter" },
  ];
  const baseLinkClasses = "mb-3 text-blue-500";
  const activeLinkClasses = "font-bold border-l-4 border-blue-500 pl-2";

  // Old custom Link code (replaced by NavLink):
  /*
  const renderedLinks = links.map((link) => {
    return (
      <Link
        key={link.label}
        to={link.path}
        className="mb-3"
        activeClassName={activeLinkClasses}
      >
        {link.label}
      </Link>
    );
  });
  */

  const renderedLinks = links.map((link) => {
    return (
      <NavLink
        key={link.label}
        to={link.path}
        className={({ isActive }) =>
          classNames(baseLinkClasses, isActive && activeLinkClasses)
        }
        end={link.path === "/"}
      >
        {link.label}
      </NavLink>
    );
  });

  return (
    <div className="sticky top-0 flex max-h-screen flex-col items-start overflow-y-auto">
      {/* Link example (react-router-dom Link): */}
      <Link className="mb-3 text-slate-700 underline" to="/">
        Home
      </Link>

      {renderedLinks}

      {/* useNavigate example (programmatic navigation): */}
      <button
        className="mt-2 rounded bg-blue-500 px-3 py-1 text-white"
        onClick={() => navigate("/buttons")}
        type="button"
      >
        Go To Buttons
      </button>
      <button
        className="mt-2 rounded border border-slate-300 px-3 py-1"
        onClick={() => navigate(-1)}
        type="button"
      >
        Back
      </button>
    </div>
  );
}

export default Sidebar;
