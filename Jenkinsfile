pipeline {
    agent any
    // environment{
    //     ARTIFACTORY_ACCESS_TOKEN = credentials('artifactory_access_token')
    // }
    stages {
       stage('build') {
          steps {
             echo 'Stage build starting'
             sh 'python3 --version'
             sh 'bash ./MainScript.sh'
             echo 'Stage build ending'
          }
       }
       stage(test) {
           steps {
               echo 'Stage test starting'
               sh 'bash ./TestScript.sh'
               echo 'Stage test ending'

           }
       }
        stage(deploy) {
            steps {
            echo 'Deploy stage start'
           }
       }
    }
//     post {
//         always {
//             archiveArtifacts artifacts: 'results.jar', fingerprint: true
//         }
//  }
}