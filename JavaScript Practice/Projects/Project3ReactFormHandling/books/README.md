This is a React Starter Project for use in Stephen Grider's courses on Udemy.
"Modern React with Redux"
-"Section 6: How to Handle Forms"

Topics Covered:

1.  State Location
    A. Parent Component --> Child Component
    -----books [ { id: number, title: string } ]-----
    We have to determin how the state is updated? Rerender the component it is defined in + all that component's children.
    Find all the components that need to use this state
    Define the state in the lower level common parent
    -- Parent Component: App.jsx
    -- Child Component: BookCreate.jsx
    -- Child Component: BookShow.jsx
    -- Child Component: BookEdit.jsx

    B. Local Storage now for books and in the future, we will use a database

    C. Receiving new Titles
    ---> i. Create an event handler in the parent component
    --->ii. Import useState from react
    iii. Add a new state property to the parent component
    -->iv. In the child component BookCreate.jsx, create a function that updates the state in the parent component
    then create the handleChange and handleSubmit functions with event.target.value and event.preventDefault()
    -->v. Pass the event handler as a prop to the child component BookCreate.jsx (handleChange)
    -->vi. Note that React treats, numbers, strings, booleans, null and undefined differently.

    D. Don't mutate that state
    -->i. Don't
    a. push() (i.e. colors.push("red") )
    b. Modifying an element (i.e. colors[0] = "red")
    c. Modifying a property (i.e. colors.name = "red")

    -->i. Instead,
    a. Mutating object, but it isn't being used as state
    b. Mutating array, but it isn't being used as state
    c. Use ...spread operator

    E. Update Techniques
    -->i. Adding elements to the start of an array
    i.e. const addColor = (newColor) => {
    const updatedColors = [newColor, ...colors];
    setColors(updatedColors);
    }

    -->ii. Inserting elements with slice(0) or slice (index, 0)
    i.e. assuming colors = ["red", "green", "blue"]
    colors.slice(0, 1) = ["red"]
    colors.slice(0, 2) = ["red", "green"]
    colors.slice(0, 0) = []
    colors.slice(1) = ["green", "blue"]
    colors.slice(2) = ["blue"]

    Adding elements to the start of an array with slice(0, 0)
    i.e. const addColor = (newColor) => {
    const updatedColors = [newColor, ...colors.slice(0, 0)];
    setColors(updatedColors);
    }

    Adding elements to the end of an array with slice(index, 0)
    i.e. const addColor = (newColor) => {
    const updatedColors = [...colors.slice(index, 0), newColor];
    setColors(updatedColors);
    }

    Adding elements to the middle of an array with slice(index, 0)
    i.e. const addColor = (newColor) => {
    const updatedColors = [...colors.slice(index, 0), newColor, ...colors.slice(index, 0)];
    setColors(updatedColors);
    }

    -->iii. Removing an element with a particular value using filter() and !==
    i.e. const removeColor = (color) => {
    const updatedColors = colors.filter((c) => c !== color);
    setColors(updatedColors);
    }

    -->iv. Removing an element with a particular index with filter() and index !==
    i.e. const removeColor = (index) => {
    const updatedColors = colors.filter((\_, i) => i !== index);
    setColors(updatedColors);
    }

    -->v. Removing an element with a particular property using filter() and id
    i.e. const [books, setBooks] = useState([{ id: 1, title: "Book 1" }, { id: 2, title: "Book 2" }, { id: 3, title: "Book 3" }]);
    const removeBookById = (id) => {
    const updatedBooks = books.filter((book) => {
    return book.id !== id;
    });
    setBooks(updatedBooks);
    }

    Note the filtering Function (FKT) Filter Keeps True - element is kept in a new array
