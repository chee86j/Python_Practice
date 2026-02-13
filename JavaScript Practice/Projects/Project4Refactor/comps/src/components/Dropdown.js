import { useState } from 'react';
import { GoChevronDown } from 'react-icons/go';
import Panel from './Panel';

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
            <div className="hover:bg-sky-100 rounded cursor-pointer p-1" 
            onClick={() => handleOptionClick(option)} key={option.value}>{option.label} </div>
        );
    });
    
    return <Panel className="w-48 relative">
        <Panel className="flex justify-between items-center cursor-pointer" onClick={handleClick}>
            {value?.label || 'Select...'}
            <GoChevronDown className="text-lg" />

            </Panel>
        {isOpen && <Panel className="absolute top-full">{renderedOptions}</Panel>}
    </Panel>;
}
// Note that <Panel> is used to wrap the content of the dropdown to minimize Tailwind

export default Dropdown;