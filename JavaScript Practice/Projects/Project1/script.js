// TODO 1: Select DOM Elements
// - Get the display element
// - Get all button elements
const display = document.getElementById("display");
const buttons = document.querySelectorAll(".button");

// TODO 2: Create variables to store:
// - First number
// - Operation
// - Second number
// - Flag for resetting display
let firstNumber = "";
let operation = null;
let shouldResetDisplay = false;

// TODO 3: Add Event Listeners
// - Add click events to all buttons
// - Consider using event delegation
buttons.forEach((button) => {
  button.addEventListener("click", () => {
    if (button.classList.contains("number")) {
      handleNumber(button.textContent);
    } else if (button.classList.contains("operator")) {
      handleOperator(button.textContent);
    } else if (button.classList.contains("equals")) {
      handleEquals();
    } else if (button.classList.contains("clear")) {
      handleClear();
    }
  });
});

// TODO 4: Create handler functions:

// handleNumber(num)
// - Update display with clicked number
// - Consider when to reset display
function handleNumber(num) {
  if (shouldResetDisplay) {
    display.value = num;
    shouldResetDisplay = false;
  } else {
    display.value += num;
  }
}

// handleOperator(op)
// - Store the first number
// - Store the operation
// - Prepare for second number input
function handleOperator(op) {
  if (operation !== null) {
    handleEquals();
  }
  firstNumber = display.value;
  operation = op;
  shouldResetDisplay = true;
}

// handleEquals()
// - Get the second number
// - Perform the stored operation
// - Update display with result
// - Handle division by zero
// - Reset calculator state
function handleEquals() {
  if (!operation) return;

  const num1 = parseFloat(firstNumber);
  const num2 = parseFloat(display.value);
  let result;

  switch (operation) {
    case "+":
      result = num1 + num2;
      break;
    case "-":
      result = num1 - num2;
      break;
    case "*":
      result = num1 * num2;
      break;
    case "/":
      if (num2 === 0) {
        display.value = "Error";
        return;
      }
      result = num1 / num2;
      break;
  }

  display.value = result;
  operation = null;
  firstNumber = "";
  shouldResetDisplay = true;
}

// handleClear()
// - Reset all variables
// - Clear the display
function handleClear() {
  display.value = "";
  firstNumber = "";
  operation = null;
  shouldResetDisplay = false;
}

// Add keyboard support
document.addEventListener("keydown", (event) => {
  const key = event.key;

  if (/[0-9]/.test(key)) {
    handleNumber(key);
  } else if (["+", "-", "*", "/"].includes(key)) {
    handleOperator(key);
  } else if (key === "Enter") {
    handleEquals();
  } else if (key === "Escape") {
    handleClear();
  }
});
