# Unit - 1 -> HTML & CSS
Intorduction to HTML: What is HTML, HTML Syntax
Semantic Markup, Structure of HTML Documents, Quick Tour of HTML Elements
HTML5 Semantic Structure Elements, HTML Tables and forms.
Introduction to CSS: What is CSS, CSS syntax, Location of Styles, Selectors.
The Cascade: How Stypes Interact, The Box Models, CSS Text Styling.

## Content -> 
## Introduction to HTML

### 1. What is HTML (HyperText Markup Language)?

* **Definition**: HTML is the standard markup language used to create and structure documents on the World Wide Web.
* **Purpose**: Describes the structure of web pages using markup elements called tags.
* **"HyperText"**: Refers to the ability to create links (hyperlinks) to other documents.
* **"Markup Language"**: Refers to the method of annotating a document in a way that is syntactically distinguishable from the text.

### 2. Key Characteristics of HTML

* **Platform-independent**: Works on all operating systems and browsers.
* **Not a programming language**: It is a markup language that structures data.
* **Text-based**: Written in plain text files with `.html` or `.htm` extensions.
* **Hierarchical structure**: Elements are nested within each other in a tree-like structure (DOM).

### 3. HTML Syntax

* **Tags**: Enclosed in angle brackets, e.g., `<tagname>`.
* **Opening and Closing Tags**: Most HTML elements use both an opening tag `<p>` and a closing tag `</p>`.
* **Empty Elements**: Tags without content; written as a single tag, e.g., `<br>`, `<img>`.
* **Attributes**: Provide additional information about elements. Written as `name="value"` within the tag.

  * Example: `<img src="image.jpg" alt="description">`
* **Case-insensitive**: HTML is not case-sensitive but lowercase is standard (as per HTML5).
* **Comments**: Written as `<!-- Comment here -->`.

### 4. Structure of an HTML Document

* **Basic Skeleton**:

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>Page Title</title>
    </head>
    <body>
      <h1>My First Heading</h1>
      <p>My first paragraph.</p>
    </body>
  </html>
  ```
* **`<!DOCTYPE html>`**: Declaration to define this document as HTML5.
* **`<html>`**: Root element that wraps all HTML content.
* **`<head>`**: Contains meta-information about the document (e.g., title, character encoding, CSS/JS links).
* **`<title>`**: Specifies the title of the document, shown in browser tab.
* **`<body>`**: Contains all visible content such as text, images, and other elements.

### 5. Uses and Applications

* **Web Page Layout**: Used to arrange text, images, videos, and other content.
* **Web Forms**: Collect input using form elements (`<form>`, `<input>`, `<textarea>`, etc.).
* **Linking**: Create internal or external links with `<a>` tags.
* **Embedding Content**: Embed multimedia, such as audio, video, and interactive elements.

### 6. Versions of HTML

* **HTML 1.0 to 4.01**: Earlier versions focused on basic web structure.
* **XHTML**: A stricter, XML-based version of HTML.
* **HTML5 (Current)**: Introduced semantic tags, multimedia support, and better form controls.

### 7. Advantages of HTML

* Easy to learn and use.
* Supported by all browsers.
* Lightweight and fast to load.
* Integrates with CSS and JavaScript for enhanced functionality and design.

### 8. Limitations of HTML

* Cannot perform logic or calculations (not a programming language).
* Static in nature (without CSS/JS).
* Poor at managing large-scale layouts or reusable components without frameworks.

## What is HTML?

### 1. Definition

* **HTML (HyperText Markup Language)** is the standard markup language used for creating and structuring content on the web.

### 2. Breakdown of the Term

* **HyperText**:

  * Refers to text containing links (hyperlinks) to other texts or web pages.
  * Enables navigation between web pages using clickable links.
* **Markup**:

  * Refers to tags used to define elements in the document.
  * These tags instruct the browser how to display content.
* **Language**:

  * A set of rules and syntax used to structure and annotate text for rendering in web browsers.

### 3. Purpose

* To structure documents for the web by using predefined tags.
* To define elements such as headings, paragraphs, images, links, tables, forms, and multimedia content.
* To create a logical organization of content that can be interpreted by web browsers.

### 4. Characteristics

* **Text-based**: Written using plain text files.
* **Tag-based**: Uses elements enclosed in angle brackets `< >`.
* **Hierarchical**: Elements are nested within one another in a parent-child structure.
* **Non-procedural**: Does not contain logic or programming constructs; focuses solely on structure and layout.

### 5. Example

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p>This is a sample paragraph.</p>
  </body>
</html>
```

### 6. Role in Web Development

* Acts as the **foundation of every web page**.
* Works in conjunction with **CSS** (for styling) and **JavaScript** (for functionality).
* Interpreted by all web browsers to render visual content.

### 7. Versions

* **HTML 4.01**: Traditional version before modern enhancements.
* **XHTML**: Stricter XML-based syntax.
* **HTML5**: Current standard with semantic elements, multimedia support, and improved form controls.

## HTML Syntax

### 1. Basic Syntax Structure

* HTML documents are made up of **elements**, which are represented by **tags**.
* Tags are enclosed in **angle brackets `< >`**.
* Most HTML elements have an **opening tag** and a **closing tag**.

#### Example:

```html
<p>This is a paragraph.</p>
```

* `<p>`: Opening tag.
* `</p>`: Closing tag.
* `This is a paragraph.`: Content between the tags.

---

### 2. HTML Elements

* An **HTML element** consists of:

  * **Start tag**
  * **Content**
  * **End tag**

#### Example:

```html
<h1>Hello World</h1>
```

---

### 3. Empty (Void) Elements

* Do **not** have closing tags.
* Used for elements that do not contain content.

#### Examples:

```html
<br>       <!-- Line break -->
<hr>       <!-- Horizontal rule -->
<img src="image.jpg" alt="description"> <!-- Image -->
<input type="text"> <!-- Input field -->
```

---

### 4. HTML Attributes

* Provide **additional information** about elements.
* Placed **inside the opening tag**.
* Written as: `attribute="value"`

#### Example:

```html
<a href="https://example.com">Visit Site</a>
<img src="logo.png" alt="Company Logo">
```

---

### 5. Nesting of Elements

* Elements can be placed inside other elements.
* Must be **properly nested**: Inner tags must be closed before outer tags.

#### Correct:

```html
<b><i>Bold and Italic</i></b>
```

#### Incorrect:

```html
<b><i>Bold and Italic</b></i> <!-- Incorrect nesting -->
```

---

### 6. Case Sensitivity

* HTML tags and attributes are **not case-sensitive**.
* However, the standard practice in HTML5 is to use **lowercase** for consistency.

#### Example:

```html
<p>Correct</p>
<!-- not preferred: <P>Incorrect</P> -->
```

---

### 7. Comments

* Comments are used to add **notes or explanations** in the code.
* Not displayed by the browser.
* Syntax: `<!-- comment here -->`

#### Example:

```html
<!-- This is a comment -->
```

---

### 8. Special Characters

* Some characters like `<`, `>`, `&`, `"` must be written using **HTML entities**.

#### Examples:

* `<` = `&lt;`
* `>` = `&gt;`
* `&` = `&amp;`
* `"` = `&quot;`

---

### 9. Doctype Declaration

* Defines the HTML version being used.
* Must be the first line in the HTML document.

#### Example (HTML5):

```html
<!DOCTYPE html>
```

---

### 10. Full Example of Syntax

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <img src="image.jpg" alt="Sample Image">
    <br>
    <!-- End of content -->
  </body>
