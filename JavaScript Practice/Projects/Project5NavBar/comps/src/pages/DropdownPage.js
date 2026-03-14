import { useState } from 'react';
import Dropdown from '../components/Dropdown';

function DropdownPage() {
  const [selected, setSelected] = useState(null);

  const handleSelect = (option) => {
    setSelected(option);
  };

  const options = [
    { label: 'Red', value: 'red' },
    { label: 'Green', value: 'green' },
    { label: 'Blue', value: 'blue' },
  ];

  return (
    <div className='flex'>
      <Dropdown options={options} value={selected} onChange={handleSelect} />
      <Dropdown options={options} value={selected} onChange={handleSelect} />
    </div>
  );
}

export default DropdownPage;
