# React Starter Project

This is a React Starter Project for use in Stephen Grider's courses on Udemy.  
"Modern React with Redux"  
-"Section 6: How to Handle Forms"

---

## Topics Covered

### 1. State Location

#### A. Parent Component --> Child Component  
-----books [ { id: number, title: string } ]-----  

We have to determine how the state is updated? Rerender the component it is defined in + all that component's children.  
Find all the components that need to use this state  
Define the state in the lower level common parent  

-- Parent Component: App.jsx  
-- Child Component: BookCreate.jsx  
-- Child Component: BookShow.jsx  
-- Child Component: BookEdit.jsx

#### B. Local Storage now for books and in the future, we will use a database

#### C. Receiving new Titles  
---> i. Create an event handler in the parent component  
--->ii. Import useState from react  
-->iii. Add a new state property to the parent component  
-->iv. In the child component BookCreate.jsx, create a function that updates the state in the parent component  
then create the handleChange and handleSubmit functions with event.target.value and event.preventDefault()  
-->v. Pass the event handler as a prop to the child component BookCreate.jsx (handleChange)  
-->vi. Note that React treats, numbers, strings, booleans, null and undefined differently.

---

### D. Don't mutate that state

#### -->i. Don't

a. push() (i.e. colors.push("red") )  
b. Modifying an Element (i.e. colors[0] = "red")  
c. Modifying a property (i.e. colors.name = "red")

#### -->ii. Instead,

a. Mutating object, but it isn't being used as state  
b. Mutating array, but it isn't being used as state  
c. Use ...spread operator  
d. Immutability tidbit: React state updates should return a NEW array/object  
(a copy) rather than mutate the existing one. If you change the same  
reference, React can miss the update and skip a re-render. Use spread,  
slice, filter, or map to create a new array.

---

### E. Update Techniques

#### (+) Element at the START of an array

```js
const addColor = (newColor) => {
const updatedColors = [newColor, ...colors];
setColors(updatedColors);
};

        (+) Element to the END of an array
        const [colors, setColors] = useState([]);

        const addColor = (newColor) => {
        const updatedColors = [...colors, newColor];
        setColors(updatedColors);
        };

---

        (+) Element with slice(0) or slice (index, 0)
        i.e.
        assuming colors = ["red", "green", "blue"]

        colors.slice(0, 1) = ["red"]
        colors.slice(0, 2) = ["red", "green"]
        colors.slice(0, 0) = []
        colors.slice(1) = ["green", "blue"]
        colors.slice(2) = ["blue"]

        (+) Element to the START of an array with slice(0, 0)
        i.e.
        const addColor = (newColor) => {
        const updatedColors = [newColor, ...colors.slice(0, 0)];
        setColors(updatedColors);
        }

        (+) Element to the END of an array with slice(index, 0)
        i.e.
        const addColor = (newColor) => {
        const updatedColors = [...colors.slice(index, 0), newColor];
        setColors(updatedColors);
        }

        (+) Element to the MIDDLE of an array with slice(index, 0)
        i.e.
        const addColor = (newColor) => {
        const updatedColors = [...colors.slice(index, 0), newColor, ...colors.slice(index, 0)];
        setColors(updatedColors);
        }

---

        (+) Element at a specific index with slice
        i.e.
        const addColorAtIndex = (newColor, index) => {

        const updatedColors = [
            ...colors.slice(0, index),
            newColor,
            ...colors.slice(index)
            ];
        setColors(updatedColors);
        };

---

        (-) Element with a particular value
        i.e.
        const removeColor = (color) => {
        const updatedColors = colors.filter((c) => c !== color);
        setColors(updatedColors);
        }

        (-) Element with a particular index
        i.e.
        const [colors, setColors] = useState(['red', 'green', 'blue']);

        const removeColorAtIndex = (indexToRemove) => {
        const updatedColors = colors.filter((color, index) => {
        return index !== indexToRemove

            });
            setColors(updatedColors);

        };

---

        (-) Element with a particular property using filter() and id
        i.e.
        const [books, setBooks] = useState([{ id: 1, title: "Book 1" }, { id: 2, title: "Book 2" }, { id: 3, title: "Book 3" }]);
        const removeBookById = (id) => {
        const updatedBooks = books.filter((book) => {
        return book.id !== id;
        });
        setBooks(updatedBooks);
        }

        Note the filtering Function (FKT) Filter Keeps True - Element is kept in a new array

=====Now ask yourself: Should I input something in my child component to only rerender and update state when the prop has changed??=====

        Practical rule of thumb: Use React.memo when the child is expensive to render or
        renders a lot in a list. First make props stable (callbacks/objects), otherwise
        memo won't help much. If you're unsure, use the React Profiler to confirm you're
        optimizing the right thing.

        1.  Rerender: React.memo (functional components)
            By default, a child rerenders whenever its parent rerenders. If you want the child to rerender only when its props change, wrap it:

                const Child = (props) => { /_ ... _/ };

                export default React.memo(Child);

        React.memo does a shallow prop compare. If the prop reference changes (new object/array/function), it counts as “changed”.

        -----Common gotcha: unstable props-----

        If you pass inline objects/functions, the reference changes every render:

            <Child onClick={() => doThing()} options={{ theme: "dark" }} />

        -----Fix by stabilizing props:-----

            const onClick = useCallback(() => doThing(), [doThing]);
            const options = useMemo(() => ({ theme: "dark" }), []);

            <Child onClick={onClick} options={options} />

        2.  Rerender control (class components)
            If you’re in classes:
            a. PureComponent (shallow compare) or
            b. shouldComponentUpdate

        3.  “Update state only when prop changes”
            If the child has local state derived from a prop, use an effect that runs only when that prop changes:

                function Child({ value }) {
                const [localValue, setLocalValue] = useState(value);

                useEffect(() => {
                setLocalValue(value);
                }, [value]);

                // ...

            }

        But if you don’t truly need local state, prefer deriving directly (less bugs, fewer renders):

            function Child({ value }) {
            const computed = value \* 2; // derive, no state needed
            }