</html>
```

## Semantic Markup

### 1. Definition

* **Semantic markup** refers to the use of **HTML elements** that convey the **meaning** or **structure** of the content.
* Unlike non-semantic elements (e.g., `<div>`, `<span>`), semantic elements clearly describe their purpose both to **browsers** and **developers**.

---

### 2. Importance of Semantic Markup

* **Improves accessibility**: Screen readers and assistive technologies can interpret content more effectively.
* **Enhances SEO**: Search engines understand the structure and meaning of content.
* **Better maintainability**: Developers can more easily read and manage code.
* **Standardization**: Encourages clean, consistent, and standards-compliant HTML.

---

### 3. Common Semantic HTML Elements

| Element        | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `<header>`     | Represents introductory content, such as a page or section header.          |
| `<nav>`        | Contains navigation links to other pages or parts of the page.              |
| `<main>`       | Represents the main content of the document (unique per page).              |
| `<section>`    | Defines a section of related content (thematic grouping).                   |
| `<article>`    | Represents a self-contained piece of content (e.g., blog post).             |
| `<aside>`      | Contains content tangentially related to the main content (e.g., sidebars). |
| `<footer>`     | Contains footer information (author, copyright, links).                     |
| `<figure>`     | Wraps content like images with captions.                                    |
| `<figcaption>` | Provides a caption for a `<figure>`.                                        |
| `<time>`       | Represents dates or times.                                                  |
| `<mark>`       | Highlights or marks text as relevant.                                       |
| `<code>`       | Displays code snippets or programming code.                                 |
| `<address>`    | Represents contact information.                                             |

---

### 4. Comparison: Semantic vs Non-Semantic Elements

| Non-Semantic Element | Semantic Alternative                    |
| -------------------- | --------------------------------------- |
| `<div>`              | `<section>`, `<article>`, `<nav>`, etc. |
| `<span>`             | `<mark>`, `<code>`, etc.                |

---

### 5. Example of Non-Semantic Markup (Not Preferred)

```html
<div id="header">My Website</div>
<div id="nav">
  <a href="#">Home</a>
  <a href="#">Contact</a>
</div>
<div id="content">
  <h1>Title</h1>
  <p>Paragraph text.</p>
</div>
```

---

### 6. Example of Semantic Markup (Preferred)

```html
<header>My Website</header>
<nav>
  <a href="#">Home</a>
  <a href="#">Contact</a>
</nav>
<main>
  <h1>Title</h1>
  <p>Paragraph text.</p>
</main>
```

---

### 7. HTML5 Contribution to Semantic Markup

* HTML5 introduced many semantic elements to improve web content structure.
* Encourages the use of meaningful tags instead of relying solely on `<div>` and `<span>`.

---

### 8. Benefits for Search Engines and Accessibility Tools

* **Search engines**: Better indexing and ranking by understanding content roles.
* **Assistive technologies**: Enhanced user experience for visually impaired users via proper landmarks and structure.

---

### 9. Browser Compatibility

* Modern browsers fully support semantic elements.
* Older browsers (e.g., IE8 and below) require additional CSS or JavaScript to render them correctly.

---

### 10. Summary

* Semantic markup makes web pages more meaningful, accessible, and easier to maintain.
* It promotes clarity in HTML structure and separates content purpose from presentation.

## Structure of HTML Documents

### 1. Overview

* An HTML document follows a hierarchical and standardized structure.
* It consists of nested HTML elements that define the layout and content of a web page.
* The structure ensures compatibility, readability, and consistent rendering across web browsers.

---

### 2. Basic Parts of an HTML Document

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Document Title</title>
  </head>
  <body>
    <h1>Main Content</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

---

### 3. Explanation of Components

#### 3.1 `<!DOCTYPE html>`

* Declares the document type.
* Must be the **first line** in every HTML5 document.
* Informs the browser that this is an HTML5-compliant page.

#### 3.2 `<html>` Element

* Root element of the HTML document.
* Encloses all other elements.
* Optional `lang` attribute specifies the language of the document (e.g., `<html lang="en">`).

#### 3.3 `<head>` Element

* Contains **meta-information** about the document (not visible on the page).
* Includes:

  * `<title>`: Defines the title shown on the browser tab.
  * `<meta>`: Defines character encoding, viewport settings, author, etc.
  * `<link>`: Links to external resources like CSS files.
  * `<style>`: Contains internal CSS styles.
  * `<script>`: Contains or links to JavaScript code.

#### 3.4 `<body>` Element

* Contains **all visible content** on the page.
* Includes headings, paragraphs, images, lists, links, tables, forms, videos, and other interactive elements.

---

### 4. Common Document Hierarchy

```
<!DOCTYPE html>
 └── <html>
      ├── <head>
      │    ├── <title>
      │    ├── <meta>
      │    ├── <link>
      │    └── <script>/<style>
      └── <body>
           ├── <header>
           ├── <nav>
           ├── <main>
           │    ├── <section>
           │    │    └── <article>
           │    └── <aside>
           └── <footer>
```

---

### 5. Example with Semantic Structure

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Page</title>
  </head>
  <body>
    <header>
      <h1>Website Title</h1>
    </header>
    <nav>
      <a href="#">Home</a>
      <a href="#">About</a>
    </nav>
    <main>
      <section>
        <h2>Introduction</h2>
        <p>This is an introductory paragraph.</p>
      </section>
      <article>
        <h2>Article Heading</h2>
        <p>Article content goes here.</p>
      </article>
    </main>
    <footer>
      <p>&copy; 2025 Company Name</p>
    </footer>
  </body>
</html>
```

---

### 6. Important Rules for Structure

* Only one `<html>`, `<head>`, and `<body>` per document.
* Always include `<!DOCTYPE html>` at the top.
* Nest tags correctly and ensure all opened tags are closed.
* Avoid placing content outside `<html>`.
* Metadata must be placed inside `<head>`.
* Displayable content must be inside `<body>`.

---

### 7. Summary

* The structure of an HTML document defines how content is organized.
* It starts with the doctype, followed by the `<html>`, `<head>`, and `<body>` sections.
* Proper structure ensures browser compatibility, accessibility, and maintainability.

## Quick Tour of HTML Elements

### 1. Text Elements

#### 1.1 Headings

* Define section headings.
* `<h1>` (highest level) to `<h6>` (lowest level).

```html
<h1>Main Title</h1>
<h2>Subheading</h2>
```

#### 1.2 Paragraph

* `<p>`: Defines a paragraph.

```html
<p>This is a paragraph.</p>
```

#### 1.3 Line Break

* `<br>`: Inserts a line break.

```html
Line 1<br>Line 2
```

#### 1.4 Horizontal Rule

* `<hr>`: Inserts a horizontal line (thematic break).

```html
<p>Paragraph 1</p>
<hr>
<p>Paragraph 2</p>
```

---

### 2. Formatting Elements

| Tag        | Purpose                           |
| ---------- | --------------------------------- |
| `<b>`      | Bold text (no semantic meaning)   |
| `<strong>` | Strong importance (semantic)      |
| `<i>`      | Italic text (no semantic meaning) |
| `<em>`     | Emphasized text (semantic)        |
| `<mark>`   | Highlighted text                  |
| `<small>`  | Smaller text                      |
| `<del>`    | Deleted text (strikethrough)      |
| `<ins>`    | Inserted text (underline)         |
| `<sub>`    | Subscript                         |
| `<sup>`    | Superscript                       |

---

### 3. List Elements

#### 3.1 Ordered List

* `<ol>`: Numbered list.
* `<li>`: List item.

```html
<ol>
  <li>First</li>
  <li>Second</li>
</ol>
```

#### 3.2 Unordered List

* `<ul>`: Bulleted list.

```html
<ul>
  <li>Item A</li>
  <li>Item B</li>
</ul>
```

#### 3.3 Description List

