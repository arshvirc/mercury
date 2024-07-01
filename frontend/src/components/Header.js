import React, { useEffect, useState } from 'react';
import { HiMenuAlt2 } from "react-icons/hi";
import { IoMdClose } from "react-icons/io";
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const Header = () => {
  const [isOpen, setIsOpen] = useState(false);
  const { logout } = useAuth();
  const navigate = useNavigate();

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  useEffect(() => {
    if (isOpen) {
      document.body.classList.add('overflow-hidden');
    } else {
      document.body.classList.remove('overflow-hidden');
    }
  }, [isOpen]);

  const handleSignOut = async () => {
    await logout()
    navigate('/login')
  }


  return (
    <header className="py-7 bg-white flex flex-col">
      <div className='flex flex-row justify-between text-xl z-30 sm:px-8'>
        
        <div className='flex flex-row gap-2 items-center justify-center'>
          <button onClick={toggleMenu} className="sm:hidden">
            {isOpen ? (<IoMdClose />): (<HiMenuAlt2 />)}
          </button>
          <Link to='/home/all'> 
            <h1>Mercury</h1>
          </Link>
          <div className='sm:flex flex-row gap-2 items-center justify-center text-sm hidden pl-24'>
            <Link to='/favourites/all' className=' px-4 py-2 text-gray-800 hover:bg-gray-200'> Favourites </Link>
            <Link to='/optimization/all' className='px-4 py-2 text-gray-800 hover:bg-gray-200'> Optimize </Link>
          </div>
        </div>
        <div className='flex flex-row gap-2 items-center justify-center'>
          <button className='w-full flex flex-row justify-center items-center gap-4 bg-black px-2 py-2 text-white text-sm rounded-3xl border' onClick={handleSignOut}>
            Sign Out
          </button>
        </div>
      </div>
      <div
        className={`fixed top-[5.5rem] z-30 left-0  bg-white w-screen shadow-lg transition-transform transform ${
          isOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        <ul className="flex flex-col p-4 space-y-2 font-medium ">
          <Link to='/favourites/all' className=' px-4 py-2 text-gray-800 hover:bg-gray-200'> Favourites </Link>
          <Link to='/optimization/all' className='px-4 py-2 text-gray-800 hover:bg-gray-200'> Optimize </Link>
        </ul>
      </div>
      <div 
        className={`fixed top-[5.5rem] z-20 left-0 bg-black bg-opacity-20 w-screen h-screen ${
          isOpen ? 'translate-x-0' : '-translate-x-full'}`}
        onClick={toggleMenu}
      >
      </div>
    </header>

  );
};

export default Header;