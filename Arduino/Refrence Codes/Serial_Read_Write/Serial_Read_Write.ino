void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  digitalWrite(13,LOW);
}

void loop() {
  if(Serial.available()>0)
  {
    Serial.write(Serial.read());
  }
}
