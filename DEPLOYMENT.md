# Deployment Guide

## System Requirements

### Minimum Requirements
- Ubuntu 20.04 LTS or 22.04 LTS
- 8 GB RAM (16 GB recommended)
- 4 CPU cores
- 100 GB SSD
- Domain name with configured DNS

### Software
- Docker 20.10+
- Docker Compose v2.0+
- Python 3.8+
- Ansible 4.0+
- Git

## Quick Deployment

### 1. Server Preparation

```bash
# System update
sudo apt update && sudo apt upgrade -y

# Dependencies installation
sudo apt install -y git python3 python3-pip

# Project cloning
git clone https://github.com/YOUR_USERNAME/openedx-custom-platform.git
cd openedx-custom-platform
```

### 2. Variable Configuration

```bash
# Copy configuration templates
cp ansible-deployment/group_vars/production.yml.example ansible-deployment/group_vars/production.yml
cp ansible-deployment/inventories/production.example ansible-deployment/inventories/production

# Edit for your settings
nano ansible-deployment/group_vars/production.yml
nano ansible-deployment/inventories/production
```

### 3. Deployment

```bash
# Navigate to Ansible directory
cd ansible-deployment

# Configuration check
ansible-playbook --syntax-check playbooks/deploy-openedx.yml

# Deployment
ansible-playbook playbooks/deploy-openedx.yml -i inventories/production
```

## Deployment Verification

After successful deployment, check:

1. **Service availability:**
   ```bash
   curl -I https://your-domain.com
   curl -I https://studio.your-domain.com
   ```

2. **Docker container status:**
   ```bash
   docker ps
   ```

3. **Application logs:**
   ```bash
   tutor local logs -f
   ```

## Troubleshooting

### SSL Certificate Issues
```bash
# Certificate status check
tutor local logs caddy

# Manual certificate update
tutor local restart caddy
```

### Database Issues
```bash
# MySQL status check
tutor local logs mysql

# Restore from backup
tutor local restore mysql backup.sql
```

### MFE Issues
```bash
# Rebuild MFE images
tutor images build mfe

# Check MFE logs
tutor local logs mfe
```
