import React from 'react'
import Header from '../components/Header';
import Divider from '../components/Divider';
import Dropdown from './DropDown';

import { stats_type } from '../utils/constants';


const HeaderLayout = ({ children }) => {

  return (
    <div className='flex flex-col h-screen px-7 gap-4'>
      <Header />
      <div className='flex flex-row gap-8 px-4'>
        <Dropdown options={stats_type}/>
        
      </div>
      <Divider />
      { children }
    </div>
  );
}

export default HeaderLayout