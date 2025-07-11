# Unit - 2 -> JavaScript
Introduciton to JavaScript: What is the javaScript and benefits of the language.
JavaScript language syntax, Variables declaration, Operators, Control Statements.
Error Handling, Understanding arrays, Function Declaration, Built in Functions.
Standard Date and Time Functions in java script.

## Content ->
## Introduction to JavaScript

---

### 1. What is JavaScript?

* **JavaScript** is a **high-level**, **interpreted**, **object-oriented** programming language used to make web pages **interactive** and **dynamic**.
* It is one of the **core technologies of the web**, along with **HTML** and **CSS**.
* JavaScript can be executed by **web browsers** directly without needing any compilation.
* It is a **scripting language** that follows the **ECMAScript** specification.

---

### 2. History and Evolution

| Year    | Event                                                                                              |
| ------- | -------------------------------------------------------------------------------------------------- |
| 1995    | JavaScript created by **Brendan Eich** at Netscape                                                 |
| 1996    | Submitted to ECMA for standardization as **ECMAScript**                                            |
| 1997    | First edition of **ECMAScript** released                                                           |
| 2009    | ECMAScript 5 (ES5) — major update                                                                  |
| 2015    | ECMAScript 6 (ES6 or ES2015) — added modern features like `let`, `const`, arrow functions, classes |
| Present | Updated yearly with new features (ES6 to ES2024)                                                   |

---

### 3. Characteristics of JavaScript

| Feature              | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| **Interpreted**      | Runs line by line in the browser without compilation            |
| **Lightweight**      | Small footprint; minimal resource usage                         |
| **Dynamic Typing**   | No need to declare variable types                               |
| **Event-driven**     | Responds to user actions like clicks, inputs, etc.              |
| **Prototype-based**  | Uses prototypes instead of classical inheritance                |
| **Cross-platform**   | Works on all major browsers and operating systems               |
| **Functional + OOP** | Supports both procedural and object-oriented programming styles |

---

### 4. Where JavaScript is Used

| Area                         | Use Case Example                                    |
| ---------------------------- | --------------------------------------------------- |
| **Web Development**          | Form validation, DOM manipulation, animations       |
| **Mobile Applications**      | Frameworks like React Native, Ionic                 |
| **Server-side Programming**  | Using Node.js to build backend services             |
| **Game Development**         | 2D/3D games using libraries like Phaser or Three.js |
| **IoT and Embedded Systems** | Controlling devices using Node.js                   |
| **Desktop Applications**     | Apps using Electron.js (e.g., Visual Studio Code)   |

---

### 5. Benefits of JavaScript

| Benefit                     | Description                                                                |
| --------------------------- | -------------------------------------------------------------------------- |
| **Client-side execution**   | Reduces server load by running logic in the browser                        |
| **Asynchronous capability** | Non-blocking behavior using events, callbacks, promises, and `async/await` |
| **Easy to learn and use**   | Simple syntax, accessible to beginners                                     |
| **Large ecosystem**         | Thousands of libraries (e.g., jQuery, React, Angular, Vue)                 |
| **Browser compatibility**   | Supported by all modern browsers without plugins                           |
| **Integration**             | Works well with HTML, CSS, APIs, and server-side tech                      |
| **Real-time updates**       | Enables chat apps, live feeds, and data refresh without page reloads       |

---

### 6. Execution Environment

* JavaScript runs in the **browser’s JavaScript engine**, like:

  * **V8** (Chrome, Node.js)
  * **SpiderMonkey** (Firefox)
  * **JavaScriptCore** (Safari)
* Also runs **outside the browser** using **Node.js** (for backend development).

---

### 7. How JavaScript Enhances HTML and CSS

| Language | Purpose                                 |
| -------- | --------------------------------------- |
| **HTML** | Defines content and structure           |
| **CSS**  | Defines presentation and layout         |
| **JS**   | Adds behavior, interactivity, and logic |

---

### 8. Basic Example

```html
<!DOCTYPE html>
<html>
<head>
  <title>JS Example</title>
</head>
<body>
  <h1 id="msg">Hello</h1>
  <button onclick="changeText()">Click Me</button>

  <script>
    function changeText() {
      document.getElementById("msg").innerHTML = "Welcome to JavaScript!";
    }
  </script>
</body>
</html>
```

---

### 9. Types of JavaScript Code Inclusion

| Method       | Description                            | Syntax Example                                    |
| ------------ | -------------------------------------- | ------------------------------------------------- |
| **Inline**   | Inside HTML elements                   | `<button onclick="alert('Hello')">Click</button>` |
| **Internal** | Inside `<script>` tag in HTML document | `<script> // JS Code </script>`                   |
| **External** | Linked `.js` file                      | `<script src="script.js"></script>`               |

---

### 10. Conclusion

* JavaScript is a **powerful**, **flexible**, and **essential** technology for modern web development.
* It enables the creation of **interactive**, **responsive**, and **intelligent** web applications by running scripts in browsers or on servers via Node.js.

## What is JavaScript?

---

### 1. Definition

* **JavaScript** is a **high-level**, **interpreted**, **dynamic**, and **object-oriented** scripting language.
* It is primarily used to make **web pages interactive**, providing **client-side** functionality like user interaction, data manipulation, animation, and more.
* JavaScript follows the **ECMAScript specification**, which standardizes the language across different environments.

---

### 2. Key Characteristics

| Feature                   | Description                                                             |
| ------------------------- | ----------------------------------------------------------------------- |
| **Scripting Language**    | Executes code at runtime without compilation.                           |
| **Client-Side**           | Runs directly in the user’s web browser (no server interaction needed). |
| **Object-Oriented**       | Supports objects, inheritance (via prototypes), and encapsulation.      |
| **Dynamic Typing**        | Variable types are determined at runtime (no need to declare types).    |
| **Event-Driven**          | Executes code in response to user actions (click, input, scroll, etc.). |
| **Cross-Platform**        | Works on all modern browsers and operating systems.                     |
| **First-Class Functions** | Functions can be passed as arguments, returned, or stored in variables. |

---

### 3. How JavaScript Works

* JavaScript code is executed by a **JavaScript engine** inside the browser (like V8 in Chrome).
* JavaScript interacts with:

  * **HTML** to manipulate content.
  * **CSS** to change styles dynamically.
  * **DOM (Document Object Model)** to access and modify elements.

---

### 4. Role in Web Development

| Technology     | Role                       |
| -------------- | -------------------------- |
| **HTML**       | Structure and content      |
| **CSS**        | Presentation and layout    |
| **JavaScript** | Behavior and interactivity |

---

### 5. Use Cases

| Area                   | Examples                                    |
| ---------------------- | ------------------------------------------- |
| **Web Interactivity**  | Form validation, dynamic content updates    |
| **Animations**         | Moving elements, fading effects             |
| **Games**              | 2D/3D games in the browser                  |
| **Mobile Apps**        | Apps using React Native, Ionic              |
| **Server-side**        | Backend using Node.js                       |
| **APIs and AJAX**      | Asynchronous HTTP requests for live content |
| **Data Visualization** | Graphs using libraries like Chart.js, D3.js |

---

### 6. Example Code

```html
<!DOCTYPE html>
<html>
<body>
  <h2 id="demo">Hello!</h2>
  <button onclick="changeText()">Click me</button>

  <script>
    function changeText() {
      document.getElementById("demo").innerHTML = "Welcome to JavaScript!";
    }
  </script>
</body>
</html>
```

