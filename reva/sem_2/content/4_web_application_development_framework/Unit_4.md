# Unit - 4 -> Web Application Frameworks
Introduction to application development frameworks - AngularJS, ReacJS.
Angular JS: Introfuction ,Angular JS Expressions, Modules, Data Binding, Controllers.
DOM, Events, Forms, Validations.

## Content ->
## Introduction to Application Development Frameworks

---

### 1. **Definition**

* An **application development framework** is a software platform or set of tools that provides a **foundation** to build and deploy applications efficiently.
* It offers **pre-built components, libraries, and conventions** that help standardize development.
* Frameworks abstract common tasks and provide structure, reducing repetitive coding.

---

### 2. **Purpose**

* Accelerate the development process.
* Ensure consistency and maintainability.
* Facilitate best practices and design patterns.
* Simplify complex programming tasks (e.g., DOM manipulation, event handling).

---

### 3. **Key Characteristics**

* **Reusable Components:** UI widgets, data handling utilities, routing.
* **Modularity:** Code organization into modules or components.
* **Data Binding:** Synchronization between UI and data model.
* **Event Handling:** Built-in mechanisms to handle user interactions.
* **Templating:** Dynamic generation of HTML views.
* **Dependency Injection:** Managing components’ dependencies automatically (in some frameworks).
* **Two-way Data Binding:** (In some frameworks like AngularJS) automatic synchronization between model and view.

---

### 4. **Benefits**

* Reduces development time and effort.
* Enhances scalability and flexibility.
* Improves code quality and readability.
* Provides community support and rich ecosystems.
* Simplifies integration with APIs and backend services.

---

### 5. **Popular Web Application Frameworks**

| Framework     | Description                                                                                |
| ------------- | ------------------------------------------------------------------------------------------ |
| **AngularJS** | A full-featured MVC framework from Google focusing on two-way data binding and modularity. |
| **ReactJS**   | A JavaScript library by Facebook focusing on building UI components and one-way data flow. |
| **Vue.js**    | Progressive framework for building user interfaces with reactive components.               |

---

### 6. **Use Cases**

* Building dynamic, single-page web applications (SPA).
* Creating rich interactive user interfaces.
* Managing complex application state and data flows.
* Rapid prototyping and development of web apps.

---

### 7. **Summary**

* Application development frameworks provide reusable structures and tools to streamline web app development.
* They help manage UI, data, and events efficiently.
* Choosing the right framework depends on project requirements and developer preferences.

---

## AngularJS

---

### 1. **Definition**

* AngularJS is a **JavaScript-based open-source front-end web framework** developed by Google.
* Designed to build **dynamic single-page applications (SPAs)**.
* Extends HTML with additional attributes and binds data to HTML with **two-way data binding**.

---

### 2. **Key Features**

* **MVC Architecture:** Supports Model-View-Controller design pattern to separate application logic, data, and presentation.
* **Two-Way Data Binding:** Automatically synchronizes data between model (JavaScript objects) and view (HTML).
* **Directives:** Special HTML attributes that extend HTML’s functionality (e.g., `ng-model`, `ng-repeat`).
* **Dependency Injection:** Built-in service that makes components reusable and easier to test.
* **Templates:** Uses HTML-based templates to declare UI components.
* **Modules:** Helps organize code into logical units.
* **Controllers:** JavaScript functions that control the data and behavior of the view.
* **Services:** Singleton objects for sharing data and functions across components.
* **Filters:** Format data displayed to the user (e.g., currency, date).
* **Routing:** Enables navigation between different views without reloading the page.

---

### 3. **Architecture Overview**

* **Model:** Holds application data.
* **View:** HTML templates rendered to the user.
* **Controller:** Connects the model and view; contains business logic.
* **Scope:** Acts as a glue between controller and view; provides context for expressions.

---

### 4. **Example: Basic AngularJS App**

```html
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="myCtrl">
  
  <p>Enter your name:</p>
  <input type="text" ng-model="name">
  
  <h1>Hello, {{name}}!</h1>
  
  <script>
    angular.module('myApp', [])
      .controller('myCtrl', function($scope) {
        $scope.name = 'World';
      });
  </script>

</body>
</html>
```

* **Explanation:**

  * `ng-app` declares the AngularJS application.
  * `ng-controller` binds the controller.
  * `ng-model` binds input data to the model.
  * `{{name}}` expression displays the data in the view.

