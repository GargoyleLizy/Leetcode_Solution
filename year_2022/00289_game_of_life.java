package org.lizy;

import java.awt.Point;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public void gameOfLife(int[][] board) {
        // initialise all the automatons.
        int rowLength = board.length;
        int colLength = board[0].length;
        GameOfLifeAutomaton[][] automatons = new GameOfLifeAutomaton[rowLength][colLength];
        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < colLength; j++) {
                automatons[i][j] = new GameOfLifeAutomaton(j, i, colLength, rowLength);
            }
        }

        // calculating the next states.
        int[][] nextBoard = new int[rowLength][colLength];
        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < colLength; j++) {
                nextBoard[i][j] = automatons[i][j].calculatingNextState(board);
            }
        }
        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < colLength; j++) {
                board[i][j] = nextBoard[i][j];
            }
        }
    }
}

class GameOfLifeAutomaton {
    private final int x;
    private final int y;

    private final int colLength;
    private final int rowLength;

    private final List<Point> neighbours;

    public GameOfLifeAutomaton(int colIndex, int rowIndex, int colLength, int rowLength) {
        x = colIndex;
        y = rowIndex;
        this.colLength = colLength;
        this.rowLength = rowLength;

        ArrayList<Point> potentialNeighbours = new ArrayList<Point>();
        potentialNeighbours.add(new Point(x - 1, y - 1));
        potentialNeighbours.add(new Point(x, y - 1));
        potentialNeighbours.add(new Point(x + 1, y - 1));
        potentialNeighbours.add(new Point(x - 1, y));
        potentialNeighbours.add(new Point(x + 1, y));
        potentialNeighbours.add(new Point(x - 1, y + 1));
        potentialNeighbours.add(new Point(x, y + 1));
        potentialNeighbours.add(new Point(x + 1, y + 1));
        neighbours = potentialNeighbours.stream().filter(
                point -> isColRowLegit(point.x, point.y)
        ).toList();
    }

    private Boolean isColRowLegit(int colIndex, int rowIndex) {
        Boolean colLegit = colIndex >= 0 && colIndex < colLength;
        Boolean rowLegit = rowIndex >= 0 && rowIndex < rowLength;
        return colLegit && rowLegit;
    }

    /**
     * Given current board, calculate whether current cell's state in the next round.
     *
     * @param currentBoard
     * @return
     */
    public int calculatingNextState(int[][] currentBoard) {
        long surroundingLives = neighbours.stream().filter(
                point -> currentBoard[point.y][point.x] == 1
        ).count();
        int currentLivingStatus = currentBoard[this.y][this.x];
        if (currentLivingStatus == 1) {
            if (surroundingLives < 2) {
                return 0;
            }
            if (surroundingLives == 2 || surroundingLives == 3) {
                return 1;
            }
            return 0;
        } else if (surroundingLives == 3) {
            return 1;
        } else {
            return 0;
        }
    }
}
