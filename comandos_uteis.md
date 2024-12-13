### **Resumo de Uso do `nohup` e Monitoramento**

#### **1. Executar com `nohup`**
Use o comando abaixo para rodar um script Python em segundo plano e redirecionar a saída para um arquivo:
```bash
nohup python script.py > output.log 2>&1 &
```
- **`output.log`**: Arquivo onde a saída será salva.
- **`2>&1`**: Inclui mensagens de erro no mesmo arquivo.
- **`&`**: Roda o script em segundo plano.

---

#### **2. Monitorar o arquivo de saída**
Para acompanhar o progresso em tempo real:
```bash
tail -f output.log
```
- Pressione `Ctrl+C` para sair do monitoramento.

---

#### **3. Verificar se está rodando**
Para verificar se o script ainda está em execução:
```bash
ps aux | grep script.py
```
- Procure o **PID** na saída para identificar o processo.

---

#### **4. Verificar detalhes do processo**
Para checar informações do processo, como **PID**, **comando**, **uso de CPU** e **uso de memória**:
```bash
ps -p <PID> -o pid,cmd,%cpu,%mem
```

---

#### **5. Acompanhar o processo**
Use o comando `top` para visualizar processos ativos em tempo real:
```bash
top
```
- Localize o script pelo nome ou PID.
- Pressione `q` para sair.

---

#### **6. Interromper o processo**
Para encerrar o script em execução, use o comando abaixo com o **PID** identificado:
```bash
kill <PID>
```
Se o processo não parar, force a interrupção:
```bash
kill -9 <PID>
``` 

--- 

### **Comandos Resumidos**
1. **Executar**:  
   `nohup python script.py > output.log 2>&1 &`
2. **Monitorar saída**:  
   `tail -f output.log`
3. **Verificar execução**:  
   `ps aux | grep script.py`
4. **Detalhes do processo**:  
   `ps -p <PID> -o pid,cmd,%cpu,%mem`
5. **Acompanhar em tempo real**:  
   `top`
6. **Interromper**:  
   `kill <PID>` ou `kill -9 <PID>`