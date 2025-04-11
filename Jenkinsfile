pipeline {
    agent any

    environment {
        SONARQUBE = 'MySonarQube' // This must match your SonarQube server name in Jenkins config
        PATH = "/opt/sonar-scanner/bin:${PATH}" // Add this if sonar-scanner is not already in Jenkins' PATH
    }

    stages {
        stage('Prepare Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
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
