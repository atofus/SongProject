import React from "react"
import { createRoot } from "react-dom/client"
import Homepage from "./Homepage";


export default function App(props) {
    //we could render this componenet inside that index.html inside templates/frontend/index.html
    return (
        <div>
            <Homepage /> 
            {/* <RoomJoinPage />
            <CreateRoomPage /> */}
        </div>
    );
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);