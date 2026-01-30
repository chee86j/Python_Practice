# Project 3: React Form Handling (Books)

This project focuses on handling forms in React while keeping state in a single parent
component and passing data and callbacks down through props.

## What this project teaches
- Controlled inputs with `useState`
- Lifting state to the common parent (`App`)
- Prop drilling for CRUD callbacks
- Side effects with `useEffect` for initial data fetch
- Immutable updates to state after API calls

## Architecture map (single chart)
```
 +------------------------+
 | App (state: books)     |
 +------------------------+
            |
   +--------+-------------------------------+
   |                                        |
   v                                        v
 +------------------------+        +------------------------+
 | BookList               |        | BookCreate             |
 | props: books           |        | props: onCreate(title) |
 +------------------------+        +------------------------+
            |                                        |
            v                                        v
 +------------------------+        +------------------------+
 | BookShow (xN)          |        | App.createBook         |
 | props: onDelete(id)    |        +------------------------+
 | props: onEdit(id,title)|                    |
 +------------------------+                    v
            |                          +------------------------+
            v                          | POST -> fetchBooks     |
 +------------------------+            | -> setBooks            |
 | BookEdit (local: title)|            +------------------------+
 | onSubmit               |
 +------------------------+
            |
    +-------+---------------------+
    |                             |
    v                             v
 +------------------------+  +------------------------+
 | App.editBookById        |  | App.deleteBookById      |
 +------------------------+  +------------------------+
            |                             |
            v                             v
 +------------------------+  +------------------------+
 | PUT -> fetchBooks       |  | DELETE -> fetchBooks    |
 | -> setBooks             |  | -> setBooks             |
 +------------------------+  +------------------------+
            |
            v
 +------------------------+
 | json-server (db.json)  |
 +------------------------+
```

## Key files
```
src/App.jsx
src/components/BookCreate.jsx
src/components/BookList.jsx
src/components/BookShow.jsx
src/components/BookEdit.jsx
```

## How to run
```
npm install
npm run server   # json-server on http://localhost:3001
npm run start    # Vite dev server
```

## Notes
- API endpoints come from `db.json` via `json-server`.
- This version intentionally uses props to show how data and callbacks move through
  a component tree before introducing Context in the refactor.
