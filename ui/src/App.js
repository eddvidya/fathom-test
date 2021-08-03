import React, { useState, useEffect } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

function App() {
  const [logs, setLog] = React.useState(null);

  useEffect(() => {
    axios.get('/logs/').then((response) => {
      const data = response.data.map(log => <p>{log.id} - {log.desc} - {log.created}</p>);
      setLog(data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {logs}
      </header>
    </div>
  );
}

export default App;
