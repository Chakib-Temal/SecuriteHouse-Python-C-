
int broche = 8;
bool etat = false;
byte etatCapteur;

void setup() {
  
  Serial.begin(9600);
  pinMode(broche, INPUT); 
  
}

void loop() {
 
   etatCapteur = digitalRead(broche);
  
  //detection 
  if (etatCapteur == 0 && etat == false ){
    Serial.println("alert,img1,alert");
    delay(1000);
    etat = true;
  }

  if (etatCapteur == 1) {
    etat = false;
  }

}
