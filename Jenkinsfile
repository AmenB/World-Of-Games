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
        stage('Docker Build') {
            steps {
                script {
                    dir('World-Of-Games') {
                        withEnv(["IMAGE_TAG=${env.BUILD_NUMBER}"]) {
                            bat "docker-compose up --build -d"
                        }
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
                    def imageTag = "${env.BUILD_NUMBER}"
                    
                    // Tag and push the Docker image with the new build number
                    bat "docker tag ${IMAGE_NAME}:latest ${IMAGE_NAME_TAG}:${imageTag}"
                    bat "docker push ${IMAGE_NAME_TAG}:${imageTag}"
                }
            }
        }
    }
}
