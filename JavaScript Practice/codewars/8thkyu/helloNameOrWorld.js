/*
Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given 
  or `name` = ""        => return "Hello, World!"

*/

// =====My Solution=========================================================================================
function hello(name) {
  // If no name is provided or it's an empty string, return the default greeting
  if (!name) {
    return "Hello, World!";
  }

  // Capitalize the first letter and lowercase the rest
  const formattedName = name[0].toUpperCase() + name.slice(1).toLowerCase();

  return `Hello, ${formattedName}!`;
}

/*
1. If the `name` is not provided or is an empty string, it returns "Hello, World!".
2. If a name is provided, it capitalizes the first letter and lowercases the rest
3. It then constructs the greeting string using template literals and returns it.
This solution is straightforward and easy to understand, making it suitable for beginners.

Note the use of Template Literals which uses backticks (``) to create a string that can include variables and expressions directly within the string.
This allows for cleaner and more readable string interpolation compared to traditional string concatenation.

*/


// Top Voted Solutions

// =====Solution 1=====
/*
const hello = s =>
  `Hello, ${s ? (s[0].toUpperCase() + s.slice(1).toLowerCase()) : 'World'}!`;
*/

// =====Solution 2=====
/*
function hello(name){
  if (name){
    return "Hello, " + name.substring(0,1).toUpperCase() + name.substring(1).toLowerCase() + '!';
  } else {
    return "Hello, World!";
  }
}
*/

// =====Solution 3=====
/*
function hello(name) {
  return `Hello, ${name ? name[0].toUpperCase() + name.slice(1).toLowerCase() : "World"}!`
}
*/
