# Project Guide

This guide explains what each project is meant to teach and which core ideas you should practice while completing it.

## OOP
Focus: object-oriented JavaScript patterns and how they compare.

- 01_Prototypes: How prototypal inheritance works, the prototype chain, and shared methods.
- 03_Factory_Functions: Creating objects with factory functions and closures.
- 04_Constructor_Functions: Using `function` constructors with `new`, instance vs. prototype methods.
- 05_Classes: ES6 class syntax as a clearer wrapper over prototypes.
- 06_More_Classes_Practice: Additional class exercises and method organization.
- 07_Extends_and_Super: Inheritance with `extends` and `super`, base vs. derived classes.

## Project 1: Calculator
Focus: DOM basics, event handling, and state in the UI.

- Build a calculator UI and wire up button clicks.
- Practice query selectors, event listeners, and updating the display.
- Keep track of current value, previous value, and chosen operation.

## Project 2: NavBar
Focus: responsive layout and interactive navigation.

- Build a navbar that adapts to screen size.
- Practice CSS layout (flex/grid), media queries, and toggling classes with JS.
- Learn how to structure a clean HTML/CSS/JS split for UI components.

## Project 3: React Form Handling
Focus: React component state, forms, and CRUD flows.

- Manage input state with `useState`.
- Fetch initial data and react to changes with `useEffect`.
- Pass data between components with props.
- Share data across components with `useContext`.
- Fetch, create, edit, and delete data from a JSON API.
- Practice component composition and list rendering.

## Project 4: Button Component
Focus: reusable component API, class composition, and design-system consistency.

- Build one Button component that everyone can reuse.
- Use simple variant props: primary, secondary, success, warning, danger.
- Add modifiers like outline and rounded to tweak the look.
- Keep variants mutually exclusive (only one at a time).
- Use classnames so Tailwind classes are applied cleanly.
- Result: consistent buttons and easy updates in one place.

Update note (why the change was made):
- Added tailwind-merge (twMerge) so Tailwind class conflicts resolve automatically.
- Spread ...rest onto the <button> so event handlers and extra attributes pass through.
- Added icons to the example buttons and a tiny CSS rule for icon spacing.
- Removed App.css (Vite starter styles) because Tailwind now handles styling.
- Updated the Tailwind entry in index.css to the newer @import "tailwindcss" format.

Note:
A few patterns show up a lot in real teams. They all aim at the same outcome: one source of truth for design decisions, so engineers don't "freestyle" styling component by component.

Design-system approaches (most common in teams)
- Component library + documented variants.
- Build (or adopt) a shared component set like Button, Input, Card, etc., and treat it as the only approved way to render those UI elements.
- Enforce variants via an API: `variant="primary"` `size="sm"` `tone="danger"`.
- Put the components in a shared package (monorepo or internal npm package).
- Bonus: add a Storybook so everyone sees the same canonical examples.

