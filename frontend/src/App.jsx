import "./App.css";
import Chat from "./components/Chat";
import Environnement from "./components/Environnement";
import MessageInput from "./components/MessageInput";
function App() {
  return (
    <div>
      <h1>
        Bienvenu sur le chat
      </h1>
      <div>
      <h2>
        Envoyer un message
      </h2>
      <MessageInput/>
      </div>
      <div>
      <Chat/>
      </div>
      <footer>
        <Environnement />
      </footer>
      </div>
  );
}

export default App;
