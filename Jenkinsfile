pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    stages {
        stage('Create Virtual Env') {
            steps {
                bat "${PYTHON} -m venv venv"
                bat ".\\venv\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat ".\\venv\\Scripts\\pytest tests\\ --html=report.html"
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML (target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: "Test Report"
                ])
            }
        }
    }
}
