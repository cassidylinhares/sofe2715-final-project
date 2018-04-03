class Board {
   int pegRadius;
   int margin;
   int lines;
   int columns;
   int topOfBoard;
   Peg[] pegArray;
   
   Board(int $pegRadius, int $pegMargin, int $numOfLines, int $numOfColumns) {
     pegRadius = $pegRadius;
     margin = $pegMargin;
     lines = $numOfLines;
     columns = $numOfColumns;
     pegArray = new Peg[lines * columns];
     topOfBoard = 200;
   }
   
   void buildPegArray() {
     int pegIndex = 0;
     int middle = width / 2;
     
     for (int line = 1; line <= lines; line++) {
       for (int col = 1; col <= columns; col++) {
         int pegOffset = 0;
         if (line % 2 == 0) {
           pegOffset = margin / 2;
         } else {
           pegOffset = 0;
         }
         int start = middle - (pegOffset + ((columns / 2) * margin));
         pegArray[pegIndex++] = new Peg(start + (col * margin),topOfBoard + line * margin, 5);
       }
     }
   }
   
   void draw() {
     fill (0,0,255);
     strokeWeight(0);
     for (int i = 0; i < pegArray.length; i++) {
       ellipse(pegArray[i].position.x, pegArray[i].position.y, pegArray[i].r, pegArray[i].r);
     }
   }
}
