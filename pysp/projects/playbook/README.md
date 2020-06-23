# Ansible Playbook
This is my project for the System Administration module of the [Python Specialization Course](https://github.com/joserequenaidv/my-eoi/blob/master/pysp/README.md).

## Links
- [Requirements](https://github.com/pythoncanarias/eoi/blob/master/07-sysadmin/miniproyecto/django-deployment.ipynb) - How to build a server with nginx and uWSGI, and deploy a Django application 
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
        - collectstatic
        - loaddata
    - uWSGI
        - Emperor and vassals
            - config files and folders
            - symlinks
    - Nginx
        - right privileges to nginx worker, www-data
        - config file
        - symlinks

#### Modules to Consider
- **Ansible**
    - become
    - lineinfile [:page_with_curl:](https://docs.ansible.com/ansible/latest/modules/lineinfile_module.html)
    - file [:page_with_curl:](https://docs.ansible.com/ansible/latest/modules/replace_module.html)
    - copy
    - git
    - django_manage
    - pip
    - apt
    - systemd

### Challenges on the Way
I got to face some issues in the process of making this project:
- understand completely the uWSGI service cicle, emperor and vassals
- uWSGI installation, apt vs pip, system-wide vs virtual env
- Ansible documentation, applying the right module in each task

### Acquired Skills
Even though I got a **502 BAD GATEWAY** error and I could not make the web accessible, I learnt:

- how to automate processes of CI and CD with Vagrant and Ansible
- how to deploy a web regardless of the provider (Digital Ocean and Virtual Box)
- how to internally secure the web (uWSGI) and build a proxy with Nginx
- how to spell sytemctl, systectl, systemclt, systemtcl... :trollface:

### What's Next :shipit:
I would love to learn more about:
- CI/CD cycle
- Nginx
- uWSGI
- DNS
- **SSL Certificates**

#### Other:
- **Jenkins**
- **Docker**
- Kubernetes
