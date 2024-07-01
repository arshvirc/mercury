import React from 'react'
import Header from '../components/Header';
import Divider from '../components/Divider';


const HeaderLayout = ({ children }) => {

  return (
    <div className='flex flex-col h-screen px-7 gap-4'>
      <Header />
      <Divider />
      { children }
    </div>
  );
}

export default HeaderLayout