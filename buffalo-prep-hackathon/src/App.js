import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MainComp from './MainComponent';
import CSVLoad from './CSVLoad';
import { Container } from 'reactstrap';
import RowAdd from './RowAdd';
import RunScript from './RunScript';

function App() {
  
  return (
    <div>
      <MainComp />
      <br />
      <RowAdd />
      <CSVLoad />
      <Container>
        <RunScript />
        <img src="/regression.png" alt="data"></img>
      </Container>
      
    </div>
  );
}

export default App;
