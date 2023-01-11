
import os
import urllib.request as request

print("FUNNY FACT ABOUT PIGS \n ")
class Animal(object):
 def __init__(self, animal):
  print(animal,"can not look up. 😇")

class Mammal(Animal):
 def __init__(self, mammal):
  print(mammal, "is warm blooded. 🐷")
  super(Mammal,
   self).__init__(mammal)

class Flightless(Mammal):
 def __init__(self, mammal):
  print(mammal, "can not fly.     😁")
  super(Flightless,
   self).__init__(mammal)

class NotAquatic(Mammal):
 def __init__(self, mammal):
  print(mammal, "can not swim.    🐷")
  super(NotAquatic,
   self).__init__(mammal)

class Pig(NotAquatic, Flightless):
 def __init__(self):
  print("Pig has 4 legs.      🐖",)
  super(Pig, self).__init__("Pig")
  
url = 'https://media2.giphy.com/media/U6isKyHvHvjCySIQE6/giphy.gif?cid=82a1493b61p5t4fzcld1uzf7el490ntrmq8g06077vttorne&rid=giphy.gif&ct=s'
request.urlretrieve(url, 'image.png')

pig = Pig()

print (""""
<style>
@import url("https://fonts.googleapis.com/css3?family=Mr+Dafoe&display=swap");
 body{
  background-color: navyblue;
  margin: auto;
  border: 10px solid dodgerblue;
  width: 70%;
  border-radius: 20px;
  box-shadow: 0 25px 30px rgba(0, 0, 0, 0.8); 
  font-family: "Mr Dafoe";
  font-weight: 800;
  font-size:1.4em;
  color:white; 
  padding: 1.5em .5em 0em 1em;   
  text-shadow: 0 0 0.05em #1E90FF, 
               0 0 0.5em #1E90FF, 
               0 0 0.5em #1E90FF;   
 }

 img {
  display: run-in;
 }
</style>""")
os.system("touch file.png")

