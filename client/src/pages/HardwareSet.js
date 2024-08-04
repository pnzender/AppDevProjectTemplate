import React, { useState } from 'react';

function HardwareInfo() {
  const [hardwareInfo, setHardwareInfo] = useState([]);
  const [error, setError] = useState(null);

  const fetchHardwareInfo = async () => {
    try {
      const response = await fetch('/get_hw_info', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setHardwareInfo(data);
    } catch (error) {
      console.error('Error fetching hardware info:', error);
      setError('Failed to fetch hardware information.');
    }
  };

  return (
    <div>
      <h2>Hardware Information</h2>
      <button onClick={fetchHardwareInfo}>Fetch Hardware Info</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {hardwareInfo.map((item, index) => (
          <li key={index}>
            {/* Customize how you display each hardware item based on its structure */}
            <pre>{JSON.stringify(item, null, 2)}</pre>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HardwareInfo;