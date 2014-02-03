use sandsdb

//all tables except n_n tables
//foreign keys are indicated
//realizado: mantener id, hacer varias instrucciones, corregir listas, corregir la colección receta
//falta: 1-n y n-n

db.createCollection('user')
db.createCollection('product')
db.createCollection('evaluation')
db.createCollection('recipe')
db.createCollection('requesttype')
db.createCollection('requestdescription')
db.createCollection('instructions')
db.createCollection('blender')
db.createCollection('hood')
db.createCollection('oven')
db.createCollection('coffeepot')
db.createCollection('kitchen')
db.createCollection('breadmachine')
db.createCollection('microwave')
db.createCollection('fridge')
db.createCollection('dishwasher')
db.createCollection('washingmachine')

//user sample
db.user.insert({
    _id: 'davidnomo',
    location:'london',
    gender: 'male',
    age: 200,
    gascompany: 'ToxicFart LLC',
    electriccompany: 'NukeBizz LLC',
    watercompany: 'DontDrinkIt LLC',
    weather: 'Rainy and Cold Summers',
    fieldcity: 'Field',
    job: 'Farmer',
    workstandsit: 'stand',
    socialstatus: 'deceased',
    children: 100,
    workschedule: 'Full-time',
    conveyance: 'Own car',
    workuniform: true,
    pets: ['dog', 'cat', 'cow'],
    
})


//product sample
db.product.insert({
    _id: '1',
    name:'sausage',
    brand:'oscarmayer',
   
})


//evaluation sample
db.user.insert({
    _id: '1',
    recipeid:'1', //foreign key
    userid:'davidnomo', //foreign key
    userevaluation:'good',
    waterconsume:'low',
    energyconsume:'medium',
    efficiency:'high',
    cost:'medium',
})


//recipe sample
db.recipe.insert({
<<<<<<< Updated upstream
_id: '1',
   
=======
   _id:'1',
>>>>>>> Stashed changes
)}


//requesttype sample
db.requesttype.insert({
   _id: '1',
   recipeaction:'washing',
   appliance:'washingmachine', 
})


//requestdescription sample
db.requestdescription.insert({
   _id: '1',
   variablename:'composition',
   value:'wool',
})


//instructions sample1/5
db.instrucions.insert({
   _id: '2',
   duration:'0',
   variable: 'door',
   value: 'open',
})

//instructions sample2/5
db.instrucions.insert({
   _id: '2',
   duration:'0',
   variable: 'soap',
   value: 'much',
})

//instructions sample3/5
db.instrucions.insert({
   _id: '3',
   duration:'30',
   variable: 'fasterwash',
   value: '800',
})

//instructions sample4/5
db.instrucions.insert({
   _id: '4',
   duration:'30',
   variable: 'RPM',
   value: '800',
})

//instructions sample5/5
db.instrucions.insert({
   _id: '5',
   duration:'0',
   variable: 'door',
   value: 'close',
})

//blender sample
db.blender.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'blendermax',
   model:'a4j',
   rotationspeed: '400',
   quantitysensor: '20',
   liquidsensor:   '40',
   solidsensor:    '10',
   owners:['davidnomo'],//foreign key
})


//hood sample
db.hood.insert({
   _id: '1',
   brand:'superhood',
   model:'bbb',
   smokedetector: true,
   speed:'200',
   light:true,
   owners:['davidnomo'],//foreign key
})


//oven sample
db.oven.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'ovenevo',
   model:'25',
   temperature:'500',
   temperaturesensor:'100',
   dirtynesssensor:'very dirty',
   pyrolysis:true,
   timer:'400',
   pyrolysistimer:'30',
   programme:'grill, hot',
   smokedetector:true,
   users:['davidnomo'],//foreign keys
})


//coffeepot sample
db.coffeepot.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'coffees',
   model:'A',
   temperature:'30',
   temperaturesensor:'10',
   watersensor:'20',
   sedimentssensor:true,
   users:['davidnomo'], //foreign keys
})


//kitchen sample
db.kitchen.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'kitchen1',
   model:'ABC',
   temperature:'90',
   galley:'4',
   temperaturesensor:'20',
   kidskey:true,
   electricenergy:true,
   gasenergy:true,
   users: ['davidnomo'], //foreign keys
)}



//breadmachine sample
db.breadmachine.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'fagor',
   model:'1',
   temperature:'30',
   temperaturesensor:'10',
   leavensensor:true,
   users:['davidnomo'],//foreign key
})


//microwave sample
db.microwave.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'zanussi',
   model:'94A',
   programme:['grill', 'thaw'],
   time:'90',
   temperature:'70',
   temperaturesensor:'40',
   rotationspeed:'30',
   light:true,
   dirtynesssensor:true,
   pyrolysis:true,
   users: ['davidnomo'], //foreign keys
})


//fridge sample
db.fridge.insert({
   _id: '1',
   brand:'electrolux',
   model:'dolphyn',
   temperature:'-40',
   temperaturesensor:'-7',
   watersensor:true,
   doorsensor:true,
   shelf:'6',
   bin:'5',
   drawer:'3',
   users: ['davidnomo'], //foreign key
})



//dishwasher sample
db.dishwasher.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'lavalava',
   model:'hola',
   programme:['fast', 'medium', 'slow'],
   temperature:'20',
   temperaturesensor:'10',
   soap:'calgon',
   soapsensor:'little',
   watersensor:true,
   users: ['davidnomo'], //foreign key
})


//washingmachine sample
db.washingmachine.insert({
<<<<<<< Updated upstream
   _id: '1',
=======
>>>>>>> Stashed changes
   brand:'balay',
   model:'asp',
   programme:['cotton','delicate','colour','white','bedclothes'],
   temperature:'90',
   temperaturesensor:'30',
   Softener:true,
   bleach:true,
   watersensor:'little',
   softenersensor:true,
   bleachsensor:'medium',
   detergent:true,
   detergentsensor:'too much',
   weightsensor:'7',
   time:'90',
   userid: ['davidnomo'], //foreigh key
})
