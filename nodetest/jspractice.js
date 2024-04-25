/*List all numbers 0 - 100, if they are a multiple of 3 print FIZZ,
if they are a multiple of 5, print BUZZ, if they are both, print
FIZZBUZZ.*/
/*
let result='';
for (let i=0;i<101;i++){
    if (i==0){
        console.log('0');
        continue;
    }
    if (i%3==0){
        result+='Fizz';
    }
    if (i%5==0){
        result+='Buzz';
    }
    if (result!=''){
        console.log(result+'!');
    }else{
        console.log(i);
    }
    result.replace('');
}
*/

/*Given an array of integers nums and an integer target, return
indicies of the two numbers such that they add up to the target*/
let numList=[];
function addRandomNums(list){
for (let i=0;i<5;i++){
    list.push(Math.floor(Math.random()*10)+1);
}}
addRandomNums(numList);
let targetNum=Math.floor(Math.random()*15)+1;
let correctNums=[];

for (let u=0;u<numList.length;u++){
    for (let y=0;y<numList.length;y++){
        if (numList[u]+numList[y]==targetNum){
            correctNums.push([numList[u],numList[y]]);
        }
    }
}
console.log(numList);
console.log(targetNum);
if (correctNums.length==0){
    console.log('No correct combinations.');
}else{
    console.log(correctNums);
}