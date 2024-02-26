var titles = [];
var xyvals = [];

function fetchJSONData() {
    fetch("./database.json")
        .then((res) => {
            if (!res.ok) {
                throw new Error
                    (`HTTP error! Status: ${res.status}`);
            }
            return res.json();
        })
        .then((data) => {
            Object.keys(data).forEach((key) => {
                const title = key;
                const value = data[key];
                xyvals.push(value);
                titles.push(title);
            });
              })
            
        .catch((error) => 
            console.error("Unable to fetch data:", error));
        
        console.log("Titles:", titles)
        console.log("Values:", xyvals)
        
    }
    fetchJSONData();



