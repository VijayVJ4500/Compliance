pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\vijay\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"%PYTHON%" -m venv venv'
            }
        }

        stage('Install Requirements') {
            steps {
                bat '''
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run all_tests.py and Generate Reports') {
            steps {
                bat '''
                venv\\Scripts\\activate
                venv\\Scripts\\python.exe all_tests.py
                '''
            }
        }
    }

    post {
        always {
            publishHTML([
                reportDir: 'Reports',
                reportFiles: 'report.html',
                reportName: 'HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])

            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}
