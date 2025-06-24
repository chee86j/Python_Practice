// Student's Final Grade
/*
Description:
Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);

This function should return a number (final grade). There are four types of final grades:

100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
0, in other cases
Examples(Inputs-->Output):

100, 12 --> 100
99, 0 --> 100
10, 15 --> 100

85, 5 --> 90

55, 3 --> 75

55, 0 --> 0
20, 2 --> 0
*Use Comparison and Logical Operators.

*/

// =====My Solution=========================================================================================
function finalGrade(exam, projects) {
  if (exam > 90 || projects > 10) return 100;
  if ((exam > 75) & (projects >= 5)) return 90;
  if ((exam > 50) & (projects >= 2)) return 75;
  return 0;
}
/*
This is the most straightforward solution, using if statements to check the conditions 
and return the appropriate grade.

It uses the logical OR (||) and AND (&) operators to check the conditions. 
The time complexity is O(1) because it only checks the conditions once.
The space complexity is O(1) because it only uses a constant amount of memory.

This is best for readability and simplicity for this problem and easy to understand for beginners.
Compared to a switch statement, this is more readable and easier to understand.
*/

// Top Voted Solutions

// =====Solution 1=====
/*
function finalGrade (exam, projects) {
  if(exam > 90 || projects > 10) return 100;
  if(exam > 75 & projects >= 5) return 90;
  if(exam > 50 & projects >= 2) return 75;
  return 0;
}
*/

// =====Solution 2=====
/*
function finalGrade(exam, projects) {
    if (exam > 90 || projects > 10) return 100;
    if (exam > 75 && projects >= 5) return 90;
    if (exam > 50 && projects >= 2) return 75;
    return 0;
}
*/

// =====Solution 3=====
/*
const finalGrade = (exam, projects) => {
  return (
    exam > 90 || projects > 10 ? 100 :
    exam > 75 && projects >= 5 ? 90 :
    exam > 50 && projects >= 2 ? 75 : 0
  )
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
