pipeline {
    agent any

    environment {
        IMAGE_NAME = "inovex-app"
        TAG = "latest"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Lint Code') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install pytest'
                sh 'pytest tests/'
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
