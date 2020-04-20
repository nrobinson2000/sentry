#include <Adafruit_NeoPixel.h>

/*
   sentry-light.ino
   Set all pixels in a NeoPixel ring to the specified color given over serial.
   Example operation:
    "255,255,255\n" - Turn all pixels white, max brightness, respond with "OK\n"
    "0,0,0\n" - Turn off all pixels, respond with "OK\n"
    "hello world" - Invalid input, respond with "NOT OK\n"
*/

// Digital pin 6 on Arduino Nano, 16 pixel NeoPixel ring
#define PIN 6
#define PIXELS 16

Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXELS, PIN, NEO_GRB + NEO_KHZ800);

// Initialize serial and pixels
void setup() {
  Serial.begin(115200);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

// Parse input and color pixels
void parseStr(const char* command) {
  uint16_t red, green, blue;
  if (sscanf(command, "%u,%u,%u", &red, &green, &blue) == 3) {
    Serial.println("OK");
    colorFill(strip.Color(red, green, blue));
  } else {
    Serial.println("NOT OK");
  }
}

// Listen for serial input
void loop() {
#define BUFFER_SIZE 50
  static char serialBuffer[BUFFER_SIZE];
  static uint16_t index = 0;

  while (Serial.available()) {
    char c = Serial.read();
    if (index == BUFFER_SIZE) index = 0;
    if (c == '\n') {
      serialBuffer[index++] = 0;
      parseStr(serialBuffer);
      index = 0;
    } else {
      serialBuffer[index++] = c;
    }
  }
}

// Set all pixels to the specified color
void colorFill(uint32_t c) {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
  }
  strip.show();
}

