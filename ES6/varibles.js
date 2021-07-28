/*
HOISTING:
Hoisting in ES6 means the way the language uses the contexts of exection. During the compilation phase the program stores these declarations in the memory. So when you execute the program, if you call a variable or a function before you initialize it in the code, it won't throw an error. Instead, due to the fact that the declaration is stored in the memory it will give it a value of undefined, because the variable is not yet initialized with a value it is only declared. This hoisting doesn't affect let and const because their scope cannot be accessed from outside their brackets. So if you call them from an outer level, they will throw an error.
*/


/* 
The main reason of why the let and const were implemented in es6 is the scope. The var has a much wider scope. This is because a var initialized in a function can be accessed from any level in the same function, and this can lead to problems later on.

Let an const have a much more secure scope. Because they can only be accessed inside the brackets where they are located. They can also be accessed from nested brackets but not from a level above, only levels that are contained in the brackets where the variables were initialized. And the main difference between let and const, is that let can be redefined over and over but const not. Once const is initialized you cannot change it's value later on your program.
*/

var m = true
function sayMessageOne(){
    if(m){
        var myAge = 19;
        console.log(myAge)
    }
    else{
        var myAge = 22;
        console.log(myAge)
    }
    //This is a bad practice but is a valid code with var
    console.log(myAge)
}

function sayMessageTwo(){
    if(m){
        let myName = 'Sebastian';
        console.log(myName);
    }
    else{
        let myName = 'Rick';
        console.log(myName);
    }
    // In the case of let this is not gonna run because the variable 
    // my name is not available in this level
    //console.log(myname);
}

function sayMessageThree(){
    const numberPi = 3.1415;
    if(m){
        // This code is not gonna run also due to the const. Once the variable is defined you cannot redefine it
        //numberPi = 3.1213;
        console.log(numberPi);
    }
    else{
        // The same applies in this case
        //numberPi = 5141.3;
        console.log(numberPi);
    }
}
