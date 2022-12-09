package main

// the max length of row/col
var length = 1000

func main() {
	//[[4,4],[5,5],[3,1],[1,4],[1,1],[2,3],[0,3],[2,4],[3,5]]
	//var stones = [][]int{{0, 0}, {0, 1}, {1, 0}, {1, 2}, {2, 1}, {2, 2}}
	// [[1,2],[6,9],[8,2],[2,9],[7,1],[3,0],[2,8],[6,1],[4,4],[5,2],[1,4],[3,8],[9,2],[0,7],[0,9],[3,4],[8,5],[1,1]]
	// var stones = [][]int{{4, 4}, {5, 5}, {3, 1}, {1, 4}, {1, 1}, {2, 3}, {0, 3}, {2, 4}, {3, 5}}
	var stones = [][]int{{1, 2}, {6, 9}, {8, 2}, {2, 9}, {7, 1}, {3, 0}, {2, 8}, {6, 1}, {4, 4}, {5, 2}, {1, 4}, {3, 8}, {9, 2}, {0, 7}, {0, 9}, {3, 4}, {8, 5}, {1, 1}}
	print(removeStones(stones))
}

func removeStones(stones [][]int) int {
	var length = 1000
	var colSets = make([]int, length)
	for i := 0; i < length; i++ {
		colSets[i] = -1
	}
	var rowSets = make([]int, length)
	for i := 0; i < length; i++ {
		rowSets[i] = -1
	}
	var setsIds = make([]int, 0)
	for i := 0; i < len(stones); i++ {
		currentStone := stones[i]
		currentCol := currentStone[0]
		currentRow := currentStone[1]
		if colSets[currentCol] == -1 && rowSets[currentRow] == -1 {
			// creating new set
			newId := len(setsIds)
			setsIds = append(setsIds, newId)
			colSets[currentCol] = newId
			rowSets[currentRow] = newId
		} else if colSets[currentCol] != -1 && rowSets[currentRow] != -1 {
			// checking if we need link sets
			colSet := colSets[currentCol]
			rowSet := rowSets[currentRow]
			colSetId := findSetId(setsIds, colSet)
			rowSetId := findSetId(setsIds, rowSet)
			var minSetsId = colSetId
			if rowSetId < colSetId {
				minSetsId = rowSetId
			}
			setsIds[colSetId] = minSetsId
			setsIds[rowSetId] = minSetsId
		} else if colSets[currentCol] != -1 {
			rowSets[currentRow] = colSets[currentCol]
		} else {
			colSets[currentCol] = rowSets[currentRow]
		}
	}
	var individualComponent = 0
	for i := 0; i < len(setsIds); i++ {
		if setsIds[i] == i {
			individualComponent++
		}
	}

	return len(stones) - individualComponent
}

func findSetId(setsId []int, set int) int {
	for setsId[set] != set {
		set = setsId[set]
	}
	return set
}
