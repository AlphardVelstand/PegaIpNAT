#Etapas
#carregar Streamlit
import streamlit as st
#Pagar IpNAT
# HTML e JavaScript para capturar o IP
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
         }
        .adsense {
            width: 100%;
            text-align: center;
            margin: 20px 0;
            border: 2px solid red; /* Borda branca */
            padding: 10px; /* Espaçamento interno */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Sombra leve */
        }
    </style>
    <script>
        async function obterIP() {
            try {
                const response = await fetch('https://api.ipify.org?format=json');
                const data = await response.json();
                document.getElementById('ip').innerText = `Seu IP NAT é: ${data.ip}`;
            } catch (error) {
                console.error('Erro ao obter IP:', error);
            }
        }
    </script>
</head>

<body onload="obterIP()">
    <h1>Bem-vindo ao nosso site!</h1>
    <p id="ip">Carregando seu IP...</p>

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

# Usar o componente HTML do Streamlit
st.components.v1.html(html_code, height=300)