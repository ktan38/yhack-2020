var express = require('express');
var router = express.Router();
const speech = require('@google-cloud/speech');
const fs = require('fs').promises;
const http = require('http');

process.stdout.on('data', data => {
  console.log(data.toString());
})
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
  console.log("hello!");
});


router.post('/test_route', (req, res, next) => {
  // console.log('post request received!');
  res.send("What's up");
});




module.exports = router;
