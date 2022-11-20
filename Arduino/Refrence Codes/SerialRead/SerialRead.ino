void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(8, INPUT);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  if (Serial.available() > 0) //if data available
  {
    String data = Serial.readString();  //read until timeout
    data.trim();   // remove any \r \n whitespace at the end of the String

    Serial.println(data);
    if (data == "forward")
    {
      if(digitalRead(8)==LOW)
      {
       digitalWrite(LED_BUILTIN, HIGH);
       delay(1000);
       while(digitalRead(8)==HIGH);
       digitalWrite(LED_BUILTIN, LOW); 
      }
    }
      
      //delay(3000);
      //digitalWrite(LED_BUILTIN, LOW);
    else if(data == "off")
    {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
