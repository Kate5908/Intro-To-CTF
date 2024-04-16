# Use an existing image as a base
FROM node:14

# Set the working directory
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json files
COPY application/package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the code
COPY application/ /usr/src/app/application
RUN chmod 755 .
RUN chown -R www-data:www-data .
# Expose the port that the app listens on
USER www-data
EXPOSE 3000

# Define the command to run the app
CMD ["node", "application/server.js"]
