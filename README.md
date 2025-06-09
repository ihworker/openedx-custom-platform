# Custom Open edX Platform with Tutor and Ansible

This project represents a custom implementation of the Open edX platform using Tutor, a custom MFE for authentication, and automated deployment through Ansible.

## Solution Architecture

### Components

1. **Tutor** - main tool for Open edX management
2. **Custom MFE Authn** - customized microfrontend for authentication
3. **Ansible Playbook** - deployment and management automation
4. **Docker** - containerization of all components

### Project Structure

```
openedx-project/
├── ansible-deployment/         # Ansible automation for deployment
│   ├── ansible.cfg            # Ansible configuration
│   ├── group_vars/           # Variables for server groups
│   ├── inventories/          # Server inventory definitions
│   ├── playbooks/            # Main deployment playbooks
│   ├── roles/                # Reusable Ansible roles
│   └── templates/            # Configuration file templates
├── frontend-app-authn/         # Custom MFE authentication fork
│   ├── src/                  # Source code directory
│   ├── public/               # Static assets
│   ├── package.json          # NPM configuration
│   └── webpack.prod.config.js # Production build config
├── tutor-data/                # Tutor working directory
│   ├── config.yml            # Main Tutor configuration
│   ├── plugins/              # Custom plugins
│   └── patches/              # Custom modifications
└── README.md                  # Project documentation
```

## Key Decisions and Trade-offs

### 1. Choosing Tutor as the main deployment platform

**Decision:** Using Tutor instead of native Open edX installation

**Advantages:**
- Simplified deployment and management
- Component isolation through Docker
- Easy updates and rollbacks
- Active community support

**Trade-offs:**
- Less control over low-level settings
- Dependency on Docker and its limitations
- Need to learn Tutor specifics

### 2. MFE customization through repository fork

**Decision:** Creating a fork of frontend-app-authn for customization

**Advantages:**
- Full control over MFE code
- Deep customization capabilities
- Version control of changes through Git

**Trade-offs:**
- Need to maintain synchronization with upstream
- Additional complexity during Open edX updates
- Requires React and frontend development knowledge

### 3. Using Ansible for automation

**Decision:** Ansible playbook using ansible-role-tutor

**Advantages:**
- Deployment idempotency
- Declarative infrastructure description
- Ability to deploy on multiple servers

**Trade-offs:**
- Additional abstraction layer
- Need to maintain Ansible code
- Dependency on ansible-role-tutor

## Production Settings

### Security

1. **HTTPS and SSL certificates**
   ```yaml
   tutor_enable_https: true
   ssl_certificate_email: "admin@example.com"
   ```

2. **Firewall configuration**
   ```bash
   # Open only necessary ports
   ufw allow 80/tcp
   ufw allow 443/tcp
   ufw allow 22/tcp
   ```

3. **Regular security updates**
   ```yaml
   # In ansible playbook
   unattended_upgrades: true
   ```

### Performance

1. **Service scaling**
   ```yaml
   tutor_worker_replicas: 3
   tutor_web_replicas: 2
   tutor_cache_redis_replicas: 2
   ```

2. **Database configuration**
   ```yaml
   mysql_max_connections: 500
   mysql_innodb_buffer_pool_size: "2G"
   ```

3. **CDN for static files**
   ```yaml
   aws_cloudfront_domain: "cdn.example.com"
   ```

### Monitoring and Logging

1. **Monitoring setup**
   ```yaml
   monitoring_stack:
     - prometheus
     - grafana
     - alertmanager
   ```

2. **Centralized logging**
   ```yaml
   log_aggregation:
     backend: elasticsearch
     retention_days: 90
   ```

### Backup

1. **Automated backups**
   ```yaml
   backup_schedule: "0 2 * * *"
   backup_retention_days: 30
   backup_s3_bucket: "openedx-backups"
   ```

2. **Restore testing**
   ```bash
   # Weekly restore testing
   ansible-playbook playbooks/test-restore.yml
   ```

## Potential Improvements

### Short-term (1-3 months)

1. **CI/CD Pipeline**
   - Automated testing of MFE changes
   - Automatic deployment to staging environment
   - GitHub Actions integration

2. **Monitoring improvements**
   - Prometheus metrics setup for Open edX
   - Grafana dashboard creation
   - Alert configuration

3. **Test automation**
   - Unit tests for custom MFE
   - Integration tests for Ansible playbook
   - E2E tests for the platform

### Medium-term (3-6 months)

1. **Microservice architecture**
   - External service separation (Redis, MySQL)
   - Using managed cloud services
   - Service mesh configuration

2. **Advanced customization**
   - Custom theme development
   - External authentication system integration
   - Custom Open edX plugins

3. **Auto-scaling**
   - Kubernetes deployment
   - Metrics-based auto-scaling
   - Multi-region deployment

### Long-term (6+ months)

1. **Full cloud integration**
   - Terraform for infrastructure
   - Helm charts for Kubernetes
   - GitOps with ArgoCD

2. **Advanced analytics**
   - Learning analytics integration
   - Big data student data processing
   - ML for learning personalization

3. **Multi-tenancy**
   - Multiple organization support
   - Data and settings isolation
   - Centralized management

## Quick Start

### For Development

```bash
# 1. Repository cloning
git clone [YOUR_REPO_URL]
cd openedx-project

# 2. Tutor setup
cd tutor-config
tutor config save --interactive
tutor plugins enable mfe
tutor dev launch

# 3. Custom MFE build
tutor images build mfe
```

### For Production

```bash
# 1. Inventory preparation
cp inventories/production.example inventories/production
# Edit the file for your servers

# 2. Variable configuration
cp group_vars/production.yml.example group_vars/production.yml
# Edit for your settings

# 3. Deployment
ansible-playbook playbooks/deploy-openedx.yml -i inventories/production
```

## Support and Development

### Open edX Updates

```bash
# 1. Upstream update in MFE fork
cd frontend-app-authn
git fetch upstream
git merge upstream/master

# 2. Tutor update
pip install --upgrade tutor

# 3. Data migration
tutor local upgrade --from=previous-version
```

### System Health Monitoring

```bash
# Service status check
tutor local logs -f

# Metrics check
curl http://localhost:9090/metrics

# Availability check
curl -I http://your-domain.com
```

## License and Contribution

This project follows the Open edX license (AGPL 3.0). 
Contributions are welcome through Pull Requests.

## Contacts

- Developer: [Your Name]
- Email: [your-email@example.com]
- Issue Tracker: [GitHub Issues URL]
