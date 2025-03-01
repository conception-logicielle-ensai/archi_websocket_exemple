import { useEffect, useState } from "react";
import MessageInput from "./MessageInput";
import { io } from "socket.io-client";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [socket, setSocket] = useState(null);
  const wsUrl = import.meta.env.VITE_WS_URL || "wss://localhost:8080";
  useEffect(() => {
    const socketInstance = io(wsUrl, {
      transports: ["websocket"], // Force WebSocket uniquement
    });

    socketInstance.on("connect", () => {
      console.log("✅ Connecté au WebSocket");
    });

    socketInstance.on("message", (data) => {
      setMessages((prev) => [...prev, data]);
    });

    socketInstance.on("disconnect", () => {
      console.log("❌ WebSocket déconnecté");
    });

    setSocket(socketInstance);

    return () => {
      socketInstance.disconnect(); // Déconnexion propre
    };
  }, []);

  const sendMessage = (user, input) => {
  if (socket && input.trim()) {
    const message = { user, reponse: input };
    socket.send(JSON.stringify(message)); // Envoie direct avec WebSocket natif
  }
  };

  return (
    <div className="p-4 border rounded-lg max-w-lg mx-auto">
      <h2>
        Renseignez votre message ici 
      </h2>
      <MessageInput onSendMessage={sendMessage}/>
      <h2 className="text-xl font-bold mb-4">Chat</h2>
      <div className="border p-2 h-64 overflow-y-auto bg-gray-100 rounded">
        {messages.map((msg, index) => (
          <div key={index} className="p-1 border-b border-gray-300">{msg}</div>
        ))}
      </div>
      
    </div>
  );
}