---

### 7. Execution Environment

* JavaScript runs:

  * **In Browsers** (Chrome, Firefox, Safari, Edge)
  * **On Servers** using **Node.js**
  * **In Mobile and Desktop apps** using frameworks like Electron, React Native

---

### 8. Benefits

| Advantage       | Description                                             |
| --------------- | ------------------------------------------------------- |
| **Lightweight** | Minimal memory and CPU usage                            |
| **Flexible**    | Supports multiple programming styles (OOP, functional)  |
| **Integrated**  | Natively supported in browsers, no extra setup required |
| **Fast**        | Immediate execution by modern JS engines                |
| **Extensible**  | Works with APIs, libraries, and third-party services    |

---

### 9. Conclusion

* **JavaScript** is an essential language for **modern web development**.
* It enables the creation of **interactive**, **responsive**, and **dynamic** user experiences in web applications and beyond.

## Benefits of JavaScript

---

### 1. **Client-Side Execution**

* JavaScript runs directly in the user's **web browser**, reducing the need to communicate with the server for simple interactions.
* Enables **faster execution** of code and **immediate responses** to user actions.

---

### 2. **Easy to Learn and Use**

* Simple and intuitive **syntax**.
* Similar to languages like **C**, **Java**, and **Python**, making it easier for developers to adopt.
* Minimal setup is required; **no compiler** or build system needed for basic usage.

---

### 3. **Cross-Platform Compatibility**

* Works on **all major browsers** (Chrome, Firefox, Edge, Safari, Opera) and platforms (Windows, Linux, macOS).
* JavaScript code behaves **consistently across different environments**, especially when using modern ECMAScript standards.

---

### 4. **Asynchronous Programming Capabilities**

* JavaScript supports **non-blocking** behavior using:

  * **Callbacks**
  * **Promises**
  * **`async/await`**
* Enables real-time functionalities like:

  * Live content updates
  * Auto-refreshing feeds
  * Background data fetching without page reloads

---

### 5. **Rich Ecosystem and Community**

* Massive library and framework support:

  * **Frontend:** React, Angular, Vue
  * **Backend:** Node.js, Express
  * **Testing:** Jest, Mocha
  * **Build tools:** Webpack, Babel
* Access to millions of reusable packages via **npm (Node Package Manager)**.
* Large developer community provides extensive **resources**, **tutorials**, and **support**.

---

### 6. **Full Stack Development Capability**

* JavaScript can be used for both:

  * **Frontend development** (in the browser)
  * **Backend development** (using Node.js)
* Enables use of **a single language** throughout the entire development stack.

---

### 7. **Interactivity and Dynamic Content**

* Enables the creation of dynamic, interactive user interfaces by:

  * Modifying HTML elements via the **DOM**
  * Responding to **user events** (clicks, keystrokes, input)
  * Creating **animations**, **sliders**, and **forms**

---

### 8. **Integration with Other Web Technologies**

* Seamlessly integrates with:

  * **HTML** (structure)
  * **CSS** (presentation)
  * **APIs** (external services)
* Easily connects to:

  * REST APIs
  * Databases (via backend frameworks)
  * WebSockets for real-time data

---

### 9. **Rich Set of Built-in Features**

* Provides many built-in objects and functions:

  * **Math**, **Date**, **Array**, **JSON**
  * Browser-specific APIs like:

    * `alert()`, `confirm()`, `prompt()`
    * `setTimeout()`, `setInterval()`

---

### 10. **Support for Object-Oriented and Functional Programming**

* Supports:

  * **Object-oriented programming**: using objects, constructors, and classes
  * **Functional programming**: using functions as first-class citizens, closures, and higher-order functions

---

### 11. **Extensibility and Flexibility**

* JavaScript can be extended using:

  * Custom libraries
  * Third-party plugins
  * Frameworks and modules
* Can be used for:

  * Web apps
  * Mobile apps (React Native)
  * Desktop apps (Electron)
  * Games (Phaser.js)

---

### 12. **Rapid Prototyping and Development**

* Easy to write and test small programs.
* Fast development cycle, especially with browser developer tools (console, debugger, inspector).

---

### 13. **Support for Modern Features (ES6+)**

* New standards include:

  * `let`, `const`
  * Arrow functions (`=>`)
  * Classes
  * Template literals
  * Destructuring
  * Modules (`import`, `export`)
  * Spread/rest operators

---

### 14. **Wide Adoption and Job Demand**

* JavaScript is one of the **most used languages** in the world.
* High demand for JavaScript developers across various roles:

  * Frontend Developer
  * Full Stack Developer
  * JavaScript Engineer

---

### 15. **No External Dependencies for Basic Use**

* JavaScript is built into all modern browsers.
* No installations or compilers are needed for basic scripting.

---

### 16. **Security Capabilities**

* Supports secure features such as:

  * Form input validation
  * Cross-site scripting protection (when handled correctly)
  * Safe interaction with web APIs through modern standards

---

### 17. **Real-Time Application Support**

* Enables real-time applications like:

  * Live chat apps
  * Online multiplayer games
  * Stock trading platforms
  * News feed updates

---

### 18. **Support for Modular Programming**

* Allows code to be **modularized** using:

  * **ES Modules**
  * **CommonJS** (Node.js)
  * Helps in organizing large projects effectively

---

### 19. **Widespread Industry Adoption**

* Used by major companies: **Google**, **Facebook**, **Netflix**, **Amazon**, **Microsoft**
* Essential technology in all modern web-based products and services

---

### 20. **Browser Developer Tools**

* Modern browsers come with powerful tools:

  * JavaScript console
  * DOM inspector
  * Network monitor
  * Real-time debugging

---

### Conclusion

JavaScript is a **versatile**, **widely-used**, and **powerful** programming language that plays a critical role in both **frontend** and **backend** development, offering a wide range of benefits for developers building modern web and cross-platform applications.


## JavaScript Language Syntax

---

### 1. Case Sensitivity

* JavaScript is **case-sensitive**.

```javascript
let value = 10;
let Value = 20; // different from 'value'
```

---

### 2. Statements

* A **JavaScript statement** is a command that the browser executes.
* Statements end with a **semicolon (`;`)**, although it is optional in many cases.

```javascript
let x = 5;
let y = x * 2;
```

---

### 3. Code Blocks

* A **code block** is a group of statements enclosed in **curly braces `{}`**.

```javascript
{
  let a = 10;
  console.log(a);
}
```

---

### 4. Comments

#### Single-line comment

```javascript
// This is a single-line comment
```

#### Multi-line comment

```javascript
/* This is a 
   multi-line comment */
```

---

### 5. Identifiers

* **Identifiers** are names used to identify **variables**, **functions**, **arrays**, **objects**, etc.
* Rules for identifiers:

  * Can contain **letters**, **digits**, **underscores**, and **\$**
  * Cannot start with a **digit**
  * Cannot be a **reserved keyword**

```javascript
let user_name;
let $amount;
let _score;
```

---

### 6. Variables

* Declared using `var`, `let`, or `const`.

```javascript
var a = 10;    // function-scoped
let b = 20;    // block-scoped
const c = 30;  // constant (cannot be reassigned)
```

---

### 7. Data Types

| Type      | Example           |
| --------- | ----------------- |
| Number    | `10`, `3.14`      |
| String    | `"Hello"`, `'Hi'` |
| Boolean   | `true`, `false`   |
| Null      | `null`            |
| Undefined | `undefined`       |
| Object    | `{name: "John"}`  |
| Array     | `[1, 2, 3]`       |
| Function  | `function() {}`   |

