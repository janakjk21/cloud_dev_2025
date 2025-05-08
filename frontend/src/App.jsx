import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";
import MainDashboard from "./searchfeatures/Maindashboard";
import Login from "./auth/login";
import Register from "./auth/register";
import JobSubmitter from "./searchfeatures/JobSubmitter";

function App() {
  return (
    <Router>
      <Routes>
        {/* JobSubmitter is now the home route */}
        <Route path="/" element={<JobSubmitter />} />
        <Route path="/jobs" element={<JobSubmitter />} />
        <Route path="/create" element={<ContactForm />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
