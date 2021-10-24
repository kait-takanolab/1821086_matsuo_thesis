
server_81="A";
server_82="D";
server_83="A";



    

print("対象：192.168.1.81サーバ");
print("応答速度が遅い為、サーバの優先度を下げています");
    
#サーバ81のコンフィグを変更。対象サーバの優先度を下げる。
f = open('test.txt', 'w', encoding='UTF-8')
datalist1 = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n']
f.writelines(datalist1)

if server_81 == "D":
    datalist2 = ['server 192.168.1.81 weight=10;\n']
    f.writelines(datalist2)
else:
    datalist2 = ['server 192.168.1.81;\n']
    f.writelines(datalist2)
    
if server_82 == "D":
    datalist3 = ['server 192.168.1.82 weight=10;\n']
    f.writelines(datalist3)
else:
    datalist3 = ['server 192.168.1.82;\n']
    f.writelines(datalist3)

if server_83 == "D":
    datalist4 = ['server 192.168.1.83 weight=10;\n']
    f.writelines(datalist4)
else:
    datalist4 = ['server 192.168.1.83;\n']
    f.writelines(datalist4)

datalist5 = ['}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']

f.writelines(datalist5)
f.close()
