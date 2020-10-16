import React, { useEffect } from 'react'
import { predict } from "./api"
import ReactJson from 'react-json-view'

import Sample from "./Sample.js";

import { Image, Grid } from 'semantic-ui-react'

import "./view.css"


function View(props) {

    const [predictions, setPredictions] = React.useState("")

    useEffect(() => {
        if (props.img_url) {
            predict(props.img_url)
            .then(function(response) {
                setPredictions(response.data);            
            })
        }
    }, [props.img_url])

    return (
        <div>
            <Grid columns={2} divided style={{marginLeft: '10%', marginTop: '2%', marginRight: '10%'}}>
            <Grid.Row>
                <Grid.Column>
                    <Image id='img' src={props.img_url} size='medium' wrapped/>
                </Grid.Column>
                <Grid.Column>
                    {predictions && <ReactJson src={predictions} theme="monokai" 
                    displayDataTypes={false} style={{width: 'fit-content'}} />}
                </Grid.Column>                
            </Grid.Row>
            </Grid>
            <Sample changeInputUrl={props.changeInputUrl}/>
        </div>
    )
}

export default View
