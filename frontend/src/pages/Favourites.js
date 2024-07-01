import React, { useEffect, useState } from 'react'
import { useAuth } from '../contexts/AuthContext';
import PropCard from '../components/PropCard';
import { getFavourites } from '../api';

const Favourites = () => {
  const { currentUser } = useAuth();
  const [cards, setCards] = useState([]);
  // console.log("BYYYEEE UN FAV")

  useEffect(() => {
    const fetchTeamCards = async () => {
      try {
        const fetchedCards = await getFavourites(currentUser.uid)
        console.log('Data updated successfully:', fetchedCards);
        setCards(fetchedCards)
      } catch (error) {
        console.error('Error updating data:', error);
      }
    };
      fetchTeamCards();
  }, [currentUser]);

  console.log(cards)

  return (
    <div className="flex flex-col h-screen px-7">
      Favourites for {currentUser.email}
      <div className="pt-8 px-2 grid gap-6 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        {cards.map((card, index) => (
          <PropCard key={index} card={card} />
        ))}
      </div>
    </div>
  )
}

export default Favourites