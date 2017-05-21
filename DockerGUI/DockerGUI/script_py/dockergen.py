
class Dockergen :


	def gen(Base , ocommande ,Paquet,Fichier,usr):
		dockerfile=open("static/"+usr+"/Dockerfile","w")

		dockerfile.write("FROM "+Base+"\n")

		i=0
		while i<len(Paquet):
		 	dockerfile.write("RUN apt-get update && apt-get install -y "+Paquet[i]+"\n")
		 	i+=1



		j=0
		while j<len(Fichier):
			if Base=="debian:wheezy":
				dockerfile.write("COPY "+Fichier[j]+" /home/docker/script/"+Fichier[j]+"\n")
			elif Base=="nginx":
				if ".config" in Fichier[i]:
					dockerfile.write("COPY"+Fichier[i]+"/etc/nginx/conf.d/defaut.conf"+"\n")
				else:
					dockerfile.write("COPY"+Fichier[i]+"/home/nginx_demo/"+Fichier[i]+"\n")
			j+=1


		dockerfile.write("RUN chmod +x home/ \n")

		"""commande par defaut"""
		if (Base=="debian:wheezy"):
			dockerfile.write("CMD [\""+ocommande+"\"]")
