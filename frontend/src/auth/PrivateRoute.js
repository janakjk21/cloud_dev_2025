// src/auth/PrivateRoute.js
import React from "react";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
  const token = sessionStorage.getItem("access_token");

  return token ? children : <Navigate to="/login" replace />;
};

export default PrivateRoute;
