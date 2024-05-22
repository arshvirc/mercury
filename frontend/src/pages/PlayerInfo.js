import React from 'react'
import { useParams } from 'react-router-dom'
import SearchBar from '../components/SearchBar';
import Prediction from '../components/Prediction';
import InfoPanel from '../components/InfoPanel';

const PlayerInfo = () => {
  const { name } = useParams();
  const decodedName = decodeURIComponent(name);
  return (
    <section className="mx-auto min-h-screen px-4 py-2 font-sans md:px-4 md:py-4 1g:px-8 lg:py-4">
      <div className='flex flex-row justify-between pb-12 sticky items-center'>
        <h1 className='pl-12'> Mercury </h1>
        <div className='w-[60%] items-end'>
          <SearchBar className='h-[60%]'/>
        </div>
      </div>

      <div className='flex flex-row w-full gap-4'>
        <InfoPanel name={decodedName} />
        <Prediction name={decodedName}/>
      </div>
    </section>
  )
}

export default PlayerInfo