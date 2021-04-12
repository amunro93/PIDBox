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
  


void setup(){
        setPoint = 0; 

void loop(){
        input = analogRead(A0);            
        output = computePID(input);
        delay(100);
        analogWrite(3, output);              
 
}
```
double computePID(double inp){     
        currentTime = millis();           
        elapsedTime = (double)(currentTime - previousTime);       
        
        error = Setpoint - inp;                               
        cumError += error * elapsedTime;               
        rateError = (error - lastError)/elapsedTime;   
 
        double out = kp*error + ki*cumError + kd*rateError;                            
 
        lastError = error;                                
        previousTime = currentTime;                        

        return out;                         

```


    #This is where the you control it by the PID value

    




    #PID output goes here when I learn how
 
       
