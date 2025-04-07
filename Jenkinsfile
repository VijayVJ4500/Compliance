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

        stage('Create Virtualenv') {
            steps {
                bat '"%PYTHON%" -m venv venv'
            }
        }

        stage('Install Requirements') {
            steps {
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                withEnv(["PYTHONPATH=src"]) {
                bat '.\\venv\\Scripts\\activate && pytest --html=report.html --self-contained-html'
                
            }
            }
        }

       stage('Publish Report') {
             steps {
                 publishHTML([
                       reportDir: '.',          // Location of report.html
                       reportFiles: 'report.html',    // The HTML file name
                       reportName: 'Test Report',     // Display name in Jenkins UI
                       keepAll: true,                 // Keep reports for all builds
                       alwaysLinkToLastBuild: true,   // Link report to latest build
                       allowMissing: false            // Fail if report is missing
                ])
            }
        }

    }
}
