import React, { Component } from "react";
import { render } from "react-dom";
import './App.css';

import Form from "./components/Form"
import View from "./components/View"


function App() {

	const [state, setState] = React.useState("")

	return (
		<div className="app">
			<div className = "Head">
				<header>
					<h1>Rapter's AI</h1>
				</header>
			</div>			
			<Form setState={setState} />
			<View img_url={state}/>
		</div>
	);
}

render(<App />, document.getElementById("root"));
