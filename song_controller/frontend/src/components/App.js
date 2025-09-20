import React from "react"
import { createRoot } from "react-dom/client"

export default function App() {
    return <h1>Testing React Component</h1> //we could render this componenet inside that index.html inside templates/frontend/index.html
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);