---

### 5. **Advantages**

* Reduces boilerplate code with directives and two-way binding.
* Supports modular development via modules and controllers.
* Simplifies development of SPAs with routing and deep linking.
* Large community and extensive documentation.
* Easily testable due to dependency injection.

---

### 6. **Limitations**

* Performance issues with large, complex applications (due to digest cycle).
* Steeper learning curve for beginners.
* AngularJS (1.x) is superseded by Angular (2+), which is a complete rewrite.

---

### 7. **Summary**

* AngularJS is a powerful framework for building dynamic web apps with rich UI.
* Offers two-way data binding, MVC architecture, and directives.
* Primarily used for single-page applications with structured code organization.

---

## ReactJS

---

### 1. **Definition**

* ReactJS (commonly called React) is an **open-source JavaScript library** for building user interfaces, developed and maintained by Facebook.
* Focuses primarily on building **component-based UI**.
* Designed for building **single-page applications** and complex interactive UIs.
* Uses a **virtual DOM** for efficient rendering and updates.

---

### 2. **Key Features**

* **Component-Based Architecture:** UI is built using reusable, self-contained components.
* **Virtual DOM:** A lightweight copy of the actual DOM that optimizes updates by minimizing direct DOM manipulation.
* **One-Way Data Binding:** Data flows from parent to child components, making state management predictable.
* **JSX Syntax:** JavaScript XML — a syntax extension allowing HTML-like code inside JavaScript.
* **Declarative:** You describe *what* the UI should look like, React handles the rendering.
* **State and Props:** Components maintain internal state and receive data via props.
* **Lifecycle Methods:** Methods to hook into different stages of a component’s life (mounting, updating, unmounting).
* **Unidirectional Data Flow:** Makes data flow predictable and easier to debug.
* **Ecosystem Support:** Integrates with libraries like Redux, React Router, etc.

---

### 3. **Basic React Component Example**

```jsx
import React, { useState } from 'react';

function Greeting() {
  const [name, setName] = useState('World');

  return (
    <div>
      <input 
        type="text" 
        value={name} 
        onChange={(e) => setName(e.target.value)} 
        placeholder="Enter your name" 
      />
      <h1>Hello, {name}!</h1>
    </div>
  );
}

export default Greeting;
```

* **Explanation:**

  * Functional component using React hooks (`useState`).
  * `name` is the state variable.
  * Input updates the state on change.
  * UI updates automatically based on state.

---

### 4. **Comparison to AngularJS**

| Feature          | ReactJS                                                   | AngularJS                       |
| ---------------- | --------------------------------------------------------- | ------------------------------- |
| Type             | Library focusing on UI                                    | Full-featured framework         |
| Data Binding     | One-way (parent → child)                                  | Two-way                         |
| DOM Manipulation | Virtual DOM for performance                               | Real DOM with digest cycle      |
| Learning Curve   | Moderate, requires understanding JSX and state management | Steeper, many built-in features |
| Architecture     | Component-based                                           | MVC pattern                     |

---

### 5. **Advantages**

* Highly performant due to virtual DOM.
* Component reusability increases maintainability.
* Large and active community with rich ecosystem.
* Can be used with various backends and APIs.
* Supports both class and functional components.

---

### 6. **Limitations**

* React is just a library, so requires additional tools for routing, state management.
* JSX syntax can be unfamiliar initially.
* Frequent updates require continuous learning.

---

### 7. **Summary**

* ReactJS is a declarative, component-based JavaScript library focused on building efficient and flexible UIs.
* Uses virtual DOM and one-way data flow for performance and predictability.
* Widely used in modern web application development.

---

## AngularJS: Introduction

---

### 1. **Definition**

* AngularJS is a **JavaScript-based open-source front-end web framework** developed by Google.
* Designed to create **dynamic, single-page web applications (SPAs)**.
* Extends HTML vocabulary by adding **custom attributes and elements** for building rich, interactive UI.

---

### 2. **Purpose**

* Simplifies development and testing of web applications.
* Provides a structured and maintainable approach to building client-side apps.
* Enables **two-way data binding** to synchronize the model and view automatically.

---

### 3. **Core Concepts**

