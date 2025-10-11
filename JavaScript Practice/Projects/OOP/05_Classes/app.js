class Color {
	constructor(r, g, b, name) {
		this.r = r;
		this.g = g;
		this.b = b;
		this.name = name;
	}
	innerRGB() {
		const { r, g, b } = this;
		return `${r}, ${g}, ${b}`;
	}
	rgb() {
		return `rgb(${this.innerRGB()})`;
	}
	rgba(a = 1.0) {
		return `rgba(${this.innerRGB()}, ${a})`;
	}
	hex() {
		const { r, g, b } = this;
		return (
			'#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)
		);
	}
}
const red = new Color(255, 67, 89, 'tomato');
const white = new Color(255, 255, 255, 'white');


/*	=====My Notes===== 
With ES6, we finally got a cleaner syntax for what we were already doing with constructor functions, but now with the
'class' keyword. Under the hood, it's still prototypes, but now it looks familiar to developers from other languages.
*/

class User {
	constructor(name, score) {
	  this.name = name;
	  this.score = score;
	}
  
	login() {
	  console.log(`${this.name} logged in`);
	}
  
	increaseScore() {
	  this.score++;
	  console.log(`${this.name} now has ${this.score} points`);
	}
  }
  
  const user1 = new User("Alice", 10);
  const user2 = new User("Bob", 20);
  
  user1.login();
  user2.increaseScore();
  
/* 
1. The 'constructor' runs automatically when you create a new instance.
2. Methods inside the class body are automatically added to the prototype.
3. So it's functionally identical to the constructor function example, but just much cleaner.
*/