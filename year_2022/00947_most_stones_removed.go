package main

// the max length of row/col
var length = 1000

type colRowPointer struct {
	isCol      bool
	index      int
	otherIndex *[]int
}

func main() {

}

func removeStones(stones [][]int) int {
	// initial the col row counts
	colCounts := make([][]int, length)
	for i := 0; i < length; i++ {
		colCounts[i] = make([]int, 0)
	}
	rowCounts := make([][]int, length)
	for i := 0; i < length; i++ {
		rowCounts[i] = make([]int, 0)
	}
	// populate the col row counts
	for x := 0; x < len(stones); x++ {
		stone := stones[x]
		colCounts[stone[1]] = append(colCounts[stone[1]], stone[0])
		rowCounts[stone[0]] = append(rowCounts[stone[0]], stone[1])
	}

	// initial the col row pointer like hashmaps.
	colRowPointers := make([][]colRowPointer, length)
	for i := 0; i < length; i++ {
		colRowPointers = make([][]colRowPointer, 0)
	}

	// populate the colRowPointers
	for i := 0; i < length; i++ {
		size := len(colCounts[i])
		newPointer := colRowPointer{true, i, &colCounts[i]}
		if colRowPointers[size] == nil {
			colRowPointers[size] = []colRowPointer{newPointer}
		} else {
			colRowPointers[size] = append(colRowPointers[size], newPointer)
		}
	}
	for i := 0; i < length; i++ {
		size := len(rowCounts[i])
		newPointer := colRowPointer{false, i, &rowCounts[i]}
		if colRowPointers[size] == nil {
			colRowPointers[size] = []colRowPointer{newPointer}
		} else {
			colRowPointers[size] = append(colRowPointers[size], newPointer)
		}
	}

	// start removing
	var removed = 0
	var notRemovable = 0
	var total = len(stones)
	for removed+notRemovable < total {
		for i := 1; i < length; i++ {
			// if we have pointers indicate a row or col has stone
			if (len(colRowPointers[i]) > 0) {
				// if we have a row or col with just one stone. Then this stone is decisive.
				// It can either be removed or not. 
				if i == 1 {
					// just pick anyone
					targetPointer := colRowPointers[1][0]
					var targetStone []int
					if(targetPointer.isCol) {
						targetStone = int[(*targetPointer.otherIndex)[0],targetPointer.index]
						var otherConnection = rowCounts[targetStone[0]]
						if otherConnection == 0 {
							removed++
						} else {
							notRemovable++
						}
						rowCounts
					} else {
						targetStone = int[targetPointer.index, (*targetPointer.otherIndex)[0]]
					}
				}
			}
			
			if len(colRowPointers[i]) > 0 {
				// just pick any pointer
				targetPointer := colRowPointers[i][0]
				// pick the stone with least connection
				var leastConnectedStone 
				for j := 0; j < len(*(targetPointer.otherIndex)); j++ {
					
				}
				break
			}
		}
	}

	return 0
}
