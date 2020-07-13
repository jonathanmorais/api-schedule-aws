package main

import (
	"fmt"
	"log"
	"github.com/gorilla/mux"
	"github.com/jonathanmorais/api-schedule-aws/routes"

)
func init() {
	log.Println("Api Ready")
}

func main()  {
	r := mux.NewRouter()
	r.Handle("/", Home).Methods("GET")
	fmt.Print("hello")
}


