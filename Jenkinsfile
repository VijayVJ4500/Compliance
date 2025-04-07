pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/VijayVJ4500/Compliance'
            }
        }

        stage('Setup Virtualenv and Install') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '%VENV_DIR%\\Scripts\\activate && pytest --html=report.html --self-contained-html'
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

    post {
        always {
            cleanWs()
        }
    }
}
