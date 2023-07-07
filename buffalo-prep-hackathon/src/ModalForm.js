import React, { useState } from 'react';
import { Button, Modal, ModalHeader, ModalBody, ModalFooter, FormGroup, Label, Input } from 'reactstrap';

const ModalForm = ({ isOpen, toggleModal, addRow }) => {
  const [formData, setFormData] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = () => {
    addRow(formData);
    setFormData({});
    toggleModal();
  };

  return (
    <Modal isOpen={isOpen} toggle={toggleModal}>
      <ModalHeader toggle={toggleModal}>Add Row</ModalHeader>
      <ModalBody>
        <FormGroup>
          <Label for="field1">Name</Label>
          <Input type="text" name="field1" id="field1" value={formData.field1 || ''} onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label for="field2">GPA</Label>
          <Input type="text" name="field2" id="field2" value={formData.field2 || ''} onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label for="field3">Dropout</Label>
          <Input type="text" name="field3" id="field3" value={formData.field3 || ''} onChange={handleChange} />
        </FormGroup>
      </ModalBody>
      <ModalFooter>
        <Button color="primary" onClick={handleSubmit}>
          Add
        </Button>
        <Button color="secondary" onClick={toggleModal}>
          Cancel
        </Button>
      </ModalFooter>
    </Modal>
  );
};

export default ModalForm;
