#!/bin/bash

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

echo "Verificando disponibilidade de $host na porta $port..."
while ! nc -z "$host" "$port"; do
  >&2 echo "Esperando pelo $host:$port para ficar disponível..."
  sleep 2
done

>&2 echo "$host:$port está disponível - Executando comando: $cmd"
exec $cmd
