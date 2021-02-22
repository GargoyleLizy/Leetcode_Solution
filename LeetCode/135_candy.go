package main

import (
	"fmt"
)

func main() {
	var test1 = []int{1, 3, 2, 2, 1}
	var res1 = candy(test1)
	fmt.Println("res1 should be 7 = ", res1)
	var test2 = []int{1, 2, 2}
	var res2 = candy(test2)
	fmt.Println("res2 should be 4 = ", res2)
	var test3 = []int{1, 0, 2}
	var res3 = candy(test3)
	fmt.Println("res3 should be 5 = ", res3)
	var test4 = []int{1, 2, 87, 87, 87, 2, 1}
	var res4 = candy(test4)
	fmt.Println("res4 should be 13 = ", res4)
}

func candy(ratings []int) int {
	var candies = make([]int, len(ratings))
	var length = len(ratings)

	var nextLowPoint = findNextLow(ratings, 0)
	var lastmarkedPoint = nextLowPoint
	candies[nextLowPoint] = 1

	for i := 0; i < length; {
		// back tracking
		if i < lastmarkedPoint {
			for j := lastmarkedPoint - 1; j >= i; j-- {
				candies[j] = maxInt(candies[j+1]+1, candies[j])
			}
		}
		if lastmarkedPoint == length-1 {
			break
		}
		// expanding
		for j := lastmarkedPoint; j < length-1; j++ {
			if ratings[j+1] > ratings[j] {
				candies[j+1] = candies[j] + 1
				i = j + 1
			} else if ratings[j+1] == ratings[j] {
				candies[j+1] = 1
				i = j + 1
			} else {
				i = j
				break
			}
		}
		// find next low and restart loop
		if i == length-1 {
			break
		}
		nextLowPoint = findNextLow(ratings, i+1)
		candies[nextLowPoint] = 1
		lastmarkedPoint = nextLowPoint
	}
	// candies should be filled and ready to be summed
	fmt.Println(candies)
	var candiesSum = 0
	for i := 0; i < length; i++ {
		candiesSum = candiesSum + candies[i]
	}

	return candiesSum
}

// return the index of next low point, low point meaning it is not bigger than surroundings.
func findNextLow(arr []int, startpoint int) int {
	if len(arr) == 1 {
		return 0
	}
	for i := startpoint; i < len(arr); i++ {
		if i == 0 {
			if arr[i] <= arr[i+1] {
				return i
			}
		} else if i < len(arr)-1 {
			var left = arr[i-1]
			var right = arr[i+1]
			if (arr[i] <= left) && (arr[i] <= right) {
				return i
			}
		}
	}
	return len(arr) - 1
}

func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}
