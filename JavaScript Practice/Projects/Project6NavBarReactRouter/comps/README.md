This is a React Starter Project for use in Stephen Grider's courses on Udemy.

## Project Overview

We start with a simple button component to standardize the button styling and behavior.

The Prop Names will be listed below and they will be boolean values with the purpose
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
Every new variant needs its own `if` branch (or a long template literal), and it is easy to forget to keep the base styles consistent.

### With `classnames`
```jsx
import classNames from "classnames";

function Button({ primary, secondary, children }) {
  const buttonClass = classNames(
    "px-3 py-1.5 border rounded transition",
    {
      "bg-blue-500 border-blue-600": primary,
      "bg-green-500 border-green-600": secondary,
    }
  );

  return <button className={buttonClass}>{children}</button>;
}
```
`classnames` keeps the helper branches short, lets you reuse the same base string, and pairs nicely with the PropTypes validation so only one variant-specific class set is added at render time.

## Styling helpers

We pull in the `classnames` library so the `Button` component can build Tailwind-friendly class lists from whichever boolean variation prop is active. `classnames` lets us conditionally append the right utility classes (for colors, outlines, rounded corners, etc.) without string concatenation, which keeps the render code readable and consistent with the PropTypes validation above. Because `PropTypes.checkVariationValue` rejects more than one active variant, `classnames` only ever sees one mutually exclusive styling block, so it can reliably produce the button class list that matches the single prop that is true.


## useEffect & useRef

This next section will focus on how React components interact with native DOM events, especially for handling clicks outside a component like a dropdown.

- Adding document-wide click handlers
- Understanding event propagation: capture, target, and bubble phases
- Checking whether a clicked element is inside or outside a component
- Using `useEffect` with and without a cleanup function
- Understanding the `useEffect` dependency array
- Using `useRef` to reference DOM elements
- Explaining why `true` is sometimes passed as the third argument to `addEventListener`
- Issues with Element References i.e. <div classNames="w-48">

## Project5NavBar - Underlying navigation mechanics before React Router
This section builds a minimal client-side router so the "why" behind React Router is visible. We use `useState`, `useEffect`, and `useContext` to recreate the core mechanics in a small, inspectable way.

### Mapping to React Router concepts
- `NavigationProvider` -> similar responsibility to `BrowserRouter` (stores current path + navigation function in context).
- `navigate(to)` -> similar to `useNavigate()` (pushes a new history entry without a full page reload).
- `Link` -> similar to `<Link>` (renders `<a>`, prevents default left-click navigation, then calls `navigate`).
- `Route` -> simplified route matcher (renders children only when `currentPath === path`).
- `activeClassName` in custom `Link` -> lightweight replacement for `<NavLink>` active styling.

### Runtime flow (what actually happens)
1. Initial render reads `window.location.pathname` into React state.
2. Clicking a custom `Link` calls `event.preventDefault()` and then `window.history.pushState(...)`.
3. The provider updates `currentPath`, which causes `Route` components to re-check matches and re-render.
4. Browser back/forward buttons trigger `popstate`; the provider listens for that and re-syncs `currentPath`.

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

Compared with React Router, this project intentionally omits advanced features (nested routes, route params, loaders/actions, and transition APIs) so the fundamentals are easier to see.

## Project6NavBarReactRouter - Navigation with React Router
This builds on Project 5 and migrates navigation to `react-router-dom`. It also adds a modal demo rendered through a React portal.

### What is active in this repo now
- `src/index.js` wraps `<App />` in `<BrowserRouter>`.
- `src/App.js` defines route config with `<Routes>` and `<Route>`.
- `src/components/Sidebar.js` uses:
  - `<Link>` for normal navigation
  - `<NavLink>` for active-state styling
  - `useNavigate()` for programmatic navigation (`navigate('/buttons')`, `navigate(-1)`)
- `src/pages/ModalPage.js` shows `Modal` with local state.
- `src/components/Modal.js` uses `ReactDOM.createPortal(...)` and mounts into `.modal-container` in `index.html`.

### Current route map
- `/` -> `DropdownPage`
- `/accordion` -> `AccordionPage`
- `/buttons` -> `ButtonPage`
- `/button` -> `ButtonPage` (alias route)
- `/modal` -> `ModalPage`

### Runtime flow with React Router
1. The app bootstraps inside `<BrowserRouter>` so the URL/location state is managed by router context.
2. Clicking `Link`/`NavLink` updates the URL without a full page reload.
3. `<Routes>` evaluates matches and renders the route's `element`.
4. Back/forward browser actions update location and re-render the matched routes automatically.
5. `useNavigate` supports essential transitions and history moves.

### Active link styling in this version
`Sidebar` uses `NavLink` + `classnames`:
- base classes: always applied
- active classes: conditionally applied via `isActive`
- `end={link.path === '/'}` prevents `/` from being marked active on every route

### Modal notes
- The modal is rendered outside the normal component tree via portal.
- `index.html` includes `<div class="modal-container"></div>` as the portal target.
- This keeps layering predictable and helps overlays sit above routed page content.
