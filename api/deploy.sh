echo "update code"
cd /var/web/content/justworld.top/api
git checkout settings/prod.py
git pull
sed -i 's/@SERVER_HOST@/服务器地址/g' settings/prod.py
sed -i 's/@ADMIN_PATH@/管理后台地址路径/g' settings/prod.py
sed -i 's/@MYSQL_PASSWORD@/数据库密码/g' settings/prod.py

echo "remove old container ..."
cid=$(docker ps -a | grep content_app |awk '{print $1}')
echo $cid
if [ x"$cid" != x ]
    then
    docker rm -f $cid
fi
echo "build new image ..."
docker build -t content_app .
echo "start container ..."
docker run -d --restart=always -p 8000:8000 \
-v /var/web/content/logs:/var/web/justworld.top/logs --name content_app content_app
echo "current container ..."
docker ps -a | grep content_app
echo "clean docker ..."
docker system prune -f