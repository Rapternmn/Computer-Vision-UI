import React, { Component } from "react";
import { Card, Container } from 'semantic-ui-react';

import {SAMPLE_IMAGES} from './data.js';

export default function Sample(props) {
    
	function onSampleImageClick(imageUrl) {
        props.changeInputUrl(imageUrl);
	}

	return (
        <Container>
            <Card.Group itemsPerRow={4}>
                {SAMPLE_IMAGES.map((value, index) => {
                    return <Card color='red' key={index} image={value} className='sample_imgs' onClick={() => onSampleImageClick(value)} />
                })}
            </Card.Group>
        </Container>
	);
}