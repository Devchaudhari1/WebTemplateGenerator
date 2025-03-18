//routes\routes.js
const express=require('express');
const path = require('path');
const {getPlaces,addPlaces}= require('../controllers/placeController.js');
const cors=  require('cors');
const Route =  express();
const axios=require('axios');
const {addUsers,getUsers,deleteUsers , updateUsers , getUsersBy ,getUsersLike,applyFilterSearchUsers}= require('../controllers/users.js');
//const bodyparser= require('body-parser');
Route.use(cors({origin:'*' ,methods:['POST','GET','PUT','DELETE','PATCH'], allowedHeaders:['Authorization']}));
Route.use(express.json());
Route.use(express.static(path.join(__dirname , '../views')));
Route.get('/', (req,res) => {
    res.sendFile(path.join(__dirname, '../views','homepage.html'));
});


Route.get('/index',(req , res)=>{
    res.sendFile(path.join(__dirname , '../views','index.html'));
});

const {addactivities,getactivities,deleteactivities , updateactivities}= require('../controllers/activities.js');

Route.get('/activitiesPage',(req , res)=>{
    res.sendFile(path.join(__dirname , '../views','activities.html'));
   });
   
   Route.get('/activities' , getactivities);
   Route.post('/activities' ,addactivities);
   Route.delete('/activities/:id',deleteactivities);
   Route.put('/activities/:id',updateactivities);


// routes/routes.js



const {addactivity_bookings,getactivity_bookings,deleteactivity_bookings , updateactivity_bookings,applyFilterSearchactivity_bookings,getactivity_bookingsLike,getactivity_bookingsBy}= require('../controllers/activity_bookings.js');
Route.get('/activity_bookingsPage',(req , res)=>{
 res.sendFile(path.join(__dirname , '../views','activity_bookings.html'));
});

Route.get('/activity_bookings' , getactivity_bookings);

Route.post('/activity_bookings' ,addactivity_bookings);

Route.delete('/activity_bookings/:id',deleteactivity_bookings);

Route.put('/activity_bookings/:id',updateactivity_bookings);


Route.get('/activity_bookingsBy',getactivity_bookingsBy);

Route.get('/activity_bookingsLike',getactivity_bookingsLike);

 Route.get('/activity_bookingsSearch',applyFilterSearchactivity_bookings);

 
const {addbus,getbus,deletebus , updatebus,applyFilterSearchbus,getbusLike,getbusBy}= require('../controllers/bus.js');
Route.get('/busPage',(req , res)=>{
 res.sendFile(path.join(__dirname , '../views','bus.html'));
});

Route.get('/bus' , getbus);

Route.post('/bus' ,addbus);

Route.delete('/bus/:id',deletebus);

Route.put('/bus/:id',updatebus);


Route.get('/busBy',getbusBy);

Route.get('/busLike',getbusLike);

 Route.get('/busSearch',applyFilterSearchbus);



Route.get('/usersLike/:id',getUsersLike);

Route.get('/usersBy/:id',getUsersBy);

Route.get('/users' , getUsers);

Route.get('/usersSearch',applyFilterSearchUsers);

Route.post('/users' ,addUsers);

Route.delete('/users/:id',deleteUsers);

Route.put('/users/:id',updateUsers);

module.exports =Route;


