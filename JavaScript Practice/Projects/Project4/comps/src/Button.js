import PropTypes from "prop-types";

function Button({
  children,
  primary,
  secondary,
  success,
  warning,
  danger,
  outline,
  rounded,
}) {
  // This is the wrapper component
  // We will use the optional JS library prop-types since we are not using TypeScript

  return <button>{children}</button>; // This is the underlying Element
}

// When we make a custom component, we can pass in props to the component.
// We can also pass in children to the component.
// The children prop is a special prop that allows us to pass in content to the component.

// Quick reminder that primary={true} is the same as just primary
// This is because the prop is passed in as an object, and the key is the prop name.
// So, primary={true} is the same as primary: true.
// This is why we can just pass in primary instead of primary={true}.

Button.propTypes = {
  checkVariationValue: (primary, secondary, success, warning, danger) => {
    const count =
      Number(!!primary) +
      Number(!!secondary) +
      Number(!!success) +
      Number(!!warning) +
      Number(!!danger);

    if (count > 1) {
      return new Error(
        "Only one of primary, secondary, success, warning, or danger can be true"
      );
    }
  },
};

export default Button;