---

### 8. Operators

#### Arithmetic Operators

```javascript
+  -  *  /  %  **  ++  --
```

#### Assignment Operators

```javascript
=  +=  -=  *=  /=  %=
```

#### Comparison Operators

```javascript
==  ===  !=  !==  >  <  >=  <=
```

#### Logical Operators

```javascript
&&  ||  !
```

---

### 9. Control Flow Syntax

#### If statement

```javascript
if (x > 0) {
  console.log("Positive");
}
```

#### If-else

```javascript
if (x > 0) {
  // ...
} else {
  // ...
}
```

#### Switch

```javascript
switch (day) {
  case 1: console.log("Mon"); break;
  case 2: console.log("Tue"); break;
  default: console.log("Other");
}
```

---

### 10. Loops

#### For loop

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

#### While loop

```javascript
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```

#### Do...while

```javascript
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 5);
```

---

### 11. Functions

```javascript
function greet(name) {
  return "Hello, " + name;
}
```

---

### 12. Objects

```javascript
let user = {
  name: "Alice",
  age: 25
};
```

---

### 13. Arrays

```javascript
let numbers = [10, 20, 30];
```

---

### 14. Template Literals (ES6)

```javascript
let name = "John";
let greeting = `Hello, ${name}`;
```

---

### 15. Strict Mode

* Enables stricter parsing and error handling.

```javascript
"use strict";
```

---

### 16. Conclusion

JavaScript syntax includes the rules and structures that define **how code is written and interpreted**, covering everything from variables, data types, operators, control structures, and function declarations, to modern ES6+ enhancements like template literals and strict mode.

## JavaScript Variable Declaration

---

### 1. What is a Variable?

* A **variable** is a **named container** used to **store data values**.
* Variables can hold different data types such as **numbers**, **strings**, **booleans**, **arrays**, **objects**, etc.
* JavaScript allows **dynamic typing**, so variables can hold any type of data.

---

### 2. Ways to Declare Variables

| Keyword | Scope Type     | Re-declaration | Re-assignment | Hoisting                               |
| ------- | -------------- | -------------- | ------------- | -------------------------------------- |
| `var`   | Function scope | Allowed        | Allowed       | Hoisted (initialized with `undefined`) |
| `let`   | Block scope    | Not allowed    | Allowed       | Hoisted (but not initialized)          |
| `const` | Block scope    | Not allowed    | Not allowed   | Hoisted (but not initialized)          |

---

### 3. Syntax

```javascript
var x = 5;       // using var
let y = 10;      // using let
const z = 15;    // using const
```

---

### 4. `var` Declaration

* **Function-scoped**
* Can be **re-declared** and **updated**
* **Hoisted** and initialized with `undefined`

```javascript
var a = 1;
var a = 2;  // Allowed

function testVar() {
  var x = 10;
  if (true) {
    var x = 20; // same variable as above
    console.log(x); // 20
  }
  console.log(x); // 20
}
```

---

### 5. `let` Declaration

* **Block-scoped**
* Can be **updated**, but **not re-declared** in the same scope
* Hoisted but **not initialized**

```javascript
let b = 5;
// let b = 10;  // Error: cannot re-declare in same block
b = 15;       // Allowed

function testLet() {
  let x = 10;
  if (true) {
    let x = 20; // different variable
    console.log(x); // 20
  }
  console.log(x); // 10
}
```

---

### 6. `const` Declaration

* **Block-scoped**
* Must be **initialized at declaration**
* Cannot be **re-assigned** or **re-declared**
* Value is **constant**, but for objects/arrays the content can still be modified

```javascript
const pi = 3.1415;
// pi = 3.14; // Error

const user = {
  name: "Alice"
};
user.name = "Bob"; // Allowed (modifying object property)
```

---

### 7. Declaration Without Initialization

* `var` and `let` can be declared without assigning a value

```javascript
var x;
let y;
console.log(x); // undefined
console.log(y); // undefined
```

* `const` must be initialized

```javascript
const z; // Error: Missing initializer in const declaration
```

---

### 8. Hoisting Behavior

* **Hoisting**: Variables declared with `var`, `let`, and `const` are moved to the top of their scope, but only `var` is initialized.

```javascript
console.log(a); // undefined
var a = 5;

console.log(b); // ReferenceError
let b = 10;
```

---

### 9. Variable Naming Rules

* Can include **letters**, **digits**, **underscore (\_)**, and **dollar sign (\$)**
* Must **not begin with a digit**
* Cannot use **reserved keywords** (`var`, `let`, `function`, etc.)

```javascript
let $name = "John";
let _score = 100;
let age3 = 25;
```

---

### 10. Global vs Local Variables

#### Global Variable:

* Declared **outside** any function
* Accessible **everywhere**

```javascript
let globalVar = "Accessible anywhere";
```

#### Local Variable:

* Declared **inside** a function or block
* Accessible **only within that scope**

```javascript
function example() {
  let localVar = "Only inside function";
}
```

---

### 11. Re-declaration and Re-assignment Summary

| Keyword | Re-declaration     | Re-assignment |
| ------- | ------------------ | ------------- |
| `var`   | Yes                | Yes           |
| `let`   | No (in same scope) | Yes           |
| `const` | No                 | No            |

---

### 12. Best Practices

* Prefer `let` for **mutable variables**
* Use `const` for **constants** and **unchanging references**
* Avoid `var` in modern JavaScript (to prevent scope confusion)

---

### 13. Conclusion

JavaScript supports flexible variable declaration through `var`, `let`, and `const`, each with specific scoping, reusability, and hoisting behaviors. Understanding these distinctions is essential for writing clean, predictable, and error-free code.

## JavaScript Operators

---

### 1. Definition

* **Operators** in JavaScript are **symbols or keywords** used to perform operations on operands (values and variables).
* Operands can be **literals**, **variables**, or **expressions**.

---

### 2. Types of Operators

| Type                 | Purpose                                      |
| -------------------- | -------------------------------------------- |
| Arithmetic Operators | Perform basic mathematical operations        |
| Assignment Operators | Assign values to variables                   |
| Comparison Operators | Compare values and return a Boolean          |
| Logical Operators    | Combine/negate boolean expressions           |
| Bitwise Operators    | Perform bit-level operations                 |
| Unary Operators      | Operate on a single operand                  |
| Ternary Operator     | Conditional expression (`condition ? x : y`) |
| String Operator      | Concatenate strings                          |
| Type Operators       | Determine type (`typeof`, `instanceof`)      |

---

### 3. Arithmetic Operators

| Operator | Name           | Example        | Result  |
| -------- | -------------- | -------------- | ------- |
| `+`      | Addition       | `5 + 2`        | `7`     |
| `-`      | Subtraction    | `5 - 2`        | `3`     |
| `*`      | Multiplication | `5 * 2`        | `10`    |
| `/`      | Division       | `10 / 2`       | `5`     |
| `%`      | Modulus        | `10 % 3`       | `1`     |
| `**`     | Exponentiation | `2 ** 3`       | `8`     |
| `++`     | Increment      | `a++` or `++a` | `a + 1` |
| `--`     | Decrement      | `a--` or `--a` | `a - 1` |

---

### 4. Assignment Operators

