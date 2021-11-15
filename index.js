const express = require('express')
const cors = require('cors')
const functions = require('firebase-functions')
const search = require('./search')

const app = express()

app.use(cors({origin:true}));
app.get('/',(req,res)=> res.status(200).send({date: new Date(), status:'ok'}));

app.get('/municipio/:municipio/negocios/:negocios', async (req,res)=>{
  let params = {}
  if (req.params.municipio) { params.municipio = req.params.municipio}
  if (req.params.negocios) { params.negocios = req.params.negocios}
  const result = await search(params)
    if (!!result) {
        res.status(200).jsonp(result);
        return
      }
    
    res.status(404).jsonp({
    error: 'not found',
    id: req.params['0'] || 'empty',
    key: req.query['key'] || 'empty'
    })
})

exports['inegi-service'] = functions.https.onRequest(app);

