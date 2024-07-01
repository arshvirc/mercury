import React, { useState, useRef, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { IoMdArrowDropdown } from "react-icons/io";

const Dropdown = ({ options }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null);
  const dropdownRef = useRef(null);
  const location = useLocation();
  const navigate = useNavigate();

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  const handleOptionClick = (option) => {
    setSelectedOption(option);
    const page = location.pathname.split('/')[1].toString()
    navigate(`/${page}${option.value}`)
    setIsOpen(false);
  };

  const handleClickOutside = (event) => {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
      setIsOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  return (
    <div className="relative" ref={dropdownRef}>
      <button
        onClick={handleToggle}
        className="border-grey-500 border px-3 rounded-lg gap-3 py-2 flex flex-row justify-center items-center"
      >
        {selectedOption ? selectedOption.label : location.pathname.split('/')[2].toString()}
        <IoMdArrowDropdown />

      </button>
      {isOpen && (
        <ul className="absolute bg-white border mt-2 rounded-xl shadow-lg w-[1/2] px-2 py-3 z-50">
          {options.map((option) => (
            <li
              key={option.value}
              onClick={() => handleOptionClick(option)}
              className="px-4 py-2 cursor-pointer hover:bg-gray-200 rounded-md text-sm font-poppins"
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Dropdown;