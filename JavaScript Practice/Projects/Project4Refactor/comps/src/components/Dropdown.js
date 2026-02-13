import { useState } from 'react';

function Dropdown({ options, value, onChange }) {
    const [isOpen, setIsOpen] = useState(false);

    const handleClick = () => {
        setIsOpen(!isOpen);
    };

    const handleOptionClick = (option) => {
        // Close the dropdown
        setIsOpen(false);
        // What option was clicked on?
        onChange(option);
    };

    const renderedOptions = options.map((option) => {
        return (
            <div onClick={() => handleOptionClick(option)} key={option.value}>{option.label}</div>
        );
    });
    
    return <div>
        <div onClick={handleClick}>{value?.label || 'Select...'}</div>
        {/* We added optional chaining to the selection.label to avoid errors if the selection is null. */}
        {isOpen && <div>{renderedOptions}</div>}
    </div>;
}

export default Dropdown;