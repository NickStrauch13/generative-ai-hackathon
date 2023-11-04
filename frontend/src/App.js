import './App.css';
import Navbar from "./components/Navbar";
import MainContent from "./components/MainContent";

function App() {

  return (
    <div className="app-container">
      <div className="navbar-container">
        <Navbar/>
      </div>
      <div className="main-content-container">
        <MainContent/>
      </div>
    </div>
  )
}

export default App;
