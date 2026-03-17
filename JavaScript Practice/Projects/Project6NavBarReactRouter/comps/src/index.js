import './index.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter } from 'react-router-dom';


const el = document.getElementById('root');
const root = ReactDOM.createRoot(el);

root.render(
  <>
    {/* Old custom router provider code (replaced by BrowserRouter): */}
    {/* 
    <NavigationProvider>
      <App />
    </NavigationProvider>
    */}

    <BrowserRouter>
      <App />
    </BrowserRouter>
  </>
);
