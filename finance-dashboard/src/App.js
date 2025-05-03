import React, { useEffect, useState } from 'react';
import axiosInstance from './axiosInstance';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axiosInstance.get('')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching API:', error);
      });
  }, []);

  return (
    <div>
      <h1>Finance Dashboard</h1>
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;