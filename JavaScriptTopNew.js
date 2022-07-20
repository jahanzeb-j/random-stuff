// Top JS advance and shorts tips

//1 : if check multi-values
// Old logic
if (x === 'abc' || x==='def' || x === 'xyz') {
    console.log('hi!');
}
// Advanced
if (['abc','xyz','def'].includes(x)) {
    console.log('hi!');
}

// ******
//2: If-else short
// old
let test;
if (x >100) {
    test = true;
} else {
    test = false;
}
// new 
let testN = (x > 10) ? true:false;
let testM = (x > 39);

// ******
// 3: Merge desclare
let test1, test2 = 1;

// ******
// 4: Combile declare multi-values
let [desc1,desc2,desc3] = [1,2,4];

// ******
// 5: && operator
// only if value true if(x == true) { callFunc()};
xCheck && callFunc();

// ******
// 6: Arrow func
const add = (a,b) => a+b;

// ******
// 7: func call 
(test === 1 ? func1:func2)();

// ******
// 8: Switch statement Short  : switch(data) { case 1: ttt...}
const data = {
    1: test1,
    2: test2,
    3: test3
}
data[x] && data[x]();

// ******
// 9: Default func param values : if(test1 = undefined){test1 =1};

const addDef = (test1 = 1,test2 = 2) => (test1+test2);

// ******
// 10: Expension operator ...
const nnn2 = [2,45,6];
const nnExp = [...nnn2]; //[2,45,6]
//
const data3 = [33,44,55];
let nnExpAgain = [22,11,...data3]; // [22,11,33,44,55];

// ******
// 11: Charater within String
// long
let name = "jaza" + " " + test2;

let nameStyle = `Hi jaza ${test2}`

// ******
// 12: find max - min val in arrays
Math.max(...nnExpAgain); // 55
Math.min(...nnExp); // 2

// 13: Desctructive array
let [ds1,ds2,ds3] = nnn2; // ds1 = 2, ds2= 45, ds3 = 6;
