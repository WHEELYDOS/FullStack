let arr = [1,2,3,4,5];

let newArr = arr.map( (n) => {return 2*n;});
console.log(newArr);

newArr = arr.filter(n=>n>3);
console.log(newArr);
console.log(typeof(newArr))

newArr = arr.find(n=>n>3);
console.log(newArr);
console.log(typeof(newArr))

// const add = (parameters)=>{statements}

const add = (a,b) => {let c = a+b;return c;}
console.log(add(6,10));

console.log("......");
console.log("......");

let arr = [1,2,3,4,5];
console.log(arr);

let newArr = arr.map( (n) => {return 2*n;});
console.log(newArr);

newArr = arr.filter(n=>n>3);
console.log(newArr);
console.log(typeof(newArr))

newArr = arr.find(n=>n>3);
console.log(newArr);
console.log(typeof(newArr))

newArr = arr.reduce((sum,n)=> sum+=n, 0);
console.log(newArr); // func, inititialization of the func