| Operator | Description         | Example   | Equivalent To |
| -------- | ------------------- | --------- | ------------- |
| `=`      | Assignment          | `a = 5`   | —             |
| `+=`     | Add and assign      | `a += 2`  | `a = a + 2`   |
| `-=`     | Subtract and assign | `a -= 2`  | `a = a - 2`   |
| `*=`     | Multiply and assign | `a *= 2`  | `a = a * 2`   |
| `/=`     | Divide and assign   | `a /= 2`  | `a = a / 2`   |
| `%=`     | Modulo and assign   | `a %= 2`  | `a = a % 2`   |
| `**=`    | Exponent and assign | `a **= 3` | `a = a ** 3`  |

---

### 5. Comparison Operators

| Operator | Description           | Example     | Result  |
| -------- | --------------------- | ----------- | ------- |
| `==`     | Equal to (loose)      | `5 == '5'`  | `true`  |
| `===`    | Equal to (strict)     | `5 === '5'` | `false` |
| `!=`     | Not equal (loose)     | `5 != '5'`  | `false` |
| `!==`    | Not equal (strict)    | `5 !== '5'` | `true`  |
| `>`      | Greater than          | `6 > 3`     | `true`  |
| `<`      | Less than             | `3 < 6`     | `true`  |
| `>=`     | Greater than or equal | `5 >= 5`    | `true`  |
| `<=`     | Less than or equal    | `4 <= 5`    | `true`  |

---

### 6. Logical Operators

| Operator | Name | Example         | Result  |        |   |         |        |
| -------- | ---- | --------------- | ------- | ------ | - | ------- | ------ |
| `&&`     | AND  | `true && false` | `false` |        |   |         |        |
| \`       |      | \`              | OR      | \`true |   | false\` | `true` |
| `!`      | NOT  | `!true`         | `false` |        |   |         |        |

---

### 7. Bitwise Operators

| Operator | Name                  | Example    | Binary Operation          |     |        |               |
| -------- | --------------------- | ---------- | ------------------------- | --- | ------ | ------------- |
| `&`      | AND                   | `5 & 1`    | `0101 & 0001 = 0001`      |     |        |               |
| \`       | \`                    | OR         | \`5                       | 1\` | \`0101 | 0001 = 0101\` |
| `^`      | XOR                   | `5 ^ 1`    | `0101 ^ 0001 = 0100`      |     |        |               |
| `~`      | NOT                   | `~5`       | `~0101 = 1010` (inverted) |     |        |               |
| `<<`     | Left shift            | `5 << 1`   | `0101 << 1 = 1010`        |     |        |               |
| `>>`     | Right shift           | `5 >> 1`   | `0101 >> 1 = 0010`        |     |        |               |
| `>>>`    | Zero-fill right shift | `-5 >>> 1` | fills with zeroes         |     |        |               |

---

### 8. Unary Operators

| Operator | Description                               | Example          | Result      |
| -------- | ----------------------------------------- | ---------------- | ----------- |
| `typeof` | Type of operand                           | `typeof 5`       | `"number"`  |
| `void`   | Evaluates expression, returns `undefined` | `void(0)`        | `undefined` |
| `delete` | Deletes a property                        | `delete obj.key` | Removes key |

---

### 9. Ternary Operator

* **Syntax**: `condition ? expr1 : expr2`
* Used for **short conditional expressions**.

```javascript
let age = 18;
let result = (age >= 18) ? "Adult" : "Minor";  // "Adult"
```

---

### 10. String Operator

* **Concatenation**: Combines strings using `+`

```javascript
let name = "John" + " " + "Doe";  // "John Doe"
```

* `+=` can also be used:

```javascript
let greeting = "Hello";
greeting += " World";  // "Hello World"
```

---

### 11. Type Operators

#### `typeof`

* Returns the **type of a variable or expression**

```javascript
typeof 123;         // "number"
typeof "hello";     // "string"
typeof true;        // "boolean"
typeof [1,2];       // "object"
typeof null;        // "object"
typeof undefined;   // "undefined"
```

#### `instanceof`

* Checks if an object is an **instance** of a constructor

```javascript
let arr = [1, 2, 3];
arr instanceof Array;    // true
arr instanceof Object;   // true
```

---

### 12. Operator Precedence (Highest to Lowest)

| Precedence Level | Example           |   |    |
| ---------------- | ----------------- | - | -- |
| Grouping         | `(a + b)`         |   |    |
| Member Access    | `object.property` |   |    |
| Function Call    | `myFunc()`        |   |    |
| Unary Operators  | `!a`, `typeof a`  |   |    |
| Multiplicative   | `*`, `/`, `%`     |   |    |
| Additive         | `+`, `-`          |   |    |
| Relational       | `>`, `<`, `>=`    |   |    |
| Equality         | `==`, `!=`, `===` |   |    |
| Logical AND      | `&&`              |   |    |
| Logical OR       | \`                |   | \` |
| Conditional      | `? :`             |   |    |
| Assignment       | `=`, `+=`, etc.   |   |    |

---

### 13. Conclusion

JavaScript provides a **rich set of operators** for performing calculations, assignments, comparisons, logical decisions, and type evaluations. Mastery of these operators is crucial for controlling logic, behavior, and data flow in JavaScript programs.

## JavaScript Control Statements

---

### 1. **Definition**

* **Control statements** are used to **control the flow** of execution in a program.
* They allow decisions to be made and actions to be repeated based on specific conditions.

---

### 2. **Types of Control Statements**

| Category        | Statements                                           |
| --------------- | ---------------------------------------------------- |
| **Conditional** | `if`, `if...else`, `if...else if`, `switch`          |
| **Looping**     | `for`, `while`, `do...while`, `for...in`, `for...of` |
| **Jump**        | `break`, `continue`, `return`                        |

---

### 3. **Conditional Statements**

---

#### A. `if` Statement

* Executes a block of code **if the condition is true**.

```javascript
let age = 20;
if (age >= 18) {
  console.log("You are an adult.");
}
```

---

#### B. `if...else` Statement

* Executes one block **if condition is true**, otherwise another block.

```javascript
let age = 16;
if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

---

#### C. `if...else if...else` Statement

* Allows **multiple conditions** to be checked in sequence.

```javascript
let marks = 85;
if (marks >= 90) {
  console.log("Grade A");
} else if (marks >= 75) {
  console.log("Grade B");
} else {
  console.log("Grade C");
}
```

---

#### D. `switch` Statement

* Selects one of many **code blocks** to execute based on a **fixed value**.

```javascript
let day = 2;
switch (day) {
  case 1: console.log("Monday"); break;
  case 2: console.log("Tuesday"); break;
  case 3: console.log("Wednesday"); break;
  default: console.log("Invalid day");
}
```

---

### 4. **Looping Statements**

---

#### A. `for` Loop

* Repeats a block of code **a fixed number of times**.

```javascript
for (let i = 1; i <= 5; i++) {
  console.log("Count:", i);
}
```

---

#### B. `while` Loop

* Repeats a block **while the condition is true**.

```javascript
let i = 0;
while (i < 3) {
  console.log(i);
  i++;
}
```

---

#### C. `do...while` Loop

* Executes block **at least once**, then checks the condition.

```javascript
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 3);
```

---

#### D. `for...in` Loop

* Iterates over **object properties**.

```javascript
let user = {name: "Alice", age: 25};
for (let key in user) {
  console.log(key + ": " + user[key]);
}
```

---

#### E. `for...of` Loop (ES6)

