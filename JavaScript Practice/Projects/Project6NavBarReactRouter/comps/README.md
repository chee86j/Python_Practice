This is a React Starter Project for use in Stephen Grider's courses on Udemy.

## Project Overview

We start with a simple button component to standardize the button styling & behavior.

The Prop Names will be listed below & they will be boolean values with the purpose
of changing the button styling.:

- primary
- secondary
- success
- warning
- danger

- outline
- rounded

Of these props, only one can be true at a time. The rest will be false.
The button will be styled based on the prop that is true.

## Writing button classes

### Without `classnames`

```jsx
function Button({ primary, secondary, children }) {
  let className = "px-3 py-1.5 border";
  if (primary) className += " bg-blue-500 border-blue-600";
  if (secondary) className += " bg-green-500 border-green-600";

  return <button className={className}>{children}</button>;
}
```

Every new variant needs its own `if` branch (or a long template literal), & it is easy to forget to keep the base styles consistent.

### With `classnames`

```jsx
import classNames from "classnames";

function Button({ primary, secondary, children }) {
  const buttonClass = classNames("px-3 py-1.5 border rounded transition", {
    "bg-blue-500 border-blue-600": primary,
    "bg-green-500 border-green-600": secondary,
  });

  return <button className={buttonClass}>{children}</button>;
}
```

`classnames` keeps the helper branches short, lets you reuse the same base string, & pairs nicely with the PropTypes validation so only one variant-specific class set is added at render time.

## Styling helpers

We pull in the `classnames` library so the `Button` component can build Tailwind-friendly class lists from whichever boolean variation prop is active. `classnames` lets us conditionally append the right utility classes (for colors, outlines, rounded corners, etc.) without string concatenation, which keeps the render code readable & consistent with the PropTypes validation above. Because `PropTypes.checkVariationValue` rejects more than one active variant, `classnames` only ever sees one mutually exclusive styling block, so it can reliably produce the button class list that matches the single prop that is true.

## useEffect & useRef

This next section will focus on how React components interact with native DOM events, especially for handling clicks outside a component like a dropdown.

- Adding document-wide click handlers
- Understanding event propagation: capture, target, & bubble phases
- Checking whether a clicked element is inside or outside a component
- Using `useEffect` with & without a cleanup function
- Understanding the `useEffect` dependency array
- Using `useRef` to reference DOM elements
- Explaining why `true` is sometimes passed as the third argument to `addEventListener`
- Issues with Element References i.e. <div classNames="w-48">

## Project5NavBar - Underlying navigation mechanics before React Router

This section builds a minimal client-side router so the "why" behind React Router is visible. We use `useState`, `useEffect`, & `useContext` to recreate the core mechanics in a small, inspectable way.

### Mapping to React Router concepts

- `NavigationProvider` -> similar responsibility to `BrowserRouter` (stores current path + navigation function in context).
- `navigate(to)` -> similar to `useNavigate()` (pushes a new history entry without a full page reload).
- `Link` -> similar to `<Link>` (renders `<a>`, prevents default left-click navigation, then calls `navigate`).
- `Route` -> simplified route matcher (renders children only when `currentPath === path`).
- `activeClassName` in custom `Link` -> lightweight replacement for `<NavLink>` active styling.

### Runtime flow (what actually happens)

1. Initial render reads `window.location.pathname` into React state.
2. Clicking a custom `Link` calls `event.preventDefault()` & then `window.history.pushState(...)`.
3. The provider updates `currentPath`, which causes `Route` components to re-check matches & re-render.
4. Browser back/forward buttons trigger `popstate`; the provider listens for that & re-syncs `currentPath`.

### Visual flow (custom router vs React Router)

```text
CUSTOM ROUTER (this project)                     REACT ROUTER (library)
-------------------------------------            --------------------------------------
+-------------------------------+                +-------------------------------+
| Click <Link to="/buttons">   |                | Click <Link to="/buttons">   |
+---------------+---------------+                +---------------+---------------+
                |                                                |
                v                                                v
+-------------------------------+                +-------------------------------+
| handleClick(event)            |                | RR Link internals             |
| - preventDefault()            |                | - prevent default nav         |
| - navigate("/buttons")        |                | - trigger router navigate     |
+---------------+---------------+                +---------------+---------------+
                |                                                |
                v                                                v
+-------------------------------+                +-------------------------------+
| window.history.pushState(...) |                | navigate("/buttons")          |
| setCurrentPath("/buttons")    |                | (via router context)          |
+---------------+---------------+                +---------------+---------------+
                |                                                |
                v                                                v
+-------------------------------+                +-------------------------------+
| Context value changes         |                | Router state/location changes |
| -> React re-render            |                | -> React re-render            |
+---------------+---------------+                +---------------+---------------+
                |                                                |
                v                                                v
+-------------------------------+                +-------------------------------+
| <Route path="/buttons">       |                | <Route path="/buttons">       |
| currentPath === path ? render |                | route match -> render element |
+-------------------------------+                +-------------------------------+

Back/Forward (both):
window "popstate" -> update current path -> re-render matching route
```

