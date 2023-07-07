import React, { useState } from 'react';
import {
  Navbar,
  NavbarBrand,
  Container,
} from 'reactstrap';

function MainComp() {
  return (
    <div>
      <Navbar dark style={{ backgroundColor: 'gray' }}>
        <NavbarBrand href="/">Teacher Database</NavbarBrand>
      </Navbar>
    </div>
  );
}

export default MainComp;