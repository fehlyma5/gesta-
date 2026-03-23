# GESTA+ 🚀

> **Plataforma Inteligente de Capacitação e Gestão de Pessoas Personalizada para PMEs de Roraima.**

O **GESTA+** é uma plataforma digital híbrida (SaaS) que integra diagnóstico organizacional, trilhas de aprendizagem personalizadas e ferramentas de gestão de pessoas em um único ambiente. O projeto foi desenhado especificamente para atender às necessidades das pequenas e médias empresas do estado de Roraima, integrando fluxos de trabalho e equipes multiculturais.

---

## 💡 Sobre a Solução

A plataforma resolve um problema estrutural do mercado regional: a falta de ferramentas de RH acessíveis e adaptadas à realidade local. O GESTA+ atua unindo três pilares fundamentais:

1. **Módulo 1: Diagnóstico Organizacional** 📊
   - Mapeamento de cultura organizacional e avaliação de competências.
   - Geração automática do Índice de Maturidade Organizacional (IMO).

2. **Módulo 2: Trilhas de Aprendizagem Personalizadas** 📚
   - Geração automática de treinamentos baseados nos GAPs de competências.
   - Suporte a múltiplos formatos (vídeos, textos e exercícios práticos) e biblioteca interna personalizável.

3. **Módulo 3: Gestão de Pessoas e Desempenho** 📈
   - Painel de indicadores de RH em tempo real.
   - Avaliação de desempenho integrada e Feedback 360°.

---

## 🛠️ Detalhes Técnicos e Stack Utilizada

O projeto utiliza uma arquitetura moderna dividida entre web e mobile:

* **Back-end:** Python 🐍 & Django Framework
* **Front-end:** HTML5, CSS3, JavaScript & React
* **Banco de Dados:** SQLite (Desenvolvimento/Padrão)
* **Versionamento & Repositório:** Git & GitHub

---

## ⚙️ Como Instalar e Rodar o Projeto Localmente

Siga o passo a passo abaixo para clonar o repositório e executar a plataforma na sua máquina.

### 📋 Pré-requisitos
Você precisará ter instalado em sua máquina:
- Python 3.x
- Git

### 🔧 Instalação

1. Clone o repositório para a sua máquina:
```bash
git clone [https://github.com/fehlyma5/gesta-.git](https://github.com/fehlyma5/gesta-.git)
cd zeronoventaecinco

2. Crie e ative o ambiente virtual VENV
# No Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# No Windows
python -m venv .venv
.venv\Scripts\activate

3. Instale as dependencias listadas no projeto
pip install -r requirements.txt

4. Execute o banco de dados (se houver)
python manage.py migrate

5. Inicie o servidor de desenvolvimento do Django
python manage.py runserver
caso tudo dê certo, aparecerá uns números algo como 128.0.0.1:8000 (é só um exemplo) clique em cima.

👥 Equipe Executora
Uma equipe multidisciplinar unindo tecnologia, finanças e gestão de pessoas:

Candice Diniz - CEO & Coordenadora (Estratégia e RH)

Diandro Felipe Nogueira Lima - CTO (Desenvolvimento Tecnológico)

Anelissa Roberta Gadelha Palmeira - CFO (Gestão Financeira e Contábil)

Victor Diniz Cunha - COO (Operações e Relacionamento)

📜 Licença
Este projeto está licenciado sob a Licença Apache 2.0. Consulte o arquivo LICENÇApara obter mais detalhes.

Projeto submetido e desenvolvido no âmbito do Programa Centelha Roraima.
