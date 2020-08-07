
<canvas id="chart6"></canvas>
<script>
    var ctx = document.getElementById("chart6");
    var lineProgress = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["2015", "2016", "2017", "2018", "2019"],
        datasets: [{
        label: "Black",
        fill: false,
        lineTension: false,
        backgroundColor: "red",
        borderColor: "red",
        pointRadius: 5,
        pointBackgroundColor: "red",
        pointBorderColor: "red",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "red",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: [56.2, 55.8, 58.2, 58.1, 59.0],
        },

        {
        label: "Asian",
        fill: false,
        lineTension: false,
        backgroundColor: "green",
        borderColor: "green",
        pointRadius: 5,
        pointBackgroundColor: "green",
        pointBorderColor: "green",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "green",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: [68.8, 68.6, 69.0, 69.9, 71.7],
        },

        {
        label: "Hispanic",
        fill: false,
        lineTension: false,
        backgroundColor: "purple",
        borderColor: "purple",
        pointRadius: 5,
        pointBackgroundColor: "purple",
        pointBorderColor: "purple",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "purple",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: [57.9, 57.3, 59.7, 59.6, 61.4],
        },

        {
        label: "White",
        fill: false,
        lineTension: false,
        backgroundColor: "blue",
        borderColor: "blue",
        pointRadius: 5,
        pointBackgroundColor: "blue",
        pointBorderColor: "blue",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "blue",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: [67.0, 66.9, 67.7, 69.5, 70.5],
        }],
    },
    options: {
        title: {
        display: true,
        text: 'Average Score by Race, Common Core Geometry'
        },
        scales: {
        xAxes: [{
            time: {
            unit: 'date'
            },
            gridLines: {
            display: false
            },
            ticks: {
            maxTicksLimit: 7
            }
        }],
        yAxes: [{
            ticks: {
            min: 55,
            max: 80,
            maxTicksLimit: 5
            },
            gridLines: {
            color: "rgba(0, 0, 0, .125)",
            }
        }],
        },
        legend: {
        display: false
        }
    }
    });
</script>