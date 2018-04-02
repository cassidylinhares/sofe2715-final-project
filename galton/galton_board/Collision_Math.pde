boolean lineCircle(int x1, int y1, int x2, int y2, float cx, float cy, int r) {
  boolean inside1 = pointCircle(x1,y1, cx,cy,r);
  boolean inside2 = pointCircle(x2,y2, cx,cy,r);
  if (inside1 || inside2) {
    return true;
  }

  float distX = x1 - x2;
  float distY = y1 - y2;
  float len = sqrt( (distX*distX) + (distY*distY) );

  float dot = ( ((cx-x1)*(x2-x1)) + ((cy-y1)*(y2-y1)) ) / pow(len,2);

  float closestX = x1 + (dot * (x2-x1));
  float closestY = y1 + (dot * (y2-y1));

  boolean onSegment = linePoint(x1,y1,x2,y2, closestX,closestY);
  if (!onSegment) {
    return false;
  }

  distX = closestX - cx;
  distY = closestY - cy;
  float distance = sqrt( (distX*distX) + (distY*distY) );

  if (distance <= r) {
    return true;
  }
  return false;
}

boolean pointCircle(float px, float py, float cx, float cy, float r) {
  float distX = px - cx;
  float distY = py - cy;
  float distance = sqrt((distX*distX) + (distY*distY));
  if (distance <= r) {
    return true;
  }
  return false;
}

boolean linePoint(float x1, float y1, float x2, float y2, float px, float py) {
  float d1 = dist(px,py, x1,y1);
  float d2 = dist(px,py, x2,y2);
  float lineLen = dist(x1,y1, x2,y2);
  float buffer = 0.1;
  if (d1+d2 >= lineLen-buffer && d1+d2 <= lineLen+buffer) {
    return true;
  }
  return false;
}
