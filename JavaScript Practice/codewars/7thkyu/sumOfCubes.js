// Sum of Cubes

/*
Write a function that takes a positive integer n, sums all the cubed values from 1 to n 
(inclusive), and returns that sum.

Assume that the input n will always be a positive integer.

Examples: (Input --> output)

2 --> 9 (sum of the cubes of 1 and 2 is 1 + 8)
3 --> 36 (sum of the cubes of 1, 2, and 3 is 1 + 8 + 27)
*/

// =====My Solution=========================================================================================
function sumCubes(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i ** 3;
  }
  return sum;
}

/* This is the best and most efficient solution for this problem that uses a for loop to iterate
   through the numbers 1 to n, and adds the cube of each number to the sum. The sum is then
   returned.

   The time complexity of this solution is O(n), where n is the input number. This is because the
   loop runs n times, and the cube operation is O(1).
   The space complexity of this solution is O(1), because it only uses a single variable to store 
   the sum.

   It is good for small arrays, but not for large arrays of numbers.
*/

// Top Voted Solutions

// =====Solution 1=====
/*
function sumCubes(n){
  if (n == 1) {
    return n**3;
  } else {
    return n**3 + sumCubes(n - 1);
  }
}
*/

/* This works best for small to medium arrays of numbers, but not for large n due to possible stack
   overflow. Compared to "My Solution", it is more efficient because it uses a recursive function 
   to calculate the sum of the cubes of the numbers in the array. 
   The time complexity of this solution is O(n), where n is the input number. This is because the
   recursive function calls itself n times, and the cube operation is O(1).
   The space complexity of this solution is O(n), because it uses a recursive function to store the
   sum of the cubes of the numbers in the array.
*/

// =====Solution 2=====The Math Formula Best for Performance=====
/*
function sumCubes(n) {
  return (n * (n + 1) / 2) ** 2;
}
*/

/* 
This solution is the best for large arrays of numbers. Compared to "My Solution", it is more 
efficient because it uses a single line of code to calculate the sum of the cubes of the numbers
in the array.
The time complexity of this solution is O(1), because it uses a single line of code to calculate 
the sum of the cubes of the numbers in the array.
The space complexity of this solution is O(1), because it only uses a single variable to store 
the sum of the cubes of the numbers in the array.
*/

// =====Solution 3=====
/*
const sumCubes = n => [...Array(n + 1).keys()].reduce((r, i) => r + i ** 3);
*/

/*
This solution is the single line of code solution. Compared to "My Solution", it is more efficient 
because it uses a single line of code to calculate the sum of the cubes of the numbers in the array.
The time complexity of this solution is O(n), where n is the input number. This is because the
reduce function runs n times, and the cube operation is O(1).
The space complexity of this solution is O(n), because it uses an array to store the numbers in 
the array.

Learning functional programming. It's clean, but not memory-efficient for very large n.
*/
