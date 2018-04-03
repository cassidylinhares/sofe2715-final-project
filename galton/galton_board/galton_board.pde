float gravity = 0.1;
float friction = -0.9;
float spring = 0.05;
int numOfBall = 100;

Board b;
Ball[] balls;

void setup() {
  size(1200, 800);
  rectMode(CENTER);
  ellipseMode(CENTER);
  b = new Board(10, 50, 10, 10);
  b.buildPegArray();
  balls = new Ball[numOfBall];
  for(int i = 0; i < balls.length; i++) {
    balls[i] = new Ball((width-100)/2, 10); 
  }
}

void draw() {
  background(255);
  strokeWeight(10);
  line((width-b.margin)/2, b.topOfBoard - b.margin, 0,0);
  line((width+b.margin)/2, b.topOfBoard - b.margin, width,0);
  b.draw();
  for(int i = 0; i < balls.length; i++) {
    balls[i].collide(i, b.pegArray);
    balls[i].draw(); 
    
  }
}
