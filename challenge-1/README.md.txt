Challenge #1
A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.




In this folder there are 4 yaml files that are used to configure the kubernetes resources. To see this in action you would need a kubernetes cluster already setup. Other prerequisite include deploying MetalLB, Nginx Ingress Controller and Cert Manager to your cluster. I've built mine using Docker Desktop on Windows 10. I have scipts that allow me to setup a Kubernetes cluster with all the prerequisites within a few minutes so I'd be happy to show you it working when we meet. Otherwise feel free to use your own kubernetes cluster. 

The openldap.yaml contains a Deployment resource, Service resource and a Configmap resource. This file creates the ldap which acts as my non relation database and stores user data. Please refer to configmap resource to see what user data is being added to ldap.

The webhook-service.yaml contains a Deployment resource, Service resource and a Ingress resource. This files creates the backend application that deals with the business logic. Its job is to extract the credentials from a user's http request. Then run a query agaisnt the ldap directory to check that the credentials exist and validate the user. Once its recieved a response from the ldap service it'll then send the response back to the user.

The webpage.yaml contains a Deployment resource, Service resource, Configmap resource and a Ingress resource. This file creates the frontend using nginx, html, javascript etc. Through a browser you'll see 2 input box for username and password and a button. You must input the credentials and select the button. A request will be sent to the webhook service with the credentials. Once it recieves a response from the webhook service it will display it on the page.

The ingress-host-docker-internal.yaml contains an Ingress resource. It defines the TLS configuration for the domain host.docker.internal. It acts as a master and its configuration is inherited by the other Ingress resources that are defined as minions.

To deploy resources use:
kubectl apply -f ./


Notes
If I had thought about this more from a networking point of view and had put this together via AWS Cloud I would put the frontend in a public subnet and the backend and database in the private subnet. However with the time constraints and not wanting to spend any money on AWS I thought I could get more done with just a small kubernetes cluster. 