#!/bin/bash
echo "Sincronizando mudanças com GitHub..."

git add .

if git diff --staged --quiet; then
    echo "Nenhuma mudança para sincronizar"
    exit 0
fi

timestamp=$(date '+%Y-%m-%d %H:%M:%S')
git commit -m "Auto-sync: $timestamp"
git push origin main

echo "Sincronizado com GitHub!"