* `<dl>`: Description list.
* `<dt>`: Term.
* `<dd>`: Description.

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
</dl>
```

---

### 4. Link Elements

* `<a>`: Creates hyperlinks.
* Uses `href` attribute to define the URL.

```html
<a href="https://example.com">Visit Example</a>
```

---

### 5. Image Elements

* `<img>`: Embeds images.
* Attributes: `src`, `alt`, `width`, `height`.

```html
<img src="image.jpg" alt="Sample Image" width="300">
```

---

### 6. Multimedia Elements

| Tag        | Purpose                                         |
| ---------- | ----------------------------------------------- |
| `<audio>`  | Embeds audio files                              |
| `<video>`  | Embeds video files                              |
| `<source>` | Defines media source for `<audio>` or `<video>` |

```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
</audio>

<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
</video>
```

---

### 7. Table Elements

* Used to display data in tabular format.

```html
<table border="1">
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>John</td>
    <td>25</td>
  </tr>
</table>
```

| Tag         | Description        |
| ----------- | ------------------ |
| `<table>`   | Table container    |
| `<tr>`      | Table row          |
| `<td>`      | Table data cell    |
| `<th>`      | Table header cell  |
| `<caption>` | Table title        |
| `<thead>`   | Table header group |
| `<tbody>`   | Table body group   |
| `<tfoot>`   | Table footer group |

---

### 8. Form Elements

* Used to collect user input.

```html
<form action="/submit" method="post">
  <label>Name:</label>
  <input type="text" name="username">
  <input type="submit" value="Submit">
</form>
```

| Tag          | Purpose                          |
| ------------ | -------------------------------- |
| `<form>`     | Form container                   |
| `<input>`    | Input field (text, button, etc.) |
| `<label>`    | Label for input field            |
| `<textarea>` | Multi-line input                 |
| `<select>`   | Drop-down list                   |
| `<option>`   | Options in drop-down             |
| `<button>`   | Clickable button                 |

---

### 9. Semantic Structure Elements

| Tag         | Purpose                             |
| ----------- | ----------------------------------- |
| `<header>`  | Document or section header          |
| `<nav>`     | Navigation links                    |
| `<main>`    | Main content of the document        |
| `<section>` | Thematic grouping of content        |
| `<article>` | Independent, self-contained content |
| `<aside>`   | Related secondary content (sidebar) |
| `<footer>`  | Footer content                      |

---

### 10. Scripting and Meta Elements

| Tag          | Purpose                               |
| ------------ | ------------------------------------- |
| `<script>`   | Embeds or references JavaScript code  |
| `<noscript>` | Content for browsers with JS disabled |
| `<meta>`     | Document metadata                     |
| `<link>`     | Link to external files (CSS, icons)   |
| `<style>`    | Internal CSS                          |

---

### 11. Grouping Elements

| Tag          | Description                   |
| ------------ | ----------------------------- |
| `<div>`      | Generic block-level container |
| `<span>`     | Generic inline container      |
| `<fieldset>` | Groups form elements          |
| `<legend>`   | Caption for `<fieldset>`      |

---

### 12. Inline vs Block Elements

| Type       | Examples                             |
| ---------- | ------------------------------------ |
| **Block**  | `<div>`, `<p>`, `<h1>`, `<section>`  |
| **Inline** | `<span>`, `<a>`, `<img>`, `<strong>` |

---

### 13. Special Characters (Entities)

* Used to represent reserved characters.

```html
&lt; = <
&gt; = >
&amp; = &
&nbsp; = non-breaking space
&quot; = "
```

---

### 14. Comment Tag

* Used for writing notes that are not displayed on the page.

```html
<!-- This is a comment -->
```

## HTML5 Semantic Structure Elements

### 1. Introduction

* HTML5 introduced **semantic structure elements** to define the **meaning** and **structure** of web content more clearly.
* These elements provide **logical division** of a webpage and improve **accessibility**, **SEO**, and **code readability**.

---

### 2. Key Semantic Elements in HTML5

#### 2.1 `<header>`

* Represents **introductory content** or a group of navigational links.
* Typically contains logos, site names, headings, and navigation links.
* Can be used multiple times (e.g., per page or per section).

```html
<header>
  <h1>Website Title</h1>
  <nav>
    <a href="#">Home</a>
    <a href="#">Contact</a>
  </nav>
</header>
```

---

#### 2.2 `<nav>`

* Represents a **section of navigation links**.
* Usually placed inside the `<header>` or as a separate block.

```html
<nav>
  <ul>
    <li><a href="home.html">Home</a></li>
    <li><a href="about.html">About</a></li>
  </ul>
</nav>
```

---

#### 2.3 `<main>`

* Represents the **main content** of the document.
* Only **one `<main>` tag** is allowed per page.
* Excludes content repeated across pages like sidebars, headers, and footers.

```html
<main>
  <h2>Welcome</h2>
  <p>This is the main content of the page.</p>
</main>
```

---

#### 2.4 `<section>`

* Represents a **thematic grouping** of content with a heading.
* Used to group related content within `<main>`, `<article>`, etc.

```html
<section>
  <h2>Features</h2>
  <p>Detail about a specific feature.</p>
</section>
```

---

#### 2.5 `<article>`

* Represents **independent, self-contained content**.
* Suitable for blog posts, news articles, comments, etc.
* Can be distributed and reused independently.

```html
<article>
  <h2>Blog Title</h2>
  <p>This is a blog post.</p>
</article>
```

---

#### 2.6 `<aside>`

* Represents content that is **indirectly related** to the main content.
* Used for sidebars, callout boxes, quotes, etc.

```html
<aside>
  <h3>Related Links</h3>
  <ul>
    <li><a href="#">External Resource</a></li>
  </ul>
</aside>
```

---

#### 2.7 `<footer>`

* Represents **footer content** for its nearest sectioning element or the entire page.
* Typically contains contact info, copyright, navigation.

```html
<footer>
  <p>&copy; 2025 Company Name</p>
</footer>
```

---

#### 2.8 `<figure>` and `<figcaption>`

* `<figure>` groups **media content** (e.g., images, charts) with a caption.
* `<figcaption>` provides the **caption** for the figure.

```html
<figure>
  <img src="image.jpg" alt="Diagram">
  <figcaption>Figure 1: Diagram Overview</figcaption>
</figure>
```

---

#### 2.9 `<time>`

* Represents a **specific time** or **date**.
* Useful for machine-readability (search engines, parsers).

```html
<time datetime="2025-07-10">July 10, 2025</time>
```

---

#### 2.10 `<mark>`

* Highlights text that is of **special relevance** or **importance**.

```html
<p>Read the <mark>important notes</mark> before submitting.</p>
```

---

### 3. Summary of Semantic Elements

| Element        | Purpose                              |
| -------------- | ------------------------------------ |
| `<header>`     | Introductory or navigational content |
| `<nav>`        | Group of navigation links            |
| `<main>`       | Main content of the page             |
| `<section>`    | Thematic grouping of related content |
| `<article>`    | Self-contained, reusable content     |
| `<aside>`      | Indirectly related content (sidebar) |
| `<footer>`     | Footer content of section or page    |
| `<figure>`     | Media element with caption           |
| `<figcaption>` | Caption for figure                   |
| `<time>`       | Represents date/time                 |
| `<mark>`       | Highlights important content         |

---

### 4. Benefits of Semantic Elements

* **Improved accessibility**: Assistive technologies understand document roles.
* **Better SEO**: Search engines can index content more meaningfully.
* **Cleaner code**: More readable and maintainable for developers.
* **Browser consistency**: Supported by all modern browsers.

## HTML Tables

### 1. Definition

* An **HTML table** is used to display data in **rows and columns**.
* Tables are created using the `<table>` element and organized with child elements like `<tr>`, `<th>`, and `<td>`.

---

### 2. Basic Table Structure

```html
<table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Data 1</td>
    <td>Data 2</td>
  </tr>
