pipeline {
    agent any

    environment {
        IMAGE_NAME = "inovex-app"
        TAG = "latest"
        K8S_DEPLOYMENT_YAML = "./inovex_app/k8s/flask-deployment.yaml"
        K8S_SERVICE_YAML = "./inovex_app/k8s/flask-service.yaml"
    }

    options {
        skipDefaultCheckout() // we will use custom checkout
        timestamps()
    }

    stages {

        stage('Checkout Code from GitHub') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/AnjanKumarS/Inovex-Devops.git',
                        credentialsId: 'github-creds' // Add this in Jenkins Credentials
                    ]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image $IMAGE_NAME:$TAG"
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                sh "kubectl apply -f ${K8S_DEPLOYMENT_YAML}"
                sh "kubectl apply -f ${K8S_SERVICE_YAML}"
            }
        }
    }

    post {
        success {
            echo "✅ Deployment succeeded!"
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}
