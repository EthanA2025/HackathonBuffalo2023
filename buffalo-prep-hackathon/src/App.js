import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MainComp from './MainComponent';
import CSVLoad from './CSVLoad';
import { Container } from 'reactstrap';
import RowAdd from './RowAdd';

function App() {
  
  return (
    <div>
      <MainComp />
      <CSVLoad />
      <Container>
        <img src="/regression.png" alt="data"></img>
      </Container>
      <RowAdd />
    </div>
  );
}

export default App;
