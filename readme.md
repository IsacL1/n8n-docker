# Access Ollalam from web #
http://ollama.localhost:8080/auth?redirect=%2F

# Access n8n #
https://n8n.localhost/

# pull modeal: Llama3.1 & Llama3.2 & Mistral #
`docker exec -it ollama ollama pull Llama3.1 && docker exec -it ollama ollama pull Llama3.2 && docker exec -it ollama ollama pull Mistral`

# Menual backup or Migrate Data
1. sudo docker compose down
2. cd ~/docker/n8n-docker
3. `tar czf [backup_name].tgz [backup_folder_name_1] [backup_folder_name_2] [backup_folder_name_n]`
4. Copy to new location
5. `tar xzf n8n_data_backup.tgz`
6. sudo docker compose up -d