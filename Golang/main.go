package main

import (
	"fmt"

	"github.com/airbusgeo/godal"
)

func main() {
	godal.RegisterAll()
	fmt.Println("We out here")
}
