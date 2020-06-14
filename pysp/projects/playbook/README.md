# Ansible Playbook
This is my project for the System Administration module of the [Python Specialization Course](https://github.com/joserequenaidv/my-eoi/blob/master/pysp/README.md).

## Links
- [Requirements](https://github.com/pythoncanarias/eoi/     blob/master/07-sysadmin/miniproyecto/django-deployment.ipynb) - How to build a server on Debian 10 with nginx and uWSGI, and deploy a Django application 
- [Ansible Playbook](https://github.com/pythoncanarias/eoi/blob/master/07-sysadmin/miniproyecto/assignment.ipynb) - Guidelines from the official repository to accomplish the tasks given by Alejandro Samarín

## Project Journal
### Introduction
The assignment consists in coding a playbook on Ansible that automates a professional deployment
### Troubleshooting the Project
The steps we need to follow are the following:
- **Vagrant**
    - Connect with root user
    - Create user with sudo privileges
- **Ansible Playbook**
    - Install dependencies
        - python3
        - git
        - python3-pip
        - python3-venv
    - Install nginx and configure files
    - Install uwsgi and configure files
    - Clone shield project and configure files
        - Configure virtual env
            - pip3 install wheel
            - pip3 install six
            - pip3 install -r "$SHIELD_DIR/requirements"
        - makemigrations
        - migrate
        - change settings.py > ALLOWED_HOSTS

#### Modules to Consider
- **Vagrant**
    - Modules
    - connect [:page_with_curl:](https://www.vagrantup.com/docs/cli/connect)
    - ssh [:page_with_curl:](https://www.vagrantup.com/docs/cli/ssh)
    - ssh-config [:page_with_curl:](https://www.vagrantup.com/docs/cli/ssh_config)
    - status (optional) [:page_with_curl:](https://www.vagrantup.com/docs/cli/status)
- **Ansible**
    - lineinfile [:page_with_curl:](https://docs.ansible.com/ansible/latest/modules/lineinfile_module.html)
    - replace [:page_with_curl:](https://docs.ansible.com/ansible/latest/modules/replace_module.html)
    - file [:page_with_curl:](https://docs.ansible.com/ansible/latest/modules/replace_module.html)
        - 
### Challenges on the Way

### Acquired Skills

### What's Next
