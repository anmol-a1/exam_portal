import axios from 'axios';

const baseURL = '134.209.157.1/';

const axiosInstance = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		'Content-Type': 'application/json',
		accept: 'application/json',
	},
});
export default axiosInstance;