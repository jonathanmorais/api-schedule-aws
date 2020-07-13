package main

import (
	"github.com/gorilla/mux"
	"github.com/jonathanmorais/api-schedule-aws/routes"
	"log"
	"net/http"
)
func init() {
	log.Println("Api Ready")
}

func main()  {
	route := mux.NewRouter()
	route.HandleFunc("/", routes.Home).Methods("GET")
	route.HandleFunc("/api/scheduler", routes.GetSchedule).Methods("POST")
	http.Handle("/", route)
	log.Fatal(http.ListenAndServe(":8030", route))
}