</table>
```

---

### 3. Table Tags and Their Purpose

| Tag         | Description                                      |
| ----------- | ------------------------------------------------ |
| `<table>`   | Container for the entire table                   |
| `<tr>`      | Table row                                        |
| `<th>`      | Table header cell (bold and centered by default) |
| `<td>`      | Table data cell                                  |
| `<caption>` | Provides a title or description for the table    |
| `<thead>`   | Groups the header content                        |
| `<tbody>`   | Groups the body content                          |
| `<tfoot>`   | Groups the footer content                        |
| `colspan`   | Attribute to merge columns                       |
| `rowspan`   | Attribute to merge rows                          |

---

### 4. Example with All Core Tags

```html
<table border="1">
  <caption>Student Scores</caption>
  <thead>
    <tr>
      <th>Name</th>
      <th>Math</th>
      <th>Science</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>85</td>
      <td>90</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>78</td>
      <td>88</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Average</td>
      <td>81.5</td>
      <td>89</td>
    </tr>
  </tfoot>
</table>
```

---

### 5. Attributes Used in Tables

#### 5.1 `border`

* Specifies the width of the border.

```html
<table border="1">
```

#### 5.2 `colspan`

* Allows a cell to span multiple columns.

```html
<td colspan="2">Merged Cell</td>
```

#### 5.3 `rowspan`

* Allows a cell to span multiple rows.

```html
<td rowspan="2">Merged Rows</td>
```

---

### 6. Styling Tables with CSS

#### 6.1 Example

```html
<style>
  table {
    border-collapse: collapse;
    width: 100%;
  }

  th, td {
    border: 1px solid black;
    padding: 10px;
    text-align: center;
  }

  caption {
    font-weight: bold;
    margin-bottom: 10px;
  }
</style>
```

---

### 7. Nested Tables

* A table placed inside a `<td>` cell of another table.

```html
<table border="1">
  <tr>
    <td>
      Outer Table
      <table border="1">
        <tr><td>Nested Table</td></tr>
      </table>
    </td>
  </tr>
</table>
```

---

### 8. Accessibility Considerations

* Always use `<caption>` to describe the table.
* Use `<th scope="col">` or `<th scope="row">` to help screen readers.

```html
<th scope="col">Name</th>
<th scope="row">Alice</th>
```

---

### 9. Use Cases of Tables

* Tabular data such as:

  * Product catalogs
  * Student mark lists
  * Financial reports
  * Schedule charts

---

### 10. Limitations

* Tables should **not** be used for layout design.
* Layout should be handled using **CSS**, not `<table>`.

---

### 11. Summary of Common Tags

| Tag         | Function            |
| ----------- | ------------------- |
| `<table>`   | Container for table |
| `<tr>`      | Table row           |
| `<td>`      | Table data cell     |
| `<th>`      | Table header cell   |
| `<caption>` | Title of the table  |
| `<thead>`   | Header group        |
| `<tbody>`   | Body group          |
| `<tfoot>`   | Footer group        |
| `colspan`   | Merge columns       |
| `rowspan`   | Merge rows          |


## HTML Forms

### 1. Definition

* An **HTML form** is a section of a document that contains **interactive controls** (like input fields, checkboxes, buttons) for collecting data from users.
* Data entered in a form can be sent to a **server** for processing using HTTP methods.

---

### 2. Basic Structure

```html
<form action="/submit" method="post">
  <input type="text" name="username">
  <input type="submit" value="Submit">
</form>
```

| Attribute | Description                                            |
| --------- | ------------------------------------------------------ |
| `action`  | URL where the form data is sent                        |
| `method`  | HTTP method (`GET` or `POST`) for submitting form data |
| `name`    | Name of the form element used as a key in submission   |

---

### 3. Common Form Elements

#### 3.1 `<input>`

* Used to create various types of input fields.

```html
<input type="text" name="username">
```

| Type       | Description                    |
| ---------- | ------------------------------ |
| `text`     | Single-line text input         |
| `password` | Password input (masked text)   |
| `checkbox` | Allows multiple selections     |
| `radio`    | Select one option from a group |
| `submit`   | Submit the form                |
| `reset`    | Reset all form fields          |
| `button`   | Custom button                  |
| `file`     | File upload field              |
| `email`    | Validates email input          |
| `number`   | Numeric input only             |
| `date`     | Date picker                    |
| `hidden`   | Hidden data field              |
| `search`   | Search field                   |

---

#### 3.2 `<label>`

* Defines a **label** for form elements.
* Improves **accessibility**.

```html
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

---

#### 3.3 `<textarea>`

* For **multi-line text input**.

```html
<textarea name="message" rows="4" cols="50"></textarea>
```

---

#### 3.4 `<select>` and `<option>`

* For **drop-down lists**.

```html
<select name="city">
  <option value="mumbai">Mumbai</option>
  <option value="delhi">Delhi</option>
</select>
```

---

#### 3.5 `<button>`

* Represents a **clickable button**.

```html
<button type="submit">Submit</button>
```

| Attribute   | Description                              |
| ----------- | ---------------------------------------- |
| `type`      | `submit`, `reset`, or `button`           |
| `disabled`  | Disables the button                      |
| `autofocus` | Sets focus on the button when page loads |

---

### 4. Form Attributes

| Attribute      | Description                                              |
| -------------- | -------------------------------------------------------- |
| `action`       | URL to send form data                                    |
| `method`       | `get` (URL parameters) or `post` (request body)          |
| `name`         | Name of the form                                         |
| `target`       | Specifies where to display the response (`_blank`, etc.) |
| `enctype`      | Encoding type (important for file uploads)               |
| `autocomplete` | Enables/disables browser autocomplete                    |

---

### 5. Input Field Attributes

| Attribute     | Description                                 |
| ------------- | ------------------------------------------- |
| `type`        | Type of input (`text`, `email`, etc.)       |
| `name`        | Key used during form submission             |
| `value`       | Initial value of the input field            |
| `placeholder` | Temporary text shown in the field           |
| `required`    | Field must be filled before submission      |
| `readonly`    | User cannot edit the field                  |
| `disabled`    | Field is disabled                           |
| `maxlength`   | Limits the number of characters             |
| `pattern`     | Regex pattern for validation                |
| `checked`     | Sets default checked state (radio/checkbox) |

---

### 6. Fieldset and Legend

* **`<fieldset>`**: Groups related form elements.
* **`<legend>`**: Title for the fieldset group.

```html
<fieldset>
  <legend>Personal Info</legend>
  <label>Name:</label>
  <input type="text" name="name">
</fieldset>
```

---

### 7. File Upload Example

```html
<form action="/upload" method="post" enctype="multipart/form-data">
  <input type="file" name="document">
  <input type="submit">
</form>
```

---

### 8. Form Submission Methods

| Method | Characteristics                                     |
| ------ | --------------------------------------------------- |
| `GET`  | Appends data to URL, visible, used for search forms |
| `POST` | Sends data in request body, used for sensitive data |

---

### 9. Form Validation (HTML5 Native)

* Use attributes like `required`, `pattern`, `min`, `max`, `type`, etc.

```html
<input type="email" required>
<input type="number" min="1" max="100">
```

---

### 10. Accessibility and Best Practices

* Always use `<label>` with `for` and `id` for accessibility.
* Use `fieldset` to group related inputs.
* Use `placeholder` for hints, not for labels.
* Avoid using tables for form layout; use CSS instead.

## Introduction to CSS

