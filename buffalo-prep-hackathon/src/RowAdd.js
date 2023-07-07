import React, { useState } from 'react';
import { Table, Button } from 'reactstrap';
import ModalForm from './ModalForm';

function RowAdd() {
  const [rows, setRows] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);

  const toggleModal = () => {
    setModalOpen((prevState) => !prevState);
  };

  const addRow = (rowData) => {
    setRows((prevRows) => [...prevRows, rowData]);
  };

  return (
    <div className="container">
      <Button color="primary" onClick={toggleModal}>
        Add Row
      </Button>

      <Table>
        <thead>
          <tr>
            <th>Student Name</th>
            <th>GPA</th>
            {/* Repeat the table headers for the remaining fields */}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, index) => (
            <tr key={index}>
              <td>{row.field1}</td>
              <td>{row.field2}</td>
              {/* Repeat the table cells for the remaining fields */}
            </tr>
          ))}
        </tbody>
      </Table>

      <ModalForm isOpen={modalOpen} toggleModal={toggleModal} addRow={addRow} />
    </div>
  );
}

export default RowAdd;
