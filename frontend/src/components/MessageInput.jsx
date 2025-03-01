import { useState } from "react";

export default function MessageInput({ onSendMessage }) {
  const [input, setInput] = useState("");
  const [user, setUser] = useState("User");

  const handleSend = () => {
    if (input.trim()) {
      onSendMessage(user, input);
      setInput("");
    }
  };

  return (
    <div className="mt-4">
      <input
        type="text"
        value={user}
        onChange={(e) => setUser(e.target.value)}
        className="p-2 border rounded w-full mb-2"
        placeholder="Entrez un username"
      />
      <div className="flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 p-2 border rounded-l"
          placeholder="Taper un message..."
        />
        <button onClick={() => handleSend(user,input)} className="p-2 bg-blue-500 text-white rounded-r">
          Envoyer le message 
        </button>
      </div>
    </div>
  );
}

