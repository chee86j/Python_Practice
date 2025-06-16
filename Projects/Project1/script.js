// TODO 1: Select DOM Elements
// - Get the display element
// - Get all button elements

// TODO 2: Create variables to store:
// - First number
// - Operation
// - Second number
// - Flag for resetting display

// TODO 3: Add Event Listeners
// - Add click events to all buttons
// - Consider using event delegation

// TODO 4: Create handler functions:

// handleNumber(num)
// - Update display with clicked number
// - Consider when to reset display

// handleOperator(op)
// - Store the first number
// - Store the operation
// - Prepare for second number input

// handleEquals()
// - Get the second number
// - Perform the stored operation
// - Update display with result
// - Handle division by zero
// - Reset calculator state

// handleClear()
// - Reset all variables
// - Clear the display

// BONUS Challenges:
// 1. Add decimal point handling
// 2. Add backspace functionality
// 3. Add keyboard support
// 4. Add error handling for invalid operations
// 5. Add memory functions (M+, M-, MR)

// Start with these functions:

function handleNumber(num) {
  // Your code here
}

function handleOperator(op) {
  // Your code here
}

function handleEquals() {
  // Your code here
}

function handleClear() {
  // Your code here
}

// DOM Elements
const display = document.getElementById("display");
const buttons = document.querySelectorAll(".btn");

// Variables to store calculator state
let firstNumber = "";
let operation = null;
let secondNumber = "";
let shouldResetDisplay = false;

// Add event listeners to all buttons
buttons.forEach((button) => {
  button.addEventListener("click", () => handleButton(button));
});

// Handle button clicks
function handleButton(button) {
  if (button.classList.contains("number")) {
    handleNumber(button.textContent);
  } else if (button.classList.contains("operator")) {
    handleOperator(button.textContent);
  } else if (button.classList.contains("equals")) {
    handleEquals();
  } else if (button.classList.contains("clear")) {
    handleClear();
  } else if (button.id === "backspace") {
    handleBackspace();
  } else if (button.id === "decimal") {
    handleDecimal();
  }
}

// Handle number input
function handleNumber(num) {
  if (shouldResetDisplay) {
    display.value = num;
    shouldResetDisplay = false;
  } else {
    display.value += num;
  }
}

// Handle operator input
function handleOperator(op) {
  if (operation !== null) handleEquals();
  firstNumber = display.value;
  operation = op;
  shouldResetDisplay = true;
}

// Handle equals button
function handleEquals() {
  if (operation === null) return;

  secondNumber = display.value;
  let result;

  switch (operation) {
    case "+":
      result = parseFloat(firstNumber) + parseFloat(secondNumber);
      break;
    case "-":
      result = parseFloat(firstNumber) - parseFloat(secondNumber);
      break;
    case "*":
      result = parseFloat(firstNumber) * parseFloat(secondNumber);
      break;
    case "/":
      if (secondNumber === "0") {
        display.value = "Error";
        return;
      }
      result = parseFloat(firstNumber) / parseFloat(secondNumber);
      break;
  }

  display.value = result;
  operation = null;
  firstNumber = "";
  secondNumber = "";
  shouldResetDisplay = true;
}

// Handle clear button
function handleClear() {
  display.value = "";
  firstNumber = "";
  secondNumber = "";
  operation = null;
}

// Handle backspace button
function handleBackspace() {
  display.value = display.value.slice(0, -1);
}

// Handle decimal point
function handleDecimal() {
  if (!display.value.includes(".")) {
    display.value += ".";
  }
}

// Add keyboard support
document.addEventListener("keydown", (event) => {
  const key = event.key;

  // Number keys
  if (/[0-9]/.test(key)) {
    handleNumber(key);
  }
  // Operator keys
  else if (["+", "-", "*", "/"].includes(key)) {
    handleOperator(key);
  }
  // Enter key for equals
  else if (key === "Enter") {
    handleEquals();
  }
  // Escape key for clear
  else if (key === "Escape") {
    handleClear();
  }
  // Backspace key
  else if (key === "Backspace") {
    handleBackspace();
  }
  // Decimal point
  else if (key === ".") {
    handleDecimal();
  }
});
