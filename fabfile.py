from fabric import task

@task
def deploy(c):
    c.run("uname -a")  # أمر لتنفيذ على الخادم
    c.run("df -h")     # أمر آخر
