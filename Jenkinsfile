pipeline {
    agent any
    environment {
        IMAGE_NAME = 'main_score'
        IMAGE_NAME_TAG = 'amenbrakat/main_score'
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
        stage('Read and Increment Build Number') {
            steps {
                script {
                    def versionsFile = 'World-Of-Games/version.txt'
                    
                    // Read the current build number
                    def currentBuildNumber = 0
                    if (fileExists(versionsFile)) {
                        currentBuildNumber = readFile(versionsFile).trim().toInteger()
                    }
                    
                    // Increment the build number
                    def newBuildNumber = currentBuildNumber + 1
                    
                    // Write the new build number back to the file
                    writeFile file: versionsFile, text: "${newBuildNumber}"
                    
                    // Set the new build number as an environment variable for use in Docker tag
                    env.BUILD_NUMBER = newBuildNumber.toString()
                    env.IMAGE_TAG = newBuildNumber.toString()
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                dir('World-Of-Games') {
                    bat "pip install --upgrade -r requirements.txt"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dir('World-Of-Games') {
                        bat "docker build -t ${IMAGE_NAME_TAG}:${IMAGE_TAG} ."
                    }
                }
            }
        }
        stage('Docker Compose Up') {
            steps {
                script {
                    dir('World-Of-Games') {
                        bat "docker-compose up -d"
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
        stage('Docker Compose Down') {
            steps {
                dir('World-Of-Games') {
                    bat "docker-compose down"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Tag and push the Docker image with the new build number
                    bat "docker push ${IMAGE_NAME_TAG}:${IMAGE_TAG}"
                }
            }
        }
    }
}
