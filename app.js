const prompt = require("prompt-sync")({sigint: true});


const functionOne = (name) => {
    console.log("hello " + name + " You chose function 1");
}

const functionTwo = (name) => {
    console.log("hello " + name + " You chose function 2");
}

const functionThree = (name) => {
    console.log("hello " + name + " You chose function 3");
}

let yourName = prompt("What is your name? ");
let option = prompt("Enter an Option [1], [2] or [3] ");

if (option == "1" && yourName == "Bob") {
    functionOne(yourName);
}
else if (option == "2") {
    functionTwo(yourName);
}
else if (option == "3") {
    functionThree(yourName);
}
else {
    console.log("Please input a number between 1 and 3 and if you chose 1 then only do that if you are Bob");
}

