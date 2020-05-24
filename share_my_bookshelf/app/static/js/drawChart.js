const drawPieChart = () => {
  const ctx = document.getElementById("bookChart");
  const data = JSON.parse(String(document.getElementById("chartData").value));
  const labels = Object.keys(data);
  const count = Object.values(data);
  new Chart(ctx, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
            data: count,
        }]
      },
      options: {
        plugins: {
          colorschemes: {
            scheme: 'brewer.SetThree12'
          }
        },
      }
    }
  );
};

drawPieChart();
