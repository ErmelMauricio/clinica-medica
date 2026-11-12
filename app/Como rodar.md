Execute os comandos abaixo no terminal, dentro da pasta `app`.

1. Iniciar o MongoDB (é necessário ter o Docker instalado):
   ```
   docker compose up -d
   ```

2. Copiar e executar os dados de exemplo no MongoDB:
   ```
   docker cp .\banco.js agenda-mongo-demo:/tmp/banco.js
   docker exec agenda-mongo-demo mongosh --file /tmp/banco.js
   ```
   O script cria as coleções necessárias e pode ser executado novamente sem duplicar os dados de exemplo.

3. Instalar o PyMongo (é necessário ter o Python instalado):
   ```
   pip install pymongo
   ```

4. Iniciar o servidor:
   ```
   python servidor.py
   ```

