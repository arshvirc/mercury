import React, { useState } from 'react'
import { CiSearch } from "react-icons/ci";
import { GiPlagueDoctorProfile } from "react-icons/gi";
import { useNavigate } from 'react-router-dom'

import all_players from '../utils/constants'


const SearchBar = () => {
  const [query, setQuery] = useState("")
  const [options, setOptions] = useState([])
  const [selectedOptionIndex, setSelectedOptionIndex] = useState(-1);
  const navigate = useNavigate()

  const handleInputChange = (event) => {
    const { value } = event.target;
    setQuery(value);
    if (value === "") {
      setOptions([]);
      setSelectedOptionIndex(-1);
    } else {
      const filteredResults = all_players.filter((name) =>
        name.toLowerCase().includes(value.toLowerCase())
      );
      setOptions(filteredResults);
      setSelectedOptionIndex(-1);
    }
  };

  const withRange = (id, size) => {
    if (selectedOptionIndex === -1 && 0 <= id && id < 5) {
      return false
    } else if (selectedOptionIndex > 2 && selectedOptionIndex - 2 <= id && id <= selectedOptionIndex + 2) {
      return false
    } else if (selectedOptionIndex <= 2 && 0 <= id && id <= 4) {
      return false
    } else if (size - 3 <= selectedOptionIndex && size - 5 <= id) {
      return false
    }
    return true
  }

  const handleKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      setSelectedOptionIndex((prevIndex) =>
        prevIndex < options.length - 1 ? prevIndex + 1 : prevIndex
      );
    } else if (e.key === 'ArrowUp') {
      setSelectedOptionIndex((prevIndex) =>
        prevIndex > 0 ? prevIndex - 1 : prevIndex
      );
    } else if (e.key === 'Enter') {
      if (selectedOptionIndex !== -1) {
        e.preventDefault()
        setQuery("")
        setOptions([])
        navigate(`/player/${options[selectedOptionIndex]}`);
      }
    }
  };

  const handleOptionClick = (e, option) => {
    setQuery("")
    setOptions([])
    navigate(`/player/${option}`);
    // onSubmit(option)
  };


  return (
      <div className='flex flex-col items-center relative'>
        <form className='flex flex-row gap-4 w-[60%] bg-white rounded-lg m-4 px-4 py-2 items-center'>
          <CiSearch />
          <input
            type='text'
            value={query}
            onChange={handleInputChange}
            onKeyDown={handleKeyDown}
            placeholder='Enter player name'
            className='outline-none'
          />
        </form>
        {options.length > 0 && (
        <ul className='flex flex-col bg-white w-[60%] rounded-lg items-start z-10 top-full absolute'>
          {options.map((option, id) => {
            return (
              <div className='flex flex-col w-full' key={id}>
                <li 
                  onClick={(e) => handleOptionClick(e, option)}
                  className={` ${id === selectedOptionIndex ? 'bg-slate-300' : ''}${ withRange(id, options.length) ? 'hidden' : ''} flex flex-row items-center w-full h-full border-b border-gray-300`}
                > 
                  <GiPlagueDoctorProfile className='mx-4'/>
                  <div className='flex flex-col'>
                    <h2 className='text-md'>{option}</h2>
                    <h2 className='text-xs'>Team Name</h2>
                  </div>
                </li>
              </div>
            )
          })}
        </ul>
        )}
      </div>
  )
}
export default SearchBar
