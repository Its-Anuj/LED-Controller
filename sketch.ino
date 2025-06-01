int Red = 0;
int Blue = 255;
int Green = 0;

void setup()
{
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);

  Serial.begin(9600);

  analogWrite(9, Red);
  analogWrite(10, Blue);
  analogWrite(11, Green);
}

void loop()
{
  if(Serial.available())
  {
    String input = Serial.readStringUntil('\n');
    Serial.println(input);

    int redindx = input.indexOf('R');
    int greenindx = input.indexOf('G');
    int blueindx = input.indexOf('B');
  
    Red = input.substring(redindx+1, greenindx).toInt();
    Green = input.substring(greenindx+1, blueindx).toInt();
    Blue = input.substring(blueindx+1).toInt();

    Serial.println(Red);
    Serial.println(Green);
    Serial.println(Blue);

    analogWrite(9, Red);
    analogWrite(10, Blue);
    analogWrite(11, Green);
  }
}