* **MVC Architecture:** Separates an application into Model (data), View (UI), and Controller (logic).
* **Two-Way Data Binding:** Changes in the UI reflect immediately in the model and vice versa.
* **Directives:** Special markers on DOM elements (attributes, tags) that tell AngularJS to attach behavior or transform the DOM.
* **Dependency Injection:** Mechanism for injecting dependencies (services, factories) into components, making code modular and testable.
* **Templates:** HTML enhanced with AngularJS markup, defining the UI.
* **Modules:** Containers to organize application parts like controllers, services, directives.

---

### 4. **Key Advantages**

* Simplifies DOM manipulation with declarative syntax.
* Reduces boilerplate code with features like data binding and directives.
* Supports testing through dependency injection.
* Provides built-in services for HTTP, routing, animation, etc.
* Large community and extensive documentation.

---

### 5. **Example**

```html
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="myCtrl">
  
  <p>Enter your name:</p>
  <input type="text" ng-model="name">
  
  <h1>Hello, {{name}}!</h1>
  
  <script>
    angular.module('myApp', [])
      .controller('myCtrl', function($scope) {
        $scope.name = 'World';
      });
  </script>

</body>
</html>
```

* Shows basic two-way binding using `ng-model` and expression `{{name}}`.

---

### 6. **Summary**

* AngularJS is a framework that enhances HTML to build dynamic web applications.
* It uses MVC design, two-way data binding, and directives to simplify frontend development.
* Ideal for creating single-page applications with responsive user interfaces.

---

## AngularJS Expressions

---

### 1. **Definition**

* AngularJS expressions are **code snippets written inside double curly braces** `{{ }}` in the HTML.
* They are used to **bind data dynamically** to the HTML view.
* Evaluate **variables, operators, and functions** against the current scope and output the result.

---

### 2. **Purpose**

* Display data from the **model (scope)** directly in the HTML.
* Perform simple computations or string concatenations inside the view.
* Keep the view **dynamic and reactive** to changes in model data.

---

### 3. **Syntax**

```html
{{ expression }}
```

* The expression is evaluated against the current `$scope`.
* The result replaces the expression in the HTML output.

---

### 4. **Examples**

```html
<p>{{ 5 + 10 }}</p>           <!-- Output: 15 -->
<p>{{ name }}</p>             <!-- Outputs the value of 'name' from scope -->
<p>{{ name.toUpperCase() }}</p>  <!-- Calls function on string -->
<p>{{ 1 == 1 }}</p>           <!-- Outputs: true -->
```

---

### 5. **Supported Expressions**

* Literals: strings, numbers, booleans.
* Variables and properties from the scope.
* Arithmetic operators: `+`, `-`, `*`, `/`, `%`.
* Logical operators: `&&`, `||`, `!`.
* Conditional expressions: ternary operator `condition ? trueValue : falseValue`.
* Function calls defined in the scope.
* Access to array elements and object properties.

---

### 6. **Features**

* **No side effects:** Expressions are designed to be **safe** and should not change application state.
* Evaluated frequently during the AngularJS **digest cycle** for data binding updates.
* AngularJS **filters** can be used within expressions to format output.

---

### 7. **Filters in Expressions**

* Format or transform output data.
* Syntax: `{{ expression | filterName }}`

Example:

```html
<p>{{ birthday | date:'fullDate' }}</p>
<p>{{ name | uppercase }}</p>
```

---

### 8. **Example with Expressions**

```html
<div ng-controller="myCtrl">
  <p>{{ greeting + ', ' + name + '!' }}</p>
  <p>{{ age >= 18 ? 'Adult' : 'Minor' }}</p>
</div>

<script>
  angular.module('myApp', [])
    .controller('myCtrl', function($scope) {
      $scope.greeting = 'Hello';
      $scope.name = 'Crimson Genesis';
      $scope.age = 21;
    });
</script>
```

---

### 9. **Summary**

* AngularJS expressions allow embedding dynamic data and logic inside HTML views.
* They simplify updating UI based on model changes.
* Provide a concise and readable way to perform computations and display values in templates.

---

## AngularJS Modules

---

### 1. **Definition**

* An AngularJS **module** is a **container for the different parts** of an application like controllers, services, directives, filters, etc.
* It helps **organize code** into cohesive blocks for better maintainability and reusability.
* Every AngularJS application has at least one module called the **root module**.

