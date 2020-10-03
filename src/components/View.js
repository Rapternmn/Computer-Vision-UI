import React, { useEffect } from 'react'
import { predict } from "./api"
import ReactJson from 'react-json-view'
import {
    Row, Col,
    Card, CardImg, CardText, CardBody,
    CardTitle, CardSubtitle, CardLink, CardHeader, CardFooter
} from 'reactstrap';

import "./view.css"


function View({ img_url }) {

    const [predictions, setPredictions] = React.useState("")

    useEffect(() => {

        if (img_url) {
            predict(img_url).then(
                response => setPredictions(response.data)
            )
        }

    }, [img_url])

    return (
        <div className="View">

            <img src={img_url} />
            <div className="Pred">
                {predictions && <ReactJson src={predictions} theme="monokai" />}
            </div>

        </div>
    )
}

export default View
