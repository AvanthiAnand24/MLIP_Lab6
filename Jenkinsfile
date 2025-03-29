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
                sh '''#!/bin/bash
                echo 'Test Step: Running pytest'

                # Manually add Conda to PATH
                export PATH=/opt/homebrew/bin:$PATH

                # Initialize Conda in this shell session
                source /opt/homebrew/etc/profile.d/conda.sh  # Ensure Conda functions properly

                # Activate Conda environment
                conda activate mlip

                # Run pytest
                pytest --maxfail=1 --disable-warnings --tb=short

                echo 'Tests completed successfully'
                '''
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
