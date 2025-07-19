pipeline {
    agent any

    environment {
        IMAGE_NAME = "inovex-app"
        TAG = "latest"
        VENV_DIR = "venv"
    }

    options {
        skipDefaultCheckout()
        timestamps()
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/AnjanKumarS/Inovex-Devops.git',
                        credentialsId: 'github-creds'
                    ]]
                ])
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Lint Code') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install flake8
                    flake8 .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install pytest
                    pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f ./inovex_app/k8s/flask-deployment.yaml'
                sh 'kubectl apply -f ./inovex_app/k8s/flask-service.yaml'
            }
        }

        stage('Cleanup Docker') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                sh 'docker system prune -af'
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
