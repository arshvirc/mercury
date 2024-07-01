import apiClient from "./apiClient";

export const retrieveTeamSuggestion = async (team_name) => {
  try {
    const response = await apiClient.get(`/team-suggestions/${team_name}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching data from Info Endpoint:', error);
    throw error;
  }
};

export const addSuggestionToFavourites = async (uid, suggestion) => {
  try {
    console.log(suggestion)
    const response = await apiClient.put(`/favourites/${uid}`, suggestion);
    return response.data;
  } catch (error) {
    console.error('Error fetching data from Info Endpoint:', error);
    throw error;
  }
};

export const getFavourites = async (uid) => {
  try {
    const response = await apiClient.get(`/favourites/${uid}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching data from Info Endpoint:', error);
    throw error;
  }
};


export const retrieveTeams = async () => {
  try {
    const response = await apiClient.get('/teams');
    return response.data;
  } catch (error) {
    console.error('Error fetching data from Info Endpoint:', error);
    throw error;
  }
};