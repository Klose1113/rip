#include <Servo.h>
#include <Ultrasonic.h>

Servo servo3;

Ultrasonic ultrasonic_right(8,9);
Ultrasonic ultrasonic_front2(6,7);

const int leftMotorPin1 = 12;
const int leftMotorPin2 = 13;
const int rightMotorPin1 = 10;
const int rightMotorPin2 = 11;

const int motorPin1 = 30;  // Connect to one of the motor pins
const int motorPin2 = 31;

const int trigPin = A1;  
const int echoPin = A0; 
int k = 0;
long duration;
float distance;
String arm;
int y;
int distance_right, distance_front2;


void setup() {
  Serial.begin(115200);
  
  servo3.attach(40);
  
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);
  
}

void loop() {
  
 if(Serial.available()>0){
      arm = Serial.readStringUntil('\n');
      y = arm.toInt();
 
    }

  // Trigger the sensor by sending a 10us high pulse to the trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  
  duration = pulseIn(echoPin, HIGH);
  
  distance = duration * 0.034 / 2;
  
 
  

  forward();



//forward();
  
if (y == 4){
  if (distance > 7 && k == 0){
    reach();
    k=1;
  }
  
  else if(distance < 7 && k == 1){
      pause();
      k = 2;
      
  }

  else if(k == 2){
    retract();
    k = 3;
  }

  else if (k == 3){
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    sprint();
  }
}

}


void reach(){

  stay();
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  

}
void pause(){
  
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);

  for (int angle = 90; angle <= 150; angle+=1){
    servo3.write(angle);
    delay(10);
  }
  
  forward();
  
  delay(5000);
  
  for (int angle = 150; angle >= 90; angle-=1){
    servo3.write(angle);
    delay(10);
  }
  delay(300);
  
}

void retract(){
  
  for (int angle = 150; angle >= 90; angle-=1){
    servo3.write(angle);
    delay(10);
  }
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  delay(2000);
}

void forward(){
  analogWrite(leftMotorPin1, 0);
  analogWrite(leftMotorPin2, 150);
  analogWrite(rightMotorPin1, 0);
  analogWrite(rightMotorPin2, 150);
}

void left(){
  analogWrite(leftMotorPin1, 200);
  analogWrite(leftMotorPin2, 0);
  analogWrite(rightMotorPin1, 0);
  analogWrite(rightMotorPin2, 200);
}

void stay(){
  
  analogWrite(leftMotorPin1, 0);
  analogWrite(leftMotorPin2, 0);
  analogWrite(rightMotorPin1, 0);
  analogWrite(rightMotorPin2, 0);
}

void sprint(){
  analogWrite(leftMotorPin1, 0);
  analogWrite(leftMotorPin2, 250);
  analogWrite(rightMotorPin1, 0);
  analogWrite(rightMotorPin2, 250);
}

/*void ReadUlst() {
  distance_right = ultrasonic_right.read();
}

if (ultFlag == 1) {

    ReadUlst();

   if (distance_right < 5 && distance_right > 0) {
      while (distance_right < 20) {
        left();
        ReadUlst();
      }
    }
    */
