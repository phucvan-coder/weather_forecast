myArr = []
myLabels = []

function addElement(x) {
    myArr.push(x);
}

function show() {
    for (let i = 0; i < myArr.length; i++) {
        if (i < 12) {
            myLabels.push(i + " am");
        } else {
            myLabels.push(i + " pm");
        }
    }
}

// Pareto chart
function Pareto_Chart() {
    const ctx = document.getElementById('Pareto_Chart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            //labels: ['1 star', '2 star', '3 star', '4 star', '5 star']
            labels: myLabels,
            datasets: [{
                label: 'Bar',
                //data: [33543, 24847, 34222, 76592, 40796],
                data: myArr,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    //'rgba(255, 206, 86, 0.2)',
                    'rgba(254, 255, 31, 1)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
            }, {
                label: 'Line',
                data: myArr,
                backgroundColor: 'rgba(255, 26, 104, 0.2)',
                borderColor: 'rgba(255, 26, 104, 1)',
                type: 'line'
            }],
        },
        options: {
            title: {
                display: true,
                text: "Degree for hour",
                fontSize: 28
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        // Include a dollar sign in the ticks
                        callback: function (value, index, values) {
                            return value + "°C";
                        }
                    }
                }
            }
        }
    });
}

// bar chart
function showBarChart() {
    const ctx = document.getElementById('canvas').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            //labels: ['1 star', '2 star', '3 star', '4 star', '5 star'],
            labels: myLabels,
            datasets: [{
                label: 'Hide',
                //data: [33543, 24847, 34222, 76592, 40796],
                data: myArr,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    //'rgba(255, 206, 86, 0.2)',
                    'rgba(254, 255, 31, 1)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text: "Degree for hour",
                fontSize: 28
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        // Include a dollar sign in the ticks
                        callback: function (value, index, values) {
                            return value + "°C";
                        }
                    }
                }
            }
        }
    });
}

// Line chart
function showLineChart() {
    let myChart = document.getElementById('LineChart').getContext('2d');
    let masspopCHart = new Chart(myChart, {
        type: 'line',
        data: {
            labels: myLabels,
            datasets: [{
                label: 'Hide',
                data: myArr,
                fill: true,
                lineTension: 0.5,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    // 'rgba(255, 206, 86, 0.2)',
                    'rgba(254, 255, 31, 1)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                ],
                borderWidth: 4,
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
            }]
        },
        options: {
            title: {
                display: true,
                // text: "rating in pie chart",
                fontSize: 18
            },
            scales: {
                x: {},
                y: {
                    ticks: {
                        // Include a dollar sign in the ticks
                        callback: function (value, index, values) {
                            return value + "°C";
                        }
                    }
                }
            }
        }
    });
}

// pie chart
function showPieChart() {
    let myChart = document.getElementById('Piechart').getContext('2d');
    let masspopCHart = new Chart(myChart, {
        type: 'pie',
        data: {
            labels: myArr,
            datasets: [{
                label: 'Star',
                data: myArr,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    // 'rgba(255, 206, 86, 0.2)',
                    'rgba(254, 255, 31, 1)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderWidth: 4,
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
            }]
        },
        options: {
            title: {
                display: true,
                // text: "rating in pie chart",
                fontSize: 18
            }
        }
    });
}

// reverse line chart
function showLineChart_reverse() {
    let myChart = document.getElementById('Linechart_2').getContext('2d');
    let masspopCHart = new Chart(myChart, {
        type: 'line',
        data: {
            labels: myLabels,
            datasets: [{
                label: 'Hide',
                data: myArr,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    // 'rgba(255, 206, 86, 0.2)',
                    'rgba(254, 255, 31, 1)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                ],
                borderWidth: 4,
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
            }]
        },
        options: {
            indexAxis: 'y',
            scales: {
                x: {
                    ticks: {
                        // Include a dollar sign in the ticks
                        callback: function (value, index, values) {
                            return value + "°C";
                        }
                    },
                },
            },
        }
    });
}

function showBarChart_vertical() {
    const ctx = document.getElementById('canvas_2').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            //labels: ['1 star', '2 star', '3 star', '4 star', '5 star'],
            labels: myLabels,
            datasets: [{
                label: 'Hide',
                //data: [33543, 24847, 34222, 76592, 40796],
                data: myArr,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    //'rgba(255, 206, 86, 0.2)',
                    'rgba(254, 255, 31, 1)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            title: {
                display: true,
                text: "Degree for hour",
                fontSize: 28
            },
            scales: {
                x: {
                    ticks: {
                        // Include a dollar sign in the ticks
                        callback: function (value, index, values) {
                            return value + "°C";
                        }
                    }
                }
            }
        }
    });
}

