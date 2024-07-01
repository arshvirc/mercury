// PrivateRoute.js
import React from 'react';
import { Navigate, useParams } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const PrivateRoute = ({ children }) => {
  const { currentUser } = useAuth();
  const { type } = useParams();
  let element = children
  // if (!(type === 'all' | type === 'pts' | type === 'reb' | type === 'ast')) {
  //   element = <Navigate to='/error' />
  // }

  if (! currentUser) element = <Navigate to="/login" />
  return element;
};

export default PrivateRoute;