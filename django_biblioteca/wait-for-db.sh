#!/bin/sh
# Espera hasta que el host MySQL responda, luego ejecuta el comando pasado

set -e

host="$1"
shift
cmd="$@"

until mysqladmin ping -h "$host" --silent; do
  echo "MySQL no está listo, esperando..."
  sleep 2
done

echo "MySQL está disponible — ejecutando comando:"
exec $cmd
