alert("Welcome")

var fn=prompt("Please enter your first name");
var ls=prompt("Please enter your last name");
var age=prompt("Please enter your age");
var ht=prompt("Please enter your height in centimeters");
var pet=prompt("Please enter your pets name");

var namecond = null;
var agecond = null;
var htcond = null;
var petcond = null;

if(fn[0]===ls[0]){
    namecond = true
}
else{
    namecond = false
}

if(age>20 && age<30){
    agecond = true;
}
else{
    agecond = false;
}

if(ht>170){
    htcond = true;
}
else{
    htcond = false;
}

if(pet[pet.length-1]==="y"){
    petcond = true;
}
else{
    petcond = false;
}

if(namecond && agecond && htcond && petcond){
    console.log("Welcome James Bond. Atlanta is waiting for you in the harbour.")
}
else{
    console.log("Nothing.")
}
