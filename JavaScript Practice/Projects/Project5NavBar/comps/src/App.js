import Sidebar from './components/Sidebar';
import Route from './components/Route';
import AccordionPage from './pages/AccordionPage';
import DropdownPage from './pages/DropdownPage';
import ButtonPage from './pages/ButtonPage';

function App() {
  return (
    <div className="container mx-auto mt-4 grid grid-cols-1 gap-4 px-4 md:grid-cols-6">
      <Sidebar />
      <div className="md:col-span-5">
        <Route path="/accordion">
          <AccordionPage />
        </Route>
        <Route path="/">
          <DropdownPage />
        </Route>
        <Route path="/buttons">
          <ButtonPage />
        </Route>
        <Route path="/button">
          <ButtonPage />
        </Route>
      </div>
    </div>
  );
}

export default App;
