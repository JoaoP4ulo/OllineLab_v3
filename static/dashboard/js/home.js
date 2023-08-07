function valor_temp(url) {
    fetch(url, {
        method: 'get',       
    }).then(function(result) {
        return result.json();
    }).then(function(data){
        document.getElementById("temp_atual").innerHTML = data.temp_atual;
    });
}

let myChart; // Declaramos a variável do gráfico fora da função para que ela seja acessível em diferentes chamadas da função
let intervalId; // Armazenar o ID do intervalo para poder limpar

function renderizar_temperatura(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        if (!myChart) {
            const ctx = document.getElementById('temp_grafic').getContext("2d");

            myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['','','','','','','','','',''],
                    datasets: [{
                        label: 'Temperatura',
                        data: data.temperatura,
                        backgroundColor: "#02152E",
                        borderColor: "FFFFFF",
                        borderWidth: 0.2
                    }]
                },
            });

            // Iniciar o intervalo para atualizar a cada 10 segundos
            intervalId = setInterval(function() {
                atualizar_temperatura(url);
            }, 1000); // 10000 milissegundos = 10 segundos
        } else {
            myChart.data.datasets[0].data = data.temperatura;
            myChart.update(); // Atualiza o gráfico com os novos dados
        }
    });
}

// Função para atualizar os dados do gráfico a cada 10 segundos
function atualizar_temperatura(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        myChart.data.datasets[0].data = data.temperatura;
        myChart.update(); // Atualiza o gráfico com os novos dados
    });
}


