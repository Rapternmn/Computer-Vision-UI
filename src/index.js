import React from "react";
import { render } from "react-dom";

import Form from "./components/Form"
import View from "./components/View"
import Header from "./components/Header"

import 'semantic-ui-css/semantic.min.css';
import './App.css';
import './styles.css'

function App() {

	const [imgUrl, setImgUrl] = React.useState("")

	function changeInputUrl(newInputUrl) {
		setImgUrl(newInputUrl);
	}

	return (
		<div className="App">
			{/* Define A Header */}
			<Header />

			{/* Define an Input Form */}
			<Form img_url={imgUrl} setState={setImgUrl} />

			{/* View The Results */}
			<View img_url={imgUrl} changeInputUrl={changeInputUrl}/>
		</div>
	);
}

render(<App />, document.getElementById("root"));
