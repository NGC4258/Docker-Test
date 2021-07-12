# Nexio Test
應用 Python Flask RESTful API 連接 SQLite 實現 User 的 CRUD 操作，並使用 Nginx 當 Web service 串接 Flask 部署在 Docker 上, 此範例在 Windows 開發

![Structure](/img/structure.jpg)

### Installation
1. Install Windows Docker
```
1. Download Windows WSL from https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
2. Download Windows Docker from https://docs.docker.com/docker-for-windows/install/
3. Install above downloaded installer
```
2. Start Docker container
```
1. Change folder to location with "docker-compose.yml"
2. docker-compose up
```

### Usage
1. Create user
```
curl -H 'Content-Type: application/json' -X POST -d '{"email":"test1@test.com","job_title":"SRE","mobile":"0912345678"}' -k https://127.0.0.1/user/test1
```

2. Update user
```
curl -H 'Content-Type: application/json' -X PATCH -d '{"mobile":"0987654321"}' -k https://127.0.0.1/user/test1
```

3. Delete User
```
curl -X DELETE -k https://127.0.0.1/user/test1
```

4. Get user
```
curl -X GET -k https://127.0.0.1/user/test1
```
