pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        // stage('Test') {
        //     steps {
        //         sh '''#!/bin/bash
        //         echo 'Test Step: We run testing tool like pytest here'

        //         # TODO fill out the path to conda here
        //         # sudo /PATH/TO/CONDA init
        //         # /opt/homebrew/bin/conda
        //         export PATH=/opt/homebrew/bin:$PATH



        //         # TODO Complete the command to run pytest
        //         # sudo /PATH/TO/CONDA run -n <Envinronment Name> <Command you want to run>
        //         conda activate mlip

        //         echo 'pytest not runned'
        //         exit 1 #comment this line after implementing Jenkinsfile
        //         '''

        //     }
        // }
        stage('Test') {
            steps {
                sh '''
                echo "Test Step: Running pytest"

                # Initialize Conda
                source /opt/homebrew/etc/profile.d/conda.sh || echo "Conda profile script not found"

                # Activate Conda environment
                conda activate mlip || { echo "Failed to activate conda env"; exit 1; }

                # Verify Python and pytest
                which python
                python --version
                which pytest

                # Install pytest if missing
                pip install pytest || { echo "pytest installation failed"; exit 1; }

                # Run pytest
                pytest --junitxml=pytest-report.xml || { echo "Tests failed"; exit 1; }
                '''
                junit 'pytest-report.xml'  // Store test results in Jenkins
            }
        }

        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our porject'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
