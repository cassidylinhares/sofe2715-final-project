class Ball {
  int position;
  int rows;
  int count;
  Ball(int startPos, int _rows) {
    position = startPos;
    rows = _rows;
    count = 0;
  }
  void move(int max) {
    int[] choice = {-1, 1};
    int rand = int(random(choice.length));
    if (count < rows && position > 0 && position < max - 1) {
      position += choice[rand];
      count++;
    }
  }
}
