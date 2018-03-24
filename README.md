AWS ECS Fargate 

###A Dockerfile along with the required application files (Flask Application) are provided. Run the below commands to create an image and push it to ECR 
(1) Build Image

    docker build -t <image-name> . 

(2) Run a test docker container

    docker run -d -p 80:80 <image-name>

(3) Confirm that the container is running successfully

    docker ps

    curl -Ik localhost:80     (This should return a 200OK)

(4) Push the image to ECR

	aws ecr get-login --no-include-email --region us-east-1 

    Invoke-Expression -Command (aws ecr get-login --no-include-email --region us-east-1)

    docker tag <image-name> <account-id>.dkr.ecr.us-east-1.amazonaws.com/<repo-name>:latest 

    docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/<repo-name>:latest


###Create CFN stack

(1)    First Create the VPC stack using the CFN console/cli 

(2)    There after create the alb-fargate stack which uses the networking resources 		   from the above stack


    
