#
# Build stage
#
FROM maven:3.6.0-jdk-11-slim AS build
COPY src /home/app/src
COPY pom.xml /home/app
WORKDIR /home/app
RUN mvn clean package -DskipTests

#
# Package stage
#
FROM openjdk:11-jre-slim
COPY --from=build /home/app/target/spring-app.jar /usr/local/lib/spring-app.jar
#COPY /target/spring-app.jar /usr/local/lib/spring-app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","/usr/local/lib/spring-app.jar"]
