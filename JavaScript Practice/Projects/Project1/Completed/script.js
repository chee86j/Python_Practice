const display = document.getElementById("display");
const buttons = document.querySelectorAll(".button");

console.log('Display element:', display);
console.log('Buttons found:', buttons.length);

if (!display) {
    console.error("Display element not found!");
    return;
}

// Initialize the display
display.value = "";

let firstNumber = "";
let operation = null;
let shouldResetDisplay = false;

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

function handleNumber(num) {
  if (shouldResetDisplay) {
    display.value = num;
    shouldResetDisplay = false;
  } else {
    display.value += num;
  }
}

function handleOperator(op) {
  if (display.value === "") return;
  
  if (operation !== null) {
    handleEquals();
  }
  
  firstNumber = display.value;
  operation = op;
  shouldResetDisplay = true;
}

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

function handleClear() {
  display.value = "";
  firstNumber = "";
  operation = null;
  shouldResetDisplay = false;
}

document.addEventListener("keydown", (event) => {
  const key = event.key;
  console.log('Key pressed:', key);

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
