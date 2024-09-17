int ledpins[]={2,3,4,5,6};
int numled = 5;

void setup() {
  // put your setup code here, to run once:
  for(int i=0; i< numled; i++){
    pinMode(ledpins[i], OUTPUT);

  }
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int fingerCount = Serial.parseInt();
    for(int i=0; i< numled; i++){
      if(i< fingerCount){
        digitalWrite(ledpins[i], HIGH);
      }
      else {
      digitalWrite(ledpins[i], LOW);
      }
    }
  }
}
