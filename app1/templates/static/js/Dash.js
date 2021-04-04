var xmlhttp = new XMLHttpRequest();
var url = "http://127.0.0.1:8000/api/data/?format=json";
xmlhttp.open("GET", url, true);
xmlhttp.send();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var data = JSON.parse(this.responseText);
        // console.log(data);
        var month = data.Temp_Data.map(function(elem) {
            return elem.date;
        });
        var High = data.Temp_Data.map(function(elem) {
            return elem.High;
        });
        var Low = data.Temp_Data.map(function(elem) {
            return elem.Low;
        });

        var ctx = document.getElementById('linechart').getContext('2d');
        var linechart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: month,
                datasets: [{
                        data: High,
                        label: '# High',
                        borderColor: "#3767ed",
                        fill: false
                    },
                    {
                        data: Low,
                        label: '# Low',
                        borderColor: "#4ed973",
                        fill: false
                    }
                    //   , { 
                    //     data: ?????????,
                    //     label: "???",
                    //     borderColor: "#3cba9f",
                    //     fill: false
                    //   }
                    //   , { 
                    //     data: ???????????,
                    //     label: "????",
                    //     borderColor: "#e8c3b9",
                    //     fill: false
                    //   }
                    //   , { 
                    //     data: ??????,
                    //     label: "?????",
                    //     borderColor: "#c45850",
                    //     fill: false
                    //     }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }
}