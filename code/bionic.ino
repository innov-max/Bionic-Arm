#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

void setup() {
  servo1.attach(9);   // Attach servo to pin 9
  servo2.attach(10);  // Attach servo to pin 10
  servo3.attach(11);  // Attach servo to pin 11
  servo4.attach(6);   // Attach servo to pin 6
  servo5.attach(5);   // Attach servo to pin 5
  servo6.attach(3);   // Attach servo to pin 3

  Serial.begin(9600);  // Initialize the serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    int servoNum = input.substring(0, 1).toInt();
    int servoPosition = input.substring(2).toInt();

    switch (servoNum) {
      case 1:
        servo1.write(servoPosition);
        break;
      case 2:
        servo2.write(servoPosition);
        break;
      case 3:
        servo3.write(servoPosition);
        break;
      case 4:
        servo4.write(servoPosition);
        break;
      case 5:
        servo5.write(servoPosition);
        break;
      case 6:
        servo6.write(servoPosition);
        break;
      default:
        break;
    }
  }
}
