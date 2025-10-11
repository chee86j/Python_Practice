/*
=====RGB=====
RGB stands for Red, Green, and Blue. This is the color model that is used to represent colors in digital images.
The RGB color model is a additive color model, which means that the colors are created by adding together the
three primary colors: red, green, and blue.

The RGB color model is a 3-dimensional color model, which means that it uses 3 values to represent a color.
The 3 values are the red, green, and blue values.

The RGB color model is a popular color model for digital images and is used in many applications.


=====HEX=====
HEX stands for Hexadecimal. This is the color model that is used to represent colors in digital images.
The HEX color model is a 6-digit hexadecimal number, which means that it uses 6 values to represent a color.
The 6 values are the red, green, and blue values.

The HEX color model is a popular color model for digital images and is used in many applications.

There are a few other color models like HSL, HSV, and CMYK, but RGB and HEX are the most popular.
*/


//This functions makes and returns an object every time it is called.
// The resulting objects all follow the same "recipe"
function makeColor(r, g, b) {
	const color = {};
	color.r = r;
	color.g = g;
	color.b = b;
	color.rgb = function() {
		const { r, g, b } = this;
		return `rgb(${r}, ${g}, ${b})`;
	};
	color.hex = function() {
		const { r, g, b } = this;
		return (
			'#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)
		);
	};
	return color;
}

const firstColor = makeColor(35, 255, 150);
firstColor.hex(); //firstColor.hex();
firstColor.rgb(); //"rgb(35, 255, 150)"

const black = makeColor(0, 0, 0);
black.rgb(); //"rgb(0, 0, 0)"
black.hex(); //"#0000s00"

/*	=====My Notes===== 
Factory Functions are the simplest way to create multple similar objects in JS.
They are just regular functions that return a new object.
*/

function createUser(name, score) {
	return {
	  name,
	  score,
	  login() {
		console.log(`${this.name} logged in`);
	  },
	  increaseScore() {
		this.score++;
		console.log(`${this.name} has ${this.score} points`);
	  }
	};
  }
  
  const user1 = createUser("Alice", 10);
  const user2 = createUser("Bob", 15);
  
  user1.login();
  user2.increaseScore();
  
/*
1. Each time we call 'createUser', it makes a new object with its own methods.
2. Now each object gets its own copy of 'login()' and 'increaseScore()'.
3. It is not efficient to do this for every user and that's where 'Prototypes', or
   'constructor functions' come in.
*/