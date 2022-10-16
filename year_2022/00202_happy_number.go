package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(isHappy(3))
}

func isHappy(n int) bool {
	if n == 1 {
		return true
	}

	var context map[int]int
	context = make(map[int]int)
	return isHappyRec(n, &context)
}

func isHappyRec(n int, context *map[int]int) bool {
	var nStr = strconv.Itoa(n)
	splitedNStr := strings.Split(nStr, "")
	sum := 0
	for _, nChar := range splitedNStr {
		nCharDigit, err := strconv.Atoi(nChar)
		if err != nil {
			return false
		}
		sum = sum + nCharDigit*nCharDigit
	}
	if sum == 1 {
		return true
	} else {
		_, isExist := (*context)[n]
		if isExist {
			return false
		}
		(*context)[n] = sum
		return isHappyRec(sum, context)
	}
}
