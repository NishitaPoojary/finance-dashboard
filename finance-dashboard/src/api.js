import axiosInstance from './axiosInstance';

// Fetch Banks
export const getBanks = async () => {
  try {
    const response = await axiosInstance.get('/banks/');
    return response.data;
  } catch (error) {
    console.error("Error fetching banks:", error);
    return[];
  }
};