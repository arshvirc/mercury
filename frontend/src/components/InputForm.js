import React, { useState } from 'react'

const InputForm = ({ onSearch }) => {
  const [query, setQuery] = useState("")

  const handleChange = (e) => {
    setQuery(e.target.value) 
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query);
    setQuery('');
  }
  return (
    <form onSubmit={handleSubmit}>
      <input
        type='text'
        value={query}
        onChange={handleChange}
        placeholder='Enter player name'
      />
      <button type='submit'>Predict</button>

    </form>
  )
}

export default InputForm