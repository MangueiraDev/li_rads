Planejamento de Desenvolvimento

Objetivo Geral:
-	Integrar CNNs e LI-RADS para diagnóstico do carcinoma hepatocelular (CHC).

Objetivos Específicos:
-	Processar e analisar imagens de RM e TC.
-	Desenvolver e treinar modelos de CNN.
-	Validar o modelo com bancos de dados públicos e independentes.
-	Integrar os resultados do LI-RADS ao modelo CNN.


Linguagem:
-	Python
-	Bibliotecas: TensorFlow, PyTorch, OpenCV e NumPy.


Ambiente de desenvolvimento: VS Code
-	Extensões úteis: Python; Pylance; Jupyter; GitLens
-	Utilizar Git para versionamento e um repositório central como GitHub
-	Criar venv
-	…


Fluxo de trabalho:
1.	Coleta e Organização dos Dados:
-	Identificação e download do banco de dados
-	Organização dos dados: 
o	Pastas organizadas para categorias como benigno, maligno e normal

2.	Pré-processamento Inicial
-	Garantir que os dados brutos estejam prontos para a segmentação e treinamento:
Usar código Python no pré-processamento
Normalização:
Ajustar valores de intensidade dos pixels para um intervalo fixo (como [0, 1] ou [-1, 1]);
o	Usar código Python no pré-processamento
o	Redimensionamento
o	Remoção de Artefatos
o	Filtragem de imagens não relevantes
3.	Segmentação

