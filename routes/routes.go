package routes

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
)

type Info struct {
	Image string `json:"image"`
	Time  string `json:"time"`
}

func Home(w http.ResponseWriter, r *http.Request ){
     w.WriteHeader(http.StatusOK)
}

func GetSchedule(w http.ResponseWriter, r *http.Request) {
	b, error := ioutil.ReadAll(r.Body)
	defer r.Body.Close()
	if error != nil {
		http.Error(w, error.Error(), 500)
		return
	}

	var info Info
	err := json.Unmarshal(b, &info)
	if err != nil {
		log.Fatal(err)
	}

	output, err := json.Marshal(info)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	w.Header().Set("content-type", "application/json")
	w.Write(output)

	http.Redirect(w, r, "/", 301)
}
