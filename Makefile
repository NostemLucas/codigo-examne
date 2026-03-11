.PHONY: help install docker-up docker-down docker-logs db-init db-migrate run clean test

help:
	@echo "Comandos disponibles para el Sistema de Florería:"
	@echo ""
	@echo "  make install      - Instalar dependencias con UV"
	@echo "  make docker-up    - Levantar MySQL con Docker"
	@echo "  make docker-down  - Detener Docker"
	@echo "  make docker-logs  - Ver logs de MySQL"
	@echo "  make db-init      - Inicializar base de datos"
	@echo "  make db-migrate   - Ejecutar migraciones"
	@echo "  make run          - Ejecutar aplicación Flask"
	@echo "  make clean        - Limpiar archivos temporales"
	@echo "  make setup        - Configuración completa desde cero"

install:
	@echo "Instalando dependencias con UV..."
	uv sync

docker-up:
	@echo "Levantando MySQL con Docker..."
	docker-compose up -d
	@echo "Esperando que MySQL esté listo..."
	@sleep 10
	@echo "MySQL está listo en localhost:3306"
	@echo "phpMyAdmin disponible en http://localhost:8080"

docker-down:
	@echo "Deteniendo contenedores de Docker..."
	docker-compose down

docker-logs:
	@echo "Mostrando logs de MySQL..."
	docker-compose logs -f db

db-init:
	@echo "Inicializando base de datos..."
	flask db init
	flask db migrate -m "Initial migration"
	flask db upgrade
	flask init-db
	@echo "Base de datos inicializada!"

db-migrate:
	@echo "Ejecutando migraciones..."
	flask db migrate -m "$(msg)"
	flask db upgrade

run:
	@echo "Ejecutando aplicación Flask..."
	python main.py

clean:
	@echo "Limpiando archivos temporales..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
	@echo "Limpieza completa!"

setup: install docker-up
	@echo "Esperando que MySQL esté completamente listo..."
	@sleep 15
	@echo "Inicializando base de datos..."
	@make db-init
	@echo ""
	@echo "=========================================="
	@echo "¡Configuración completa!"
	@echo "=========================================="
	@echo ""
	@echo "Ahora crea un usuario admin:"
	@echo "  flask create-admin"
	@echo ""
	@echo "Luego ejecuta la aplicación:"
	@echo "  make run"
	@echo ""
	@echo "URLs disponibles:"
	@echo "  - Aplicación: http://localhost:5000"
	@echo "  - phpMyAdmin: http://localhost:8080"
	@echo ""
