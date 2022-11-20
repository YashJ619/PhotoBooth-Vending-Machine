#define pinSignal A5 // pin connected to pin O module sound sensor  
int signals[1000];
void setup()
{
  pinMode (pinSignal, INPUT); // Set the signal pin as input
  Serial.begin (115200);
}

void loop()
{
  int sum = 0;
  for (int i = 0; i < 1000; i++)
  {
    signals[i] = analogRead (pinSignal);
    sum += signals[i];
    //Serial.println(signals[i]);
    if (i == 999) {
      delayMicroseconds(50);
      Serial.println(sum / 1000);
      //Serial.println("x");
    }
  }

  //signals = analogRead (pinSignal);
  //Serial.print("Sound Signal: ");


}
