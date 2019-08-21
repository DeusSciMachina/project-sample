
function terminal(){
  if (document.getElementById("commandLineInput").value != "stop"){
  var btn = document.createElement("BUTTON");
  btn.innerHTML = "CLICK ME";
  document.body.appendChild(btn);
  }
}

function welcome(){
var txtWelcomeInput = document.getElementById("commandLineInput");
var txtWelcomeOutput = document.getElementById("commandLineOutput");
var input = commandLineInput.value;
txtWelcomeOutput.value = "hi there, " + input + "welcome to our educational game that is centered around a simulation of drugs."
}

// input box variable when the user is on nicotine
if (document.getElementById("commandLineInput") == "walk") {
  run()

}
else {
  turnRight()
}EnterInfoHandler

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
}
if (document.getElementById("commandLineInput")== "turn right"){
  turnLeft()
}
else {
walk()
}
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
