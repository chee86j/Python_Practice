
/*
Complete the function, which calculates how much you need to tip based 
on the total amount of the bill and the service.

You need to consider the following ratings:

---Terrible: tip 0%
---Poor: tip 5%
---Good: tip 10%
---Great: tip 15%
---Excellent: tip 20%

The rating is case insensitive (so "great" = "GREAT"). If an UNRECOGNISED 
rating is received, then you need to return:

---"Rating not recognised" in Javascript, Python and Ruby...

---...or null in Java

---...or -1 in C#

Because you're a nice person, you ALWAY ROUND UP THE TIP, regardless of 
the service.
*/

// =====My Solution=========================================================================================
function calculateTip(amount, rating) {
  switch (rating.toLowerCase()) {
    case "terrible":
      return 0;
    case "poor":
      return Math.ceil(amount * 0.05);
    case "good":
      return Math.ceil(amount * 0.1);
    case "great":
      return Math.ceil(amount * 0.15);
    case "excellent":
      return Math.ceil(amount * 0.2);
    default:
      return "Rating not recognised";
  }
}

/*
My Solution is a switch statement that checks the rating and returns the tip amount.
It accounts for:
--Terrible: tip 0%
--Poor: tip 5%
--Good: tip 10%
--Great: tip 15%
--Excellent: tip 20%

It also accounts for an UNRECOGNISED rating by returning "Rating not recognised" & rounds up the tip amount.

The time and space complexity of my solution is O(1) because it only has one switch statement.
It is also a simple solution that is easy to understand and maintain for beginners.


*/

// Top Voted Solutions

// =====Solution 1=====
// const TIPS = {
// const TIPS = {
//   "terrible": 0.0,
//   "poor": 0.05,
//   "good": 0.1,
//   "great": 0.15,
//   "excellent": 0.2
// };

// const calculateTip = (amount, rating) => {
//   rating = rating.toLowerCase();
  
//   return rating in TIPS ? Math.ceil(TIPS[rating] * amount) : "Rating not recognised";
// };

// =====Solution 2=====
// function calculateTip(amount, rating) {
//   switch(rating.toLowerCase()){
//     case "terrible":return 0;
//     case "poor":return Math.ceil(amount * 0.05);
//     case "good":return Math.ceil(amount * 0.1);
//     case "great":return Math.ceil(amount * 0.15);
//     case "excellent":return Math.ceil(amount * 0.2);
//     default:return "Rating not recognised";
//   }
// }

// =====Solution 3=====
// function calculateTip(amount, rating) {
//   switch (rating.toLowerCase()) {
//     case "terrible":
//       return 0;
//       break;
//     case "poor":
//       return Math.ceil(amount * 0.05);
//       break;
//     case "good":
//       return Math.ceil(amount * 0.10);
//       break;
//     case "great":
//       return Math.ceil(amount * 0.15);
//       break;
//     case "excellent":
//       return Math.ceil(amount * 0.20);
//       break;
//     default:
//       return "Rating not recognised"
//   }
// }