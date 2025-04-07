pipeline {
    agent any

    tools {
        python 'Python3.10'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-org/python-automation-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.', 
                    reportFiles: 'report.html', 
                    reportName: 'Test Report',
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true
                ])
            }
        }
    }
}
