package main

import (
	"fmt"
)

func main() {
	var test = []int{0, 1, 1, 0}
	fmt.Println(isOneBitCharacter(test))
}

func isOneBitCharacter(bits []int) bool {
	if len(bits) == 1 {
		return true
	}

	var n = len(bits)
	if bits[n-2] == 0 {
		return true
	} else {
		var lastOneGroupCount = 0
		for i := n - 2; i >= 0 && (bits[i] == 1); i-- {
			lastOneGroupCount++
		}
		return lastOneGroupCount%2 == 0
	}
}
