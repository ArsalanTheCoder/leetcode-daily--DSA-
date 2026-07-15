
var map = function(arr, fn){
    result = [];
    for (var i=0; i<arr.length; i++){
        result.push(fn(arr[i], i));
    }
    return result;
};
