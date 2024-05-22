import React, { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import LandingPage from './pages/LandingPage';
import PlayerInfo from './pages/PlayerInfo';

function App() {

  return (
    <div className="mx-auto h-full px-4 py-4 font-sans md:px-4 md:py-4 1g:px-8 lg:py-4">
      <Router>
        <Routes>
          <Route path="" element={<LandingPage />}/>
          <Route path="/player/:name" element={<PlayerInfo />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
