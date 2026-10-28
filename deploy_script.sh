#!/bin/bash
ENV=$1
echo ">>> [DevFlow] Iniciando deploy em: $ENV"

cd /var/www/devflow-$ENV
git pull origin $ENV
pip install -r requirements.txt --quiet

# Blue-green style restart
if command -v pm2 &> /dev/null; then
  pm2 restart devflow-$ENV --update-env
else
  docker-compose up -d --build
fi

# Healthcheck
sleep 3
curl -f http://localhost:5000/health || (echo "ROLLBACK!" && git reset --hard HEAD~1 && exit 1)

echo ">>> Deploy $ENV finalizado com sucesso!"