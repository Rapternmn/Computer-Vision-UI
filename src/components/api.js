import axios from 'axios'

// const base_url = "http://ec2-user@ec2-18-218-22-14.us-east-2.compute.amazonaws.com:8080"
const base_url = "http://ubuntu@ec2-18-224-73-223.us-east-2.compute.amazonaws.com:8080"
// const base_url = "http://0.0.0.0:8080"

export const predict = url => {
    return axios
        .post(base_url + '/predict_img_url_kaggle', {"url":url})
        .then(response => {
            return response;
        })
}
