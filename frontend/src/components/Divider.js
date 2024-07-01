import React from 'react'


const Divider = ({text}) => {
  return (
    text ? (
      <div className="flex items-center justify-center sm:hidden">
        <div className="flex-grow border-t border-gray-300"></div>
          <span className="mx-4 text-xs text-gray-500">{text}</span>
        <div className="flex-grow border-t border-gray-300"></div>
      </div>
    ) : (
      <div className="flex items-center justify-center border-t border-gray-400 sm:hidden">
      </div>
    )
  )
}

export default Divider