import React, { useEffect, useState } from 'react';
import { Table } from 'reactstrap';
import Papa from 'papaparse'

function CSVLoad() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch CSV data
    fetch('/example.csv')
      .then((response) => response.text())
      .then((text) => {
        // Parse CSV to array of objects
        const { data } = Papa.parse(text, { header: true });
        setData(data);
      });
  }, []);

  return (
    <div className="container">
      <Table>
        <thead>
          <tr>
            {Object.keys(data[0] || {}).map((header) => (
              <th key={header}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, index) => (
            <tr key={index}>
              {Object.values(row).map((value, index) => (
                <td key={index}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default CSVLoad;
