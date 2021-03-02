currentTime = millis();
elapsedTime = currentTime - previousTime;
error = setPoint - input;
cumError += error * elapsedTime;
rateError = elapsedTime;
output = Kp * error + Ki * cumError + Kd   //defininig my keys
LastError = error;
previousTime = currentTime;


double kp = 2
double ki = 5
double kd = 1
  




    //This is where the you control it by the PID value

    




    //PID output goes here when I learn how
 
       