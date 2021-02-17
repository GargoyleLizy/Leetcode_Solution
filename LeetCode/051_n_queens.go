package main

import (
	"fmt"
	"strings"
)

var avail = 0
var noAvail = 1

// Solution contains solution by far
type Solution struct {
	n int
	// currentBoard is an array that contains Queens column pos for each row
	placedQueens []int
	step         int
}

func main() {
	fmt.Println(solveNQueens(5))
}

func solveNQueens(n int) [][]string {
	if n == 1 {
		var oneBoard = make([][]string, 1)
		oneBoard[0] = []string{"Q"}
		return oneBoard
	}

	var finalAns = [][]string{}
	for i := 0; i < n; i++ {
		var placedQueens = make([]int, n)
		placedQueens[0] = i
		var solution = Solution{n, placedQueens, 1}
		var ans = recSolution(solution)
		for j := 0; j < len(ans); j++ {
			finalAns = append(finalAns, translateSolution(ans[j], n))
		}
		//fmt.Println("final step translated", finalAns)

	}

	return finalAns
}

func recSolution(solution Solution) [][]int {
	var step = solution.step + 1
	var rowNum = solution.step
	var availablePos = calculateAvailPos(solution.placedQueens, rowNum, solution.n)

	var finalAns = [][]int{}

	if step == solution.n {
		for i := 0; i < solution.n; i++ {
			if availablePos[i] == avail {
				solution.placedQueens[rowNum] = i
				var successAns = make([]int, solution.n)
				for j := 0; j < solution.n; j++ {
					successAns[j] = solution.placedQueens[j]
				}
				return append(finalAns, successAns)
			}
		}
		//fmt.Println("fail", finalAns)
		return finalAns
	} else {
		for i := 0; i < solution.n; i++ {
			if availablePos[i] == avail {
				solution.placedQueens[rowNum] = i
				solution.step = step
				var ans = recSolution(solution)
				for j := 0; j < len(ans); j++ {
					finalAns = append(finalAns, ans[j])
				}
			}
		}
		//fmt.Println("middle", finalAns)
		return finalAns
	}
}

// Given a board that has placed Queen, update board with attacked spots.
func calculateAvailPos(placedQueens []int, rowNum int, n int) []int {
	var row = make([]int, n)
	if rowNum == 0 {
		return row
	}

	for i := 0; i < rowNum; i++ {
		var prevQueen = placedQueens[i]
		row[prevQueen] = noAvail
		var diff = rowNum - i
		if prevQueen-diff >= 0 {
			row[prevQueen-diff] = noAvail
		}
		if prevQueen+diff <= n-1 {
			row[prevQueen+diff] = noAvail
		}
	}
	return row
}

func translateSolution(placedQueens []int, n int) []string {
	var translated = make([]string, n)
	var sb strings.Builder
	for i := 0; i < n; i++ {
		sb.Reset()
		for j := 0; j < n; j++ {
			if j == placedQueens[i] {
				sb.WriteString("Q")
			} else {
				sb.WriteString(".")
			}
		}
		translated[i] = sb.String()
	}
	return translated
}
