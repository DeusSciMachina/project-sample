
var input = document.getElementById("myBtn");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   document.getElementById("myBtn").click();
  }
});

var myTest = () => {
  console.log("test123")
}



var clickFunction = () => {

  var txtWelcomeInput = document.getElementById("commandLineInput").textContent;
  var txtWelcomeOutput = document.getElementById("commandLineOutput").textContent;
  txtWelcomeOutput = txtWelcomeInput;
  console.log(txtWelcomeInput)
  console.log(txtWelcomeOutput)
  console.log("testing space")
}

const testPrint = (txtWelcomeInput) => {
  balance = 0;
  // Set the value for customer_name equal to name below

  return "does this print"//write the statment you need to return here
};

commandLineOutput = input;

function welcome(){
/*var txtWelcomeInput = document.getElementById("commandLineInput").textContent;
var txtWelcomeOutput = document.getElementById("commandLineOutput").textContent; */
var input = commandLineInput.value;
txtWelcomeOutput.value = "hi there, " + input + "welcome to our educational game that is centered around a simulation of drugs."
}

/*

// input box variable when the user is on nicotine
function walk(){
  print // you are now walking forward
}
function run(){
  print // you are running
}
function turnLeft(){
  print // you have now turned left
}
function turnRight(){
  print // you have now turned right
}
if (document.getElementById("commandLineInput") == "walk") {
  run()

}
else {
  turnRight()
return
}

EnterInfoHandler

if (document.getElementById("commandLineInput") == "run") {
  walk()
}
else {
  turnRight()


}
if (document.getElementById("commandLineInput") == "turn left "){
turnRight()
}
else {
  run()
return
}
if (document.getElementById("commandLineInput")== "turn right"){
  turnLeft()
}
else {
walk()
return
}
// Get the input field
var input = document.getElementById("commandLine");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("myBtn").click();
  }
  return
});
*/
