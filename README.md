# TradeSmartly Development Guide

## Overview

### Architecture

```mermaid
architecture-beta
    group ec2(cloud)[EC2]
    service db(database)[Relational Database] in ec2
    service in_mem_cache(database)[In Memory Cache] in ec2
    service api_server(server)[API Server] in ec2
    service frontend(server)[Static File Server] in ec2
    service reverse_proxy(server)[Reverse Proxy] in ec2
    service scheduler(server)[Scheduler] in ec2
    service internet(internet)[Internet]

    internet:B --> T:reverse_proxy
    reverse_proxy:R --> L:api_server
    reverse_proxy:L --> R:frontend
    api_server:R --> L:db
    api_server:B --> L:in_mem_cache
    scheduler:L --> R:db
    scheduler:B --> R:in_mem_cache
```

### Branches

```mermaid
%%{init: { 'theme': 'base', 'gitGraph': {'showBranches': false}} }%%
gitGraph
   commit
   commit
   branch feature/xxx
   switch feature/xxx
   commit
   commit
   switch main
   merge feature/xxx
   commit
   branch bug_fix/xxx
   switch bug_fix/xxx
   commit
   commit
   switch main
   merge bug_fix/xxx
   commit
```

### Tech Stack

- API Server
  - Programming Language: Python
  - Framework: Django
- Frontend
  - Programming Language: TypeScript
  - Framework: React
- Database: PostgreSQL
- Cache: Redis
- Reverse Proxy: Nginx
- Scheduler
  - Programming Language: Python

## Development

### Prerequisites

- Operating System: MacOS or Linux
- Git (>=2.34.0)
- GNU Make (>=3.81.0)
- Docker (>=27.4.0)
- Visual Studio Code (or any other editor that supports devcontainer)

### Setup

#### Step 0: Clone the repository

```bash
git clone git@github.com:bingyangchen/trade-smartly.git
cd trade-smartly
```

#### Step 1: Create .env file

```bash
cp example.env .env
```

Fill in the values for the environment variables.

#### Step 2: Build the images for development

```bash
make build-dev
```

#### Step 3: Install Git hooks

```bash
make install-git-hooks
```

This command will add some essential scripts into the .git/hooks/ directory.

#### Step 4: Generate SSL certificates and keys for development

```bash
make cert-dev
```

### Run the Development Server

```bash
make start
```

### Stop the Development Server

```bash
make stop
```

### The Development Workflow

- **Step 1:** Create a branch from `main`, naming it `feature/xxx` or `hot_fix/xxx`.
- **Step 2:** Complete your work, then commit and push your changes.
- **Step 3:** Open a pull request on GitHub and obtain approval for your PR.
- **Step 4:** Merge your branch into `main`.
- **Step 5:** Build new images for **production** from the latest `main` on your local machine.
- **Step 6:** Push the new images to Docker Hub.
- **Step 7:** SSH into the EC2 instance, pull the latest code and images.
- **Step 8:** Restart all Docker containers. You're done!

## Production

### Prerequisites

- Operating System: Linux (Ubuntu >=22.04)
- Domain name: trade-smartly.com
- Git (>=2.34.0)
- GNU Make (>=3.81.0)
- Docker (>=27.4.0)

### Setup

```bash
git clone git@github.com:bingyangchen/trade-smartly.git
cd ~/trade-smartly
cp example.env .env
# Update ~/trade-smartly/.env
make cert-prod
sudo usermod -aG docker $USER
newgrp docker
make pull-images-prod
sudo timedatectl set-timezone Asia/Taipei
make start

# Restore the database from the backup:
docker cp ~/db-backups/backup.sql trade-smartly-db-1:/backup.sql
make shell-db
    # In the db container:
    psql trade_smartly < /backup.sql
    exit
```
