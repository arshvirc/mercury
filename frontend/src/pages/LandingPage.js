import React from 'react'
import SearchBar from '../components/SearchBar'

const LandingPage = () => {
  return (
    <section className="mx-auto min-h-screen px-4 py-4 font-sans md:px-4 md:py-4 1g:px-8 lg:py-4">
      <div className='pt-24 pb-12 text-center'>
        <h1 className='font-bold text-5xl text-accent'>Mercury</h1>
        <p className='pt-4'>Find out what you should be betting</p>
      </div>
      <SearchBar className='h-screen border'/>
    </section>
  )
}

export default LandingPage