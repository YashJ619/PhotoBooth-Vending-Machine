#define rake1_pin 2
#define rake2_pin 4
#define rake3_pin 6
#define rake4_pin 7
#define rake5_pin 9

#define rake_read 11

void setup() {
  Serial.begin(115200);

  pinMode(rake1_pin, OUTPUT);
  pinMode(rake2_pin, OUTPUT);
  pinMode(rake3_pin, OUTPUT);
  pinMode(rake4_pin, OUTPUT);
  pinMode(rake5_pin, OUTPUT);
  pinMode(13,OUTPUT);

  pinMode(rake_read, INPUT);
  
  digitalWrite(13,LOW);
}

void loop() {
  if (Serial.available() > 0) //if data available
  {
    String data = Serial.readString();  //read until timeout
    data.trim();   // remove any \r \n whitespace at the end of the String

    //Serial.println(data);
    
    if (data == "rake1on")
    {
      //digitalWrite(13,HIGH);
      rakeon(rake1_pin);
      //digitalWrite(13,LOW);
    }
    if (data == "rake2on")
    {
      //digitalWrite(13,HIGH);
      rakeon(rake2_pin);
      //digitalWrite(13,LOW);
    }
    if (data == "rake3on")
    {
      //digitalWrite(13,HIGH);
      rakeon(rake3_pin);
      //digitalWrite(13,LOW);
    }
    if (data == "rake4on")
    {
      //digitalWrite(13,HIGH);
      rakeon(rake4_pin);
      //digitalWrite(13,LOW);
    }
    if (data == "rake5on")
    {
      //digitalWrite(13,HIGH);
      rakeon(rake5_pin);
      //digitalWrite(13,LOW);
    }
  }
}

void rakeon(int rake_pin)
{
  //Serial.println(rake_pin);
  if (digitalRead(rake_read) == LOW)
  {
    //Serial.print("Done");
    digitalWrite(rake_pin, HIGH);
    delay(1000);
    while (digitalRead(rake_read) == HIGH);
    digitalWrite(rake_pin, LOW);
  }
}
