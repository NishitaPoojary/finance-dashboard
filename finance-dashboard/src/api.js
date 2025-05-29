import axiosInstance from './axiosInstance';

// Fetch Banks
export const getBanks = async () => {
  try {
    const response = await axiosInstance.get('/banks/');
    return response.data;
  } catch (error) {
    console.error("Error fetching banks:", error);
    return [];
  }
};

// Fetch Salary Ranges
export const getSalaryRanges = async () => {
  try {
    const response = await axiosInstance.get('/salary-ranges/');
    return response.data;
  } catch (error) {
    console.error("Error fetching salary ranges:", error);
    return [];
  }
};