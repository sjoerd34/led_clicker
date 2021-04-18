String x;
const int RedLed = 10;
const int YellowLed = 12;
const int GreenLed = 4;
const int BlueLed = 5;
String pin;
String state;
int Pin;
bool stateVal;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2);
  pinMode(RedLed, OUTPUT);
  pinMode(YellowLed, OUTPUT);
  pinMode(GreenLed, OUTPUT);
  pinMode(BlueLed, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {

      //Receives data with of the format 'pin:on/off'
      //To turn the RedLed on this would look like '10:1'
      //To turn the RedLed off the data would look like '10:0'
      //RedLed pin is assumed to be 10 in this case
      x = Serial.readString();

      //splits the received data in two parts. 
      // The part before the colon, this is the pin number
      // The part after the colon, a 1 or 0 to denote on or off.
      pin = getValue(x, ':', 0);
      state = getValue(x, ':', 1);

      //Converts the String pin to an integer
      Pin = pin.toInt();

      //Converts the String 1 or 0 to an integer 
      stateVal = state.toInt();
      
      digitalWrite(Pin, stateVal);
    
      }
    }

String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
