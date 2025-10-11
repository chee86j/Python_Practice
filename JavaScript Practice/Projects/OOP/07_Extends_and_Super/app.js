class Pet {
	constructor(name, age) {
		console.log('IN PET CONSTRUCTOR!');
		this.name = name;
		this.age = age;
	}
	eat() {
		return `${this.name} is eating!`;
	}
}

class Cat extends Pet {
	constructor(name, age, livesLeft = 9) {
		console.log('IN CAT CONSTRUCTOR!');
		super(name, age);
		this.livesLeft = livesLeft;
	}
	meow() {
		return 'MEOWWWW!!';
	}
}

class Dog extends Pet {
	bark() {
		return 'WOOOF!!';
	}
	eat() {
		return `${this.name} scarfs his food!`;
	}
}

/*	=====My Notes===== 
Now let's look at how inheritance works in modern JavaScript with 'extends' and 'super'.
*/

class Animal {
	constructor(name) {
	  this.name = name;
	}
	speak() {
	  console.log(`${this.name} makes a noise.`);
	}
  }
  
  class Dog extends Animal {
	constructor(name, breed) {
	  super(name); // call parent constructor
	  this.breed = breed;
	}
	speak() {
	  super.speak(); // optional: call parent method
	  console.log(`${this.name} the ${this.breed} barks loudly!`);
	}
  }
  
  const dog = new Dog("Buddy", "Labrador");
  dog.speak();

/*
- 'extends' create a parent-child relationship (Dog inherits from Animal)
- 'super()' calls the parent class's constructor which is required before using 'this' in a child class.
- 'super.speak()' calls the parent's version of the method.
- This demonstrates both inheritance and polymorphism. -'speak() behaves differently depending on which class calls it

This structure keeps your code modular and DRY. You can build hierarchies like Animal -> Dog -> Puppy or 
Vehicle -> Car -> ElectricCar.
*/



/*	=====Wrapping Up - OOP - Advanced Concepts===== 
- Inheritance: Create a parent-child relationship between classes.
- Polymorphism: The same method name behaves differently depending on the class.
- Encapsulation: Keep related data and methods together.
- Abstraction: Hide complex details and show only essential features.

1. Prototypes - the foundation of how JS shares behavior.
2. Factory Functions - easy to read by duplicate methods.
3. Constructor Functions - more efficient, share methods via prototypes.
4. Classes - syntactic sugar for constructors and prototypes.
5. Extends and Super - inheritance and polymorphism in action.


So whether you're building a complext app or explaining this in an interview, the key takeaway is:
-Objects in JavaScript aren't magical - they're just linked to other objects.
-Inheritance is delegation.
-And classes are a cleaner way to do what prototypes already did.

*/