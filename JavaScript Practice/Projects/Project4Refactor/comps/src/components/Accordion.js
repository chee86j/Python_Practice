import { useState } from 'react';

function Accordion({ items }) {
    const [expandedIndex, setExpandedIndex] = useState(0);

    // Adding Conditional Rendering
    const renderedItems = items.map((item) => {
        const isExpanded = index === expandedIndex;
    
        return (
        <div key={item.id}>
            <div>{item.label}</div>
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
*/