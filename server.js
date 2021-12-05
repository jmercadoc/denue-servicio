const createHandler = require("azure-function-express").createHandler;
const express = require('express');
var axios = require('axios');
const cors = require('cors');
require('dotenv').config();
const app = express();

app.use(cors());

app.get('/', (req, res) => {
    res.send('App running.');
});

/**
 * Endpoint that receives the data from the API and returns the response
 */
app.get('/municipio/:localidad/negocios/:negocios', async function (req, res) {
    const localidad = req.params.localidad;
    const negocios = req.params.negocios;
    const data = localidad + " " + negocios

    let result = await makePetition(data);
    res.json(result);
});

/**
 * Function that makes the petition to the API
 * @param {string} data - The data to be sent to the API
 * @returns {object} - The response from the API
 */
const makePetition = async (data) => {

    let base_url = "https://www.inegi.org.mx"
    let query_path = "/app/api/denue/v1/consulta/BuscarEntidad/"
    
    var config = {
        method: 'GET',
        url: `${base_url}${query_path}${data}/00/1/100/${process.env.TOKEN}`
    }

    /**
     * The axios request to the API
     */
    return await axios(config)
        .then(function (response) {
            return response.data;
        })
        .catch(function (error) {
            console.log(error);
            return error;
        });
}

app.listen(3000, () => console.log('App is listening on port 3000.'));
module.exports = createHandler(app);