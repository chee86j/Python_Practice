import { useState, useEffect, useRef } from 'react';
import { GoChevronDown } from 'react-icons/go';
import Panel from './Panel';

function Dropdown({ options, value, onChange }) {
    const [isOpen, setIsOpen] = useState(false);
    /* We use a ref so we can "point at" the real DOM node for this dropdown.
    That gives us a reliable way to check if a click happened inside or outside. */
    const divEl = useRef();

    useEffect(() => {
        /*This handler runs on every document click so we can close the dropdown
        when the user clicks anywhere outside of it.*/
        const handler = (event) => {
            // If the ref isn't attached yet, we can't check containment, so just bail out.
            if (!divEl.current) {
                return;
            }
            /* If the click target is NOT inside the dropdown, close it.
            `contains` returns true when the target is inside the ref element. */
            if (!divEl.current.contains(event.target)) {
                setIsOpen(false);
                }
            };

            /* Passing true makes this run in the capture phase:
            capture -> target -> bubble
            We want capture so this listener runs before React's onClick handlers. */
            document.addEventListener('click', handler, true);
            return () => {
                /* Cleanup: remove the document listener when the component unmounts.
                This prevents memory leaks and duplicate handlers. */
                document.removeEventListener('click', handler, true);
            };
        // [] means run once on mount (great for event listeners) and clean up on unmount.
        }, []);

    const handleClick = () => {
        // Toggle the open/closed state when the dropdown header is clicked.
        setIsOpen((currentIsOpen) => !currentIsOpen);
    };

    const handleOptionClick = (option) => {
        // Close the dropdown when an option is selected.
        setIsOpen(false);
        // Send the selected option back up to the parent.
        onChange(option);
    };

    const renderedOptions = options.map((option) => {
    return (
      <div
        className="hover:bg-sky-100 rounded cursor-pointer p-1"
        onClick={() => handleOptionClick(option)}
        key={option.value}
      >
        {option.label}
      </div>
    );
  });
    
    return (
        // Sometimes divEl might be null on first render, so we check it before accessing it.
        <div ref={divEl} className='relative w-48'>
            <Panel
            className='flex justify-between items-center cursor-pointer'
            onClick={handleClick}>
                {/* Show the chosen label, or a default prompt if nothing is selected yet. */}
                {value?.label || 'Select...'}
                <GoChevronDown className='text-lg' />
            </Panel>
            {isOpen && <Panel className='absolute top-full z-10'>
                {/* Each option calls handleOptionClick with the option data. */}
                {renderedOptions}
            </Panel>}
        </div>
    );
}

export default Dropdown;