* Iterates over **iterable objects** like arrays or strings.

```javascript
let arr = [10, 20, 30];
for (let value of arr) {
  console.log(value);
}
```

---

### 5. **Jump Statements**

---

#### A. `break` Statement

* Terminates the **current loop or switch** statement.

```javascript
for (let i = 1; i <= 5; i++) {
  if (i == 3) break;
  console.log(i);  // Output: 1, 2
}
```

---

#### B. `continue` Statement

* Skips the **current iteration** and continues with the next one.

```javascript
for (let i = 1; i <= 5; i++) {
  if (i == 3) continue;
  console.log(i);  // Output: 1, 2, 4, 5
}
```

---

#### C. `return` Statement

* Exits a function and **returns a value**.

```javascript
function add(a, b) {
  return a + b;
}
let result = add(3, 4);  // result = 7
```

---

### 6. **Nested Control Structures**

* Control statements can be **nested** inside each other.

```javascript
for (let i = 1; i <= 3; i++) {
  if (i % 2 == 0) {
    console.log(i + " is even");
  } else {
    console.log(i + " is odd");
  }
}
```

---

### 7. **Labelled Statements**

* Labels can be used with `break` or `continue` in **nested loops**.

```javascript
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j == 1) break outer;
    console.log(i, j);
  }
}
```

---

### 8. **Conclusion**

JavaScript control statements are fundamental constructs that **govern the decision-making** and **repetition logic** in a program. They allow the execution path to change based on data and conditions, enabling dynamic and interactive behaviors.

## JavaScript Error Handling

---

### 1. **Definition**

* **Error handling** in JavaScript is the process of **detecting**, **responding to**, and **recovering from errors** that occur during code execution.
* JavaScript provides **built-in constructs** to manage errors gracefully without crashing the program.

---

### 2. **Types of Errors**

| Type                 | Description                                              | Example                                   |
| -------------------- | -------------------------------------------------------- | ----------------------------------------- |
| **Syntax Errors**    | Errors in the code structure or grammar                  | `if (x 5)` — missing operator             |
| **Runtime Errors**   | Errors that occur during program execution               | `undefinedVariable + 1`                   |
| **Logical Errors**   | Code runs but gives incorrect results due to logic flaws | Wrong formula for calculation             |
| **Type Errors**      | Using incompatible types or invalid operations on types  | `"abc" * 2` or `null.f()`                 |
| **Reference Errors** | Refers to an undefined variable                          | `console.log(x)` when `x` is not declared |

---

### 3. **`try...catch` Statement**

* The primary structure for error handling.
* **Syntax**:

```javascript
try {
  // code that may throw an error
} catch (error) {
  // code to handle the error
}
```

* **Example**:

```javascript
try {
  let x = y + 1;  // y is not defined
} catch (err) {
  console.log("Error occurred: " + err.message);
}
```

---

### 4. **`finally` Block**

* Optional block that runs **after try and catch**, regardless of the outcome.
* Used to **release resources**, **close connections**, or do **cleanup tasks**.

```javascript
try {
  let result = 10 / 0;
} catch (error) {
  console.log("Handled error");
} finally {
  console.log("This will always execute");
}
```

---

### 5. **Throwing Custom Errors (`throw`)**

* You can create and throw your own error messages using `throw`.

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero is not allowed");
  }
  return a / b;
}

