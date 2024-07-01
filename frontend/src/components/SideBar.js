import React from 'react'
import Header from './Header';
import Divider from './Divider';
import Dropdown from './DropDown';

import { stats_type } from '../utils/constants';


const SideBar = ({ children }) => {

  return (
    <div className='flex flex-row h-screen w-screen'>
      <div className='max-w-[1/5]'>
        <Header />
      </div>
      <div className='flex flex-col gap-8'>
        <Dropdown options={stats_type}/>
        { children }
      </div>
    </div>
  );
}

export default SideBar