### 1. Definition

* **CSS (Cascading Style Sheets)** is a **stylesheet language** used to **describe the presentation** (look and formatting) of a document written in **HTML or XML**.
* It **controls layout, colors, fonts, spacing, borders, positioning, animations**, and **visual effects** on web pages.

---

### 2. Purpose of CSS

* To **separate content from presentation**.
* Enhances the **visual appearance** and **user experience** of web pages.
* Allows **multiple web pages** to share the same style settings via external stylesheets.
* Enables **responsive design** for different screen sizes and devices.

---

### 3. Key Features of CSS

* Defines **how HTML elements** should be displayed.
* Supports **selectors** to target specific elements.
* Allows **inheritance**, **cascading**, and **specificity** for flexible styling.
* Can be reused across multiple HTML pages using **external CSS** files.

---

### 4. Advantages of CSS

* **Efficiency**: Change styles globally with a single stylesheet.
* **Maintainability**: Easier to update and manage than inline styles.
* **Consistency**: Uniform look and feel across all pages.
* **Accessibility**: Improves content readability for all users.

---

### 5. Versions of CSS

| Version | Description                                             |
| ------- | ------------------------------------------------------- |
| CSS1    | Initial release (1996), limited features                |
| CSS2    | Added positioning, media types, and z-index             |
| CSS2.1  | Improved stability and interoperability                 |
| CSS3    | Modularized, introduced media queries, animations, etc. |
| CSS4    | Not an official version; updates are modular in CSS3+   |

---

### 6. Syntax of CSS

```css
selector {
  property: value;
}
```

#### Example:

```css
p {
  color: red;
  font-size: 16px;
}
```

| Term         | Description                                 |
| ------------ | ------------------------------------------- |
| **Selector** | Identifies which HTML element to style      |
| **Property** | Defines what aspect to change (e.g., color) |
| **Value**    | The specific style setting (e.g., `red`)    |

---

### 7. Types of CSS

#### 7.1 Inline CSS

* Defined directly inside the HTML element using the `style` attribute.

```html
<p style="color:blue;">Blue text</p>
```

#### 7.2 Internal CSS

* Defined within a `<style>` tag inside the `<head>` of the HTML document.

```html
<head>
  <style>
    p { color: green; }
  </style>
</head>
```

#### 7.3 External CSS

* Defined in a separate `.css` file and linked using `<link>` tag.

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

---

### 8. Basic Properties in CSS

| Property           | Description                              |
| ------------------ | ---------------------------------------- |
| `color`            | Text color                               |
| `background-color` | Background color                         |
| `font-size`        | Size of text                             |
| `font-family`      | Font type                                |
| `text-align`       | Alignment (left, right, center, justify) |
| `margin`           | Space outside element border             |
| `padding`          | Space inside element border              |
| `border`           | Defines element border                   |
| `width`/`height`   | Set size of the element                  |
| `display`          | Controls box type (block, inline, flex)  |

---

### 9. Example CSS Styling

#### HTML:

```html
<p class="highlight">Hello, world!</p>
```

#### CSS:

```css
.highlight {
  color: white;
  background-color: black;
  padding: 10px;
}
```

---

### 10. Conclusion

* CSS is essential for designing visually appealing, consistent, and responsive web pages.
* It works together with HTML to define **structure** (HTML) and **style** (CSS).

## What is CSS?

### 1. Definition

* **CSS (Cascading Style Sheets)** is a **stylesheet language** used to define the **presentation**, **layout**, and **style** of HTML or XML documents.
* It controls **how elements appear on a web page**, such as their colors, fonts, sizes, spacing, and positioning.

---

### 2. Full Form

* **C** – Cascading
* **S** – Style
* **S** – Sheets

---

### 3. Purpose

* To **separate the structure/content (HTML)** from the **presentation/design (CSS)**.
* Provides a way to apply **consistent styling** across multiple web pages.
* Enables **customization**, **visual enhancements**, and **responsive design**.

---

### 4. How CSS Works

* CSS applies styles to HTML elements using **selectors**.
* Styles are defined in **property-value** pairs inside **rulesets**.
* Browsers read the CSS and apply the styles to matching HTML elements.

```css
/* CSS Rule Example */
p {
  color: red;
  font-size: 16px;
}
```

---

### 5. Example of CSS with HTML

#### HTML:

```html
<p class="highlight">Welcome!</p>
```

#### CSS:

```css
.highlight {
  color: blue;
  background-color: yellow;
}
```

---

### 6. Key Characteristics

| Feature                  | Description                                              |
| ------------------------ | -------------------------------------------------------- |
| **Cascading**            | Styles are applied based on priority and specificity     |
| **Reusable**             | One stylesheet can style multiple pages                  |
| **Platform-independent** | Works across all browsers and devices                    |
| **Flexible**             | Can style individual or grouped elements in various ways |

---

### 7. Types of CSS

| Type             | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| **Inline CSS**   | Styles written directly in HTML elements using `style` attribute |
| **Internal CSS** | CSS written inside a `<style>` tag within the `<head>` of HTML   |
| **External CSS** | CSS written in a separate `.css` file and linked to HTML         |

---

### 8. Advantages

* **Separation of concerns**: Structure and design are handled separately.
* **Reusability**: One stylesheet for many pages.
* **Maintainability**: Easy to update and manage.
* **Performance**: Reduces page load time by caching external stylesheets.

---

### 9. Applications of CSS

* Set **text color**, **font**, and **size**.
* Control **spacing** (margin/padding) and **alignment**.
* Apply **backgrounds**, **borders**, and **shadows**.
* Design **layouts** using Flexbox, Grid, etc.
* Create **animations** and **transitions**.
* Build **responsive** interfaces for all devices.

---

### 10. Summary

| Aspect       | Detail                              |
| ------------ | ----------------------------------- |
| Language     | Style Sheet Language                |
| Used With    | HTML or XML                         |
| Focus        | Styling and presentation            |
| Main Benefit | Separates content from presentation |


## CSS Syntax

### 1. Structure of a CSS Rule

```css
selector {
  property: value;
}
```

| Term         | Description                             |
| ------------ | --------------------------------------- |
| **Selector** | Identifies the HTML element(s) to style |
| **Property** | A style attribute to be applied         |
| **Value**    | The setting for the given property      |

---

### 2. Example

```css
h1 {
  color: blue;
  font-size: 24px;
}
```

* `h1` = selector (targets all `<h1>` elements)
* `color` = property (text color)
* `blue` = value
* `font-size` = property (text size)
* `24px` = value (24 pixels)

---

### 3. Multiple Properties

* Multiple properties can be written within one block:

```css
p {
  color: black;
  background-color: lightgray;
  text-align: justify;
  line-height: 1.6;
}
```

---

### 4. Multiple Selectors

* Apply the same styles to multiple elements:

```css
h1, h2, h3 {
  font-family: Arial, sans-serif;
  color: darkblue;
}
```

---

### 5. Comments in CSS

```css
/* This is a CSS comment */
p {
  font-size: 16px; /* This sets paragraph font size */
}
```

* Comments are enclosed in `/* ... */`
* Ignored by browsers

---

### 6. CSS Declaration Block

```css
selector {
  property1: value1;
  property2: value2;
}
```

* The block is wrapped in **curly braces `{}`**
* Each **declaration** ends with a **semicolon `;`**
* One or more declarations can be added per block

---

### 7. Units in CSS Values

| Unit    | Description                   |
| ------- | ----------------------------- |
| `px`    | Pixels                        |
| `%`     | Percentage relative to parent |
| `em`    | Relative to current font size |
| `rem`   | Relative to root font size    |
| `vh/vw` | Viewport height/width         |
| `pt`    | Points (print)                |

