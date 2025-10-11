// This is a Constructor Function...
function Color(r, g, b) {
	this.r = r;
	this.g = g;
	this.b = b;
}

//If you call it on its own like a regular function...
Color(35, 60, 190); //undefined
//It returns undefined. Seems useless!

// *****************
// THE NEW OPERATOR!
// *****************

// 1. Creates a blank, plain JavaScript object;
// 2. Links (sets the constructor of) this object to another object;
// 3. Passes the newly created object from Step 1 as the this context;
// 4. Returns this if the function doesn't return its own object.

Color.prototype.rgb = function() {
	const { r, g, b } = this;
	return `rgb(${r}, ${g}, ${b})`;
};

Color.prototype.hex = function() {
	const { r, g, b } = this;
	return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
};

Color.prototype.rgba = function(a = 1.0) {
	const { r, g, b } = this;
	return `rgba(${r}, ${g}, ${b}, ${a})`;
};

const color1 = new Color(40, 255, 60);
color1.hex();
const color2 = new Color(0, 0, 0);
color2.hex();



/*	=====My Notes===== 
In ES5, before classes existed, we used constructor functions to mimic classes.
*/

function User(name, score) {
	this.name = name;
	this.score = score;
  }
  
  User.prototype.login = function() {
	console.log(`${this.name} logged in`);
  };
  
  User.prototype.increaseScore = function() {
	this.score++;
	console.log(`${this.name} now has ${this.score} points`);
  };
  
  const user1 = new User("Alice", 10);
  const user2 = new User("Bob", 20);
  
  user1.login();
  user2.increaseScore();

/*
1. The 'new' keyword does 4 things:
	1. Creates a new empty object.
	2. Binds 'this' inside the constructor to that new object.
	3. Links that object automatically to the prototype.
	4. Returns the new object automatically.
2. Methods defined on 'User.prototype' are shared by all instances - much more efficient than
   factory functions.
*/