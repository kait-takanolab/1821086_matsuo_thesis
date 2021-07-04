# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:57:12 2021

@author: 1821086

ロードバランサ簡略版
応答速度を測定し簡易評価を基にロードバランスする。

極端に遅ければ（5秒以上）、Pythonのファイル書き込みを利用し、コンフィグを書き換える。
その後適用させる為にリロード。

"""
import requests

#ラズパイの測定
url_81 = 'http://kait.jp'
res_81 = requests.get(url_81)
time_elapsed_81 = res_81.elapsed.total_seconds()
print("81サーバ：現在の応答速度：",time_elapsed_81);

url_82 = 'http://kait.jp'
res_82 = requests.get(url_82)
time_elapsed_82 = res_82.elapsed.total_seconds()
print("82サーバ：現在の応答速度：",time_elapsed_82);

url_83 = 'http://kait.jp'
res_83 = requests.get(url_83)
time_elapsed_83 = res_83.elapsed.total_seconds()
print("83サーバ：現在の応答速度：",time_elapsed_83);


server_81="OK";
server_82="OK";
server_83="OK";

#簡易評価
if(5<=time_elapsed_81):
    server_81="D";
    
elif(5<=time_elapsed_82):
    server_82="D";
    
elif(5<=time_elapsed_83):
    server_83="D";


    
if server_81 == "D":
    print("対象：192.168.1.81サーバ");
    print("応答速度が遅い為、サーバの優先度を下げています");
    
    #サーバ81のコンフィグを変更。対象サーバの優先度を下げる。
    f = open('nginx.conf', 'w', encoding='UTF-8')
    datalist = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n','server 192.168.1.81 weight=1;\n','server 192.168.1.82 weight=10;\n','server 192.168.1.83 weight=10;\n','}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']
    f.writelines(datalist)
    f.close()
    
elif server_82 == "D":
    print("対象：192.168.1.82サーバ");
    print("応答速度が遅い為、サーバの優先度を下げています");
    
    #サーバ81のコンフィグを変更。対象サーバの優先度を下げる。
    f = open('nginx.conf', 'w', encoding='UTF-8')
    datalist = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n','server 192.168.1.81 weight=10;\n','server 192.168.1.82 weight=1;\n','server 192.168.1.83 weight=10;\n','}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']
    f.writelines(datalist)
    f.close()

elif server_83 == "D":
    print("対象：192.168.1.83サーバ");
    print("応答速度が遅い為、サーバの優先度を下げています");
    
    #サーバ81のコンフィグを変更。対象サーバの優先度を下げる。
    f = open('nginx.conf', 'w', encoding='UTF-8')
    datalist = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n','server 192.168.1.81 weight=10;\n','server 192.168.1.82 weight=10;\n','server 192.168.1.83 weight=1;\n','}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']
    f.writelines(datalist)
    f.close()

else:
    print("ロードバランサはリーストコネクションで稼働中");
    #サーバ81のコンフィグを変更。対象サーバの優先度を下げる。
    f = open('nginx.conf', 'w', encoding='UTF-8')
    datalist = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n','server 192.168.1.81 weight=10;\n','server 192.168.1.82 weight=10;\n','server 192.168.1.83 weight=1;\n','}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']
    f.writelines(datalist)
    f.close()


     

