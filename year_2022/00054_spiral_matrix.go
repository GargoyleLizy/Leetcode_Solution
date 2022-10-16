package main

import (
	"fmt"
)

func main() {
	//matrix1 := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	matrix2 := [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}
	fmt.Println(spiralOrder(matrix2))
}

func spiralOrder(matrix [][]int) []int {
	zeroSlice := make([]int, 0)
	return spiralOrderRec(matrix, 0, len(matrix), 0, len(matrix[0]), 0, zeroSlice)
}

func spiralOrderRec(matrix [][]int, mLow int, mHigh int, nLow int, nHigh int, mode int, accumulateSlice []int) []int {
	if mLow == mHigh || nLow == nHigh {
		return accumulateSlice
	}
	var thisSlice []int
	switch mode {
	case 0:
		thisSlice = make([]int, nHigh-nLow)

		for i := 0; i <= nHigh-1-nLow; i++ {
			//fmt.Println("Case0: m:", mLow, ";n:", nLow+i)
			//fmt.Println("i: ", i, "limit: ", nHigh-1-nLow)
			//fmt.Println("target: ", mLow, nLow+i, "; ", matrix[mLow][nLow+i])
			thisSlice[i] = matrix[mLow][nLow+i]
		}
		newAccumulated := append(accumulateSlice, thisSlice...)
		return spiralOrderRec(matrix, mLow+1, mHigh, nLow, nHigh, 1, newAccumulated)
	case 1:
		thisSlice = make([]int, mHigh-mLow)
		for i := 0; i <= mHigh-1-mLow; i++ {
			thisSlice[i] = matrix[mLow+i][nHigh-1]
		}
		newAccumulated := append(accumulateSlice, thisSlice...)
		return spiralOrderRec(matrix, mLow, mHigh, nLow, nHigh-1, 2, newAccumulated)
	case 2:
		thisSlice = make([]int, nHigh-nLow)
		for i := 0; i <= nHigh-1-nLow; i++ {
			thisSlice[i] = matrix[mHigh-1][nHigh-1-i]
		}
		newAccumulated := append(accumulateSlice, thisSlice...)
		return spiralOrderRec(matrix, mLow, mHigh-1, nLow, nHigh, 3, newAccumulated)
	default:
		thisSlice = make([]int, mHigh-mLow)
		for i := 0; i <= mHigh-1-mLow; i++ {
			thisSlice[i] = matrix[mHigh-1-i][nLow]
		}
		newAccumulated := append(accumulateSlice, thisSlice...)
		return spiralOrderRec(matrix, mLow, mHigh, nLow+1, nHigh, 0, newAccumulated)
	}

}
