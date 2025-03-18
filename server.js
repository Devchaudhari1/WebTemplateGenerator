//server.js
const mysql = require('mysql2');
const db = require('./db.js');
const express= require('express');
const path = require('path');
const cors =require('cors');
const Route = require('./routes/routes.js');
const port = 3000;
const server = express();

      server.listen(port, function(err)
      {
      
      if(err)
          console.error("Failed to listen in port", err);
      else
          console.log(`Database is listening in port http://localhost:${port}\nIndex in http://localhost:${port}/index\n`);  });
server.use(express.json());
server.use(express.urlencoded({extended:true}));
server.use('/', Route);


server.use(express.static(path.join(__dirname,'views')));
