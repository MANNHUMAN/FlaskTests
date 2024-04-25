const EventEmitter=require('events');
var url='https://www.twitter.com/';
class Logger extends EventEmitter{
    //Function defined in Class doesn't need function defining
    //Function in Class is called Method.
    log(message){
        console.log(message);
        this.emit('messageLogged',{id:1,url:'http://'});
    }
}

module.exports=Logger;