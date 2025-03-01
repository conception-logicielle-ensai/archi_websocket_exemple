import { useEffect, useState } from "react";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [ws, setWs] = useState(null);
  const wsUrl = import.meta.env.VITE_API_URL || "localhost:8000";
  useEffect(() => {
    const socket = new WebSocket(`wss://${wsUrl}`);

    socket.addEventListener("open", () => {
      console.log("Connected to WebSocket");
    });

    socket.addEventListener("message", (event) => {
      setMessages((prev) => [...prev, event.data]);
    });

    socket.addEventListener("close", () => {
      console.log("WebSocket disconnected");
    });

    setWs(socket);

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div className="p-4 border rounded-lg max-w-lg mx-auto">
      <h2 className="text-xl font-bold mb-4">Chat</h2>
      <div className="border p-2 h-64 overflow-y-auto bg-gray-100 rounded">
        {messages.map((msg, index) => (
          <div key={index} className="p-1 border-b border-gray-300">{msg}</div>
        ))}
      </div>
    </div>
  );
}