---

### 2. **Purpose**

* Group related components and features.
* Define dependencies between different modules.
* Bootstrap the AngularJS application.

---

### 3. **Creating a Module**

```javascript
var app = angular.module('myApp', []);
```

* `'myApp'` is the **name** of the module.
* The second argument `[]` is the **array of dependencies** (other modules this module depends on).
* If the array is omitted, it refers to an **existing module**.

---

### 4. **Using Modules**

* Modules serve as the **main entry point** for an AngularJS app.
* Attach controllers, services, directives, etc., to modules:

```javascript
app.controller('myCtrl', function($scope) {
  $scope.message = "Hello, AngularJS Modules!";
});
```

* In HTML, the module is linked using `ng-app` directive:

```html
<body ng-app="myApp" ng-controller="myCtrl">
  {{ message }}
</body>
```

---

### 5. **Dependency Injection**

* Modules can depend on other modules to reuse functionality.

Example:

```javascript
var app = angular.module('myApp', ['ngRoute', 'ngAnimate']);
```

* `ngRoute` and `ngAnimate` are built-in AngularJS modules injected as dependencies.

---

### 6. **Multiple Modules**

* Large applications can be broken down into **multiple modules** for scalability.
* These modules can be composed and injected as dependencies.

---

### 7. **Summary**

* Modules are the **foundation** of AngularJS applications.
* They organize application code logically.
* Manage dependencies between components.
* Bootstrap and configure the app.

---

## AngularJS Data Binding

---

### 1. **Definition**

* Data binding in AngularJS is the **automatic synchronization** between the **model** (JavaScript variables) and the **view** (HTML).
* It connects the UI and the data so that changes in one automatically update the other.

---

### 2. **Types of Data Binding in AngularJS**

#### a. **Two-Way Data Binding**

* Changes in the **model** update the **view**.
* Changes in the **view** (user input) update the **model**.
* Achieved using directives like `ng-model`.

**Example:**

```html
<input type="text" ng-model="name">
<p>Hello, {{name}}!</p>
```

* Typing in the input box updates `name`.
* The paragraph automatically reflects the updated `name`.

---

#### b. **One-Way Data Binding**

* Data flows from the **model to the view** only.
* Changes in the model update the view, but changes in the view do not affect the model.
* Used with expressions like `{{ }}`.

---

### 3. **How It Works**

* AngularJS uses a **digest cycle** to watch for changes in scope variables.
* When a model changes, AngularJS updates the view automatically.
* When user interacts with the view, AngularJS updates the model automatically.

---

### 4. **Advantages**

* Reduces the need for manual DOM manipulation.
* Keeps UI and data in sync effortlessly.
* Simplifies development and improves maintainability.

---

### 5. **Summary**

* Data binding is a key feature of AngularJS enabling seamless synchronization between model and view.
* Two-way data binding allows interactive and dynamic web applications with minimal code.
* One-way binding is used for simple data display.

---

## AngularJS Controllers

---

### 1. **Definition**

* Controllers in AngularJS are **JavaScript functions** that contain the business logic for a specific part of the application.
* They are responsible for **managing the data (model)** and **interacting with the view** via the `$scope` object.
* Controllers act as the **bridge** between the model and the view.

---

### 2. **Role**

* Initialize the model data.
* Define behavior and functions accessible from the view.
* Respond to user inputs and update the model accordingly.
* Facilitate communication between the view and other services or components.

---

### 3. **Creating a Controller**

```javascript
angular.module('myApp', [])
  .controller('myCtrl', function($scope) {
    $scope.message = "Hello, AngularJS Controllers!";
  });
```

* `'myCtrl'` is the controller name.
* `$scope` is injected and used to expose data and functions to the view.

---

### 4. **Using Controller in HTML**

```html
<div ng-app="myApp" ng-controller="myCtrl">
  <p>{{ message }}</p>
</div>
```

* `ng-controller` directive associates the controller with the HTML element.
* The `message` variable is accessed in the view via the `$scope`.

---

### 5. **Multiple Controllers**

* An application can have multiple controllers, each managing its own scope and functionality.
* Controllers can be nested for modularization.

---

### 6. **Controller As Syntax**

* Alternative to `$scope` is using **controller as syntax** which binds controller instance to a variable.

Example:

