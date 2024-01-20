import React from "react";
import ReactDOM from "react-dom/client";
import { App } from "./App";
import "./fonts.css";

const root = document.getElementById("root");
if (!root) throw new Error("root was not found");
ReactDOM.createRoot(root).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
