/*
#define rake1_pin 13
#define rake2_pin 13
#define rake3_pin 13
#define rake4_pin 13
#define rake5_pin 13
*/

#define rake1_pin 2
#define rake2_pin 3
#define rake3_pin 4
#define rake4_pin 5
#define rake5_pin 6

#define rake1_read 7
#define rake2_read 8
#define rake3_read 9
#define rake4_read 10
#define rake5_read 11
/*
int rake1_objects = 9;
int rake2_objects = 9;
int rake3_objects = 9;
int rake4_objects = 9;
int rake5_objects = 9;

bool rake1_state = true;
bool rake2_state = true;
bool rake3_state = true;
bool rake4_state = true;
bool rake5_state = true;
*/
void setup() {
  Serial.begin(115200);

  pinMode(rake1_pin, OUTPUT);
  pinMode(rake2_pin, OUTPUT);
  pinMode(rake3_pin, OUTPUT);
  pinMode(rake4_pin, OUTPUT);
  pinMode(rake5_pin, OUTPUT);
  pinMode(13,OUTPUT);

  pinMode(rake1_read, INPUT);
  pinMode(rake2_read, INPUT);
  pinMode(rake3_read, INPUT);
  pinMode(rake4_read, INPUT);
  pinMode(rake5_read, INPUT);

  intrakes();
  /*
  while (!Serial) {
    digitalWrite(13,HIGH); // wait for serial port to connect. Needed for native USB port only
  }*/
  digitalWrite(13,LOW);
}

void loop() {
  if (Serial.available() > 0) //if data available
  {
    String data = Serial.readString();  //read until timeout
    data.trim();   // remove any \r \n whitespace at the end of the String

    Serial.println(data);
    
    if (data == "rake1on")
    {
      digitalWrite(13,HIGH);
      rakeon(rake1_pin,rake1_read);
      digitalWrite(13,LOW);
    }
    if (data == "rake2on")
    {
      rakeon(rake2_pin,rake2_read);
    }
    if (data == "rake3on")
    {
      rakeon(rake3_pin,rake3_read);
    }
    if (data == "rake4on")
    {
      rakeon(rake4_pin,rake4_read);
    }
    if (data == "rake5on")
    {
      rakeon(rake5_pin,rake5_read);
    }
  }
}

void setrake(int rake_pin, int rake_read)
{
  digitalWrite(rake_pin, HIGH);
  delay(1000);
  while (digitalRead(rake_read) == HIGH);
  digitalWrite(rake_pin, LOW);
}

void rakeon(int rake_pin, int rake_read)
{
  Serial.print(rake_pin);
  if (digitalRead(rake_read) == LOW)
  {
    Serial.print("Done");
    digitalWrite(rake_pin, HIGH);
    delay(1000);
    while (digitalRead(rake_read) == HIGH);
    digitalWrite(rake_pin, LOW);
  }
  else
  {
    setrake(rake_pin, rake_read);
  }
}

void intrakes()
{
  if (digitalRead(rake1_read) == HIGH)
  {
    setrake(rake1_pin, rake1_read);
  }
  if (digitalRead(rake2_read) == HIGH)
  {
    setrake(rake2_pin, rake2_read);
  }
  if (digitalRead(rake3_read) == HIGH)
  {
    setrake(rake3_pin, rake3_read);
  }
  if (digitalRead(rake4_read) == HIGH)
  {
    setrake(rake4_pin, rake4_read);
  }
  if (digitalRead(rake5_read) == HIGH)
  {
    setrake(rake5_pin, rake5_read);
  }
}
