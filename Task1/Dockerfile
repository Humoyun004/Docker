# Бу йерда мен яратайотган Docker Image имни,Node.js Imagedan node:11 Alpine версиясини асос килиб олиб яратайапман.
FROM node:11-alpine

# Бу йерда /app.js/ файл ни Docker топа олиши учун copy клб койайапман. 
COPY app.js .

# Бу йерда `Node.js` interpratato ри `node` ни ишга туширайапман ва `app.js` унга аргумент сифатида корсатиб кетайарман унинг ичида ни код ни run килиши учун.
CMD ["node", "app.js"]

# Кейинги иш терминалда Docker Image яратиб олиш:
# 1. path -> Task1/  `docker build -t area_of_disk .`
# 2. `docker run area_of_disk`


