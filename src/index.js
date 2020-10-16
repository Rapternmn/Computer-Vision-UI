import React, { Component } from "react";
import { render } from "react-dom";
import 'semantic-ui-css/semantic.min.css';
import './App.css';

import Form from "./components/Form"
import View from "./components/View"

import {Segment, Header} from 'semantic-ui-react'

function App() {

	const [imgUrl, setImgUrl] = React.useState("")

	function changeInputUrl(newInputUrl) {
		setImgUrl(newInputUrl);
	}

	return (
		<div>
			<Segment piled color='teal' style={{textAlign: 'center', marginTop: '10%', 
				marginLeft: '10%', marginRight: '10%'}}>
				<Header as='h2' color='teal'>Computer Vision - Person Recognition</Header>
			</Segment>
			<Form setState={setImgUrl} />
			<View img_url={imgUrl} changeInputUrl={changeInputUrl}/>
		</div>
	);
}

render(<App />, document.getElementById("root"));
