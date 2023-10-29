rem del /s /q *.pyo
del addons.xml
del addons.xml.md5
cd .\zips
del addons.xml
del addons.xml.md5
addons_xml_generator.py
copy addons.xml ..\
copy addons.xml.md5 ..\


