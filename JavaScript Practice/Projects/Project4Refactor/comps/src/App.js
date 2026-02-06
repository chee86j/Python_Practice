import Accordion from './components/Accordion';

function App() {
  const items = [
    {
      id: 1,
      label: 'Can I use React on a project?',
      content: 'Yes, you can use React on any project you want.',
    },
    {
      id: 2,
      label: 'Can I use JavaScript on a project?',
      content: 'Yes, you can use JavaScript on any project you want.',
    },
    {
      id: 3,
      label: 'Can I use CSS on a project?',
      content: 'Yes, you can use CSS on any project you want.',
    },
  ];

  return (
      <Accordion items={items} />
  );
}

export default App;
