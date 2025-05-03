import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const getSalaryRanges = () => axios.get(`${API_BASE_URL}/salary/`);
export const getBanks = () => axios.get(`${API_BASE_URL}/banks/`);
export const getInvestments = () => axios.get(`${API_BASE_URL}/investments/`);