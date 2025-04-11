pipeline {
    agent any

    environment {
        SONARQUBE = 'MySonarQube' // Must match the name from Jenkins config
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
