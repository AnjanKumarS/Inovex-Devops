pipeline {
    agent any

    environment {
        IMAGE_NAME = "inovex-app"
        TAG = "latest"
        VENV_DIR = "venv"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AnjanKumarS/Inovex-Devops.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    %VENV_DIR%\\Scripts\\python.exe -m pip install --upgrade pip
                """
            }
        }

        stage('Lint Code') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    %VENV_DIR%\\Scripts\\python.exe -m pip install flake8
                    %VENV_DIR%\\Scripts\\flake8 inovex_app/
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    %VENV_DIR%\\Scripts\\python.exe -m pip install pytest
                    %VENV_DIR%\\Scripts\\pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%TAG% ."
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat """
                    kubectl apply -f inovex_app/k8s/flask-deployment.yaml
                    kubectl apply -f inovex_app/k8s/flask-service.yaml
                """
            }
        }

        stage('Cleanup Docker') {
            steps {
                bat "docker system prune -af"
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD Pipeline Succeeded!'
        }
        failure {
            echo '❌ CI/CD Pipeline Failed!'
        }
    }
}
