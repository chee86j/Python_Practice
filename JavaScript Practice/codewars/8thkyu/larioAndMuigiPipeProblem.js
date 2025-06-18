/*
Issue
Looks like some hoodlum plumber and his brother has been running around and damaging your stages 
again.

The pipes connecting your level's stages together need to be fixed before you receive any more 
complaints.

The pipes are correct when each pipe after the first is 1 more than the previous one.

Task
Given a list of unique numbers sorted in ascending order, return a new list so that the values 
increment by 1 for each index from the minimum value up to the maximum value (both included).

Example
Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8
*/

// =====My Solution=========================================================================================
function pipeFix(numbers) {
  let fixedPipes = [];
  for (let i = numbers[0]; i <= numbers[numbers.length - 1]; i++) {
    fixedPipes.push(i);
  }
  return fixedPipes;
}

/*
My Solution is a for loop that iterates through the numbers array and pushes the numbers into the 
fixedPipes array. Compared to Solution 1, it is a more efficient solution because it does not use the 
Array.from method.

The time complexity of my solution is O(n) because it iterates through the numbers array once.
The space complexity of my solution is O(n) because it creates a new array to store the fixed pipes.

It works well for all array sizes and is simple and easy to understand for beginners.

*/

// Top Voted Solutions

// =====Solution 1=====
/*
function pipeFix(numbers){
  var first = numbers[0];
  var last = numbers[numbers.length-1];
  
  var arr = [];
  for(var i = first; i <= last; i++) {
    arr.push(i);
  }
  return arr;
}
*/

// =====Solution 2=====
/*
function pipeFix(numbers){
  var min = numbers[0];
  var max = numbers[numbers.length - 1];
  var array = [];
  
  for(var i = min; i<=max; i++)
  {
    array.push(i);
  }
  
  return array;
}
*/

// =====Solution 3=====
// let pipeFix = nums => Array.from({ length: nums.pop() - nums[0] + 1 }, (v, i) => i + nums[0]);
