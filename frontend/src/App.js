import React, { useState } from 'react'
import './App.css';
import InputForm from './components/InputForm';
import Prediction from './components/Prediction';

function App() {
  const [playerName, setPlayerName] = useState("")

  const handleQuery = (value) => {
    setPlayerName(value);
  };

  return (
    <div className="App">
      <h1>Mercury</h1>
      <InputForm onSearch={handleQuery}/>
      <Prediction name={playerName} />
    </div>
  );
}

export default App;
