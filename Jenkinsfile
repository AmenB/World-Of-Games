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
                    bat "python World-Of-Games/increment_version.py"
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
        stage('Docker Compose Build') {
            steps {
                script {
                    dir('World-Of-Games') {
                        bat "docker-compose build"
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
        stage('Docker Tagging') {
            steps {
                script {
                    def flaskTag = "${IMAGE_NAME_TAG}:flask"
                    def mysqlTag = "${IMAGE_NAME_TAG}:mysql-custom"

                    // Tag Docker images
                    bat "docker tag world-of-games-flask ${flaskTag}"
                    bat "docker tag mysql ${mysqlTag}"
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
        stage('Push Docker Images') {
            steps {
                script {
                    def flaskTag = "${IMAGE_NAME_TAG}:flask"
                    def mysqlTag = "${IMAGE_NAME_TAG}:mysql-custom"

                    // Push Docker images
                    bat "docker push ${flaskTag}"
                    bat "docker push ${mysqlTag}"
                }
            }
        }
    }
}
