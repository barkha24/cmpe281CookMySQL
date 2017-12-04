all: build
	ls cmpe281p2.zip

clean:
	$(MAKE) -C backend clean
	$(MAKE) -C server clean
	rm -rf bld
	rm -rf cmpe281p2.zip

build:
	rm -rf bld
	mkdir bld
	cp -r backend bld
	cp -r server bld
	cp -r flaskapp.py bld
	cp backend/installer.sh bld/backend-installer.sh
	cp -r frontend bld
	cp frontend/installer.sh bld/frontend-installer.sh
	cd bld && zip -r cmpe281p2.zip .  || true
	mv bld/cmpe281p2.zip .
	ls cmpe281p2.zip
