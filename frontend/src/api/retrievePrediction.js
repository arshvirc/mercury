import apiClient from './apiClient';

export const retrievePrediction = async (name) => {
  try {
    const response = await apiClient.get(`/api/player-prediction/${name}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching data from retrieve Info:', error);
    throw error;
  }
};