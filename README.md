Weblogic Ansible Role
------------
Role used to install weblogic domain on docker container.  Run validation tests.  

Usage
------------

```bash
molecule create 
molecule converge
molecule verify
molecule destroy
```

Start Weblogic
```bash
molecule converge -- --tags start
```

