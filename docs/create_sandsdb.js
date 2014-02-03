use sandsdb

//sandsdb_appliances.js

db.createCollection('user')
db.createCollection('product')
db.createCollection('evaluation')
db.createCollection('recipe')
db.createCollection('requesttype')
db.createCollection('requestdescription')
db.createCollection('instructions')
db.createCollection('appliances')


//blender sample
var blender_id = ObjectId()
db.appliances.insert({
    _id: blender_id,
    type: 'blender',
    brand:'blendermax',
    model:'a4j',
    rotationspeed: '400',
    quantitysensor: '20',
    liquidsensor:   '40',
    solidsensor:    '10',
    owners:[],//foreign key
})


//hood sample
var hood_id = ObjectId()
db.appliances.insert({
    _id: hood_id,
    type: 'hood',
    brand:'superhood',
    model:'bbb',
    smokedetector: true,
    speed:'200',
    light:true,
    owners:[],//foreign key
})


//oven sample
var oven_id = ObjectId()
db.appliances.insert({
    _id: oven_id,
    type: 'oven',
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
    owners:[],//foreign keys
})


//coffeepot sample
var cf_id = ObjectId()
db.appliances.insert({
    _id: cf_id,
    type: 'coffee-machine',
    brand:'coffees',
    model:'A',
    temperature:'30',
    temperaturesensor:'10',
    watersensor:'20',
    sedimentssensor:true,
    owners:[], //foreign keys
})


//kitchen sample
var kit_id = ObjectId()
db.appliances.insert({
    _id: kit_id(),
    type: 'kitchen',
    brand:'kitchen1',
    model:'ABC',
    temperature:'90',
    galley:'4',
    temperaturesensor:'20',
    kidskey:true,
    electricenergy:true,
    gasenergy:true,
    owners: [], //foreign keys
)}



//breadmachine sample
var bm_id = ObjectId()
db.appliances.insert({
    _id: bm_id,
    type: 'bread maker',
    brand:'fagor',
    model:'1',
    temperature:'30',
    temperaturesensor:'10',
    leavensensor:true,
    owners:[],//foreign key
})


//microwave sample
var mw_id = ObjectId()
db.appliances.insert({
    _id: mw_id,
    type: 'microwave-oven',
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
    owners: [], //foreign keys
})


//fridge sample
var fdge_id = ObjectId()
db.appliances.insert({
    _id: fdge_id,
    type: 'fridge',
    brand:'electrolux',
    model:'dolphyn',
    temperature:'-40',
    temperaturesensor:'-7',
    watersensor:true,
    doorsensor:true,
    shelf:'6',
    bin:'5',
    drawer:'3',
    owners: [], //foreign key
})



//dishwasher sample
var dw_id = ObjectId()
db.appliances.insert({
    _id: dw_id,
    type: 'dish-washer',
    brand:'lavalava',
    model:'hola',
    programmes:['fast', 'medium', 'slow'],
    temperature:'20',
    temperaturesensor:'10',
    soap:'calgon',
    soapsensor:'little',
    watersensor:true,
    owners: [], //foreign key
})


//washingmachine sample
var wm_id = ObjectId()
db.appliances.insert({
    _id: wm_id,
    type: 'microwave-oven',
    brand:'balay',
    model:'asp',
    programmes: ['cotton','delicate','colour','white','bedclothes'],
    temperatures: ['0', '10', '20', '30', '90'],
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
    owners: [], //foreigh key
})


db.appliances.ensureIndex( { type: 1 } )



//user sample
var user_id = ObjectId()

db.user.insert({
    _id: user_id,
    name: 'davidnomo',
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

    appliances: [], //list of appliance ids
    evaluations: [], //list of evaluation ids
})

//db.volumes.ensureIndex( { topics: 1 } )

//recipe sample
var rcp_id = ObjectId()
db.recipe.insert({
    _id: rcp_id,
    users: [user_id],
    instructions: [inst1_id, inst2_id, inst3_id, inst4_id, inst5_id],
})


//product sample
var prod_id = ObjectId()
db.product.insert({
    _id: prod_id,
    name:'sausage',
    brand:'oscarmayer',
})


//evaluation sample
var eval_id = ObjectId()
db.evaluation.insert({
    _id: eval_id,
    recipe: rcp_id, //foreign key
    user: user_id, //foreign key
    userevaluation:'good',
    waterconsume:'low',
    energyconsume:'medium',
    efficiency:'high',
    cost:'medium',
})


//requesttype sample
var rqsttype_id = ObjectId()
db.requesttype.insert({
    _id: rqsttype_id,
    recipeaction:'washing',
    appliance:'washingmachine', 
})


//requestdescription sample
var rqsttype_desc = ObjectId()
db.requestdescription.insert({
    _id: rqsttype_desc,
    variablename:'composition',
    value:'wool',
})


//instructions sample
var inst1_id = ObjectId()
var inst2_id = ObjectId()
var inst3_id = ObjectId()
var inst4_id = ObjectId()
var inst5_id = ObjectId()

//instructions sample1/5
db.instrucions.insert({
    _id: inst1_id,
    duration:'0',
    variable: 'door',
    value: 'open',
})

//instructions sample2/5
db.instrucions.insert({
    _id: inst2_id,
    duration:'0',
    variable: 'soap',
    value: 'much',
})

//instructions sample3/5
db.instrucions.insert({
    _id: inst3_id,
    duration:'30',
    variable: 'fasterwash',
    value: '800',
})


//instructions sample4/5
db.instrucions.insert({
    _id: inst4_id,
    duration:'30',
    variable: 'RPM',
    value: '800',
})


//instructions sample5/5
db.instrucions.insert({
    _id: inst5_id,
    duration:'0',
    variable: 'door',
    value: 'close',
})






