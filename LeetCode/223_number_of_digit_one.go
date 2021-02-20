package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	var testResult = countDigitOne(10000)
	fmt.Println(testResult)
}

func countDigitOne(n int) int {
	var s = strconv.Itoa(n)
	var accumulateDigitCounts = 0
	for i := 0; i < len(s); i++ {
		var beforeStr = s[0:i]
		var afterStr string
		if i == len(s)-1 {
			afterStr = ""
		} else {
			afterStr = s[i+1 : len(s)]
		}
		var thisDigitStr = s[i : i+1]
		thisDigitInt, err := strconv.Atoi(thisDigitStr)
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
		var thisDigitCount = countDigitOneOnIndex(beforeStr, afterStr, thisDigitInt)
		accumulateDigitCounts += thisDigitCount
	}
	return accumulateDigitCounts
}

func countDigitOneOnIndex(beforeStr string, afterStr string, thisDigit int) int {
	var beforeInt int
	var err error
	if len(beforeStr) == 0 {
		beforeInt = 0
	} else {
		beforeInt, err = strconv.Atoi(beforeStr)
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
	}

	var afterInt int
	if len(afterStr) == 0 {
		afterInt = 0
	} else {
		afterInt, err = strconv.Atoi(afterStr)
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
	}

	var prevCounts = beforeInt * int(math.Pow10(len(afterStr)))
	var currentCounts int
	switch thisDigit {
	case 0:
		currentCounts = 0
	case 1:
		currentCounts = 1 + afterInt
	default:
		currentCounts = int(math.Pow10(len(afterStr)))
	}

	return prevCounts + currentCounts
}