try {
  divide(10, 0);
} catch (e) {
  console.log(e.message); // Division by zero is not allowed
}
```

---

### 6. **Error Object Properties**

| Property  | Description                            |
| --------- | -------------------------------------- |
| `name`    | Type of error (e.g., `ReferenceError`) |
| `message` | Human-readable description             |
| `stack`   | Stack trace (debugging info)           |

```javascript
try {
  null.f();  // error
} catch (err) {
  console.log(err.name);    // TypeError
  console.log(err.message); // Cannot read properties of null
}
```

---

### 7. **Built-in Error Types**

| Constructor      | Description                            |
| ---------------- | -------------------------------------- |
| `Error`          | Base error class                       |
| `SyntaxError`    | Invalid syntax                         |
| `ReferenceError` | Referencing a non-existent variable    |
| `TypeError`      | Using incorrect data type              |
| `RangeError`     | Value not in valid range               |
| `URIError`       | Malformed URI handling                 |
| `EvalError`      | Error related to the `eval()` function |

```javascript
let a = new TypeError("Wrong type");
throw a;
```

---

### 8. **Nested `try...catch`**

* You can nest multiple error-handling blocks.

```javascript
try {
  try {
    throw new Error("Inner error");
  } catch (e) {
    console.log("Inner:", e.message);
    throw e;
  }
} catch (e) {
  console.log("Outer:", e.message);
}
```

---

### 9. **Best Practices**

* Always catch expected errors to prevent app crashes.
* Provide **informative error messages** to users.
* Log critical errors for debugging.
* Avoid catching errors you don't intend to handle.
* Use `finally` for **clean-up logic** (e.g., closing files or connections).
* Avoid excessive use of `try...catch` in performance-critical sections.

---

### 10. **Conclusion**

JavaScript error handling is achieved using the `try...catch...finally` structure and `throw` statements. It helps prevent unexpected crashes and allows developers to manage exceptional situations in a controlled and user-friendly way.

## Understanding Arrays in JavaScript

---

### 1. **Definition**

* An **array** is a **special object** used to store **multiple values** in a **single variable**.
* Arrays are **ordered**, **indexed**, and can contain **heterogeneous data types** (numbers, strings, objects, functions, etc.).

```javascript
let colors = ["red", "green", "blue"];
```

---

### 2. **Array Declaration**

#### A. Using Array Literals (Preferred)

```javascript
let fruits = ["apple", "banana", "mango"];
```

#### B. Using the Array Constructor

```javascript
let fruits = new Array("apple", "banana", "mango");
```

#### C. Empty Array

```javascript
let emptyArray = [];
```

---

### 3. **Accessing Elements**

* Elements are accessed by **index**, starting from **0**.

```javascript
let arr = [10, 20, 30];
console.log(arr[0]); // 10
console.log(arr[2]); // 30
```

---

### 4. **Array Properties**

| Property | Description                    |
| -------- | ------------------------------ |
| `length` | Returns the number of elements |

```javascript
let items = [1, 2, 3];
console.log(items.length); // 3
```

---

### 5. **Common Array Methods**

| Method       | Description                             | Example             |
| ------------ | --------------------------------------- | ------------------- |
| `push()`     | Adds element to the **end**             | `arr.push("x")`     |
| `pop()`      | Removes last element                    | `arr.pop()`         |
| `shift()`    | Removes first element                   | `arr.shift()`       |
| `unshift()`  | Adds element to the **start**           | `arr.unshift("x")`  |
| `indexOf()`  | Returns index of element                | `arr.indexOf("x")`  |
| `includes()` | Checks if element exists                | `arr.includes("x")` |
| `splice()`   | Adds/removes elements at index          | `arr.splice(1, 2)`  |
| `slice()`    | Returns portion of array                | `arr.slice(1, 3)`   |
| `join()`     | Joins elements into string              | `arr.join(", ")`    |
| `concat()`   | Merges arrays                           | `arr.concat(arr2)`  |
| `reverse()`  | Reverses the array                      | `arr.reverse()`     |
| `sort()`     | Sorts elements (default is string sort) | `arr.sort()`        |

---

### 6. **Looping Through Arrays**

#### A. `for` Loop

```javascript
let nums = [10, 20, 30];
for (let i = 0; i < nums.length; i++) {
  console.log(nums[i]);
}
```

#### B. `for...of` Loop

```javascript
for (let num of nums) {
  console.log(num);
}
```

#### C. `forEach()` Method

```javascript
nums.forEach(function(num) {
  console.log(num);
});
```

---

### 7. **Multidimensional Arrays**

```javascript
let matrix = [
  [1, 2],
  [3, 4]
];
console.log(matrix[1][0]); // 3
```

---

### 8. **Array of Mixed Data Types**

```javascript
let mixed = [10, "text", true, { name: "John" }, [1, 2, 3]];
```

---

### 9. **Checking If a Value Is an Array**

```javascript
Array.isArray([1, 2, 3]);     // true
Array.isArray("text");        // false
```

---

### 10. **Modifying Elements**

```javascript
let names = ["Alice", "Bob"];
names[0] = "Charlie";  // ["Charlie", "Bob"]
```

---

### 11. **Emptying an Array**

```javascript
let arr = [1, 2, 3];
arr.length = 0;         // []
```

---

### 12. **Copying Arrays**

#### A. Using `slice()`

```javascript
let copy = arr.slice();
```

#### B. Using Spread Operator

```javascript
let copy = [...arr];
```

---

### 13. **Array Destructuring**

```javascript
let [a, b] = [10, 20];
console.log(a); // 10
console.log(b); // 20
```

---

### 14. **Map, Filter, Reduce (Advanced)**

| Method     | Description                                |
| ---------- | ------------------------------------------ |
| `map()`    | Creates a new array by applying a function |
| `filter()` | Filters elements based on condition        |
| `reduce()` | Reduces array to a single value            |

---

### 15. **Conclusion**

Arrays in JavaScript are powerful and flexible data structures that allow storing, manipulating, and traversing collections of values. They support various built-in methods for common tasks and are fundamental to efficient JavaScript programming.

## Function Declaration in JavaScript

---

### 1. **Definition**

* A **function** is a **block of code** designed to perform a **specific task**.
* Functions are **reusable** and can be called multiple times with different arguments.

---

### 2. **Syntax of Function Declaration**

```javascript
function functionName(parameters) {
  // function body
  return value;  // optional
}
```

---

### 3. **Example**

```javascript
function greet(name) {
  return "Hello, " + name;
}
console.log(greet("Alice"));  // Output: Hello, Alice
```

---

### 4. **Function Components**

| Part            | Description                                  |
| --------------- | -------------------------------------------- |
| `function`      | Keyword to declare a function                |
| `functionName`  | Identifier for the function                  |
| `parameters`    | Input values (optional, can be multiple)     |
| `return`        | Returns a value to the caller (optional)     |
| `function body` | Code block that defines the function’s logic |

---

### 5. **Calling a Function**

* Use the function name followed by parentheses.

```javascript
greet("John");
```

---

### 6. **Parameters and Arguments**

* **Parameters** are placeholders in the function declaration.
* **Arguments** are actual values passed when calling the function.

```javascript
function add(a, b) {
  return a + b;
}
add(5, 3);  // Arguments: 5 and 3
```

---

### 7. **Return Statement**

* Ends function execution and **returns a value**.

```javascript
function square(x) {
  return x * x;
}
```

* A function without `return` returns `undefined`.

---

### 8. **Default Parameters (ES6)**

* Provide **default values** for parameters.

```javascript
function greet(name = "Guest") {
  return "Hello, " + name;
}
greet();  // Output: Hello, Guest
```

---

### 9. **Function with No Parameters**

```javascript
function sayHello() {
  console.log("Hello!");
}
sayHello();
```

---

### 10. **Anonymous Functions**

* Functions without a name; often used in expressions.

```javascript
let greet = function(name) {
  return "Hi " + name;
};
```

---

### 11. **Function Expression**

* Assigning a function to a variable.

```javascript
let multiply = function(x, y) {
  return x * y;
};
```

---

### 12. **Arrow Functions (ES6)**

* Shorter syntax for anonymous functions.

```javascript
let add = (a, b) => a + b;
```

---

### 13. **Immediately Invoked Function Expression (IIFE)**

* Function that runs **immediately after declaration**.

```javascript
(function() {
  console.log("IIFE executed");
})();
```

---

### 14. **Function Scope**

* Variables declared inside a function are **not accessible** outside.

```javascript
function test() {
  let x = 10;
}
console.log(x);  // Error: x is not defined
```

---

### 15. **Nested Functions**

* A function inside another function.

```javascript
function outer() {
  function inner() {
    console.log("Inside inner");
  }
  inner();
}
```

---

### 16. **Hoisting of Function Declarations**

* Function declarations are **hoisted**, meaning they can be used before they are defined.

```javascript
sayHello();
function sayHello() {
  console.log("Hello!");
}
```

---

### 17. **Rest Parameters (ES6)**

* Allows variable number of arguments.

```javascript
function sum(...nums) {
  return nums.reduce((a, b) => a + b);
}
sum(1, 2, 3);  // 6
```

---

### 18. **Arguments Object (Pre-ES6)**

* `arguments` is an array-like object accessible inside functions.

```javascript
function showArgs() {
  console.log(arguments[0], arguments[1]);
}
```

---

### 19. **Pure vs Impure Functions**

| Type   | Description                              |
| ------ | ---------------------------------------- |
| Pure   | No side effects, returns same output     |
| Impure | Has side effects (e.g., modifies global) |

---

### 20. **Conclusion**

Function declarations in JavaScript are a fundamental concept that allow modular, reusable, and organized code. They support various features like parameters, default values, hoisting, and different styles of declaration to enhance flexibility and control.

## Built-in Functions in JavaScript

---

### 1. **Definition**

* **Built-in functions** are **predefined functions** provided by JavaScript to perform **common operations**.
* Available globally and **do not require external libraries**.
* Grouped under **global functions**, **Math**, **String**, **Array**, **Number**, **Date**, and **Object** categories.

---

### 2. **Global Functions**

| Function       | Description                                  | Example                              |
| -------------- | -------------------------------------------- | ------------------------------------ |
| `parseInt()`   | Converts a string to an integer              | `parseInt("42") → 42`                |
| `parseFloat()` | Converts a string to a floating-point number | `parseFloat("3.14") → 3.14`          |
| `isNaN()`      | Checks if a value is `NaN`                   | `isNaN("abc") → true`                |
| `isFinite()`   | Checks if value is a finite number           | `isFinite(100) → true`               |
| `eval()`       | Executes a string as JavaScript code         | `eval("2 + 2") → 4`                  |
| `encodeURI()`  | Encodes a URI                                | `encodeURI("https://a.com?a=1&b=2")` |
| `decodeURI()`  | Decodes an encoded URI                       | `decodeURI(...)`                     |

---

### 3. **Math Object Functions**

| Function              | Description               | Example                    |
| --------------------- | ------------------------- | -------------------------- |
| `Math.round(x)`       | Rounds to nearest integer | `Math.round(4.6) → 5`      |
| `Math.floor(x)`       | Rounds down               | `Math.floor(4.9) → 4`      |
| `Math.ceil(x)`        | Rounds up                 | `Math.ceil(4.1) → 5`       |
| `Math.max(a, b, ...)` | Returns largest number    | `Math.max(1, 2, 3) → 3`    |
| `Math.min(a, b, ...)` | Returns smallest number   | `Math.min(1, 2, 3) → 1`    |
| `Math.random()`       | Random number \[0, 1)     | `Math.random() → 0.123...` |
| `Math.abs(x)`         | Absolute value            | `Math.abs(-5) → 5`         |
| `Math.sqrt(x)`        | Square root               | `Math.sqrt(25) → 5`        |
| `Math.pow(x, y)`      | Power function (x^y)      | `Math.pow(2, 3) → 8`       |

---

### 4. **String Methods (Built-in Functions)**

| Function          | Description                              | Example                              |
| ----------------- | ---------------------------------------- | ------------------------------------ |
| `charAt(i)`       | Returns character at index `i`           | `"abc".charAt(1) → "b"`              |
| `indexOf(str)`    | Finds index of `str`                     | `"hello".indexOf("e") → 1`           |
| `includes(str)`   | Checks if string contains `str`          | `"hello".includes("ll") → true`      |
| `substring(a, b)` | Extracts substring from index `a` to `b` | `"abcdef".substring(1, 4)`           |
| `toUpperCase()`   | Converts to upper case                   | `"abc".toUpperCase() → "ABC"`        |
| `toLowerCase()`   | Converts to lower case                   | `"ABC".toLowerCase() → "abc"`        |
| `trim()`          | Removes whitespace                       | `"  abc  ".trim() → "abc"`           |
| `replace(a, b)`   | Replaces `a` with `b`                    | `"dog".replace("d", "f") → "fog"`    |
| `split()`         | Splits string into array                 | `"a,b,c".split(",") → ["a","b","c"]` |

---

### 5. **Array Methods (Built-in Functions)**

| Function     | Description                      | Example                       |
| ------------ | -------------------------------- | ----------------------------- |
| `push()`     | Adds to end                      | `[1,2].push(3) → [1,2,3]`     |
| `pop()`      | Removes last element             | `[1,2,3].pop() → 3`           |
| `shift()`    | Removes first element            | `[1,2,3].shift() → 1`         |
| `unshift()`  | Adds to beginning                | `[1,2].unshift(0) → [0,1,2]`  |
| `indexOf()`  | Returns index of element         | `[10,20].indexOf(20) → 1`     |
| `includes()` | Checks for element               | `[1,2].includes(2) → true`    |
| `join()`     | Converts array to string         | `["a","b"].join("-") → "a-b"` |
| `reverse()`  | Reverses array                   | `[1,2].reverse() → [2,1]`     |
| `sort()`     | Sorts array                      | `[2,1].sort() → [1,2]`        |
| `splice()`   | Add/remove at index              | `arr.splice(1, 1, 99)`        |
| `slice()`    | Extracts section                 | `[1,2,3].slice(0,2) → [1,2]`  |
| `map()`      | Applies function to each element | `[1,2].map(x => x * 2)`       |
| `filter()`   | Filters based on condition       | `[1,2].filter(x => x > 1)`    |
| `reduce()`   | Reduces to single value          | `[1,2,3].reduce((a,b)=>a+b)`  |

---

### 6. **Number Methods**

| Function             | Description                         | Example                       |
| -------------------- | ----------------------------------- | ----------------------------- |
| `toFixed(n)`         | Rounds number to `n` decimal places | `(2.345).toFixed(2) → "2.35"` |
| `toString()`         | Converts number to string           | `(100).toString() → "100"`    |
| `parseInt()`         | Converts string to integer          | `parseInt("20.5") → 20`       |
| `parseFloat()`       | Converts string to float            | `parseFloat("20.5") → 20.5`   |
| `Number.isInteger()` | Checks if value is integer          | `Number.isInteger(5) → true`  |

---

### 7. **Date Object Functions**

| Function         | Description                     | Example                  |
| ---------------- | ------------------------------- | ------------------------ |
| `new Date()`     | Creates new Date object         | `new Date()`             |
| `getFullYear()`  | Returns full year               | `date.getFullYear()`     |
| `getMonth()`     | Returns month (0–11)            | `date.getMonth()`        |
| `getDate()`      | Returns day of the month (1–31) | `date.getDate()`         |
| `getDay()`       | Returns day of week (0–6)       | `date.getDay()`          |
| `getHours()`     | Returns hour                    | `date.getHours()`        |
| `getMinutes()`   | Returns minutes                 | `date.getMinutes()`      |
| `getSeconds()`   | Returns seconds                 | `date.getSeconds()`      |
| `setFullYear(y)` | Sets the year                   | `date.setFullYear(2025)` |

---

### 8. **Object Methods**

| Function              | Description                            | Example                                |
| --------------------- | -------------------------------------- | -------------------------------------- |
| `Object.keys(obj)`    | Returns array of property names        | `Object.keys({a:1, b:2}) → ["a", "b"]` |
| `Object.values(obj)`  | Returns array of property values       | `Object.values({a:1, b:2}) → [1, 2]`   |
| `Object.entries(obj)` | Returns key-value pairs                | `Object.entries({a:1}) → [["a", 1]]`   |
| `Object.assign()`     | Copies values from one or more objects | `Object.assign({}, obj1, obj2)`        |
| `hasOwnProperty(key)` | Checks if object has the key           | `obj.hasOwnProperty("name")`           |

---

### 9. **Console Object Functions**

| Function          | Description                    | Example                    |
| ----------------- | ------------------------------ | -------------------------- |
| `console.log()`   | Prints output to console       | `console.log("Hello")`     |
| `console.error()` | Displays error message         | `console.error("Error!")`  |
| `console.warn()`  | Displays warning message       | `console.warn("Warning!")` |
| `console.table()` | Displays array/object in table | `console.table([1,2,3])`   |

---

### 10. **Conclusion**

JavaScript provides a wide range of **built-in functions** that help perform common tasks in **math**, **string processing**, **array manipulation**, **date handling**, and more. Mastery of these functions is essential for efficient and powerful programming.


## Standard Date Functions in JavaScript

---

### 1. **Definition**

* JavaScript provides the built-in `Date` object to work with **dates and times**.
* The `Date` object represents a **single moment in time** in a **platform-independent format**.

---

### 2. **Creating Date Objects**

| Syntax                                                          | Description                                  |
| --------------------------------------------------------------- | -------------------------------------------- |
| `new Date()`                                                    | Current date and time                        |
| `new Date(milliseconds)`                                        | Date based on milliseconds since Jan 1, 1970 |
| `new Date(dateString)`                                          | Date from a string format                    |
| `new Date(year, month, day, hour, minute, second, millisecond)` | Custom date components (month is 0-indexed)  |

#### Examples:

```javascript
let now = new Date();                            // Current date and time
let fromString = new Date("2025-07-10");         // Date from string
let fromNumbers = new Date(2025, 6, 10, 14, 30); // July 10, 2025, 14:30 (Month 6 = July)
```

---

### 3. **Getting Date Information**

| Method              | Description                     | Example             |
| ------------------- | ------------------------------- | ------------------- |
| `getFullYear()`     | Returns 4-digit year            | `2025`              |
| `getMonth()`        | Returns month (0–11)            | `0 = Jan, 11 = Dec` |
| `getDate()`         | Returns day of the month (1–31) | `10`                |
| `getDay()`          | Returns day of the week (0–6)   | `0 = Sunday`        |
| `getHours()`        | Returns hour (0–23)             | `14`                |
| `getMinutes()`      | Returns minutes (0–59)          | `30`                |
| `getSeconds()`      | Returns seconds (0–59)          | `45`                |
| `getMilliseconds()` | Returns milliseconds (0–999)    | `200`               |
| `getTime()`         | Milliseconds since Jan 1, 1970  | `timestamp`         |
| `Date.now()`        | Current timestamp               | `milliseconds`      |

---

### 4. **Setting Date Information**

| Method                | Description           | Example                     |
| --------------------- | --------------------- | --------------------------- |
| `setFullYear(y)`      | Sets the year         | `date.setFullYear(2030)`    |
| `setMonth(m)`         | Sets the month (0–11) | `date.setMonth(0)`          |
| `setDate(d)`          | Sets the day of month | `date.setDate(15)`          |
| `setHours(h)`         | Sets the hour         | `date.setHours(10)`         |
| `setMinutes(m)`       | Sets the minutes      | `date.setMinutes(45)`       |
| `setSeconds(s)`       | Sets the seconds      | `date.setSeconds(30)`       |
| `setMilliseconds(ms)` | Sets the milliseconds | `date.setMilliseconds(500)` |

---

### 5. **Formatting Dates (toString Methods)**

| Method                 | Output Example                        |
| ---------------------- | ------------------------------------- |
| `toString()`           | `"Thu Jul 10 2025 14:30:00 GMT+0530"` |
| `toDateString()`       | `"Thu Jul 10 2025"`                   |
| `toTimeString()`       | `"14:30:00 GMT+0530"`                 |
| `toLocaleDateString()` | `"10/7/2025"` or `"07/10/2025"`       |
| `toLocaleTimeString()` | `"2:30:00 PM"`                        |
| `toUTCString()`        | `"Thu, 10 Jul 2025 09:00:00 GMT"`     |
| `toISOString()`        | `"2025-07-10T09:00:00.000Z"`          |

---

### 6. **Comparing Dates**

```javascript
let d1 = new Date("2025-01-01");
let d2 = new Date("2025-12-31");

