all: build
	ls cmpe281p2.tgz

clean:
	$(MAKE) -C backend clean
	rm -rf bld
	rm -rf cmpe281p2.tgz

build:
	rm -rf bld
	mkdir bld
	cp -r backend bld
	cp backend/installer.sh bld/backend-installer.sh
	cp -r frontend bld
	cp frontend/installer.sh bld/frontend-installer.sh
	cd bld && tar -cvzf cmpe281p2.tgz .  || true
	mv bld/cmpe281p2.tgz .
	ls cmpe281p2.tgz
