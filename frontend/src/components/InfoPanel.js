import React, { useEffect, useState } from 'react'
import { retrieveInfo } from '../api/retrieveInfo';

const InfoPanel = ({ name }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        const result = await retrieveInfo(name);
        setData(result);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, [name]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  console.log(data)

  return (
    <div className='w-1/2 bg-slate-400 rounded-md'>
      <h1>{name}</h1>
    </div>
  )
}

export default InfoPanel