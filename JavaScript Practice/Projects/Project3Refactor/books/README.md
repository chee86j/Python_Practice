# Project 3 Refactor: Context (Books)

This refactor replaces prop drilling with React Context while keeping the UI behavior
the same. It centralizes data fetching and CRUD actions in a Provider.

## What this project teaches
- When to refactor prop drilling into Context
- Building a custom Provider with shared state and actions
- Consuming context with `useContext` in child components
- Keeping local UI state local (edit toggle, input value)
- Side effects with `useEffect` for initial data fetch

## Architecture map (single chart)
```
 +-----------------------------------+
 | BooksContext.Provider             |
 | value: books, fetchBooks,         |
 | createBook, editBookById,         |
 | deleteBookById                    |
 +-----------------------------------+
                 |
                 v
 +-------------------------------+
 | App                           |
 | uses: fetchBooks (initial)    |
 +-------------------------------+
        |
   +----+-------------------------------+
   |                                    |
   v                                    v
 +------------------+           +---------------------+
 | BookList         |           | BookCreate          |
 | uses: books      |           | uses: createBook    |
 +------------------+           +---------------------+
        |                                    |
        v                                    v
 +---------------------------+   +----------------------+
 | BookShow (xN)             |   | POST -> fetchBooks    |
 | uses: deleteBookById      |   | -> setBooks           |
 | local: showEdit           |   +----------------------+
 +---------------------------+
        |
        v
 +---------------------------+
 | BookEdit                  |
 | uses: editBookById         |
 | local: title               |
 +---------------------------+
        |
   +----+---------------------+
   |                          |
   v                          v
 +----------------------+  +----------------------+
 | PUT -> fetchBooks     |  | DELETE -> fetchBooks |
 | -> setBooks           |  | -> setBooks          |
 +----------------------+  +----------------------+
        |
        v
 +----------------------+
 | json-server (db.json)|
 +----------------------+
```

## Key files
```
src/context/books.jsx
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
- This version removes CRUD props from the component tree and gets them from Context.
- Only local UI state is kept in the components that need it.
