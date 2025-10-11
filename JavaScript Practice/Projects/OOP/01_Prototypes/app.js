//String.prototype is a "template object" for every single string.
//We could go crazy and add our own method called yell...
String.prototype.yell = function() {
	return `OMG!!! ${this.toUpperCase()}!!!!! AGHGHGHG!`;
};

'bees'.yell(); //"OMG!!! BEES!!!!! AGHGHGHG!"

//We can overwrite an existing Array method like pop (not a good idea):
Array.prototype.pop = function() {
	return 'SORRY I WANT THAT ELEMENT, I WILL NEVER POP IT OFF!';
};
const nums = [ 6, 7, 8, 9 ];
nums.pop(); // "SORRY I WANT THAT ELEMENT, I WILL NEVER POP IT OFF!"



/*
'.this' is a special keyword in JavaScript that refers to the object that the method is being called on.
It automatically points to the object that is calling the method.

Template Literals are a way to create strings that can contain variables.
They are denoted by backticks (`) and can contain placeholders for variables.
Variables are denoted by ${variableName}.

Template Literals are a more modern way to create strings in JavaScript.
They are more readable and easier to write than string concatenation.
*/



/*	=====My Notes===== 
JS is a Prototype-Based Language (Unlike other Class-Based Languages JS uses PROTOTYPE CHAINING)
Every prototype has an internal link to another object (called a prototype) and that prototype
can have a prototype, and so on... until we stop at null.
*/

const person = {
	name: 'John',
	greet() {
		console.log(`Hello, my name is ${this.name}`);
	}
}

const teacher = Object.create(person);	
teacher.name = 'Mr. Smith';
teacher.subject = 'Math';

teacher.greet();
console.log(Object.getPrototypeOf(teacher) === person); // true

/*
1. 'person' is our base object.
2. We use 'Object.create(person)' to make 'teacher', which also inherits from 'person'.
3. When we call 'teacher.greet()', it first looks in 'teacher' for a 'greet' method and if it doesn't find it,
   so it looks up the prototype chain and finds it in 'person'.
*/


/*
Intro to OOP (Object Oriented Programming)
OOP is a paradigm. It's a way of organizing code around objects that bundle data and methods together.
Objects are like blueprints for entities. You can think of a 'Car' object with properties like 'make', 'model', and
methods like 'start()' and 'stop()'.

There are 4 Key OOP Principles:
1. Encapsulation - keeping related data and methods together.
2. Abstraction - hiding the complex details and showing only the essential features in a simple interface.
3. Inheritance - reusing code from other classes or prototypes.
4. Polymorphism - the ability for different objects to respond to the same method in different ways.

*/