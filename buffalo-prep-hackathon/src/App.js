import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MainComp from './MainComponent';
import CSVLoad from './CSVLoad';

function App() {
  return (
    <div>
      <MainComp />
      <CSVLoad />
    </div>
  );
}

export default App;
