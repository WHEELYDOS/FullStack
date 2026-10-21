let num = 1563;
let ans = 0;
let d = num.toString().length;
//console.log(d);
let cpy = num;
while(cpy>0){
    ans+=(cpy%10)**d;
    cpy = Number.parseInt(cpy/10);
}
console.log(ans);
if(parseInt(ans)===num) console.log("Armstrong");
else console.log("Not")