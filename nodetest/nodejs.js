function testFunc(args){
    console.log('Kill yourself '+args+'!!');
}
testFunc('killjulating myselfington');

console.log(__filename);
console.log(__dirname);

//Instead of Window, in Node it's 'global'.
//Global is file scoped.
let swag = '';
console.log(global.swag)

let url = 'https://twitter.com';
function log(message){
    //sending HTTP request
    console.log(message)
}

module.exports.log = log;
module.exports.endPointUrl = url;