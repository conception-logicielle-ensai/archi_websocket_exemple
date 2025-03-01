import "./App.css";
import UserList from "./components/UserList";
import AddUserForm from "./components/AddUserForm";

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Environnement from "./components/Environnement";
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
