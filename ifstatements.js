function readInterpeter(input){
  let response = ""
  if (input == "run"){
    response = "you are running!"
  }
  else if (input == "walk") {
  response = "you are walking"
  }
  else if (input == "turn left") {
  response = "you have turned to face left"
  }
  else if (input == "turn right") {
  response = "you have turned to face right"
  }
  else {
    response = "you have stopped moving"
  }
return response
}





function walk(){
  print ("you are now walking forward")
}
function run(){
  print ("you are running")
}
function turnLeft(){
  print ("you have now turned left")
}
function turnRight(){
  print ("you have now turned right")
}
console.log(readInterpeter("run"))
