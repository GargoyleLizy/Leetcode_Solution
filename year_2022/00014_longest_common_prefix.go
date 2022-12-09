package main

import (
	"fmt"
	"strings"
)

func main() {
	testStrings := []string{"cir", "car"}
	result := longestCommonPrefix(testStrings)
	fmt.Println(result)
}

func longestCommonPrefix(strs []string) string {
	commonPrefix := strs[0]
	for i := 1; i < len(strs); i++ {
		commonPrefix = findCommonOf(strs[i], commonPrefix)
		if commonPrefix == "" {
			break
		}
	}
	return commonPrefix
}

func findCommonOf(strOne string, strTwo string) string {
	var sb strings.Builder
	minLengh := min(len(strOne), len(strTwo))
	for i := 0; i < minLengh; i++ {
		if strOne[i] == strTwo[i] {
			sb.WriteByte(strOne[i])
		} else {
			break
		}
	}
	return sb.String()
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
