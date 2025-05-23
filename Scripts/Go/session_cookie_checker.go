/*
===========================================================================================================================================================
 /$$      /$$           /$$                /$$$$$$                                          /$$   /$$                       /$$                 /$$      
| $$  /$ | $$          | $$               /$$__  $$                                        |__/  | $$                      | $$                | $$      
| $$ /$$$| $$  /$$$$$$ | $$$$$$$         | $$  \__/  /$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$  /$$ /$$$$$$   /$$   /$$        | $$        /$$$$$$ | $$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$__  $$ /$$$$$$|  $$$$$$  /$$__  $$ /$$_____/| $$  | $$ /$$__  $$| $$|_  $$_/  | $$  | $$ /$$$$$$| $$       |____  $$| $$__  $$
| $$$$_  $$$$| $$$$$$$$| $$  \ $$|______/ \____  $$| $$$$$$$$| $$      | $$  | $$| $$  \__/| $$  | $$    | $$  | $$|______/| $$        /$$$$$$$| $$  \ $$
| $$$/ \  $$$| $$_____/| $$  | $$         /$$  \ $$| $$_____/| $$      | $$  | $$| $$      | $$  | $$ /$$| $$  | $$        | $$       /$$__  $$| $$  | $$
| $$/   \  $$|  $$$$$$$| $$$$$$$/        |  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$      | $$  |  $$$$/|  $$$$$$$        | $$$$$$$$|  $$$$$$$| $$$$$$$/
|__/     \__/ \_______/|_______/          \______/  \_______/ \_______/ \______/ |__/      |__/   \___/   \____  $$        |________/ \_______/|_______/ 
                                                                                                          /$$  | $$                                      
                                                                                                         |  $$$$$$/                                                                                                                                            \______/                                       
===========================================================================================================================================================
===========================================================================================================================================================
 Script     : session_cookie_checker.go
 Auteur     : Lysius
 Date       : 01/07/2023
 Description: Programme Go pour vérifier les cookies de session.
===========================================================================================================================================================
*/

package main
import (
    "flag"
    "fmt"
    "net/http"
)

func main() {
    url := flag.String("url", "http://localhost", "URL à tester")
    flag.Parse()
    client := http.Client{}
    resp, err := client.Get(*url)
    if err != nil {
        fmt.Println("Erreur:", err)
        return
    }
    defer resp.Body.Close()
    cookies := resp.Cookies()
    for _, c := range cookies {
        secure := ""
        if c.Secure {
            secure = " (secure)"
        }
        fmt.Printf("Cookie %s: HttpOnly=%t%s
", c.Name, c.HttpOnly, secure)
    }
}