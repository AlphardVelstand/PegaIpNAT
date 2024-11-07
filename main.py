<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Captura de IP</title>
    <style>
        body {
            background-color: white;
            color: black;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        
        #ip {
            font-size: 20px;
            margin-top: 20px;
            font-weight: bold;
        }

        #btn-atualizar {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
        }

        #btn-atualizar:hover {
            background-color: #0056b3;
        }

        .adsense {
            width: 100%;
            text-align: center;
            margin: 20px 0;
            border: 2px solid red;
            padding: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

    <h1>Bem-vindo ao nosso site!</h1>

    <!-- Área onde o IP será exibido -->
    <p id="ip">Carregando seu IP...</p>

    <!-- Botão para atualizar o IP -->
    <button id="btn-atualizar" onclick="atualizarIP()">Atualizar IP</button>

    <div class="adsense">
        <!-- Exemplo de código de AdSense -->
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-xxxxxxxxxx"
             data-ad-slot="xxxxxxxxxx"
             data-ad-format="auto"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>

    <div class="adsense">
        <!-- Exemplo de código de AdSense para outra posição -->
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-xxxxxxxxxx"
             data-ad-slot="xxxxxxxxxx"
             data-ad-format="auto"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>

    <footer class="adsense">
        <div>
            <!-- Exemplo de código de AdSense para o rodapé -->
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-xxxxxxxxxx"
                 data-ad-slot="xxxxxxxxxx"
                 data-ad-format="auto"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
        </div>
    </footer>

    <script>
        // Função para obter o IP
        async function obterIP() {
            try {
                const response = await fetch('https://api.ipify.org?format=json');
                const data = await response.json();
                document.getElementById('ip').innerText = `Seu IP NAT é: ${data.ip}`;
            } catch (error) {
                console.error('Erro ao obter IP:', error);
                document.getElementById('ip').innerText = 'Não foi possível obter o IP.';
            }
        }

        // Função para atualizar o IP
        function atualizarIP() {
            obterIP(); // Chama a função para atualizar o IP
        }

        // Carregar o IP assim que a página for carregada
        window.onload = obterIP;
    </script>

</body>
</html>