---

### 8. Color Values

| Type              | Example                |
| ----------------- | ---------------------- |
| Color names       | `red`, `blue`, `green` |
| Hexadecimal       | `#ff0000`              |
| RGB               | `rgb(255, 0, 0)`       |
| RGBA (with alpha) | `rgba(255, 0, 0, 0.5)` |
| HSL               | `hsl(0, 100%, 50%)`    |

---

### 9. Case Sensitivity

* CSS properties and values are **case-insensitive**
* CSS selectors matching **HTML** elements are **case-insensitive**

---

### 10. Complete Example

```css
/* Global styles */
body {
  font-family: Verdana, sans-serif;
  background-color: #f0f0f0;
  margin: 0;
}

/* Heading styles */
h1 {
  color: navy;
  text-align: center;
}

/* Paragraph styling */
p {
  font-size: 16px;
  color: #333333;
  line-height: 1.5;
}
```

---

### 11. Summary Table

| Component       | Description                       |
| --------------- | --------------------------------- |
| **Selector**    | Targets HTML elements             |
| **Property**    | Specifies style to apply          |
| **Value**       | Defines how the style should look |
| **Declaration** | One `property: value;` pair       |
| **Rule Set**    | Selector + declaration block      |
| **Comment**     | `/* your comment */`              |


## Location of Styles in CSS

CSS styles can be applied to an HTML document in **three different locations**:

---

### 1. Inline CSS

#### Definition:

* Styles are applied **directly within the HTML element** using the `style` attribute.

#### Syntax:

```html
<tag style="property: value;">Content</tag>
```

#### Example:

```html
<p style="color: red; font-size: 18px;">This is red text.</p>
```

#### Characteristics:

* Applied to a **single element only**
* Has the **highest priority** (overrides internal and external styles)
* **Not reusable**
* Decreases code maintainability

---

### 2. Internal CSS

#### Definition:

* Styles are written **within a `<style>` tag** inside the `<head>` section of the HTML document.

#### Syntax:

```html
<head>
  <style>
    selector {
      property: value;
    }
  </style>
</head>
```

#### Example:

```html
<head>
  <style>
    p {
      color: green;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <p>This is green text.</p>
</body>
```

#### Characteristics:

* Affects **only the current HTML document**
* Useful for **single-page styling**
* More organized than inline CSS
* Still **not reusable across multiple pages**

---

### 3. External CSS

#### Definition:

* Styles are written in a **separate `.css` file** and linked to the HTML document using the `<link>` tag in the `<head>`.

#### Syntax in HTML:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

#### Syntax in `style.css`:

```css
p {
  color: blue;
  font-size: 20px;
}
```

#### Characteristics:

* Most **efficient and maintainable** method
* Enables **reusability** across multiple web pages
* Keeps content (HTML) and design (CSS) **separated**
* Preferred in large websites

---

### 4. Comparison Table

| Type     | Location              | Scope                   | Reusability | Priority                   |
| -------- | --------------------- | ----------------------- | ----------- | -------------------------- |
| Inline   | Inside HTML tag       | Single element          | No          | Highest                    |
| Internal | `<style>` in `<head>` | Whole HTML document     | No          | Medium                     |
| External | Separate `.css` file  | Multiple HTML documents | Yes         | Lowest (unless overridden) |

---

### 5. Order of Precedence (Cascade Priority)

When all three are used, **priority is determined as**:

1. **Inline CSS**
2. **Internal CSS**
3. **External CSS**

This is part of the **Cascading** nature of CSS.

## CSS Selectors

### 1. Definition

* **Selectors** are patterns used in CSS to **target and apply styles to specific HTML elements**.
* A selector specifies **which element(s)** a CSS rule applies to.

---

### 2. Types of Selectors

---

### 2.1 Universal Selector (`*`)

* Selects **all elements** in the HTML document.

```css
* {
  margin: 0;
  padding: 0;
}
```

---

### 2.2 Type Selector (Element Selector)

* Targets **specific HTML elements** by their tag name.

```css
p {
  color: blue;
}
h1 {
  font-size: 32px;
}
```

---

### 2.3 Class Selector (`.classname`)

* Selects all elements with a given **class** attribute.
* Classes are **reusable** on multiple elements.

```css
.highlight {
  background-color: yellow;
}
```

```html
<p class="highlight">Highlighted text</p>
```

---

### 2.4 ID Selector (`#idname`)

* Selects a **single element** with a specific **id** attribute.
* IDs must be **unique** per page.

```css
#main-title {
  color: red;
}
```

```html
<h1 id="main-title">Page Title</h1>
```

---

### 2.5 Grouping Selector

* Applies the same styles to **multiple selectors** separated by commas.

```css
h1, h2, p {
  font-family: Arial, sans-serif;
}
```

---

### 2.6 Descendant Selector (Space)

* Selects elements **nested inside** another element.

```css
div p {
  color: green;
}
```

```html
<div>
  <p>This paragraph will be green.</p>
</div>
```

---

### 2.7 Child Selector (`>`)

* Selects only elements that are **direct children** of a specified parent.

```css
ul > li {
  color: purple;
}
```

---

### 2.8 Adjacent Sibling Selector (`+`)

* Selects the **immediately next sibling** element.

```css
h1 + p {
  font-style: italic;
}
```

---

### 2.9 General Sibling Selector (`~`)

* Selects all siblings **after** a specific element.

```css
h1 ~ p {
  color: brown;
}
```

---

### 2.10 Attribute Selector

* Targets elements with specific attributes or values.

```css
input[type="text"] {
  border: 1px solid black;
}
```

---

### 2.11 Pseudo-Class Selector

* Targets elements in a **specific state**.

| Selector        | Description                        |
| --------------- | ---------------------------------- |
| `:hover`        | When mouse hovers over the element |
| `:focus`        | When element is focused            |
| `:first-child`  | First child of a parent            |
| `:last-child`   | Last child of a parent             |
| `:nth-child(n)` | The nth child of a parent          |

```css
a:hover {
  color: red;
}
```

---

### 2.12 Pseudo-Element Selector

* Targets **parts of elements** (not the entire element).

| Selector         | Description                    |
| ---------------- | ------------------------------ |
| `::before`       | Adds content before an element |
| `::after`        | Adds content after an element  |
| `::first-line`   | Styles the first line of text  |
| `::first-letter` | Styles the first letter        |

```css
p::first-letter {
  font-size: 200%;
  color: blue;
}
```

---

### 3. Selector Specificity

| Selector Type     | Specificity Value |
| ----------------- | ----------------- |
| Inline styles     | 1000              |
| ID selectors      | 100               |
| Class/selectors   | 10                |
| Element selectors | 1                 |

* More specific selectors **override** less specific ones.
* If specificity is equal, the **last rule** defined takes precedence.

---

### 4. Summary Table

| Selector       | Description               | Example              |
| -------------- | ------------------------- | -------------------- |
| `*`            | Universal selector        | `* { margin: 0; }`   |
| `element`      | Type selector             | `p { }`              |
| `.class`       | Class selector            | `.box { }`           |
| `#id`          | ID selector               | `#header { }`        |
| `A B`          | Descendant selector       | `div p { }`          |
| `A > B`        | Child selector            | `ul > li { }`        |
| `A + B`        | Adjacent sibling selector | `h1 + p { }`         |
| `A ~ B`        | General sibling selector  | `h1 ~ p { }`         |
| `[attr=value]` | Attribute selector        | `input[type="text"]` |
| `:hover`       | Pseudo-class              | `a:hover { }`        |
| `::before`     | Pseudo-element            | `p::before { }`      |



## The Cascade in CSS

### 1. Definition

