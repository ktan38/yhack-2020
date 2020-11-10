var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/podcast', function(req, res, next) {
  res.send('respond with a resource');
  console.log("hello!");
});

module.exports = router;
