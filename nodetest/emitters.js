const EventEmitter=require('events');
const emitter=new EventEmitter();
var url='htts://www.twitter.com';
function log(message){
    console.log(message);
    emitter.emit('messageLogged',{id:1,url:'http://'});
}
module.exports=log;