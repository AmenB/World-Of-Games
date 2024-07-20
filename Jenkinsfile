pipeline {
    agent any

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
    }
}
