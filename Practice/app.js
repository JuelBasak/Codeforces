// var time = 0;
//
// var timer = setInterval(function () {
//     time += 1;
//     console.log(time + 'sec(s) passed');
//     if (time > 5) {
//         clearInterval(timer);
//     }
// }, 1000)
// console.log(__dirname)
// console.log(__filename)


let fun1 = function(a, b){
    return a + b;
};

console.log(`Main File : ${fun1(10,20)}`);

module.exports = {
    fun1: fun1
};

console.log(module);
