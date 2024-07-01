import React, { useState, useRef, useEffect } from 'react';

const Dropdown = ({ options, selectedOption, onSelect }) => {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef(null);

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  const handleOptionClick = (option) => {
    onSelect(option);
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
        className="bg-blue-500 text-white rounded"
      >
        {selectedOption ? selectedOption.label : 'Select an option'}
      </button>
      {isOpen && (
        <ul className="absolute bg-white border mt-2 rounded shadow-lg w-[1/2]">
          {options.map((option) => (
            <li
              key={option.value}
              onClick={() => handleOptionClick(option)}
              className="px-4 py-2 cursor-pointer hover:bg-gray-200"
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

const options = [
  { label: 'All', value: '/all' },
  { label: 'Points', value: '/pts' },
  { label: 'Rebounds', value: '/reb' },
  { label: 'Assists', value: '/ast' },
];

const StatFilter = () => {
  const [selectedOption, setSelectedOption] = useState(options[0]);

  const handleSelect = (option) => {
    setSelectedOption(option);
  };

  return (
    <div className="">
      <Dropdown
        options={options}
        selectedOption={selectedOption}
        onSelect={handleSelect}
      />
    </div>
  );
};

export default StatFilter;