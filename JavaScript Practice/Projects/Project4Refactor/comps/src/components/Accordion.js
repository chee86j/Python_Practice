import { useState } from 'react';

function Accordion({ items }) {
    const [expandedIndex, setExpandedIndex] = useState(0);

    const handleClick = (nextIndex) => {
        setExpandedIndex(nextIndex);
    };

    // Adding Conditional Rendering
    const renderedItems = items.map((item, index) => {
        const isExpanded = index === expandedIndex;
    
        return (
        <div key={item.id}>
            <div onClick={() => handleClick(nextIndex)}>{item.label}</div>
            {isExpanded && <div>{item.content}</div>}
        </div>
        );
    });
    return <div>{renderedItems}</div>
}

export default Accordion;

/*
Our conditional rendering logic in the above code follows this pattern:
1. Check if the current item is the expanded item that matches the index 
of the item that was clicked.
2. If it is, render the content (renderedItems)
3. If it is not, do not render the content (renderedItems)
4. With the addition of the onClick event, we can now set the expanded
index to the index of the item that was clicked. This will cause the
conditional rendering logic to re-evaluate and render the content for
the item that was clicked only while the other items are collapsed.
*/

/*
With a hybrid shorthand and longhand approach, we can achieve the same
result with less code. We have to use the longhand approach to set the
expanded index to the index of the item that was clicked by placing the
event handler (handleClick function) outside of the map function. Then we have to shorthand
with the arrow function to set the expanded index to the index of the item that was clicked.
*/