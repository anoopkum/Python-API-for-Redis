# Python-API-for-Redis 
Built by Anoop Kumar

1. First set up Redis with helm chart.

    1. standard Redis chart and image to deploy Redis:
        helm repo add bitnami https://charts.bitnami.com/bitnami
        helm install my-release bitnami/redis --set auth.password=xxxxxxxx

    2. expose to localhost.
        kubectl port-forward --namespace default svc/my-release-redis-master 6379:6379

2. Step-by-step instructions to set up the Python API with FastAPI framework 

    1. Install Python 3.10x on your docker.
    2. Create a virtual environment for your project with command:
        python3 -m venv myenv
    3. Install the required Python packages:
        pip3 install fastapi uvicorn "[standard]" redis pyyaml
        pip3 install python-multipart
    4. Create a Python file for your FastAPI application main.py and add the your code
    5. Start the FastAPI application using the following command:
        uvicorn main:app --reload
    6. Test the API using a tool like curl you can use the following command:
        curl -F file=@./person.yaml http://localhost:8000/person
        where person.yaml is a YAML file containing the person's information
    7. To retrieve a person record, you can use the following command:
        curl localhost:8000/person/<first_name>
        where <first_name> is the first name of the person you want to retrieve.
    8. That's it! You now have a Python API with FastAPI framework running on your local host.

3. Deploy nginx with nginx/bitnami image with following steps
    helm repo add bitnami https://charts.bitnami.com/bitnami
    helm install my-release bitnami/nginx-ingress-controller

4. Build docker Image for Python API with dockerfile
    1. Build and tag the Docker image:
        docker build -t fastapi-app:latest .
    2. Push the Docker image to a container registry, such as Docker Hub:
        docker push <username>/fastapi-app:latest

5. Helm Chart Configuration
    1. Create a Helm chart for Python Api to deploy in kubernetes.
        helm create fastapi-helm
    2. Directory structure for helm chart will be created as follow :
        fastapi-helm/
        Chart.yaml
        values.yaml
        templates/
        deployment.yaml
        service.yaml
        ingress.yaml
    3. Update the Helm Chart files:
        Chart.yaml: Update the version and appVersion fields to match your API version.
        values.yaml: Define the default values for your chart. Set the image.repository and image.tag to the values of your Docker image.
        deployment.yaml: Define the Kubernetes deployment for your API. Set the image field to the values of your Docker image. Define any additional environment variables for application.service.yaml: Define the Kubernetes service for your API. Set the port and targetPort fields to the appropriate values.
        ingress.yaml: Define the Nginx Ingress for your API. Set the host field to the appropriate value ( this is not required as my deployment as I deployed nginx with bitnami repo)
 
    4. Deploy the Helm Chart:
        Use the following command to deploy the Helm chart:
        helm install fast-api ./fastapi-helm
        This will deploy the API to Kubernetes using the values defined in your Helm chart.
 
    5. Verify the Deployment:
        Use the following command to verify the deployment:
        kubectl get all
        This will show you the pods and services created by your Helm chart.
    6.  Validate the app with following commands to post person.yaml and retrieve the data from Redis
            curl  -F file=@./person.yaml http://localhost:8000/person
            curl localhost:8000:/person/Suman   
    7. Further Improvements:
        Use a Kubernetes Secret to store sensitive information like API keys or database passwords.
        Use Kubernetes Horizontal Pod Autoscaler to automatically scale the API based on traffic.
        Use Kubernetes StatefulSet to manage stateful applications.
        Use Kubernetes ConfigMap to store configuration data separately from the code.
        Use Kubernetes Service Mesh (like Istio) to handle service-to-service communication and security.