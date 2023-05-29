pipeline {
    agent any
    stages {
       stage('build') {
          steps {
             echo 'Stage build starting'
             sh 'MainScript.sh'
             echo 'Stage build ending'
          }
       }
       stage(test) {
           steps {
               echo 'Stage test starting'
               sh 'TestScript.sh'
               echo 'Stage test ending'

           }
       }
    }
 }