function showAll() {
    showBarChart();
    showLineChart()
    // showPieChart();
    showLineChart_reverse();
    showBarChart_vertical();
    Pareto_Chart();
}

var check = new Array(100).fill(0);
var c = [];
var d = [];
var e = [];
var h_25 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
exportToCsv = function () {
    d = []
    e = []
    for (let i = 0; i < myArr.length; ++i) {
        myArr[i] += "°C";
        if (i < 12) {
            d.push(h_25[i] + " am");
            e.push("\ " + i + " AM");
        } else {
            d.push(h_25[i] + " pm");
            e.push("\ " + i + " PM");
        }
    }
    var Results = [
        // ["Col1", "Col2", "Col3", "Col4"],
        // ["Data", 50, 100, 500],
        // ["Data", -100, 20, 100],
        // myLabels,
        d,
        e,
        myArr,
    ];
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    today = dd + '/' + mm + '/' + yyyy;
    var CsvString = "";
    CsvString += "Data result of " + today + "\n";
    Results.forEach(function (RowItem, RowIndex) {
        RowItem.forEach(function (ColItem, ColIndex) {
            CsvString += ColItem + ',';
        });
        CsvString += "\r\n";
    });
    CsvString = "data:application/csv;charset=utf-8,%EF%BB%BF" + encodeURIComponent(CsvString);
    var x = document.createElement("A");
    x.setAttribute("href", CsvString);
    x.setAttribute("download", "data_" + today + ".csv");
    document.body.appendChild(x);
    x.click();
}

function PDFexport(id, title) {
    const canvas = document.getElementById(id);
    const img = canvas.toDataURL('img/jpeg', 1.0);
    console.log(img);
    let pdf = new jsPDF();
    pdf.setFontSize(20);
    pdf.addImage(img, 'JPEG', 5, 5, 200, 180);
    pdf.text(15, 15, title);
    pdf.save(title + '.pdf');
}

// function PDFexport() {
//     // return renderPDF('canvas', 'Bar chart');
//     // for (let i = 0; i < pdfId.length; ++i)
//     //     renderPDF(pdfId[i], pdfTitle[i]);
//     return renderPDF()
// }

function PDF_AllChart() {
    var reportPageHeight = 3500;
    var reportPageWidth = 4096;

    // create a new canvas object that we will populate with all other canvas objects
    var pdfCanvas = $('<canvas />').attr({
        id: "canvaspdf",
        width: reportPageWidth,
        height: reportPageHeight
    });

    // keep track canvas position
    var pdfctx = $(pdfCanvas)[0].getContext('2d');
    var pdfctxX = 0;
    var pdfctxY = 0;
    var buffer = 100;

    // for each chart.js chart
    $("canvas").each(function (index) {
        // get the chart height/width
        var canvasHeight = 1080;
        var canvasWidth = 1920;

        // draw the chart into the new canvas
        pdfctx.drawImage($(this)[0], pdfctxX, pdfctxY, canvasWidth, canvasHeight);
        pdfctxX += canvasWidth + buffer;

        // our report page is in a grid pattern so replicate that in the new canvas
        if (index & 1) {
            pdfctxX = 0;
            pdfctxY += canvasHeight + buffer;
        }
    });

    // create new pdf and add our new canvas as an image
    var pdf = new jsPDF('l', 'pt', [reportPageWidth, reportPageHeight]);
    pdf.addImage($(pdfCanvas)[0], 'PNG', 0, 0);

    // download the pdf
    pdf.save('allchart.pdf');
}
// Line chart
var performLabel = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
var performArr = [100, 75, 95, 77, 85, 60, 76, 61, 95, 80, 115, 130]
function showPerform() {
    let myChart = document.getElementById('Perform').getContext('2d');
    let masspopCHart = new Chart(myChart, {
        type: 'line',
        data: {
            labels: performLabel,
            datasets: [{
                label: 'Hide',
                data: performArr,
                fill: true,
                lineTension: 0.5,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    // 'rgba(255, 206, 86, 0.2)',
                    'rgba(254, 255, 31, 1)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                ],
                borderWidth: 4,
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
            }]
        },
        options: {
            title: {
                display: true,
                // text: "rating in pie chart",
                fontSize: 18
            },
            scales: {
                x: {},
                y: {
                    ticks: {
                        // Include a dollar sign in the ticks
                        callback: function (value, index, values) {
                            return value;
                        }
                    }
                }
            }
        }
    });
}