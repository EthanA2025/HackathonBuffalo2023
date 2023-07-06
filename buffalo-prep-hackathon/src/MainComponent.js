import React, { useState } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  NavbarText,
  Container,
} from 'reactstrap';

function MainComp(args) {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar dark style={{ backgroundColor: 'gray'}}>
        <NavbarBrand href="/">Teacher Database</NavbarBrand>        
      </Navbar>
    </div>
  );
}

export default MainComp;