int numOfBalls = 10000; 
int columns = 80;
int rows = 40;
int addPerFrame = 1;
ArrayList<Ball> balls = new ArrayList<Ball>();
Graph g;
int stepCount = 0;

void setup() {
  frameRate(1000);
  size(1200, 800);
  g = new Graph(width / (columns));
  balls.add(new Ball(columns % 2 == 0 ? columns / 2 : (columns - 1)/2, rows));
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
}
