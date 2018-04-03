class Ball {
  int radius = 10;
  PVector position;
  PVector velocity;
  PVector acceleration;
  Ball(int $x, int $y) {
    position = new PVector($x, $y);
    velocity = new PVector(0, 0);
    acceleration = new PVector(0, gravity);
  }
  
  void draw() {
    updatePosition();
    fill(255,0,0);
    strokeWeight(0);
    ellipse(position.x, position.y, radius, radius);
  }
  
  void collide(int id, Peg[] pa) {
    if (lineCircle((width-b.margin)/2, b.topOfBoard - b.margin, 0,0, position.x, position.y, radius)) {
      float dx = pa[i].position.x - position.x;
      float dy = pa[i].position.y - position.y;
      float distance = sqrt(dx*dx + dy*dy);
      float minDist = pa[i].r + radius;
      if (distance < minDist) { 
        float angle = atan2(dy, dx);
        float targetX = position.x + cos(angle) * minDist;
        float targetY = position.y + sin(angle) * minDist;
        float ax = (targetX - pa[i].position.x);
        float ay = (targetY - pa[i].position.y);
        velocity.x -= ax;
        velocity.y -= ay;
      }
    }
    if (lineCircle((width+b.margin)/2, b.topOfBoard - b.margin, width, 0, position.x, position.y, radius)) {
      
    }
    for (int i = 0; i < pa.length; i++) {
      float dx = pa[i].position.x - position.x;
      float dy = pa[i].position.y - position.y;
      float distance = sqrt(dx*dx + dy*dy);
      float minDist = pa[i].r + radius;
      if (distance < minDist) { 
        float angle = atan2(dy, dx);
        float targetX = position.x + cos(angle) * minDist;
        float targetY = position.y + sin(angle) * minDist;
        float ax = (targetX - pa[i].position.x);
        float ay = (targetY - pa[i].position.y);
        velocity.x -= ax;
        velocity.y -= ay;
      }
    }   
  }
  
  void updatePosition() {
    velocity.add(acceleration);
    position.add(velocity);
    if (position.y + radius > height) {
      position.y = height;
    }
  }
}
