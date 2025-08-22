# Hello, World !!!

# Q1 
> create a dir /tmp/gdir 
> yuvraj is the owner of this dir. 
> recent all the users, should not be able to create file inside the dir.. 
> yuvraj of all file and sub dir, and alian and sujau should be able to add content all the file inside the dir "/tmp/gdir"
# Q2
> 
> when user loged in who command w command should display, and the default permission of file should be 444

ans >>>

```bash
echo $(who)
echo $(w)
umask 222
# in the bashrc or zshrc.
```

