import Link from './components/Link';
import Route from './components/Route';
import AccordionPage from './pages/AccordionPage';
import DropdownPage from './pages/DropdownPage';

function App() {
  return (
    <div>
      <div>
        <Link to="/accordion">AccordionPage</Link>
        <Link to="/dropdown">DropdownPage</Link>
      </div>
      <Route path="/accordion">
        <AccordionPage />
      </Route>
      <Route path="/dropdown">
        <DropdownPage />
      </Route>
    </div>
  );
}

export default App;
