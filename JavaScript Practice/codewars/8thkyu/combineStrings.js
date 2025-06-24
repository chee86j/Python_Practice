// Grasshopper - Combine Strings
/*
Combine strings function
Create a function named combineNames/combine_names/CombineNames that accepts two parameters 
(first and last name). The function should return the full name.

Example:

With "James" as the first name and "Stevens" as the last name should return "James Stevens"

*/

// =====My Solution=========================================================================================
function combineNames(first, last) {
  return first + " " + last;
}
/*
This is the most straightforward solution, using the + operator to concatenate the two strings.
*/

// Top Voted Solutions

// =====Solution 1=====
/*
const combineNames = (...names) => names.join(' ');
*/

// =====Solution 2=====
/*
const combineNames = (a, b) => `${a} ${b}`;
*/

// =====Solution 3=====
/*
function combineNames(firstName, lastName) {
  if(typeof firstName === 'string' && typeof lastName === 'string') {
    if(firstName !== '' && lastName !== '') {
      return firstName + ' ' + lastName;
    }
    else {
      return 'Sorry firstname or lastname cannot be blank'
    }
  }
  
  else {
    return 'firstName and lastName must be a string';
  }
  
}
*/

// Title
/*


*/

// =====My Solution=========================================================================================

/*

  */

// Top Voted Solutions

// =====Solution 1=====
/*

  */

// =====Solution 2=====
/*

  */

// =====Solution 3=====
/*

  */
