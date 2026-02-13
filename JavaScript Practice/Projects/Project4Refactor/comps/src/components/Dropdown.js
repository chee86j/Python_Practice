import { useState } from 'react';

function Dropdown({ options, selection, onSelect }) {
    const [isOpen, setIsOpen] = useState(false);

    const handleClick = () => {
        setIsOpen(!isOpen);
    };

    const handleOptionClick = (option) => {
        // Close the dropdown
        setIsOpen(false);
        // What option was clicked on?
        onSelect(option);
    };

    const renderedOptions = options.map((option) => {
        return (
            <div onClick={() => handleOptionClick(option)} key={option.value}>{option.label}</div>
        );
    });

    
    return <div>
        <div onClick={handleClick}>{selection?.label || 'Select...'}</div>
        {isOpen && <div>{renderedOptions}</div>}
    </div>;
}

export default Dropdown;