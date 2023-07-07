import React, { useEffect, useState } from 'react';
import { Table } from 'reactstrap';

function CSVLoad() {
    const [data, setData] = useState([]);
    const [isOpen, setIsOpen] = useState(false);
    const toggle = () => setIsOpen(!isOpen);

    useEffect(() => {
        // Fetch CSV data
        fetch('student_data.csv')
            .then((response) => response.text())
            .then((text) => {
                // Convert CSV to array of objects
                const rows = text.split('\n');
                const headers = rows[0].split(',');
                const rowData = rows.slice(1).map((row) => {
                    const values = row.split(',');
                    return headers.reduce((obj, header, index) => {
                        obj[header] = values[index];
                        return obj;
                    }, {});
                });

                setData(rowData);
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