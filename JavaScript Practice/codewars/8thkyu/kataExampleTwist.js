// This is an easy twist to the example kata (provided by Codewars when learning how to
// create your own kata).

// Add the value "codewars" to the array websites 1,000 times.

// ==============================================================================================
// add the value "codewars" to the websites array 1,000 times
let websites = [];

for (let i = 0; i < 1000; i++) {
  websites.push("codewars");
}

console.log(websites);

// Top Voted Solutions

// // =====Solution 1=====
// var websites = new Array(1000).fill("codewars");

// // =====Solution 2=====
// var websites = [];
// while (websites.length < 1000) websites.push("codewars");

// // =====Solution 3=====
// var websites = []
// for (i=0; i<1000; i++)
// {
//   websites.push("codewars");
// }
