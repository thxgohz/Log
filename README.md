# Gerador Automático de Logs  

Este projeto tem como objetivo padronizar a geração de logs para aplicações de execução constante e intensiva. Ele organiza os logs em um diretório chamado `logs`, separado por ano e mês. Cada arquivo de log inclui um banner ASCII personalizado, a assinatura do autor e a data no nome do arquivo.  

## Uso  

Para iniciar a captura de logs, basta chamar a assinatura e configurar o logger:  

```python
Assinatura()
logger = logging.getLogger(__name__)
```  

### Registrando mensagens  

Para inserir mensagens no log, utilize os seguintes métodos:  

```python
logger.info("Mensagem informativa")
logger.warning("Aviso importante")
logger.error("Erro detectado")
```  

### Estrutura da Log  

Cada log gerado contém um banner ASCII e a assinatura do autor, como no exemplo abaixo:  

```
 _     _                              _           
| |_  | |__   __  __   __ _    ___   | |__    ____  
| __| | '_ \  \ \/ /  / _` |  / _ \  | '_ \  |_  /  
| |_  | | | |  >  <  | (_| | | (_) | | | | |  / /   
 \__| |_| |_| /_/\_\  \__, |  \___/  |_| |_| /___|  
                       |___/                        
Autor: Thiago Inacio  
```

## Configuração do Caminho dos Logs  

O local onde os logs serão salvos é definido no arquivo `local_settings`:  

```python
log_path = "C:\\Projects\\My\\Log\\logs"
```  

Por padrão, os logs serão armazenados dentro do diretório `logs`, organizado por ano e mês automaticamente. 🚀