Compared with React Router, this project intentionally omits advanced features (nested routes, route params, loaders/actions, & transition APIs) so the fundamentals are easier to see.

## Project6NavBarReactRouter - Navigation with React Router

This builds on Project 5 & migrates navigation to `react-router-dom`. It also adds a modal demo rendered through a React portal.

### What is active in this repo now

- `src/index.js` wraps `<App />` in `<BrowserRouter>`.
- `src/App.js` defines route config with `<Routes>` & `<Route>`.
- `src/components/Sidebar.js` uses:
  - `<Link>` for normal navigation
  - `<NavLink>` for active-state styling
  - `useNavigate()` for programmatic navigation (`navigate('/buttons')`, `navigate(-1)`)
- `src/pages/ModalPage.js` shows `Modal` with local state.
- `src/components/Modal.js` uses `ReactDOM.createPortal(...)` & mounts into `.modal-container` in `index.html`.

### Current route map

- `/` -> `DropdownPage`
- `/accordion` -> `AccordionPage`
- `/buttons` -> `ButtonPage`
- `/button` -> `ButtonPage` (alias route)
- `/modal` -> `ModalPage`

### Runtime flow with React Router

1. The app bootstraps inside `<BrowserRouter>` so the URL/location state is managed by router context.
2. Clicking `Link`/`NavLink` updates the URL without a full page reload.
3. `<Routes>` evaluates matches & renders the route's `element`.
4. Back/forward browser actions update location & re-render the matched routes automatically.
5. `useNavigate` supports essential transitions & history moves.

### Active link styling in this version

`Sidebar` uses `NavLink` + `classnames`:

- base classes: always applied
- active classes: conditionally applied via `isActive`
- `end={link.path === '/'}` prevents `/` from being marked active on every route

### Modal notes

- The modal is rendered outside the normal component tree via portal.
- `index.html` includes `<div class="modal-container"></div>` as the portal target.
- This keeps layering predictable & helps overlays sit above routed page content.

### Table

Current implementation:

- `TablePage` passes `data` (rows) & `config` (column definitions) into `Table`.
- `config` uses objects with:
  - `label`: text for the table header
  - `render(row)`: function that returns what to show in each cell for that column
- `Table` maps `config` once to render headers & maps it again per row to render cells.
- The table supports a var number of rows & columns.
- The number of columns does not need to match every property on each row object.

What this teaches:

- Data-driven UI: defined structure with configuration instead of hardcoding each column w/o the config.
- Passing behavior as props: `render` functions are passed from parent to child.
- Reusable component design: one `Table` can render many datasets regardless of type
- Separation of concerns:
  - `TablePage` decides what data/columns exist
  - `Table` decides how to draw the grid

### SortableTable

- Sortable columns for numbers & strings using the values returned by each column's `sortValue` function.
- Sort order cycles from unsorted to ascending to descending to unsorted.
- Clicking a different sortable header resets sorting to ascending for that newly selected column.
- `SortableTable` looks at each object in the config array.
- If a column object has a `sortValue` function, that column becomes sortable.
- `SortableTable` adds a custom `header` property so the column label becomes clickable.
- The `useSort` custom hook manages `sortOrder`, `sortBy`, `sortedData`, & `setSortColumn`.
- When the user clicks a sortable header, the sorted data is passed down to `Table`.
- Custom cell rendering (icons, badges, conditional colors).
- Derived cells computed from multiple properties.

### Custom Reuseable Hooks

- Custom hooks let us move related stateful logic out of a component & reuse it elsewhere.
- `useSort` groups together sorting state, derived sorted data, & the function used when a header is clicked.
- `useCounter` groups together `count`, the logging side effect, & the increment behavior for the counter example.
- The general workflow is:
  - identify logic in a component that belongs together
  - move it into a function whose name starts with `use`
  - pass in needed values through arguments
  - return the state & helper functions the component needs
- This keeps page components focused on rendering while the hooks manage reusable behavior.
