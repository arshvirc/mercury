import React from 'react'
import { useAuth } from '../contexts/AuthContext';
import { addSuggestionToFavourites } from '../api';
import { CiCirclePlus, CiStar } from "react-icons/ci";
import { VictoryPie } from 'victory';

const ProgressCircleVictory = ({ numerator, denominator }) => {
  const percentage = (numerator / denominator) * 100;
  const data = [{ x: 1, y: percentage }, { x: 2, y: 100 - percentage }];

  return (
    <div className="w-full h-full flex flex-col ">
      <VictoryPie
        data={data}
        innerRadius={50}
        labels={({ datum }) => null}
        style={{
          data: {
            fill: ({ datum }) => (datum.x === 1 ? '#00C49F' : '#F0F0F0'),
          },
        }}
      />
      <div className="flex items-center justify-center">
        <span className="text-sm">{`${numerator}/${denominator}`}</span>
      </div>
    </div>
  );
};

const fetchTeamCards = async (uid, card) => {
  try {
    const fetchedCards = await addSuggestionToFavourites(uid, card)
    console.log('Data updated successfully:', fetchedCards);
  } catch (error) {
    console.error('Error updating data:', error);
  }
};

const PropCard = ({ card }) => {
  const { currentUser } = useAuth();

  const handleFavorite = async (e) => {
    e.preventDefault();
    try {
      const result = await fetchTeamCards(currentUser.uid, card);
      console.log('User favorited successfully:', result);
      // Handle the result as needed
    } catch (error) {
      console.error('Error favoriting user:', error);
    }
  };

  return (
    <div className="border border-gray-400 rounded-lg aspect-h-[1/2] aspect-w-1">
      <div className="absolute inset-0 flex flex-col gap-2 items-center rounded-lg p-8 justify-center bg-green-500 bg-opacity-100 z-10 opacity-0 hover:opacity-100 transition-opacity duration-300 border border-green-500 text-white">
          <div className="flex flex-col text-sm">
            <div className='flex flex-row gap-2 items-center'>
              <CiCirclePlus />
              <p>Add to Parlay</p>
            </div>
            <div className='flex flex-row gap-2 items-center'>
            <button onClick={(e) => handleFavorite(e)} className='bg-blue-300'>
                <CiStar />
                <p>Add to Favourites</p>
              </button>
            </div>
          </div>
          <p className='text-sm pt-4'>Click for More Info </p>
        </div>
      
      <div className=' bg-slate-50 rounded-lg flex flex-col items-center justify-center h-full'>
        <div className='w-full h-full p-4 flex flex-row gap-2'>
          <div className='w-full h-full flex flex-col gap-2 items-left justify-center pl-2 text-xs'>
            <p className='text-sm'>{card.player}</p>
            {card.bet365_prop_milestone ? (<p>BET365 - {card.bet365_prop_milestone} {card.stat}</p>) : (<></>)}
            {card.fanduel_prop_milestone ? (<p>FanDuel - {card.fanduel_prop_milestone} {card.stat}</p>) : (<></>)}
          </div>
          <div className='w-[1/5]'>
            <ProgressCircleVictory numerator={card.fails} denominator={card.games_started}/>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PropCard;