console.log(d1 < d2);  // true
console.log(d1.getTime() === d2.getTime()); // false
```

---

### 7. **Date Arithmetic**

* Add 7 days to a date:

```javascript
let date = new Date();
date.setDate(date.getDate() + 7);  // Adds 7 days
```

* Subtract 1 month:

```javascript
date.setMonth(date.getMonth() - 1);
```

---

### 8. **Parsing Dates**

| Function          | Description                       |
| ----------------- | --------------------------------- |
| `Date.parse(str)` | Parses a string into milliseconds |

```javascript
let timestamp = Date.parse("July 10, 2025");
let date = new Date(timestamp);
```

---

### 9. **Custom Date Formatting (Manual)**

```javascript
let d = new Date();
let day = d.getDate();
let month = d.getMonth() + 1;
let year = d.getFullYear();

console.log(`${day}-${month}-${year}`);  // e.g., 10-7-2025
```

---

### 10. **Conclusion**

JavaScript's `Date` object provides robust tools for working with **time**, **calendar**, and **timestamps**. Functions are available to **create**, **access**, **modify**, and **format** dates and times for all common use cases.

## Standard Time Functions in JavaScript

---

### 1. **Definition**

* JavaScript provides **built-in time-related functions** through the `Date` object and **timers** like `setTimeout()` and `setInterval()`.
* Time functions are used to **retrieve**, **manipulate**, **measure**, and **schedule** time-based operations.

---

### 2. **Getting Current Time Components**

Using the `Date` object:

```javascript
let now = new Date();
```

| Function            | Description                          | Example Output  |
| ------------------- | ------------------------------------ | --------------- |
| `getHours()`        | Returns current hour (0–23)          | `14` (for 2 PM) |
| `getMinutes()`      | Returns current minutes (0–59)       | `30`            |
| `getSeconds()`      | Returns current seconds (0–59)       | `45`            |
| `getMilliseconds()` | Returns current milliseconds (0–999) | `200`           |

```javascript
console.log(now.getHours());        // 0 to 23
console.log(now.getMinutes());      // 0 to 59
console.log(now.getSeconds());      // 0 to 59
console.log(now.getMilliseconds()); // 0 to 999
```

---

### 3. **Setting Time**

| Function              | Description       | Example                     |
| --------------------- | ----------------- | --------------------------- |
| `setHours(h)`         | Sets hour         | `date.setHours(10)`         |
| `setMinutes(m)`       | Sets minutes      | `date.setMinutes(45)`       |
| `setSeconds(s)`       | Sets seconds      | `date.setSeconds(30)`       |
| `setMilliseconds(ms)` | Sets milliseconds | `date.setMilliseconds(500)` |

```javascript
let date = new Date();
date.setHours(12);
date.setMinutes(15);
date.setSeconds(0);
```

---

### 4. **Timestamp Functions**

| Function     | Description                            | Output Example         |
| ------------ | -------------------------------------- | ---------------------- |
| `Date.now()` | Returns current time in milliseconds   | `1720619400000`        |
| `getTime()`  | Returns milliseconds since Jan 1, 1970 | `new Date().getTime()` |

```javascript
let timestamp = Date.now(); // milliseconds since epoch
```

---

### 5. **Timers**

Used to **schedule code execution**.

---

#### A. `setTimeout()`

* Executes a function **once after a delay** (in milliseconds).

```javascript
setTimeout(function() {
  console.log("Executed after 3 seconds");
}, 3000);
```

---

#### B. `clearTimeout()`

* Cancels a timeout.

```javascript
let timer = setTimeout(() => console.log("Delayed"), 5000);
clearTimeout(timer);
```

---

#### C. `setInterval()`

* Executes a function **repeatedly at specified intervals**.

```javascript
setInterval(function() {
  console.log("Every 1 second");
}, 1000);
```

---

#### D. `clearInterval()`

* Cancels an interval.

```javascript
let interval = setInterval(() => console.log("Repeat"), 1000);
clearInterval(interval);
```

---

### 6. **Measuring Execution Time**

```javascript
let start = Date.now();
// Code to be measured
for (let i = 0; i < 1000000; i++) {}
let end = Date.now();

