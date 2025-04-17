package main
import (
	"fmt"
	"net/http"
)

func hello( w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<h1>Hello, World - Welcome to Golang!</h1>")
}
func main() {
	http.HandleFunc("/", hello)
	fmt.Println("Server is running on port 8080")
	http.ListenAndServe(":8080", nil)
}
	