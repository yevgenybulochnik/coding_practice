package main

import "fmt"
import "time"

// Brute force solution
func countOdds(lo int, hi int) int {
    count := 0
    s := make([]int, hi-lo + 1)


    for i := range s {
        s[i] = lo + i
        if (lo + i) % 2 != 0 {
            count ++
        }
    }
    fmt.Println(count)
    return count
};

func main() {
    start := time.Now()
    // using 1, 700000000 as args takes this function almost 8 seconds to run
    countOdds(3, 7)
    fmt.Println(time.Since(start))
}
