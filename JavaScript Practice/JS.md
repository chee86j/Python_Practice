# 🔁 JavaScript Refresher – SparkNotes Edition

📦 **Assets**

- [Zip](#)
- [PDF](#)
- [Slides - Link](#)

---

## 🚀 Why JavaScript is Awesome

JavaScript powers interactive web experiences. It’s used for both frontend (in the browser) and backend (with Node.js). Versatile, dynamic, and essential in full-stack development.

---

## 🧱 Primitives & The Console

JavaScript has primitive types: `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, and `bigint`. Use `console.log()` for quick inspection during development.

```js
console.log("Hello, JS!");
```

---

## 🔢 JavaScript Numbers

JS uses one numeric type for all numbers. Integers and floats are treated the same.

```js
let total = 10 + 3 * 2;
```

---

## 🧠 WTF is NaN?

NaN = Not a Number. It happens when math fails, like dividing 0 by 0 or converting a non-number string.

```js
let result = Number("abc"); // NaN
```

---

## 🧮 Variables & `let`

Use `let` for block-scoped variables that may change. Avoid `var` for modern code.

```js
let score = 100;
```

---

## 🔄 Updating Variables

Update values with assignment and shorthand operators like `+=`, `-=`, etc.

```js
points += 3;
```

---

## ➕ Increment Operator

Use `++` to increment numbers. Know the difference between pre- and post-increment.

```js
count++; // uses then adds
++count; // adds then uses
```

---

## 📌 `const` & `var`

- `const`: value can’t be reassigned.
- `var`: function-scoped and legacy — avoid when possible.

---

## ✅ Booleans

Used for logic. Perfect for conditionals and truthy/falsey checks.

```js
let isReady = true;
if (isReady) console.log("Go!");
```

---

## 🧠 Variable Naming & Conventions

Use `camelCase`. Be descriptive. Don’t start with numbers or use dashes.

```js
let userAge = 30;
```

---

🧪 **Quick Recap**

- Use `let`/`const`, skip `var`
- `console.log()` is your best friend
- Know JS types: dynamic, but predictable with practice
- Keep variable names clear and meaningful

---
