===============================
🖐 POKÉGESTURESEC – SEGURANÇA COM GESTOS
===============================

📌 DESCRIÇÃO  
O PokéGestureSec é uma solução de reconhecimento de gestos desenvolvida com **Python + MediaPipe**, voltada para **situações de falta de energia elétrica**, onde a comunicação visual e sonora pode salvar vidas.  
Ele permite que pessoas em ambientes escuros emitam **comandos por gestos**, ativando respostas de voz automatizadas. Ideal para uso em **hospitais, residências, centros de comando** e outros locais críticos.

---

🛠️ TECNOLOGIAS UTILIZADAS

- Python 3.x  
- OpenCV (processamento de vídeo)  
- MediaPipe Hands (reconhecimento de mão)  
- Pyttsx3 (áudio offline via TTS)  
- Logging interno para depuração

---

📱 FUNCIONALIDADES

🔍 Reconhecimento de Gestos  
- Dedo indicador levantado → **"AJUDA"**  
- Dois dedos levantados → **"PAZ"**  
- Nenhum dedo → **"PUNHO" (sem ação específica)**

🔊 Ações Automatizadas  
- Resposta por voz (Text-To-Speech)  
- Geração de logs dos eventos  
- Permite acionar respostas específicas com segurança, mesmo no escuro

🎛️ Comportamento Seguro  
- Filtro contra repetição excessiva (anti-flood com intervalo de 2 segundos)  
- Modular e fácil de expandir com novos gestos  
- Código comentado e pronto para integração com sistemas maiores

---

📂 ESTRUTURA DO PROJETO

```
pokegesturesec/
├── main.advanced.py          → Código principal da aplicação
├── README.me               → Este arquivo com informações detalhadas
├── requirements.txt         → Lista de dependências Python
├── diagrama_funcionamento.png → Imagem explicativa do fluxo do sistema
├── simulacao_interface.png    → Imagem exemplo de execução
├── pokegesturesec.log       → Log dos gestos detectados (gerado em tempo de execução)
```

---

▶️ COMO EXECUTAR

### 1. Clone o repositório

```bash
git clone https://github.com/efsartorelli/fiap-gs1-iotiob
cd pokegesturesec
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o aplicativo

```bash
python main_advanced.py
```

- O app abrirá a câmera e exibirá os gestos reconhecidos na tela.
- Pressione `ESC` para encerrar.

---

🧪 TESTES E SIMULAÇÕES

- Ambientes escuros simulados com baixa luz
- Testes com webcam do notebook
- Detecção estável mesmo com iluminação precária
- Voz sintetizada confirmando gestos reconhecidos

---

🎥 DEMONSTRAÇÃO EM VÍDEO

- Link do vídeo no YouTube: https://youtu.be/mUxOwwzbuGI

---

👥 AUTORES

- **Eduardo Nistal** — RM94524 
- **Enzo Vazquez Sartorelli** — RM94618  

Turma: **FIAP - Engenharia de Software 2025**

---

📚 NOTAS FINAIS

- Projeto acadêmico desenvolvido para desafios de cibersegurança em apagões
- Código modular, adaptável para inclusão de novas ações e integração com APIs
- 100% funcional em ambientes offline
- Sem necessidade de sensores externos

🗓️ Última atualização: 03/06/2025
