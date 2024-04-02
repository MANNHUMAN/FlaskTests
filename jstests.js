swag = 'NOW YOU DONT';//can be auto declared
var zwag = 'swaggy';
const szwag = 'xdxd';
xdxd  = `woah you can also use tildas which 
makes using ' and " way easier.`;
xdxdd = "This: \' is a single quote, this: \" is a double quote, this \\ is a backslash.";
var x;//or manually
let y;
let peanits = 'swag', peanuts = 'swaggier', size = 6.8;
let length = peanits.length;
let position = peanits.charAt(1);//will return 'w'.
listing = ['xd', 'xdxd'];
swaggy, swagalicious = listing;
girth = 1.2;
let u = '7';
uNum = Number(u);
xdxdbuttwice = listing[1].repeat(2);
swaggggy = xdxdbuttwice.replace(/XD/i,'PEANITS');
const mappy = new Map([
    ["Peanits", 6.5],
    ["Bunttenhole", 0],
    ["WOAG??", 1]
]);
mappy.set("WAGINA?? ?", "0o");
gotten = mappy.get('Bunttenhole')
mappy.delete('Peanits')

// /i makes it case insensitive, /g replaces ALL matches not just first which can
// also be done with .replaceAll(replacement, subject)
xdxdd.split("");
//splits every letter, though can be on a comma, blank space, or anything really.
const array1 = [];
cars[0] = "thing 1";

const array2 = [
    "thing 1",
    "thing 2"
];
array2[2] = "thing 3"; // wtf it's a constant why can i change it ???
// can also be done wotj array2.push(item)
let array2len = array2.length;
let text = "<ul>";
for (let i = 0; i < array2len; i++) {
    text += "<li>" + array2[i] + "<li>";
}
text += "</ul>>";

for (executedvar; conditionforexecuting; thingtoexecuteoneveryloop) {
    return
}

for (let i=0,sexboner;i<5;i++) {
    sexboner+="ZIS NUMBAH IS "+i+"<br>";
}

for (;boner==True;boner=False){
    return;
}

i=0;
while (i<10) {
    i++;
}
i=0;
do{
    i++
    if (i==3) {break;}
    if (i==2) {continue;}
}
while (i<10);

new Date(year, month, day, hours, minutes, seconds, ms)
//6 numbers signify y/m/d/h/m/s, 5 is y/m/d/h/m, 4 is y/m/d/h, etc etc.
//Can be .toDateString(), .toUTCString(), & .toISOString().

Math.random(); //always returns a random floating number 0-1 lmao
Math.floor(Math.random()*11)+1;//Returns a random number 1-10 xdxd


x=5;
y=6;
let z = y + (x * y);

x += y;
x === y; //Checks if same value AND type
x !== y; //Checks if NOT same value & type
x++; //Increases by 1 lmfao
typeof x; //returns "number", a string would return "string", etc.


swagmobile = new {
    name:"cybertruck",
    type:"shit",
    good:false,
    engine : function() {//FUNCTIONS INSIDE OBJECTS MUST BE NAMED function() !!
    return this.type;
    }
};
swagmobile.good = True;
swagmobile.engine()


//sex on boner style
/*
sex
on 
boner
style
*/
arrowFunction = () => {
    return "Wowza";
}

betterArrowFunction = (parameterthing) => "MORE WOWZA!! " + parameterthing;


function getRndInteger(min,max) {
    return Math.floor(Math.random()*(max-min))+min;
}

function swagFunction() {
    document.getElementById("demo").innerHTML = swag;
};


function displayTest() {
    document.getElementById("demo").innerHTML = 5 + 6;
    window.alert('swag');
    console.log('peanits againe');
};



function multiply(v1, v2) {
    return v1 * v2;
};

if (20+1==9+10) {
    return "you stupid"
} else if (9+9==18){
    return "You intrigueing..."
} else {
    return "You stupid !!"
}

function beCalled(some) {
    document.getElementById("demo").innerHTML = some;
}

function myCalc(num1, num2, getCalled){
    let sum = num1+num2;
    return getCalled(sum);
}

myCalc(5,5,beCalled);



switch (Math.floor(Math.random()*2)) {
    case 0:
        day = 'swag';
        break;
    case 1:
        day = 'swagger';
        break;
    default:
        day = 'oh...'
}

class swagClass {
    constructor(wife, kid){
        this.wife = wife;
        this.kid = kid;
    }
    info() {
        return "This is my wife, "+this.wife+"...and this is my kid, "+this.kid;
    }
}

/*"Producing Code" is code that takes time,
"Consuming Code" is code that must wait for a result,
a "Promise" is an Object that uses both.*/

setTimeout(myFunction, 3000);//This function will be called after 3 seconds (3000 milliseconds)

setInterval(myFunction, 1000)//This function will be called every second.

function myFunction(){
    document.getElementById("demo").innerHTML = "swag pimping";
}

let myPromise = new Promise(function(myResolve, myReject){
    myResolve(); //runs when successful
    myReject(); //runs when error
});

myPromise.then(
    function(value){ /* Code to run if successful*/ },
    function(error) {/* Code to run if error occurs */ }
);
//honest to god i dont understand a lot of this "promise" shit.

async function asynchronousFunction(){
    return 'hihi';
}//...is the same as
function otherAsyncFunc(){
    return Promise.resolve('hihi')
}
asynchronousFunction().then(
    function(value) {'fuck off';},
    function(error) {'also fuck off';}
)
let waiting = await myPromise;

/*
window.setTimeout(function, milliseconds) executes a function after a set time.
window.setInterval() does the same thing but repeats it continuously.
window.clearTimeout(timeoutVariable)
document.cookie = "key=thing, expires=utctime"
let x = document.cookie;
deleting a cookie is literally just setting the time to something in the past.
*/

function validation(){
    const inpObj = document.getElementById("anID");
    if (!inpObj.checkValidity()){
        //.checkValidity() returns a boolean for if valid data is in it.
        document.getElementById("anID2").innerHTML=inpObj.validationMessage;
        //.validationMessage is the message displayed if .checkValidity() returns false.
    }
}
/* webworkers should be in their own files.
let i = 0;
function webWorker(){
    i++;
    postMessage(i);
    setTimeout("timedCount()",500);
}
webWorker();
*/

/*
customError	    Set to true, if a custom validity message is set.
patternMismatch	Set to true, if an element's value does not match its pattern attribute.
rangeOverflow	Set to true, if an element's value is greater than its max attribute.
rangeUnderflow	Set to true, if an element's value is less than its min attribute.
stepMismatch	Set to true, if an element's value is invalid per its step attribute.
tooLong	        Set to true, if an element's value exceeds its maxLength attribute.
typeMismatch	Set to true, if an element's value is invalid per its type attribute.
valueMissing	Set to true, if an element (with a required attribute) has no value.
valid	        Set to true, if an element's value is valid.
*/