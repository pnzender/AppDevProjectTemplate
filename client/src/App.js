import React, { useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Login from "./pages/MyLoginPage";
import Project from "./pages/Project";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/projects" element={<Project />} />
        {/* Add more routes as needed */}
        {/* Use Navigate for redirects */}
        {/* <Route path="/main" element={isLoggedIn ? <Dashboard /> : <Navigate to="/" />} /> */}
      </Routes>
    </Router>
  );
}

export default App;