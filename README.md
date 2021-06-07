# PIDBox
Group project making a traditional PIDBox with a twist. 

## Ideal Outcome 

## Onshape

### Updates
(WED,FEB 14) These shapes will make up the shape of are PIDBox. 

(FRI,MAR 5) This is the shape of are box without any parts.

(THU,MAR 25) This is are wheel. 

#### Images 


## Code 
### Updates 
#### Images 
<img src="blob:chrome-untrusted://media-app/484c3d45-1b55-4ab4-91bf-4fd459ea56e0" alt="The Code" width="389">


## Final 
#### Images
#### Reflection 
currentTime = millis();
elapsedTime = currentTime - previousTime;
error = setPoint - input;
cumError += error * elapsedTime;
rateError = elapsedTime;
output = Kp * error + Ki * cumError + Kd   #defininig my keys
LastError = error;
previousTime = currentTime;


double kp = 2
double ki = 5
double kd = 1


int Led = 13;
int buttonpin = 3;
int val;
void setup(){
        setPoint = 0;
        pinMode(Led, OUTPUT);
		pinMode(buttonpin, INPUT);
void loop(){
        input = analogRead(A0);
        output = computePID(input);
        delay(100);
        analogWrite(3, output);

	val=digitalRead(buttonpin);
	if(val == HIGH)
	{
	digitalWrite(Led,HIGH);
	}
	else
	{
	digitalWrite(Led,LOW);
		}
		}
motor1 = Motor(4, 14)
motor2 = Motor(17, 27)
motor1.forward(0.5)
motor2.backward(0.5)
while True:
    sleep(5)
    motor1.reverse()
    motor2.reverse()



