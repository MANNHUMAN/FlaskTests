/*
jQuery notes
document.getElementByID("id") = $('#id')
document.getElementsByTagName("p") = $('p')
document.getElementsByClassName("swag") = $('.swag')
get text content: $('#id').text
$('#id').remove()

*/

function swagFunction(){
    const element = $('#demo');
    element.innerHTML = 'SWAG PIMPING';
    document.getElementById('pimpin').src = 'static/css/assets/nero.jpg';
}


function nincompooping(){
    const text1=document.getElementById('yatta');
    text1.innerHTML='NINCOMPOOP!!';
}


function nincompoop(){
    const text1=document.getElementById('yatta');
    const text2=document.getElementById('yatta2');
    text2.innerHTML='Click the one you were just mousing over...';
    text1.addEventListener('click',nincompooping);
    text2.remove();
}

function swaggerFunction(id){
    $('#'+id).html("NOW YOU DON'T!!!");
    $('#pimpin').attr('src','static/css/assets/nero.jpg');
}

function dynamic(id){
    $('#'+id).html('swag');
    //is the same as
    document.getElementById('yatta').innerHTML = 'swag';
}

function swagPimping(){
    const node = document.createTextNode('New text!!');
    const para = document.createElement("p");
    para.appendChild(node);
    const element = document.getElementById("demo");
    //append
    element.appendChild(para);
    //add to beginning
    element.insertBefore(para);
}


/*HTMLCollection is like an array but isn't affected by array methods like pop or valueOf
HTMLCollection is called with getElementsByX, NodeList is called with querySelectorX
HTMLCollection can be accessed by name, ID, or Index Number, NodeList is only by Index Number.*/
function redAllParagraphs(){
    const collection = document.querySelectorAll("p");
    const collLength = collection.length;
    for (let i = 0; i < collLength; i++){
        collection[i].style.color="red";
    }
}


function windowTest(){
    window.location.assign("message");
}


function alerting(){
    if (confirm('KILL YUORSLEF !! 11 !')){
        alert('Swag!!');
    }else{
        alert('i hate you...\nforever .');
    }
}


function prompting(){
    let promptulation = prompt("Enter a sentance.", "Make me?");
    let text;
    if (promptulation == null || promptulation == ''){
        text = "Cancelled... :(";
    }else{
        text = "Okay shitlips, " + promptulation + " it is then.";
    }
}