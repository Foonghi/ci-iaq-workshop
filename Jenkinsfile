pipeline {
    agent any

    environment {
      HCLOUD_TOKEN = credentials('hcloud-token')
    }

    stages {
        stage('Start Test VM') {
            steps {
              dir('ci-test-vm') {
                sh 'terraform init'
                terraform apply -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"
              }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
              sh 'ansible-galaxy collection install -r requirements.yml'
              ansible-playbook -i inventory/test.hcloud.yml install- hero-app.yml
            }
        }
    }
    post {
        always {
          dir('ci-test-vm') {
             terraform destroy -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"
          }
         }
    }
}
