# CSS Notes

## 📑 Table of Contents

1. [The World of CSS Selectors](#sect-7-the-world-of-css-selectors)
2. [The CSS Box Model](#sect-8-the-css-box-model)
3. [Other Assorted Useful CSS Properties](#sect-9-other-assorted-useful-css-properties)
4. [Responsive CSS & Flexbox](#sect-10-responsive-css--flexbox)
5. [CSS Frameworks - Bootstrap](#sect-12-css-frameworks-bootstrap)

---

# Sect. 7: The World of CSS Selectors

### 📎 Resources

- [MDN CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS-Tricks: Selectors Guide](https://css-tricks.com/almanac/selectors/)

---

```css
selector {
  property: value;
}
```

### Universal & Element Selectors

- **Universal Selector** (`*`): Applies to all elements.

```css
* {
  margin: 0;
  padding: 0;
}
```

- **Element Selector**: Targets specific HTML elements.

```css
p {
  color: blue;
}
```

---

### The ID Selector

- **ID Selector** (`#`): Targets a unique element by its `id` attribute.

```css
#header {
  background-color: #f0f0f0;
}
```

- **Best Practice**: Use IDs sparingly—they are unique and can't be reused.
- ⚠️ **Watch Out**: IDs have high specificity and can make styles harder to override!

---

### The Class Selector

- **Class Selector** (`.`): Targets elements with a specific `class` attribute.

```css
.highlight {
  background-color: yellow;
}
```

- **Best Practice**: Use classes for reusable styles.
- 📝 **TODO**: Try creating a reusable button class with hover effects!

---

### The Descendant Selector

- **Descendant Selector** (`space`): Targets elements nested inside another element.

```css
div p {
  font-size: 16px;
}
```

- **Example**: Styles all `<p>` elements inside a `<div>`.
- ⚠️ **Watch Out**: Descendant selectors can be less performant than direct child selectors!

---

### The Adjacent & Direct-Descendant Selectors

- **Adjacent Sibling Selector** (`+`): Targets the element immediately following another.

```css
h2 + p {
  margin-top: 10px;
}
```

- **Direct-Descendant Selector** (`>`): Targets direct children only.

```css
ul > li {
  list-style-type: disc;
}
```

- 📝 **TODO**: Practice using these selectors to style a navigation menu!

---

### The Attribute Selector

- **Attribute Selector** (`[attr]`): Targets elements with a specific attribute.

```css
input[type="text"] {
  border: 1px solid #ccc;
}
```

- **Example**: Styles all text inputs.
- ⚠️ **Watch Out**: Some attribute selectors have limited browser support!

---

### Pseudo Classes

- **Pseudo Classes** (`:`) target elements in a specific state.

```css
a:hover {
  color: red;
}
```

- **Common Pseudo Classes**: `:hover`, `:active`, `:focus`, `:first-child`, `:last-child`.
- 📝 **TODO**: Create an interactive button using multiple pseudo-classes!

---

### Pseudo Elements

- **Pseudo Elements** (`::`) create or style parts of an element.

```css
p::first-line {
  font-weight: bold;
}
```

- **Common Pseudo Elements**: `::before`, `::after`, `::first-line`, `::first-letter`.
- ⚠️ **Watch Out**: Remember the double colon syntax for pseudo-elements!

---

### The CSS Cascade

- **Cascade**: Determines which styles apply when multiple rules target the same element.
- **Order of Importance**: Inline styles > IDs > Classes > Elements.
- **Best Practice**: Use specificity and `!important` sparingly.
- ⚠️ **Watch Out**: Overusing `!important` can lead to maintenance nightmares!

---

### Specificity

- **Specificity**: Determines which CSS rule is applied.
- **Formula**: Inline styles (1000) > IDs (100) > Classes (10) > Elements (1).
- **Example**: `#header .title` has higher specificity than `.title`.
- 📝 **TODO**: Calculate specificity for these selectors: `#nav .item p` vs `.nav-item p`

---

### Chrome Dev Tools & CSS

- Use DevTools (F12) to inspect and debug CSS.
- **Features**: Live editing, computed styles, box model visualization.
- 📝 **TODO**: Practice using DevTools to debug a layout issue!

---

### Inline Styles

- **Inline Styles**: Applied directly to HTML elements using the `style` attribute.

```html
<p style="color: red;">This is red text.</p>
```

- **Pitfall**: Harder to maintain and override.
- ⚠️ **Watch Out**: Inline styles have the highest specificity!

---

### CSS Inheritance

- **Inheritance**: Child elements inherit styles from parent elements.
- **Properties**: `color`, `font-family`, `font-size` are inherited.
- **Override**: Use more specific selectors or `!important` to override inherited styles.
- 📝 **TODO**: Create a nested structure and observe inheritance in action!

---

# Sect. 8: The CSS Box Model

### 📎 Resources

- [MDN Box Model](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model)

---

### Width & Height

- **Width & Height**: Define the size of an element.

```css
.box {
  width: 200px;
  height: 100px;
}
```

- **Box Sizing**: Use `box-sizing: border-box;` to include padding and border in the element's total width/height.
- ⚠️ **Watch Out**: Default `box-sizing: content-box` can lead to unexpected layouts!

---

### Border & Border-Radius

- **Border**: Defines the border around an element.

```css
.box {
  border: 2px solid black;
  border-radius: 10px;
}
```

- **Border-Radius**: Rounds the corners of an element.
- 📝 **TODO**: Create a card component with different border styles!

---

### Padding

- **Padding**: Space between the content and the border.

```css
.box {
  padding: 20px;
}
```

- **Shorthand**: `padding: top right bottom left;`
- ⚠️ **Watch Out**: Padding increases the element's total size unless using `box-sizing: border-box`!

---

### Margin

- **Margin**: Space outside the border.

```css
.box {
  margin: 10px;
}
```

- **Auto Margins**: Center elements horizontally with `margin: 0 auto;`
- 📝 **TODO**: Practice centering elements using different margin techniques!

---

### The Display Property

- **Display**: Controls how an element is rendered.

```css
.inline {
  display: inline;
}
.block {
  display: block;
}
.flex {
  display: flex;
}
```

- **Common Values**: `inline`, `block`, `flex`, `grid`, `none`.
- ⚠️ **Watch Out**: Changing display can affect how margins and padding work!

---

### CSS Units Revisited

- **Absolute Units**: `px`, `pt`, `in`, `cm`, `mm`.
- **Relative Units**: `em`, `rem`, `%`, `vw`, `vh`.
- 📝 **TODO**: Create a responsive layout using different CSS units!

---

### Ems

- **Em**: Relative to the font size of the element.

```css
.box {
  font-size: 16px;
  padding: 1em; /* 16px */
}
```

- **Pitfall**: Can compound when nested.
- ⚠️ **Watch Out**: Nested em values multiply, which can lead to unexpected sizes!

---

### Rems

- **Rem**: Relative to the font size of the root element (`<html>`).

```css
.box {
  font-size: 16px;
  padding: 1rem; /* 16px */
}
```

- **Best Practice**: Use `rem` for consistent scaling.
- 📝 **TODO**: Convert a layout from px to rem for better accessibility!

---

# Sect. 9: Other Assorted Useful CSS Properties

### 📎 Resources

- [MDN CSS Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)

---

### Opacity & the Alpha Channel

- **Opacity**: Controls the transparency of an element.

```css
.box {
  opacity: 0.5;
}
```

- **Alpha Channel**: Use `rgba()` for color transparency.

```css
.box {
  background-color: rgba(255, 0, 0, 0.5);
}
```

- ⚠️ **Watch Out**: Opacity affects the entire element, including its children!

---

### The Position Property

- **Position**: Controls how an element is positioned.

```css
.box {
  position: relative;
  top: 10px;
  left: 20px;
}
```

- **Values**: `static`, `relative`, `absolute`, `fixed`, `sticky`.
- 📝 **TODO**: Create a sticky header and a modal using different position values!

---

### CSS Transitions

- **Transitions**: Smoothly change property values over time.

```css
.box {
  transition: background-color 0.3s ease;
}
```

- **Properties**: `transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay`.
- ⚠️ **Watch Out**: Not all properties can be transitioned!

---

### Transforms

- **Transforms**: Modify the shape, size, and position of elements.

```css
.box {
  transform: rotate(45deg);
}
```

- **Common Functions**: `rotate()`, `scale()`, `translate()`, `skew()`.
- 📝 **TODO**: Create an interactive card with hover transforms!

---

### The Truth About Background

- **Background**: Sets the background of an element.

```css
.box {
  background: url("image.jpg") no-repeat center/cover;
}
```

- **Properties**: `background-color`, `background-image`, `background-repeat`, `background-position`, `background-size`.
- ⚠️ **Watch Out**: Large background images can impact performance!

---

### Google Fonts is Amazing

- **Google Fonts**: Easily add custom fonts to your project.

```html
<link
  href="https://fonts.googleapis.com/css2?family=Roboto&display=swap"
  rel="stylesheet"
/>
```

```css
body {
  font-family: "Roboto", sans-serif;
}
```

- 📝 **TODO**: Experiment with different font combinations for a blog layout!

---

# Sect. 10: Responsive CSS & Flexbox

### 📎 Resources

- [MDN Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)
- [CSS-Tricks: Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

---

### What on Earth is Flexbox

- **Flexbox**: A layout model for arranging elements in a container.

```css
.container {
  display: flex;
}
```

- **Benefits**: Easy alignment, distribution, and reordering of elements.
- 📝 **TODO**: Create a responsive navigation bar using flexbox!

---

### Flex-Direction

- **Flex-Direction**: Defines the direction of flex items.

```css
.container {
  flex-direction: row; /* default */
  flex-direction: column;
}
```

- **Values**: `row`, `row-reverse`, `column`, `column-reverse`.
- ⚠️ **Watch Out**: Remember that flex-direction changes the main and cross axes!

---

### Justify-Content

- **Justify-Content**: Aligns flex items along the main axis.

```css
.container {
  justify-content: space-between;
}
```

- **Values**: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`.
- 📝 **TODO**: Create a card layout with different justify-content values!

---

### Flex-Wrap

- **Flex-Wrap**: Controls whether flex items wrap to the next line.

```css
.container {
  flex-wrap: wrap;
}
```

- **Values**: `nowrap`, `wrap`, `wrap-reverse`.
- ⚠️ **Watch Out**: Without flex-wrap, items might overflow their container!

---

### Align-Items

- **Align-Items**: Aligns flex items along the cross axis.

```css
.container {
  align-items: center;
}
```

- **Values**: `flex-start`, `flex-end`, `center`, `stretch`, `baseline`.
- 📝 **TODO**: Create a vertical navigation with centered items!

---

### Align-Content & Align-Self

- **Align-Content**: Aligns flex lines when there is extra space.

```css
.container {
  align-content: space-around;
}
```

- **Align-Self**: Overrides `align-items` for individual items.

```css
.item {
  align-self: flex-end;
}
```

- ⚠️ **Watch Out**: Align-content only works when there are multiple lines of flex items!

---

### Flex-Basis, Grow, & Shrink

- **Flex-Basis**: Defines the initial size of a flex item.

```css
.item {
  flex-basis: 100px;
}
```

- **Flex-Grow**: Defines how much an item can grow.

```css
.item {
  flex-grow: 1;
}
```

- **Flex-Shrink**: Defines how much an item can shrink.

```css
.item {
  flex-shrink: 0;
}
```

- 📝 **TODO**: Create a responsive grid layout using flex properties!

---

### Flex Shorthand

- **Flex Shorthand**: Combines `flex-grow`, `flex-shrink`, and `flex-basis`.

```css
.item {
  flex: 1 0 100px; /* grow shrink basis */
}
```

- ⚠️ **Watch Out**: The order of values in the flex shorthand is important!

---

### Responsive Design & Media Queries

- **Media Queries**: Apply styles based on screen size or device.

```css
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
```

- **Best Practice**: Use mobile-first design.
- 📝 **TODO**: Convert a desktop layout to be mobile-responsive!

---

### The Power of Media Queries

- **Breakpoints**: Common breakpoints for responsive design.

```css
@media (min-width: 768px) {
  /* tablets */
}
@media (min-width: 1024px) {
  /* desktops */
}
```

- ⚠️ **Watch Out**: Don't rely on specific device breakpoints - use content-based breakpoints!

---

### Building a Responsive Nav

- **Responsive Nav**: Use flexbox and media queries to create a mobile-friendly navigation.

```css
.nav {
  display: flex;
  justify-content: space-between;
}
@media (max-width: 768px) {
  .nav {
    flex-direction: column;
  }
}
```

- 📝 **TODO**: Create a hamburger menu for mobile navigation!

---

# Section 12: CSS Frameworks - Bootstrap

## What is Bootstrap?

Bootstrap is a free, open-source front-end framework developed by Twitter that simplifies web development. It includes:

- Pre-built components and styles
- Responsive grid system
- JavaScript plugins
- Mobile-first approach
- Extensive documentation and community support

## Including Bootstrap & Containers

### Adding Bootstrap to Your Project

```html
<!-- Add to your HTML head -->
<link
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
  rel="stylesheet"
/>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

### Containers

- `.container` - Fixed-width container
- `.container-fluid` - Full-width container
- `.container-{breakpoint}` - Responsive containers

## Bootstrap Buttons

### Button Classes

- `.btn` - Base button class
- `.btn-primary` - Primary action
- `.btn-secondary` - Secondary action
- `.btn-success` - Success/confirmation
- `.btn-danger` - Dangerous/warning action
- `.btn-warning` - Warning/caution
- `.btn-info` - Informational
- `.btn-light` - Light theme
- `.btn-dark` - Dark theme

### Button Sizes

- `.btn-lg` - Large button
- `.btn-sm` - Small button
- `.btn-block` - Full-width button

## Bootstrap Typography & Utilities

### Typography Classes

- `.display-1` to `.display-6` - Large display headings
- `.lead` - Emphasized paragraph
- `.text-{color}` - Text colors
- `.font-weight-{bold|normal|light}`
- `.font-italic`

### Text Utilities

- `.text-center` - Center alignment
- `.text-left` - Left alignment
- `.text-right` - Right alignment
- `.text-justify` - Justified text
- `.text-uppercase` - Transform to uppercase
- `.text-lowercase` - Transform to lowercase

## Badges, Alerts, & Button Groups

### Badges

```html
<span class="badge bg-primary">New</span>
<span class="badge bg-secondary">Label</span>
```

### Alerts

```html
<div class="alert alert-success">Success message!</div>
<div class="alert alert-danger">Error message!</div>
```

### Button Groups

```html
<div class="btn-group">
  <button class="btn btn-primary">Left</button>
  <button class="btn btn-primary">Middle</button>
  <button class="btn btn-primary">Right</button>
</div>
```

## Bootstrap Grid System

### Basic Grid Structure

```html
<div class="container">
  <div class="row">
    <div class="col-sm-6">Column 1</div>
    <div class="col-sm-6">Column 2</div>
  </div>
</div>
```

### Grid Breakpoints

- `col-` - Extra small (<576px)
- `col-sm-` - Small (≥576px)
- `col-md-` - Medium (≥768px)
- `col-lg-` - Large (≥992px)
- `col-xl-` - Extra large (≥1200px)
- `col-xxl-` - Extra extra large (≥1400px)

## Useful Grid Utilities

### Spacing Utilities

- `m-{0-5}` - Margin
- `p-{0-5}` - Padding
- `mx-auto` - Horizontal center
- `my-{0-5}` - Vertical margin

### Flexbox Utilities

- `.d-flex` - Display flex
- `.justify-content-{start|center|end|between|around}`
- `.align-items-{start|center|end|stretch|baseline}`

## Bootstrap & Forms

### Form Classes

```html
<form>
  <div class="form-group">
    <label for="input">Label</label>
    <input type="text" class="form-control" id="input" />
  </div>
</form>
```

### Form Validation

- `.was-validated` - Form validation styles
- `.is-valid` - Valid input
- `.is-invalid` - Invalid input

## Bootstrap Navbars

### Basic Navbar

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Brand</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

## Bootstrap Icons

### Including Icons

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css"
/>
```

### Using Icons

```html
<i class="bi bi-heart"></i> <i class="bi bi-star-fill"></i>
```

## Other Bootstrap Utilities

### Display Properties

- `.d-none` - Hide element
- `.d-block` - Display block
- `.d-inline` - Display inline
- `.d-inline-block` - Display inline-block

### Position Utilities

- `.position-relative`
- `.position-absolute`
- `.position-fixed`
- `.position-sticky`

## Mixed Bag of Other Bootstrap Features

### Cards

```html
<div class="card">
  <img class="card-img-top" src="..." />
  <div class="card-body">
    <h5 class="card-title">Title</h5>
    <p class="card-text">Content</p>
  </div>
</div>
```

### Modals

```html
<button data-bs-toggle="modal" data-bs-target="#myModal">Open Modal</button>
<div class="modal" id="myModal">
  <!-- Modal content -->
</div>
```

### Tooltips

```html
<button data-bs-toggle="tooltip" title="Tooltip text">Hover me</button>
```

### Carousel

```html
<div id="carousel" class="carousel slide">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <!-- Slide content -->
    </div>
  </div>
</div>
```

Remember to initialize JavaScript components:

```javascript
// Initialize tooltips
var tooltipTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});
```
