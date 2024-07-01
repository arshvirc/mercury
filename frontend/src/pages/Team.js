import React, { useEffect, useState } from 'react'
import PropCard from '../components/PropCard';
import { retrieveTeamSuggestion } from '../api';

const Team = () => {
    const [cards, setCards] = useState([]);

    useEffect(() => {
        const fetchTeamCards = async () => {
            try {
              const fetchedCards = await retrieveTeamSuggestion('Dallas Mavericks')
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
    <div className="pt-8 px-2 grid gap-6 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        {cards.map((card, index) => (
            <PropCard key={index} card={card} />
        ))}
    </div>
  );
};

export default Team