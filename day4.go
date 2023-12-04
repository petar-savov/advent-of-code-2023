package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	f, _ := os.Open("input-4.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)

	ticketCopies := make(map[int]int)
	s := 0
	i := 0
	for scanner.Scan() {

		i += 1
		line := scanner.Text()

		parts := strings.Split(line, ":")

		tickets := strings.Split(parts[1], "|")
		winning := strings.Fields(strings.TrimSpace(tickets[0]))
		mine := strings.Fields(strings.TrimSpace(tickets[1]))

		extraTickets := 0
		ticketScore := 0
		for j := range winning {
			for k := range mine {
				if winning[j] == mine[k] {
					if ticketScore == 0 {
						ticketScore = 1
					} else {
						ticketScore *= 2
					}
					extraTickets += 1
					ticketCopies[i+extraTickets] += 1 + ticketCopies[i]
				}
			}
		}

		s += ticketScore

	}

	t := 0
	for _, v := range ticketCopies {
		t += v
	}
	fmt.Println(s)
	fmt.Println(t + i)

}