console.log("Execution time: " + (end - start) + " ms");
```

---

### 7. **Formatting Time**

Custom display of current time:

```javascript
let now = new Date();
let hours = now.getHours().toString().padStart(2, '0');
let minutes = now.getMinutes().toString().padStart(2, '0');
let seconds = now.getSeconds().toString().padStart(2, '0');

console.log(`${hours}:${minutes}:${seconds}`); // e.g., "09:30:45"
```

---

### 8. **Time Comparison**

```javascript
let t1 = new Date("2025-07-10T10:00:00");
let t2 = new Date("2025-07-10T12:00:00");

console.log(t2 > t1);  // true
console.log(t2.getTime() - t1.getTime());  // 7200000 ms (2 hours)
```

---

### 9. **Converting Between Local and UTC Time**

| Function              | Description                    |
| --------------------- | ------------------------------ |
| `getUTCHours()`       | Hours in UTC                   |
| `getUTCMinutes()`     | Minutes in UTC                 |
| `getTimezoneOffset()` | Difference from UTC in minutes |

```javascript
let now = new Date();
console.log(now.getUTCHours());
console.log(now.getTimezoneOffset());  // e.g., -330 for IST
```

---

### 10. **Conclusion**

JavaScript provides comprehensive time functions via the `Date` object and timer methods (`setTimeout`, `setInterval`). These allow for retrieving, manipulating, comparing, and scheduling time-based operations efficiently in any application.

