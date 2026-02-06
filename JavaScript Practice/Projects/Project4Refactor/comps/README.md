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
