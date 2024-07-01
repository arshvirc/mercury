import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import SignIn from './pages/SignUp';
import LogIn from './pages/LogIn';
import { AuthProvider } from './contexts/AuthContext';
import PrivateRoute from './components/PrivateRoute';
import ErrorPage from './pages/ErrorPage';
import Favourites from './pages/Favourites';
import Optimization from './pages/Optimization';
import Team from './pages/Team';
import Home from './pages/Home';
import HeaderLayout from './components/HeaderLayout';

function App() {

  return (
    <Router>
      <AuthProvider>
        <Routes>  
            <Route path="/login" element={<LogIn />}/>
            <Route path="/signup" element={<SignIn />}/>
            <Route
              path="/home/:type"
              element={
                <PrivateRoute>
                  <HeaderLayout>
                    <Home />
                  </HeaderLayout>
                </PrivateRoute>
              }
            />
            <Route
              path="/team/:team"
              element={
                <PrivateRoute>
                  <HeaderLayout>
                    <Team />
                  </HeaderLayout>
                </PrivateRoute>
              }
            />
            <Route
              path="/favourites/:type"
              element={
                <PrivateRoute>
                  <HeaderLayout>
                    <Favourites />
                  </HeaderLayout>
                </PrivateRoute>
              }
            />
            <Route
              path="/optimization/:type"
              element={
                <PrivateRoute>
                  <HeaderLayout>
                    <Optimization />
                  </HeaderLayout>
                </PrivateRoute>
              }
            />
            <Route path="*" element={<ErrorPage />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
