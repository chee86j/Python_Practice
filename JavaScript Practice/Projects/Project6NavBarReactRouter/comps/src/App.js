import Sidebar from './components/Sidebar';
import { Routes, Route } from 'react-router-dom';
import AccordionPage from './pages/AccordionPage';
import DropdownPage from './pages/DropdownPage';
import ButtonPage from './pages/ButtonPage';
import ModalPage from './pages/ModalPage';
import TablePage from './pages/TablePage';

function App() {
  return (
    <div className="container mx-auto mt-4 grid grid-cols-1 gap-4 px-4 md:grid-cols-6">
      <Sidebar />
      <div className="md:col-span-5">
        {/* Old custom Route implementation (replaced by react-router-dom): */}
        {/* 
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
        */}

        <Routes>
          <Route path="/" element={<DropdownPage />} />
          <Route path="/accordion" element={<AccordionPage />} />
          <Route path="/buttons" element={<ButtonPage />} />
          <Route path="/button" element={<ButtonPage />} />
          <Route path="/modal" element={<ModalPage />} />
          <Route path="/table" element={<TablePage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
