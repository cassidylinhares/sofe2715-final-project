class Graph {
   int[] data;
   int w;
   Graph(int _w) {
     w = _w;
   }
  void draw(int[] d) {
    stroke(0,0,0);
    strokeWeight(10);
    line(0, 0, width, 0);
    line(0,0,0,-height);
    int[] sorted = sort(d);
    int maxHeight = sorted[sorted.length-1];
    for (int i = 0; i < d.length; i++) {
      float factor = (map(d[i], 0, maxHeight, 0, 12)); 
      fill(0,255,0);
      stroke(0,0,255);
      strokeWeight(5);
      rect(5 + (i * w), 5, w, -10 + (-50 * factor));
      textAlign(CENTER);
      fill(0);
      textSize(20);
      text(d[i], 5 + (i * w) + (w/2), (-50 * factor) - 20);
    }
  }
}
