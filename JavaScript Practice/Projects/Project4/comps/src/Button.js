import PropTypes from "prop-types";
import classNames from "classnames";

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
  const baseClasses =
    "inline-flex items-center justify-center px-6 py-2 border-2 text-lg font-semibold transition-transform duration-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-400";

  const variantStyles = {
    primary: {
      fill: "bg-blue-500 border-blue-600 text-white",
      outline: "bg-white border-blue-600 text-blue-600",
    },
    secondary: {
      fill: "bg-white border-black text-black",
      outline: "bg-white border-black text-black",
    },
    success: {
      fill: "bg-green-500 border-green-600 text-white",
      outline: "bg-white border-green-600 text-green-600",
    },
    warning: {
      fill: "bg-yellow-400 border-yellow-500 text-white",
      outline: "bg-white border-yellow-500 text-white",
    },
    danger: {
      fill: "bg-red-500 border-red-600 text-white",
      outline: "bg-white border-red-600 text-red-600",
    },
  };

  const hasVariant = primary || secondary || success || warning || danger;

  const variantClass = classNames({
    [variantStyles.primary.fill]: primary && !outline,
    [variantStyles.primary.outline]: primary && outline,
    [variantStyles.secondary.fill]: secondary && !outline,
    [variantStyles.secondary.outline]: secondary && outline,
    [variantStyles.success.fill]: success && !outline,
    [variantStyles.success.outline]: success && outline,
    [variantStyles.warning.fill]: warning && !outline,
    [variantStyles.warning.outline]: warning && outline,
    [variantStyles.danger.fill]: danger && !outline,
    [variantStyles.danger.outline]: danger && outline,
    "bg-white border-black text-black": !hasVariant,
  });

  const classes = classNames(baseClasses, variantClass, {
    "rounded-full": rounded,
  });

  return <button className={classes}>{children}</button>;
}

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
