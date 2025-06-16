# Basic Calculator Project Instructions

## Project Overview

Build a basic calculator that performs arithmetic operations using HTML, CSS, and JavaScript. This project will help reinforce fundamental web development concepts.

## HTML Structure Requirements

1. Create a container `div` for the calculator
2. Create a display section using semantic HTML
   - Use an `input` or `div` element with appropriate attributes for the display
   - Make it read-only if using input
3. Create a grid of buttons using semantic HTML
   - Numbers 0-9
   - Operations (+, -, \*, /)
   - Clear (C) and Equals (=) buttons
   - Each button should have appropriate classes for styling

**Expected HTML Result:**

- A well-structured calculator layout
- Proper use of semantic elements
- Accessible elements with appropriate ARIA labels
- All buttons properly labeled and grouped

## CSS Styling Requirements

1. Style the calculator container
   - Fixed width and centered on page
   - Add padding and border-radius
   - Use box-shadow for depth
2. Style the display
   - Full width
   - Right-aligned text
   - Appropriate font size and padding
3. Create a grid layout for buttons
   - Use CSS Grid or Flexbox
   - Equal spacing between buttons
4. Style the buttons
   - Consistent size and spacing
   - Different colors for numbers vs operations
   - Hover and active states
   - Responsive design for different screen sizes

**Expected CSS Result:**

- Professional-looking calculator interface
- Responsive layout that works on different screens
- Clear visual hierarchy
- Interactive button states

## JavaScript Functionality Requirements

1. Create variables to store:
   - First number
   - Operation
   - Second number
   - Result
2. Implement event listeners for:
   - Number buttons (0-9)
   - Operation buttons (+, -, \*, /)
   - Equals button (=)
   - Clear button (C)
3. Create functions for:
   - Updating display
   - Performing calculations
   - Clearing calculator
   - Handling decimal points
   - Error handling (division by zero)

**Expected JS Result:**

- Calculator should:
  - Accept number input
  - Perform basic operations
  - Display results accurately
  - Handle errors gracefully
  - Clear display when needed

## Bonus Challenges

1. Add keyboard support
2. Add decimal point functionality
3. Add backspace button
4. Add memory functions (M+, M-, MR)
5. Add percentage calculations

## Learning Objectives

This project will test your understanding of:

- HTML semantic structure and forms
- CSS layout (Grid/Flexbox)
- CSS styling and responsiveness
- JavaScript event handling
- JavaScript math operations
- DOM manipulation
- Error handling

## Getting Started

1. Create three files:
   - `index.html`
   - `styles.css`
   - `script.js`
2. Start with the HTML structure
3. Add basic CSS styling
4. Implement JavaScript functionality
5. Test and debug
6. Add advanced features

## Testing Checklist

- [ ] Calculator displays correctly on different screen sizes
- [ ] All buttons are clickable and responsive
- [ ] Basic operations work correctly
- [ ] Error handling works (e.g., division by zero)
- [ ] Clear button resets the calculator
- [ ] Display updates correctly with user input
- [ ] Calculator handles decimal numbers correctly
- [ ] Visual feedback on button clicks works
