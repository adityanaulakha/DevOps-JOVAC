# Base image
FROM node:20

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy app files
COPY . .

# Expose port
EXPOSE 3000

# Start app
CMD ["npm", "start"]
