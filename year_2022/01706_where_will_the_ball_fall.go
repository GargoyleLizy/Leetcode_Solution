package main

import "fmt"

func main() {
	sampleGrid := [][]int{
		{1, 1, 1, -1, -1}, {1, 1, 1, -1, -1}, {-1, -1, -1, 1, 1}, {1, 1, 1, 1, -1}, {-1, -1, -1, -1, -1},
	}
	result := findBall(sampleGrid)
	fmt.Println(result)
}

func findBall(grid [][]int) []int {
	m := len(grid)
	n := len(grid[0])
	procGrid := make([][]int, m)
	rows := make([]int, m*n)
	for i := 0; i < n*m; i++ {
		rows[i] = -1
	}
	for i := 0; i < m; i++ {
		procGrid[i] = rows[i*n : (i+1)*n]
	}
	// create the inital row
	initialRow := make([]int, n)
	for i := 0; i < n; i++ {
		initialRow[i] = i
	}
	// find the balls falling in each row
	for i := 0; i < m; i++ {
		if i == 0 {
			findBallRow(&procGrid, grid, i, initialRow)
		} else {
			findBallRow(&procGrid, grid, i, procGrid[i-1])
		}
	}
	// using the last row of procGrid to calculating
	resultRow := make([]int, n)
	for i := 0; i < n; i++ {
		resultRow[i] = -1
	}
	for i := 0; i < n; i++ {
		result := procGrid[m-1][i]
		if result != -1 {
			resultRow[result] = i
		}
	}
	return resultRow
}

func findBallRow(procGrid *([][]int), grid [][]int, rowIndex int, lastRow []int) {
	n := len((*procGrid)[0])
	for i := 0; i < n; i++ {
		lastBall := lastRow[i]
		direction := grid[rowIndex][i]
		if lastBall == -1 {
			// not a legit ball
			continue
		}
		if direction == 1 {
			if i < n-1 && grid[rowIndex][i+1] == 1 {
				(*procGrid)[rowIndex][i+1] = lastRow[i]
			}
		} else {
			if i > 0 && grid[rowIndex][i-1] == -1 {
				(*procGrid)[rowIndex][i-1] = lastRow[i]
			}
		}
	}
}
