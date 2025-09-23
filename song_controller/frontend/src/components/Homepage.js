import React from "react"
import { createRoot } from "react-dom/client"
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
//How we'll route our room join and create room page
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

export default function Homepage(props) {
    return (
        <Router>
            {/* All the different routes that we could go in the homepage */}
            <Routes>
                {/* If the path is true and it matches, we'll return the component */}
                <Route path='/' element={<p>This is the home page</p>} />
                <Route path='/join' element={<RoomJoinPage />} />
                <Route path='/create' element={<CreateRoomPage />} />
            </Routes>
        </Router>
    );
}

