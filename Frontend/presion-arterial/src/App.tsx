// App.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { LoginForm, RegisterForm, UserProfile } from './routes';


const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <h1>Bienvenido a la App de Presión Arterial</h1>
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/profile" element={<UserProfile />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;


