import Navbar from './components/Navbar';
import Route from './components/Route';
import AccordionPage from './pages/AccordionPage';
import ButtonPage from './pages/ButtonPage';
import DropdownPage from './pages/DropdownPage';

function App() {
  return (
    <div className='mx-6 mt-6 grid grid-cols-4 gap-6'>
      <Navbar />
      <main className='col-span-3'>
        <Route path='/'>
          <div className='rounded border bg-white p-5 shadow'>
            {/* Short landing content so route transitions are easy to test while building your custom nav pieces. */}
            <h1 className='mb-3 text-2xl font-semibold'>Project 5: Nav + Custom Routing</h1>
            <p>Select a component page from the navbar to test navigation behavior.</p>
          </div>
        </Route>

        <Route path='/accordion'>
          <AccordionPage />
        </Route>

        <Route path='/dropdown'>
          <DropdownPage />
        </Route>

        <Route path='/buttons'>
          <ButtonPage />
        </Route>
      </main>
    </div>
  );
}

export default App;
