# MySQL with Docker – Quickstart  
  
---  
  
## 🚀 Run MySQL Container  
```bash  
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:9  
```  
  
- `-d` = Run in detached mode  
- `-p 3306:3306` = Map host port to container port  
- `-e MYSQL_ROOT_PASSWORD=root` = Set root password  
- `mysql:9` = Use MySQL version 9 image  
  
---  
  
## 🧳 Access MySQL Container Shell  
```bash  
docker exec -it <container_id_or_name> bash  
```  
  
Example:  
```bash  
docker exec -it e2b bash  
```  
  
---  
  
## 💾 Login to MySQL from Inside Container  
```bash  
mysql -u root -proot  
```  
  
- `-u root` = Username  
- `-p` = Prompt for password (`root`)  
  
