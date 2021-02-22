package main

import "fmt"

func main() {
	// var testStats = []Stat{{0, 10}, {-1, 1}, {-2, 2}}
	// var newStats = generateNextStats(testStats, 1)
	// fmt.Println(newStats)
	// var testStats2 = []Stat{{1, 5}, {-1, 2}, {-3, 3}}
	// var combined = combineTwoStatArr(testStats, testStats2)
	// fmt.Println(combined)

	var testDungeon = [][]int{{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}}
	var res = calculateMinimumHP(testDungeon)
	fmt.Println(res)
}

// Stat record the lowest health point and current health
type Stat struct {
	lowest        int
	currentHealth int
}

func calculateMinimumHP(dungeon [][]int) int {
	var m = len(dungeon)
	var n = len(dungeon[0])
	var stats = make([][][]Stat, m)
	for i := range stats {
		stats[i] = make([][]Stat, n)
	}
	//fmt.Println(stats)
	// init
	stats[0][0] = []Stat{{dungeon[0][0], dungeon[0][0]}}
	if n > 1 {
		for i := 1; i < n; i++ {
			stats[0][i] = generateNextStats(stats[0][i-1], dungeon[0][i])
		}
	}
	if m > 1 {
		for i := 1; i < m; i++ {
			stats[i][0] = generateNextStats(stats[i-1][0], dungeon[i][0])
		}
	}
	//fmt.Println(stats)
	// induction
	if n > 1 && m > 1 {
		for i := 1; i < m; i++ {
			for j := 1; j < n; j++ {
				var leftStats = stats[i][j-1]
				var topStats = stats[i-1][j]
				var combined = combineTwoStatArr(leftStats, topStats)
				var updatedCombined = generateNextStats(combined, dungeon[i][j])
				stats[i][j] = updatedCombined
			}
		}
	}
	//fmt.Println(stats)

	return findMinHealth(stats[m-1][n-1])
}

func generateNextStats(stats []Stat, tileVal int) []Stat {
	var newStats = make([]Stat, len(stats))
	for i := 0; i < len(stats); i++ {
		newStats[i].currentHealth = stats[i].currentHealth + tileVal
		newStats[i].lowest = minInt(newStats[i].currentHealth, stats[i].lowest)
	}
	return newStats
}

func minInt(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// remove stat that inferior than rest, meaning its lowest and currentHealth are
// both smaller or equal, compare one of the rest.
func combineTwoStatArr(stats1 []Stat, stats2 []Stat) []Stat {
	var flag1 = make([]int, len(stats1))
	var flag2 = make([]int, len(stats2))
	var unflag = 0
	var flaggedOut = 1
	for i := 0; i < len(stats1); i++ {
		for j := 0; j < len(stats2); j++ {
			if (flag1[i] == unflag) && (flag2[j] == unflag) {
				var compareResult = compareTwoStat(stats1[i], stats2[j])
				//fmt.Println("1:", stats1[i], "; 2: ", stats2[j], "; compare result: ", compareResult)
				switch compareResult {
				case 1:
					flag2[j] = flaggedOut
				case 2:
					flag1[i] = flaggedOut
				default:
					// no one is inferior, keep both.
				}
			}
		}
	}
	// combine the unflaggedOut Stat
	var combined = []Stat{}
	var combinedCount = 0
	for i := 0; i < len(stats1); i++ {
		if flag1[i] == unflag {
			combined = append(combined, stats1[i])
			combinedCount++
		}
	}
	for j := 0; j < len(stats2); j++ {
		if flag2[j] == unflag {
			combined = append(combined, stats2[j])
			combinedCount++
		}
	}
	return combined
}

// Compare two stat. Return 1 if first stat is superior than second.
// Return 2 if second stat is superior than first.
// Return 0 if no one is superior than other.
// Superior means higher lowest and higher currentHealth
// While if both's lowest health is higher than 0, then lowest does not matter
func compareTwoStat(firstStat Stat, secondStat Stat) int {
	if (firstStat.lowest >= 0) && (secondStat.lowest >= 0) {
		if firstStat.currentHealth >= secondStat.currentHealth {
			return 1
		}
		return 2
	}

	if (firstStat.lowest <= secondStat.lowest) && (firstStat.currentHealth <= secondStat.currentHealth) {
		return 2
	}
	if (secondStat.lowest <= firstStat.lowest) && (secondStat.currentHealth <= firstStat.currentHealth) {
		return 1
	}
	return 0
}

func findMinHealth(stats []Stat) int {
	var highestLowest = stats[0].lowest
	for i := 0; i < len(stats); i++ {
		if highestLowest < stats[i].lowest {
			highestLowest = stats[i].lowest
		}
	}
	if highestLowest >= 0 {
		return 1
	}
	return 1 - highestLowest
}
