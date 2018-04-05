int numOfBalls = 100000; 
int columns = 40;
int rows = 20;
int addPerFrame = 1000;
ArrayList<Ball> balls = new ArrayList<Ball>();
Graph g;
int stepCount = 0;

void setup() {
  frameRate(60);
  size(1200, 800);
  g = new Graph(width / (columns));
  balls.add(new Ball(columns % 2 == 0 ? columns / 2 : (columns - 1)/2, rows));
}

Boolean sketchDone() {
  int doneCount = 0;
  for (int i = 0; i < balls.size(); i++) {
    if (balls.get(i).didFall()) {
      doneCount++; 
    }
  }
  return doneCount >= balls.size();
}

void draw() {
  translate(0, height);
  background(255);
  if (stepCount < numOfBalls) {
    stepCount += addPerFrame;
    for(int i = 0; i < addPerFrame; i++) {
      balls.add(new Ball(columns % 2 == 0 ? columns / 2 : (columns - 1)/2, rows));
    }
  } 
  for (int i = 0; i < balls.size(); i++) {
    balls.get(i).move(columns);
  }
  
  int[] d = new int[columns];
  for (int i = 0; i < balls.size(); i++) {
    d[balls.get(i).position] += 1;
  }
  g.draw(d);
  text(stepCount, 50, -height + 50);
  if (sketchDone()) {
    print("Processing Time: ", millis()/1000.0, "s");
    noLoop();
  }
}
