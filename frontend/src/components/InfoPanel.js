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

  // useEffect(() => {
  //   const fetchData = async () => {
  //     console.log(name)
  //     try {
  //       const response = await fetch(`http://127.0.0.1:5000/api/player-info/${name}`);
  //       if (!response.ok) {
  //         throw new Error('Failed to fetch data');
  //       }
  //       const result = await response.json();
  //       setData(result);
  //       console.log(result)
  //     } catch (error) {
  //       setError(error.message);
  //     }
  //   };

  //   fetchData(); // Call fetchData when the component mounts

  // }, [name]); // Empty dependency array ensures the effect runs only once on mount

  return (
    <div className='w-1/2 bg-slate-400 rounded-md'>
      <h1>{name}</h1>
      {/* <h2>{player?.name}</h2>
      <p>Team: {player?.team}</p>
      <p>Position: {player?.position}</p> */}
      {/* Add more player details as needed */}
      {/* <table border="1" cellPadding="5" cellSpacing="0">
          <tbody>
            {Object.keys(playerData).map((key) => (
              <tr key={key}>
                <td><strong>{key}</strong></td>
                <td>{renderValue(playerData[key])}</td>
              </tr>
            ))}
          </tbody>
        </table> */}
    </div>
  )
}

export default InfoPanel