* The **cascade** in CSS is the **decision-making process** that determines **which style rules apply** to an element when there are **conflicts** between multiple CSS declarations.
* The cascade follows specific **priority rules** based on:

  * **Origin**
  * **Importance**
  * **Specificity**
  * **Source Order**

---

### 2. Sources of CSS

| Source                | Description                                               |
| --------------------- | --------------------------------------------------------- |
| **Author styles**     | CSS written by the developer (inline, internal, external) |
| **User styles**       | Custom styles set by the browser user (via settings)      |
| **User-agent styles** | Default styles provided by browsers for all HTML elements |

---

### 3. Cascade Decision Order

The browser determines the final style of an element using the **cascade algorithm** in the following order of precedence:

#### Step 1: **Importance**

| Rule Type                    | Priority Level |
| ---------------------------- | -------------- |
| Author’s `!important`        | Highest        |
| User `!important`            | 2nd            |
| Author (normal)              | 3rd            |
| User (normal)                | 4th            |
| User agent (browser default) | Lowest         |

#### Step 2: **Specificity**

* The **more specific** a selector, the **higher priority** it has.
* Specificity is calculated using a 4-part value: `(a, b, c, d)`

| Selector Type                | Specificity  |
| ---------------------------- | ------------ |
| Inline styles                | (1, 0, 0, 0) |
| ID selector                  | (0, 1, 0, 0) |
| Class/attribute/pseudo-class | (0, 0, 1, 0) |
| Element/pseudo-element       | (0, 0, 0, 1) |

#### Example:

```css
/* Specificity: (0,0,0,1) */
p { color: red; }

/* Specificity: (0,0,1,0) */
.text { color: blue; }

/* Specificity: (0,1,0,0) */
#main { color: green; }
```

→ `#main` has the highest specificity, so the element color will be **green**.

#### Step 3: **Source Order**

* If two rules have the same importance and specificity, the **last one written** in the source code takes precedence.

```css
p {
  color: red;
}
p {
  color: blue;
}
```

→ Result: `color: blue;`

---

### 4. `!important` Declaration

* Overrides all other rules **regardless of specificity or source order**.

```css
p {
  color: red !important;
}
```

→ This color will be applied even if other selectors are more specific.

---

### 5. Inheritance

* Some properties (like `color`, `font-family`) are **inherited** from parent elements.
* Inherited values are **considered the weakest** in the cascade.

---

### 6. Summary Table

| Priority Level | Rule Type                               | Example                              |
| -------------- | --------------------------------------- | ------------------------------------ |
| 1 (Highest)    | Inline CSS with `!important`            | `<p style="color:red !important;">`  |
| 2              | External/Internal CSS with `!important` | `#id { color: red !important; }`     |
| 3              | Inline CSS (no `!important`)            | `<p style="color: red;">`            |
| 4              | ID selectors                            | `#id { color: red; }`                |
| 5              | Class, attribute, pseudo-class          | `.class { color: red; }`             |
| 6              | Element, pseudo-element                 | `p { color: red; }`                  |
| 7 (Lowest)     | Browser default styles                  | (e.g. `body` margin, `h1` font-size) |

---

### 7. Conclusion

* The **cascade** ensures a consistent rule resolution when multiple styles apply.
* Understanding the cascade is crucial for **debugging**, **overriding**, and **designing CSS** effectively.

## How Styles Interact in CSS

### 1. Overview

* When multiple CSS styles apply to the same HTML element, the **final style** is determined by how those styles **interact**, based on:

  1. **Inheritance**
  2. **Specificity**
  3. **Cascade Order**
  4. **Importance (`!important`)**
  5. **Source (inline, internal, external)**

---

### 2. Inheritance

#### 2.1 What is Inheritance?

* Some CSS properties are **inherited** automatically from the **parent element** to the **child elements**.

#### 2.2 Inherited Properties (Examples)

* `color`
* `font-family`
* `font-size`
* `line-height`
* `visibility`

#### 2.3 Non-Inherited Properties (Examples)

* `margin`, `padding`, `border`, `width`, `height`

#### 2.4 Forcing Inheritance

```css
div {
  color: inherit;
}
```

---

### 3. Specificity

* More **specific** selectors override less specific ones.

| Selector Type                    | Specificity Value |
| -------------------------------- | ----------------- |
| Inline Style                     | (1,0,0,0)         |
| ID Selector                      | (0,1,0,0)         |
| Class / Attribute / Pseudo-class | (0,0,1,0)         |
| Element / Pseudo-element         | (0,0,0,1)         |

#### Example:

```css
p { color: red; }               /* (0,0,0,1) */
.text { color: blue; }          /* (0,0,1,0) */
#main { color: green; }         /* (0,1,0,0) */
```

→ Final color: **green**

---

### 4. Cascade Order

* When multiple rules apply to the same element with **equal specificity**, the **last rule written** takes precedence.

```css
p {
  color: blue;
}
p {
  color: orange;
}
```

→ Final color: **orange**

---

### 5. Importance with `!important`

* Rules with `!important` **override** all other rules regardless of specificity or source order.

```css
p {
  color: black !important;
}
```

→ Final color: **black**, even if other rules are more specific.

---

### 6. Rule Origins

| Source Type          | Priority (High to Low) |
| -------------------- | ---------------------- |
| Inline styles (HTML) | Highest                |
| Internal stylesheet  | Medium                 |
| External stylesheet  | Medium                 |
| Browser default      | Lowest                 |

---

### 7. Combining Selectors

* Multiple selectors can be combined to target elements more precisely.

```css
/* Targets all <p> inside a container with class "box" */
.box p {
  color: teal;
}
```

* More complex selectors = more **specific** = higher **priority** (unless overridden)

---

### 8. Conflicting Styles Example

```html
<p id="text" class="highlight" style="color: red;">Example</p>
```

```css
.highlight { color: blue; }     /* Specificity: (0,0,1,0) */
#text { color: green; }         /* Specificity: (0,1,0,0) */
```

* Final Color: **red**
  → because **inline style** has the **highest priority**

---

### 9. Summary Table

| Interaction Rule  | Behavior                                       |
| ----------------- | ---------------------------------------------- |
| **Inheritance**   | Child gets values from parent if applicable    |
| **Specificity**   | Higher specificity wins over lower             |
| **Cascade Order** | Last defined rule wins if specificity is equal |
| **Importance**    | `!important` overrides all other rules         |
| **Source Origin** | Inline > Internal > External > Browser Default |

---

### 10. Conclusion

* The interaction of styles ensures that **conflicting rules are resolved** logically.
* Understanding **how styles interact** is critical to **effective CSS development** and **debugging styling issues**.


## The Box Model in CSS

### 1. Definition

* The **CSS Box Model** is a fundamental concept that defines how HTML elements are **structured and displayed** on a web page.
* Every HTML element is considered as a **rectangular box**, consisting of **four areas**:

  1. **Content**
  2. **Padding**
  3. **Border**
  4. **Margin**

---

### 2. Structure of the Box Model

```
+---------------------------+
|        Margin             |
|  +---------------------+  |
|  |     Border          |  |
|  |  +---------------+  |  |
|  |  |   Padding     |  |  |
|  |  | +-----------+ |  |  |
|  |  | |  Content  | |  |  |
|  |  | +-----------+ |  |  |
|  |  +---------------+  |  |
|  +---------------------+  |
+---------------------------+
```

---

### 3. Box Model Components

#### 3.1 Content

* The **actual text, image, or other data** inside the element.
* Size is set using `width` and `height`.

```css
width: 300px;
height: 150px;
```

---

#### 3.2 Padding

* **Space between content and border**.
* Transparent area inside the border.
* Affects the **internal spacing** of content.

