/**
 * @author Steve
 * @date 2022/11/23
 * *
 * Compilation: go run make_withdraw.go
 * *
 * description:
 **/

package main

import "fmt"

func main() {
	wd := make_withdraw(100)
	wd(10) // 90
	wd(10) // 80
}

func make_withdraw(balance int) func(amount int)  {
	return func(amount int)  {
		if amount > balance {
			fmt.Println("Insufficient funds") 
		}
		balance -= amount
		fmt.Println(balance)

	}

}