```javascript
angular.module('myApp', [])
  .controller('myCtrl', function() {
    this.message = "Hello using Controller As syntax";
  });
```

HTML:

```html
<div ng-controller="myCtrl as ctrl">
  <p>{{ ctrl.message }}</p>
</div>
```

---

### 7. **Summary**

* Controllers hold application logic and data.
* They expose model data and methods to the view through `$scope` or `this`.
* Integral to AngularJS’s MVC architecture for managing interaction between UI and data.

---

## Document Object Model (DOM)

---

### 1. **Definition**

* The **DOM** is a **programmatic representation** of an HTML or XML document.
* It represents the page structure as a **tree of objects** (nodes), where each element, attribute, and piece of text is a node.
* Allows programming languages like JavaScript to **access, manipulate, and update** the document content, structure, and style dynamically.

---

### 2. **Structure**

* The DOM tree consists of:

  * **Document node** (root)
  * **Element nodes** (tags like `<div>`, `<p>`)
  * **Attribute nodes** (element attributes like `id`, `class`)
  * **Text nodes** (text inside elements)

---

### 3. **Importance in Web Development**

* Enables **dynamic content changes** without reloading the page.
* Facilitates event handling on elements.
* Essential for **interactive web applications**.

---

### 4. **DOM Manipulation**

* Using JavaScript, developers can:

  * Select elements (`getElementById`, `querySelector`)
  * Change element content (`innerHTML`, `textContent`)
  * Modify styles (`style` property)
  * Add or remove elements (`appendChild`, `removeChild`)
  * Handle events (`addEventListener`)

---

### 5. **Example**

```html
<div id="demo">Hello</div>

<script>
  const div = document.getElementById('demo');
  div.textContent = "Hello, DOM!";
</script>
```

* This changes the content inside the `<div>` dynamically.

---

### 6. **AngularJS and DOM**

* AngularJS uses **directives** to extend HTML and manipulate the DOM declaratively.
* It abstracts direct DOM manipulation, binding UI and data through its framework.

---

### 7. **Summary**

* DOM is a tree-like structure representing HTML/XML documents.
* It allows scripts to interact with and modify the web page dynamically.
* Fundamental for client-side web programming and frameworks like AngularJS.

---

## Events

---

### 1. **Definition**

* Events are **actions or occurrences** that happen in the system or user interface, which the application can respond to.
* Common events include **user interactions** like clicks, key presses, mouse movements, form submissions, etc.

---

### 2. **Event Handling in Web Development**

* Allows applications to **respond to user inputs** or system-generated signals.
* Events can be captured and handled using **event listeners** or handlers.

---

### 3. **Common Event Types**

| Event Type          | Description                                 |
| ------------------- | ------------------------------------------- |
| `click`             | Triggered when a mouse button is clicked    |
| `keydown` / `keyup` | Triggered when a key is pressed or released |
| `mouseover`         | Mouse pointer moves over an element         |
| `submit`            | Form submission event                       |
| `change`            | Input or select element changes             |
| `load`              | Page or resource has loaded                 |

---

### 4. **Event Handling in JavaScript**

* Attach event handlers using:

  * HTML attributes (inline): `<button onclick="doSomething()">Click</button>`
  * DOM Level 2: `element.addEventListener('click', doSomething);`

---

### 5. **AngularJS Event Directives**

* AngularJS simplifies event handling via **directives**:

  * `ng-click` for click events
  * `ng-submit` for form submission
  * `ng-change` for input changes
  * `ng-keypress`, `ng-keydown`, `ng-keyup` for keyboard events

---

### 6. **Example: AngularJS Event Handling**

```html
<div ng-app="myApp" ng-controller="myCtrl">
  <button ng-click="count = count + 1">Click Me</button>
  <p>Button clicked {{count}} times.</p>
</div>

<script>
  angular.module('myApp', [])
    .controller('myCtrl', function($scope) {
      $scope.count = 0;
    });
</script>
```

* Clicking the button updates the count displayed.

---

### 7. **Summary**

* Events enable interactive user interfaces.
* AngularJS provides simple directives to bind event handlers declaratively.
* Event handling connects user actions to application logic seamlessly.

---

## AngularJS Forms

---

### 1. **Definition**

