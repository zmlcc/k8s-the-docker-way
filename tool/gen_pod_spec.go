package main

import (
	"fmt"
	// change version as needed
	api "k8s.io/api/core/v1"
)

func main() {
	fmt.Println("OK")

	aaa := api.Pod{}
	bbb := fmt.Sprintf("%#v", aaa)
	printGoType(bbb)
	fmt.Println()
}

func printIndent(n int) {
	for i := 0; i < n; i++ {
		fmt.Print("  ")
	}
}

func printGoType(s string) {
	idn := 0
	for _, c := range s {
		switch c {
		case ':':
			fmt.Print(": ")
		case ' ':
		case '{':
			idn = idn + 1
			fmt.Println("{")
			printIndent(idn)

		case '}':
			idn = idn - 1
			fmt.Println()
			printIndent(idn)

			fmt.Print("}")
		case ',':
			fmt.Println(",")
			printIndent(idn)

		default:
			fmt.Printf("%c", c)
		}
	}
}
