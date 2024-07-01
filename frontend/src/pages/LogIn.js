import React, { useRef, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FcGoogle } from "react-icons/fc";
import { useAuth } from '../contexts/AuthContext';
import Divider from '../components/Divider';


const LogIn = () => {
  const emailRef = useRef();
  const passwordRef = useRef();
  const { login, googleSignIn } = useAuth();
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      setError('');
      setLoading(true);
      await login(emailRef.current.value, passwordRef.current.value);
      setLoading(false);
      console.log("after")
      navigate("../home/all")
      // history.push("/");
    } catch(e) {
      setError(`Failed to log in ${e}`);
    }

    setLoading(false);
  };

  const handleGoogleSignIn = async () => {
    try {
      await googleSignIn();
      navigate("../home/all")
    } catch (e) {

    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <div className="p-8 max-w-md w-full flex flex-col gap-2">
        <div>
          <h1 className='text-left text-lg font-semibold pb-8'>Log in to Mercury</h1>
          <div className="text-center">
            <button
              onClick={handleGoogleSignIn}
              className="btn-primary"
            >
              <FcGoogle />
              <p className='text-xs font-semibold'>Log In with Google</p>
            </button>
          </div>
        </div>
        <Divider text={"or log in with email"}/>
        {error && <p>{error}</p>}
        <p className='text-xs font-semibold'>Email</p>
        <input
          type="email"
          ref={emailRef}
          className="w-full px-4 py-2 border rounded-lg"
        />
        <p className='text-xs font-semibold'>Password</p>
        <input
          type="password"
          ref={passwordRef}
          className="w-full px-4 py-2 border rounded-lg"
        />
        <div className="text-center">
          <button
            onClick={handleSubmit}
            className="btn-primary bg-slate-900 text-white mt-8"
            disabled={loading}
            type='submit'
          >
            Sign In
          </button>
        </div>
        <div className="text-center text-slate-900 text-xs">
          <p>
            Don't have an account? 
            <Link to="/signup" className="text-slate-900 text-xs underline pl-1">Sign Up</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LogIn;