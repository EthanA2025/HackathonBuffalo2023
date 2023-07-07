import React, { useState } from 'react';
import {
  Navbar,
  NavbarBrand,
  Container,
} from 'reactstrap';
import CSVLoad from './CSVLoad';

function MainComp(args) {

  return (
    <div>
      <Navbar dark style={{ backgroundColor: 'gray' }}>
        <NavbarBrand href="/">Teacher Database</NavbarBrand>
      </Navbar>
      <div>
        <CSVLoad />
      </div>
    </div>
  );
}

export default MainComp;