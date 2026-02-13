import Accordion from './components/Accordion';
import Dropdown from './components/Dropdown';

function App() {
  const options = [
    { label: 'Red', value: 'red' },
    { label: 'Green', value: 'green' },
    { label: 'Blue', value: 'blue' },
  ];

  return <Dropdown options={options} />    
}

export default App;
