import streamlit as st
import streamlit.components.v1 as components

# HTML e JavaScript para capturar o IP e adicionar o botão de atualizar
html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
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
        .adsense {
            width: 100%;
            text-align: center;
            margin: 20px 0;
            border: 2px solid red;
            padding: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        #ip {
            font-size: 20px;
            margin-top: 20px;
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
    </style>
    <script>
        let ipAtual = "";

        async function obterIP() {
            try {
                const response = await fetch('https://api.ipify.org?format=json');
                const data = await response.json();
                ipAtual = data.ip;
                document.getElementById('ip').innerText = `Seu IP NAT é: ${ipAtual}`;
            } catch (error) {
                console.error('Erro ao obter IP:', error);
            }
        }

        function atualizarIP() {
            obterIP();  // Chama a função para atualizar o IP
        }
    </script>
</head>

<body onload="obterIP()">
    <h1>Bem-vindo ao nosso site!</h1>
    <p id="ip">Carregando seu IP...</p>

    <!-- Botão de atualização do IP -->
    <button id="btn-atualizar" onclick="atualizarIP()">Atualizar IP</button>

    <div class="adsense">
        <!-- Insira o código do seu AdSense aqui -->
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
        <!-- Insira o código do seu AdSense aqui novamente para a lateral ou outro lugar -->
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
            <!-- Insira o código do AdSense para o rodapé -->
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
</body>
</html>
"""

# Usar o componente HTML do Streamlit para exibir o HTML e o JS
components.html(html_code, height=1600)

# Se você preferir um botão que interaja diretamente com o backend Python do Streamlit, use:
# if st.button('Atualizar IP'):
#     st.write('Atualizando IP...')
