// Burada ileride kullanılmak üzere JavaScript kodlarınızı ekleyebilirsiniz
console.log("JavaScript file loaded successfully.");

var ctx = document.getElementById('portal-activity-chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['28/07', '31/07', '03/08', '06/08', '09/08', '12/08', '15/08', '18/08', '21/08', '24/08', '27/08'],
        datasets: [
            {
                label: 'Logins',
                data: [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            },
            {
                label: 'Course completions',
                data: [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }
        ]
    }
});

var ctx2 = document.getElementById('courses-progress-chart').getContext('2d');
var myDoughnutChart = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Completed', 'In progress', 'Not started', 'Not passed'],
        datasets: [{
            data: [100, 0, 0, 0],
            backgroundColor: ['#4CAF50', '#FF9800', '#DDDDDD', '#F44336'],
            hoverBackgroundColor: ['#388E3C', '#F57C00', '#CCCCCC', '#D32F2F']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});
