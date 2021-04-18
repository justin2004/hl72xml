build:
	docker build -t justin2004/hl72xml .

run: 
	docker run --name hl72xml --rm -it justin2004/hl72xml make -f Makefile.app start

send:
	docker exec -it hl72xml python python_src/sendHL7.py

stop:
	docker stop hl72xml

