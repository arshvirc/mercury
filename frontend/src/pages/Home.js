import React, { useEffect, useState } from 'react'
import SearchBar from '../components/SearchBar';
import { retrieveTeams } from '../api';
import { useParams } from 'react-router-dom';

const Home = () => {
    const [cards, setCards] = useState([]);
    const { type } = useParams();
    console.log(type)

    useEffect(() => {
        const fetchTeamCards = async () => {
            try {
              const fetchedCards = await retrieveTeams()
              console.log('Data updated successfully:', fetchedCards);
              // Handle the updated data as needed
              setCards(fetchedCards)
            } catch (error) {
              console.error('Error updating data:', error);
            }
        };
        fetchTeamCards();
      }, []);

  return (
    <div className=" border-black border">
      <SearchBar results={cards.map((card) => card.full_name)}/>
      {/* <StatFilter /> */}

        {/* {cards.map((card, index) => (
            <PropCard key={index} card={card} />
        ))} */}
    </div>
  );
};

export default Home