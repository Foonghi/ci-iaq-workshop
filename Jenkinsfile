pipeline {
    agent any

    environment {
      HCLOUD_TOKEN = credentials('hcloud-token')
    }

    stages {
        stage('Lint Ansible Playbook') {
            steps {
              sh 'ansible-lint install-hero-app.yml'
            }
        }
        stage('Start Test VM') {
            steps {
              dir('ci-test-vm') {
                sh 'terraform init'
                sh 'terraform apply -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"'
              }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
              sh 'ansible-galaxy collection install -r requirements.yml'
              sh 'ansible-playbook -i inventory/test.hcloud.yml install-hero-app.yml'
            }
        }

        stage('Run Testinfra Tests') {
            steps {
              sh "py.test --connection=ansible --ansible-inventory inventory/test.hcloud.yml --hosts='ansible://ansible-test-instance-foonghi' --force-ansible -v test/*.py"
            }
        }
    }
    post {
        always {
          dir('ci-test-vm') {
            sh 'terraform destroy -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"'
          }
         }
    }
}
