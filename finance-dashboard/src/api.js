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

// Fetch Investment Suggestions (Updated parameters)
export const getInvestmentSuggestions = async (bankId, investmentAmount) => { // Removed salaryRangeId
  if (!bankId || !investmentAmount) { // Add basic validation
    console.warn("Bank ID or Investment Amount missing for suggestions.");
    return [];
  }
  try {
    // Pass investment_amount and (optionally) duration_months to backend
    const response = await axiosInstance.get(
      `/investment-suggestions/?bank_id=${bankId}&investment_amount=${investmentAmount}&duration_months=12` // Added default duration
    );
    return response.data; // This will be an array of objects
  } catch (error) {
    console.error("Error fetching investment suggestions:", error);
    return []; // Return empty array on error
  }
};
