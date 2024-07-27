pipeline {
    agent any
    environment {
        IMAGE_NAME = 'amenbrakat/main_core'
        IMAGE_TAG = 'latest'
    }
    stages {
        stage('Clean UP') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repo') {
            steps {
                bat "git clone https://github.com/AmenB/World-Of-Games.git"
            }
        }
        stage('Install Dependencies') {
            steps {
                dir('World-Of-Games') {
                    bat "pip install -r requirements.txt"
                }
            }
        }
        stage('Docker') {
            steps {
                script {
                    dir('World-Of-Games') {
                        bat "docker-compose up --build -d"
                    }
                }
            }
        }
        stage('E2E') {
            steps {
                dir('World-Of-Games') {
                    bat "python e2e.py"
                }
            }
        }
        stage('Finalize') {
            steps {
                dir('World-Of-Games') {
                    bat "docker-compose down"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub and push the Docker image
                    bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}
