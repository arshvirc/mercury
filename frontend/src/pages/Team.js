import React, { useEffect, useState } from 'react'
import PropCard from '../components/PropCard';
import { retrieveTeamSuggestion } from '../api';
import { useParams } from 'react-router-dom';

const Team = () => {
    const [cards, setCards] = useState([]);
    const { team } = useParams();
    console.log(team)

    useEffect(() => {
        const fetchTeamCards = async () => {
            try {
              const fetchedCards = await retrieveTeamSuggestion(team)
              console.log('Data updated successfully:', fetchedCards);
              // Handle the updated data as needed
              setCards(fetchedCards)
            } catch (error) {
              console.error('Error updating data:', error);
            }
        };
        fetchTeamCards();
      }, [team]);

  return (
    <div className="pt-8 px-2 grid gap-6 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        {cards.map((card, index) => (
            <PropCard key={index} card={card} />
        ))}
    </div>
  );
};

export default Team