```css
padding: 10px;          /* all sides */
padding: 10px 20px;     /* vertical | horizontal */
padding: 10px 15px 5px 0px;  /* top | right | bottom | left */
```

---

#### 3.3 Border

* **Line surrounding the padding and content**.
* Can have width, style, and color.

```css
border: 2px solid black;
```

---

#### 3.4 Margin

* **Space outside the border**, separating the element from other elements.
* Used to control layout spacing between boxes.

```css
margin: 20px;
margin: 10px 15px 5px 0px;
```

---

### 4. Total Box Size Calculation (Default Behavior)

```text
Total Width = width + padding-left + padding-right + border-left + border-right + margin-left + margin-right

Total Height = height + padding-top + padding-bottom + border-top + border-bottom + margin-top + margin-bottom
```

#### Example:

```css
width: 200px;
padding: 10px;
border: 2px solid black;
margin: 20px;
```

→ Total Width = 200 + 10 + 10 + 2 + 2 + 20 + 20 = **264px**
→ Total Height = Similar calculation for height.

---

### 5. Changing the Box Model

#### 5.1 `box-sizing` Property

| Value         | Description                                                                            |
| ------------- | -------------------------------------------------------------------------------------- |
| `content-box` | Default. Width and height apply to **content only**. Padding and border are **added**. |
| `border-box`  | Width and height include **content + padding + border**. Margin is outside.            |

```css
box-sizing: border-box;
```

---

### 6. Visual Example

```css
div {
  width: 300px;
  height: 100px;
  padding: 20px;
  border: 5px solid black;
  margin: 30px;
  box-sizing: border-box;
}
```

* Here, `width: 300px` includes padding and border.
* Actual content width = 300 − 20 − 20 − 5 − 5 = **250px**

---

### 7. Common Use Cases

* Use **`box-sizing: border-box`** to simplify layout calculations.
* Adjust **padding** for spacing inside boxes (e.g., text inside a button).
* Use **margin** to space boxes apart in layout design.
* Use **border** for visual outlines and separation.

---

### 8. Summary Table

| Component | Description                | Affects Size? | Colorable |
| --------- | -------------------------- | ------------- | --------- |
| Content   | Actual element data        | Yes           | Yes       |
| Padding   | Space inside the element   | Yes           | No        |
| Border    | Outline around the element | Yes           | Yes       |
| Margin    | Space outside the element  | No            | No        |

---

### 9. Conclusion

* Understanding the **Box Model** is essential for precise layout and spacing control in CSS.
* Mastery of how padding, borders, and margins interact leads to better **responsive**, **flexible**, and **clean** designs.

## CSS Text Styling

### 1. Overview

CSS provides multiple properties to control the **appearance**, **alignment**, **spacing**, and **decoration** of text content on a webpage. These properties help improve **readability**, **aesthetics**, and **usability**.

---

### 2. Text Color

#### `color`

* Sets the **text color**.

```css
p {
  color: red;
}
```

---

### 3. Font Properties

#### 3.1 `font-family`

* Specifies the **font type** used.
* Can use multiple fonts as a fallback list.

```css
p {
  font-family: Arial, Helvetica, sans-serif;
}
```

#### 3.2 `font-size`

* Controls the **size of the text**.

```css
p {
  font-size: 16px;
}
```

| Unit  | Description                         |
| ----- | ----------------------------------- |
| `px`  | Pixels                              |
| `em`  | Relative to parent font size        |
| `rem` | Relative to root font size          |
| `%`   | Percentage of parent element's font |

#### 3.3 `font-weight`

* Sets the **thickness** of text.

```css
p {
  font-weight: bold;
}
```

| Value     | Meaning                   |
| --------- | ------------------------- |
| `normal`  | Default                   |
| `bold`    | Bold text                 |
| `100–900` | Numeric values for weight |

#### 3.4 `font-style`

* Sets the **italic style**.

```css
p {
  font-style: italic;
}
```

| Value     | Description     |
| --------- | --------------- |
| `normal`  | Regular text    |
| `italic`  | Italicized text |
| `oblique` | Slanted version |

#### 3.5 `font-variant`

* Controls **small-caps**.

```css
p {
  font-variant: small-caps;
}
```

---

### 4. Text Alignment

#### `text-align`

* Aligns text **horizontally**.

```css
p {
  text-align: center;
}
```

| Value     | Description             |
| --------- | ----------------------- |
| `left`    | Align text to left      |
| `right`   | Align text to right     |
| `center`  | Center the text         |
| `justify` | Align both left & right |

---

### 5. Text Decoration

#### `text-decoration`

* Adds **lines or effects** to text.

```css
a {
  text-decoration: underline;
}
```

| Value          | Description        |
| -------------- | ------------------ |
| `none`         | Removes decoration |
| `underline`    | Underlines text    |
| `overline`     | Line above text    |
| `line-through` | Strikethrough      |

---

### 6. Text Transformation

#### `text-transform`

* Controls **letter casing** of text.

```css
p {
  text-transform: uppercase;
}
```

| Value        | Description              |
| ------------ | ------------------------ |
| `none`       | No change                |
| `capitalize` | Capitalizes first letter |
| `uppercase`  | Converts to upper case   |
| `lowercase`  | Converts to lower case   |

---

### 7. Letter and Word Spacing

#### `letter-spacing`

* Controls the **space between characters**.

```css
p {
  letter-spacing: 2px;
}
```

#### `word-spacing`

* Controls the **space between words**.

```css
p {
  word-spacing: 10px;
}
```

---

### 8. Line Height

#### `line-height`

* Sets the **vertical spacing** between lines of text.

```css
p {
  line-height: 1.5;
}
```

* Can be a **number**, **percentage**, or **unit**.

---

### 9. Text Indentation

#### `text-indent`

* Indents the **first line** of text.

```css
p {
  text-indent: 30px;
}
```

---

### 10. Text Shadow

#### `text-shadow`

* Adds a **shadow** to the text.

```css
h1 {
  text-shadow: 2px 2px 5px gray;
}
```

| Value Order | Meaning           |
| ----------- | ----------------- |
| `2px`       | Horizontal offset |
| `2px`       | Vertical offset   |
| `5px`       | Blur radius       |
| `gray`      | Shadow color      |

---

### 11. White Space Control

#### `white-space`

* Controls **how white space and line breaks** are handled.

```css
p {
  white-space: nowrap;
}
```

| Value    | Description                              |
| -------- | ---------------------------------------- |
| `normal` | Collapses white space (default)          |
| `nowrap` | Prevents line breaks                     |
| `pre`    | Preserves white space (like `<pre>` tag) |

---

### 12. Overflow and Ellipsis

#### `overflow`, `text-overflow`, `white-space` combination

* Truncates long text with an ellipsis.

```css
p {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

---

### 13. Summary Table

| Property          | Purpose                          |
| ----------------- | -------------------------------- |
| `color`           | Sets text color                  |
| `font-family`     | Specifies font type              |
| `font-size`       | Defines font size                |
| `font-weight`     | Sets boldness                    |
| `font-style`      | Italic/normal/oblique            |
| `text-align`      | Horizontal alignment             |
| `text-decoration` | Underline, strikethrough, etc.   |
| `text-transform`  | Capitalization effects           |
| `letter-spacing`  | Spacing between letters          |
| `word-spacing`    | Spacing between words            |
| `line-height`     | Line spacing                     |
| `text-indent`     | First-line indent                |
| `text-shadow`     | Text shadow effects              |
| `white-space`     | White space handling             |
| `text-overflow`   | Handles overflow text (ellipsis) |

---

### 14. Conclusion

CSS text styling provides fine-grained control over **font appearance**, **readability**, and **layout formatting** for all types of text on web pages.


