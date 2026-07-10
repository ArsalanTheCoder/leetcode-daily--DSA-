var createCounter = function(n){
    return function(){
        return n++;
    }
}

closure = createCounter(10);
console.log(closure());
console.log(closure());
console.log(closure());
