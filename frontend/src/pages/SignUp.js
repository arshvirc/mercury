import React, { useRef, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { auth } from '../firebase';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { FcGoogle } from 'react-icons/fc';
import { useAuth } from '../contexts/AuthContext';

const SignUp = () => {
  const { googleSignIn, signInWithEmail } = useAuth();
  const [createAccount, setCreateAccount] = useState(false)
  const navigate = useNavigate();

  const handleGoogleSignIn = async () => {
    try {
      await googleSignIn();
      navigate("../home/all")
    } catch (error) {
      console.error("Google Sign-In Error:", error);
    }
  };

  const handleEmailCreateAccount = async (email, password) => {
    try {
      await signInWithEmail(auth, email, password);
      navigate("../home/all")
    } catch (error) {
      console.error("Google Sign-In Error:", error);
    }
  };

  return (
    createAccount ? (<EmailSignIn signUpWithEmail={handleEmailCreateAccount}/>) : 
    (<ShowSignInOptions setUpUsingEmail={setCreateAccount} googleSignIn={handleGoogleSignIn}/>)
  );
};


const ShowSignInOptions = ({ setUpUsingEmail, googleSignIn }) => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <div className="p-8 max-w-md w-full flex flex-col gap-2">
        <div>
          <h1 className='text-left text-lg font-semibold pb-8'>Sign in to Mercury</h1>
          <div className="text-center">
            <button
              onClick={googleSignIn}
              className="btn-primary bg-slate-900 text-white"
            >
              <FcGoogle />
              <p className='text-xs font-semibold'>Sign Up with Google</p>
            </button>
          </div>
        </div>
        <div className="flex items-center justify-center my-4">
          <div className="flex-grow border-t border-gray-300"></div>
            <span className="mx-4 text-xs text-gray-500">or </span>
          <div className="flex-grow border-t border-gray-300"></div>
        </div>
        <div>
          <div className="text-center">
            <button
              onClick={ () => setUpUsingEmail(true)}
              className="btn-primary "
              
            >
              <p className='text-xs font-semibold'>Continue with email</p>
            </button>
          </div>
        </div>
        <div className="text-center text-slate-900 text-xs">
          <p>
            Already have an account? 
            <Link to="/" className="text-slate-900 text-xs underline pl-1">Log In</Link>
          </p>
        </div>
      </div>
    </div>
  );
}


const EmailSignIn = ({signUpWithEmail}) => {
  const emailRef = useRef()
  const passwordRef = useRef();


  const handleSignUp = async () => {
    try {
      await createUserWithEmailAndPassword(auth, emailRef.current.value, passwordRef.current.value);
    } catch (error) {
      console.error("Google Sign-In Error:", error);
    }
  };


  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-4">
      <div className='px-8 flex flex-col items-center justify-center gap-4'>
        <h1 className='max-w-md w-full text-left text-xl font-bold py-4'>Sign up to Mercury</h1>
        <div className='flex flex-row gap-2'>
          <div>
            <p className='text-xs font-semibold'>Name</p>
            <input
              type="name"
              placeholder=""
              // value={name}
              // onChange={handleEmailChange}
              className="w-full px-4 py-2 border rounded-md"
            />
          </div>
          <div>
            <p className='text-xs font-semibold'>Username</p>
            <input
              type="username"
              placeholder=""
              // value={username}
              // onChange={handlePasswordChange}
              className="w-full px-4 py-2 border rounded-md"
            />
          </div>
        </div>
        <div className='w-full'>
          <p className='text-xs font-semibold pb-1'>Username</p>
          <input
            type="email"
            placeholder="Email Address"
            ref={emailRef}
            className="w-full px-4 py-2 border rounded-md"
          />
        </div>
        <div className='w-full'>
          <p className='text-xs font-semibold pb-1'>Password</p>
          <input
            type="password"
            placeholder="6+ characters"
            ref={passwordRef}
            className="w-full px-4 py-2 border rounded-md"
          />
        </div>
        <div className="text-center w-full">
          <button
            onClick={handleSignUp}
            className="btn-primary bg-slate-900 text-white mt-8"
          >
            Create Account
          </button>
        </div>
        <div className="text-center text-slate-900 text-xs">
          <p>
            Already have an account? 
            <Link to="/login" className="text-slate-900 text-xs underline pl-1">Log In</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default SignUp;