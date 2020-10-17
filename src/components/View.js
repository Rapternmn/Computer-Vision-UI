import React, { useEffect } from 'react'
import { predict } from "./api"
import ReactJson from 'react-json-view'
import Sample from "./Sample.js";
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';

import { useStyles } from "./styles"

function View(props) {

    const [predictions, setPredictions] = React.useState("")
    const classes = useStyles();

    useEffect(() => {
        if (props.img_url) {
            predict(props.img_url)
                .then(function (response) {
                    setPredictions(response.data);
                })
        }
    }, [props.img_url])

    return (
        <div>
            <Sample changeInputUrl={props.changeInputUrl} />
            <Grid container spacing={4} justify="center">
                <Grid item key="img" xs={12} sm={6} md={4}>
                    {
                        props.img_url &&
                        <Card className={classes.card}>
                            <CardMedia
                                className={classes.cardMedia}
                                image={props.img_url}
                                title="Image title"
                            />
                            <CardContent className={classes.cardContent}>
                                <Typography gutterBottom color="primary" variant="h5" component="h2" align="center">
                                    Query Image
                                </Typography>
                            </CardContent>
                        </Card>
                    }
                </Grid>
                <Grid item key="prediction" xs={12} sm={6} md={4}>
                    {
                        predictions &&
                        <Card className={classes.cardJson}>
                            <ReactJson src={predictions}
                                theme="monokai"
                                displayDataTypes={false}
                                style={{ width: 'auto' }}
                                collapsed={1}
                            />
                            <CardContent className={classes.cardContent}>
                                <Typography gutterBottom color="primary" variant="h5" component="h2" align="center">
                                    JSON Response
                                </Typography>
                            </CardContent>
                        </Card>
                    }
                </Grid>
            </Grid>
        </div>
    )
}

export default View
