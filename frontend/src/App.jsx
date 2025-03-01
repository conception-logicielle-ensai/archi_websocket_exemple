import "./App.css";
import Chat from "./components/Chat";
import Environnement from "./components/Environnement";
function App() {
  return (
    <div>
      <h1>
        Bienvenu sur le chat
      </h1>
      <div>
      <Chat/>
      </div>
      <footer>
        <h2>Variables d'environnement / Configuration</h2>
        <Environnement />
      </footer>
      </div>
  );
}

export default App;
