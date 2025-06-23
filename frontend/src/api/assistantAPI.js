import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const getAnswer = async (question, context) => {
  const response = await axios.post(`${API_URL}/answer`, { question, context });
  return response.data.answer;
};