* AngularJS **forms** are HTML forms enhanced with AngularJS directives and features.
* They enable **two-way data binding, validation, and state tracking** within forms.
* Provide a robust way to handle user input, validation, and submission.

---

### 2. **Form Directives**

* `ng-submit`: Binds a function to form submission.
* `ng-model`: Binds form inputs to model data for two-way binding.
* `ng-required`, `ng-minlength`, `ng-maxlength`: Built-in validation directives.
* `ng-pattern`: Validates input against a regular expression.

---

### 3. **Form States**

AngularJS tracks the form and its controls states:

| State        | Description                                   |
| ------------ | --------------------------------------------- |
| `$pristine`  | The control/form has not been interacted with |
| `$dirty`     | The control/form has been changed             |
| `$valid`     | The control/form passes all validation checks |
| `$invalid`   | The control/form fails validation             |
| `$touched`   | The control has lost focus at least once      |
| `$untouched` | The control has not lost focus                |

---

### 4. **Example: Simple AngularJS Form**

```html
<div ng-app="myApp" ng-controller="formCtrl">
  <form name="userForm" ng-submit="submitForm()" novalidate>
    <label>Name:</label>
    <input type="text" name="username" ng-model="user.name" required />
    <span ng-show="userForm.username.$dirty && userForm.username.$invalid">
      Name is required.
    </span>

    <br/>

    <label>Email:</label>
    <input type="email" name="useremail" ng-model="user.email" required />
    <span ng-show="userForm.useremail.$dirty && userForm.useremail.$invalid">
      Valid email is required.
    </span>

    <br/>

    <button type="submit" ng-disabled="userForm.$invalid">Submit</button>
  </form>
</div>

<script>
  angular.module('myApp', [])
    .controller('formCtrl', function($scope) {
      $scope.submitForm = function() {
        if ($scope.userForm.$valid) {
          alert('Form submitted successfully!');
        }
      };
    });
</script>
```

---

### 5. **Features**

* Real-time validation feedback.
* Disable submit button until the form is valid.
* Validation messages tied to form control states.
* Supports custom validation directives.

---

### 6. **Summary**

* AngularJS forms enhance HTML forms with two-way data binding and validation.
* Track form state to provide user feedback.
* Make form handling and validation efficient and declarative.

---

## AngularJS Validations

---

### 1. **Definition**

* AngularJS validations are mechanisms to **ensure that user input meets certain criteria** before processing.
* They are integrated with AngularJS forms to provide **real-time feedback** and control over form submission.

---

### 2. **Built-in Validation Directives**

| Directive       | Purpose                                 |
| --------------- | --------------------------------------- |
| `required`      | Marks a field as mandatory              |
| `ng-required`   | Dynamically sets the required attribute |
| `ng-minlength`  | Sets minimum length for input           |
| `ng-maxlength`  | Sets maximum length for input           |
| `ng-pattern`    | Validates input against a regex pattern |
| `type="email"`  | Validates proper email format           |
| `type="url"`    | Validates proper URL format             |
| `type="number"` | Validates numeric input                 |

---

### 3. **Form and Control Validation States**

* AngularJS exposes validation states via form and control objects:

  * `$valid` / `$invalid`: Whether the control or form is valid.
  * `$pristine` / `$dirty`: Whether the control or form has been modified.
  * `$touched` / `$untouched`: Whether the control has lost focus.

---

### 4. **Example: Form Validation**

```html
<form name="userForm" ng-submit="submitForm()" novalidate>
  <input type="text" name="username" ng-model="user.name" required />
  <span ng-show="userForm.username.$dirty && userForm.username.$invalid">
    Name is required.
  </span>

  <input type="email" name="email" ng-model="user.email" required />
  <span ng-show="userForm.email.$dirty && userForm.email.$invalid">
    Enter a valid email.
  </span>

  <button type="submit" ng-disabled="userForm.$invalid">Submit</button>
</form>
```

---

### 5. **Custom Validations**

* Create custom validation directives by implementing validation logic.
* Example: Check if a username is unique via a custom validator.

---

### 6. **Benefits**

* Improves user experience with instant validation feedback.
* Prevents submission of invalid data.
* Helps maintain data integrity.

---

### 7. **Summary**

* AngularJS provides built-in and custom validations tied to form controls.
* Validations update the form and control states automatically.
* AngularJS directives and state flags help display validation messages and control form submission.

---


