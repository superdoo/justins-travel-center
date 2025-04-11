pipeline {
    agent any

    environment {
        SONARQUBE = 'SonarQube' // Must match the name from Jenkins config
    }

    stages {
        stage('Clone repo') {
            steps {
                git url: 'https://github.com/superdoo/justins-travel-center.git', branch: 'main'
            }
        }

        stage('Prepare Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
