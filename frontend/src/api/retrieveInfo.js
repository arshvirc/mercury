import apiClient from './apiClient';

export const retrieveInfo = async (name) => {
  try {
    const response = await apiClient.get(`/api/player-info/${name}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching data from Info Endpoint:', error);
    throw error;
  }
};